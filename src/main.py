"""
Main entry point for the Food Truck Research Agents application.
"""

import os
import sys
from typing import Optional
from dotenv import load_dotenv

from graph.workflow import FoodTruckResearchWorkflow


def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()
    
    # Check for required API keys
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not openai_key and not anthropic_key:
        print("❌ Error: No API keys found!")
        print("Please set either OPENAI_API_KEY or ANTHROPIC_API_KEY environment variable.")
        print("You can create a .env file with:")
        print("OPENAI_API_KEY=your-key-here")
        print("# or")
        print("ANTHROPIC_API_KEY=your-key-here")
        sys.exit(1)
    
    return openai_key, anthropic_key


def get_model_config() -> tuple[str, float]:
    """Get model configuration from environment or use defaults."""
    model_name = os.getenv("MODEL_NAME", "gpt-4")
    temperature = float(os.getenv("TEMPERATURE", "0.1"))
    
    # Validate model availability based on API keys
    openai_key, anthropic_key = load_environment()
    
    if "claude" in model_name.lower() and not anthropic_key:
        print(f"⚠️  Warning: {model_name} requires ANTHROPIC_API_KEY, falling back to gpt-4")
        model_name = "gpt-4"
    elif "gpt" in model_name.lower() and not openai_key:
        print(f"⚠️  Warning: {model_name} requires OPENAI_API_KEY, falling back to claude-3-sonnet-20240229")
        model_name = "claude-3-sonnet-20240229"
    
    return model_name, temperature


def get_location_input() -> str:
    """Get location input from user with validation."""
    while True:
        location = input("\n🏙️  Enter the city and state for food truck research (e.g., 'Austin, TX'): ").strip()
        
        if not location:
            print("❌ Please enter a valid location.")
            continue
        
        # Basic validation - should contain at least city and state
        if "," not in location or len(location.split(",")) < 2:
            print("❌ Please enter location in format: 'City, State' (e.g., 'Austin, TX')")
            continue
        
        return location


def display_header():
    """Display welcome header."""
    print("=" * 80)
    print("🚚 FOOD TRUCK RESEARCH AGENTS")
    print("Multi-Agent Business Analysis System")
    print("=" * 80)
    print("\nThis system uses 4 specialized AI agents to research food truck opportunities:")
    print("📊 Market Research Analyst - Competition & demand analysis")
    print("💰 Financial Advisor - Costs, revenue & profitability")
    print("⚙️  Operations Consultant - Permits, logistics & operations")
    print("🎯 Business Consultant - Strategic recommendations")
    print()


def display_progress(step: str, current: int, total: int):
    """Display progress indicator."""
    progress = "▓" * current + "▒" * (total - current)
    print(f"\n[{progress}] Step {current}/{total}: {step}")


def run_interactive_mode():
    """Run the application in interactive mode."""
    display_header()
    
    # Load environment and configure model
    load_environment()
    model_name, temperature = get_model_config()
    
    print(f"🤖 Using model: {model_name} (temperature: {temperature})")
    
    # Get location from user
    location = get_location_input()
    
    print(f"\n🔍 Starting research for: {location}")
    print("This may take 2-5 minutes as each agent completes their analysis...")
    
    # Initialize and run workflow
    try:
        workflow = FoodTruckResearchWorkflow(model_name=model_name, temperature=temperature)
        
        # Run research with progress updates
        display_progress("Market Research Analysis", 1, 4)
        results = workflow.run_research(location)
        
        # Check for errors
        if results.get("status") == "error":
            print(f"\n❌ Research failed: {results.get('error_message')}")
            return
        
        # Display results
        display_progress("Research Complete", 4, 4)
        print("\n" + "=" * 80)
        print("📋 RESEARCH RESULTS")
        print("=" * 80)
        
        formatted_report = workflow.format_results(results)
        print(formatted_report)
        
        # Offer to save results
        save_option = input("\n💾 Save results to file? (y/n): ").strip().lower()
        if save_option in ['y', 'yes']:
            save_results_to_file(formatted_report, location)
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Research cancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        print("Please check your API keys and try again.")


def save_results_to_file(report: str, location: str):
    """Save research results to a file."""
    try:
        # Create filename from location
        safe_location = location.replace(" ", "_").replace(",", "").lower()
        filename = f"food_truck_research_{safe_location}.md"
        
        with open(filename, 'w') as f:
            f.write(report)
        
        print(f"✅ Results saved to: {filename}")
        
    except Exception as e:
        print(f"❌ Failed to save file: {str(e)}")


def run_command_line_mode(location: str, model: Optional[str] = None):
    """Run the application in command-line mode."""
    print(f"🚚 Food Truck Research: {location}")
    
    # Load environment
    load_environment()
    model_name, temperature = get_model_config()
    
    # Override model if specified
    if model:
        model_name = model
    
    print(f"🤖 Model: {model_name}")
    
    try:
        workflow = FoodTruckResearchWorkflow(model_name=model_name, temperature=temperature)
        results = workflow.run_research(location)
        
        if results.get("status") == "error":
            print(f"❌ Error: {results.get('error_message')}")
            sys.exit(1)
        
        # Output results
        formatted_report = workflow.format_results(results)
        print(formatted_report)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


def main():
    """Main application entry point."""
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        location = sys.argv[1]
        model = sys.argv[2] if len(sys.argv) > 2 else None
        run_command_line_mode(location, model)
    else:
        run_interactive_mode()


if __name__ == "__main__":
    main()