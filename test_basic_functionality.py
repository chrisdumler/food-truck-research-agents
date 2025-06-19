#!/usr/bin/env python3
"""
Basic functionality test for the Food Truck Research Agents system.
This script tests the core workflow without requiring API keys.
"""

import sys
import os
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def test_imports():
    """Test that all modules can be imported successfully."""
    print("🧪 Testing imports...")
    
    try:
        # Test model imports
        from models.research_models import (
            FoodTruckResearchState, 
            MarketResearchData,
            FinancialAnalysisData,
            OperationsAnalysisData,
            BusinessRecommendation,
            AgentResponse
        )
        print("✅ Models imported successfully")
        
        # Test agent imports (without initialization)
        from agents.base_agent import BaseAgent
        from agents.market_research_agent import MarketResearchAgent
        from agents.financial_advisor_agent import FinancialAdvisorAgent
        from agents.operations_consultant_agent import OperationsConsultantAgent
        from agents.business_consultant_agent import BusinessConsultantAgent
        print("✅ Agents imported successfully")
        
        # Test workflow imports
        from graph.workflow import FoodTruckResearchWorkflow, WorkflowState
        print("✅ Workflow imported successfully")
        
        # Test utilities
        from utils.retry_handler import RetryHandler, retry_api_call
        print("✅ Utilities imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


def test_model_validation():
    """Test Pydantic model validation."""
    print("\n🧪 Testing model validation...")
    
    try:
        from models.research_models import (
            MarketResearchData, 
            FinancialAnalysisData,
            FoodTruckResearchState
        )
        
        # Test MarketResearchData
        market_data = MarketResearchData(
            location="Austin, TX",
            competition_level="Medium",
            target_customers=["Office workers", "Students"],
            peak_hours=["11:30 AM - 1:30 PM"],
            seasonal_factors=["Weather dependent"],
            market_size_estimate="500 daily customers",
            competition_analysis=[{
                "name": "Test Truck",
                "type": "Mexican",
                "location": "Downtown",
                "strengths": "Good food",
                "weaknesses": "Limited hours"
            }],
            opportunities=["Corporate catering"],
            challenges=["Permit complexity"]
        )
        print("✅ MarketResearchData validation passed")
        
        # Test FoodTruckResearchState
        state = FoodTruckResearchState(
            location="Austin, TX",
            market_research=market_data,
            messages=["Test message"]
        )
        print("✅ FoodTruckResearchState validation passed")
        
        return True
        
    except Exception as e:
        print(f"❌ Model validation failed: {e}")
        return False


def test_agent_initialization():
    """Test agent initialization without API calls."""
    print("\n🧪 Testing agent initialization...")
    
    try:
        # Mock environment to avoid API key requirements
        os.environ["OPENAI_API_KEY"] = "test-key"
        
        from agents.market_research_agent import MarketResearchAgent
        from agents.financial_advisor_agent import FinancialAdvisorAgent
        
        # Test agent properties without making API calls
        market_agent = MarketResearchAgent(model_name="gpt-4")
        assert market_agent.agent_name == "Market Research Analyst"
        assert "market" in market_agent.agent_description.lower()
        
        financial_agent = FinancialAdvisorAgent(model_name="gpt-4")
        assert financial_agent.agent_name == "Financial Advisor"
        assert "financial" in financial_agent.agent_description.lower()
        
        print("✅ Agent initialization passed")
        return True
        
    except Exception as e:
        print(f"❌ Agent initialization failed: {e}")
        return False


def test_workflow_structure():
    """Test workflow structure without execution."""
    print("\n🧪 Testing workflow structure...")
    
    try:
        # Mock environment
        os.environ["OPENAI_API_KEY"] = "test-key"
        
        from graph.workflow import FoodTruckResearchWorkflow
        
        # Initialize workflow (this creates the graph structure)
        workflow = FoodTruckResearchWorkflow(model_name="gpt-4")
        
        # Verify workflow has the required components
        assert hasattr(workflow, 'workflow')
        assert hasattr(workflow, 'market_agent')
        assert hasattr(workflow, 'financial_agent')
        assert hasattr(workflow, 'operations_agent')
        assert hasattr(workflow, 'business_agent')
        
        print("✅ Workflow structure test passed")
        return True
        
    except Exception as e:
        print(f"❌ Workflow structure test failed: {e}")
        return False


def test_retry_handler():
    """Test retry handler functionality."""
    print("\n🧪 Testing retry handler...")
    
    try:
        from utils.retry_handler import RetryHandler, is_retryable_api_error
        
        # Test retry handler initialization
        handler = RetryHandler(max_attempts=3, base_delay=0.1)
        assert handler.max_attempts == 3
        assert handler.base_delay == 0.1
        
        # Test delay calculation
        delay = handler.calculate_delay(1)
        assert delay > 0
        
        # Test error classification
        assert is_retryable_api_error(Exception("rate limit exceeded")) == True
        assert is_retryable_api_error(Exception("invalid api key")) == False
        
        print("✅ Retry handler test passed")
        return True
        
    except Exception as e:
        print(f"❌ Retry handler test failed: {e}")
        return False


def test_system_prompts():
    """Test that agents can generate system prompts."""
    print("\n🧪 Testing system prompt generation...")
    
    try:
        os.environ["OPENAI_API_KEY"] = "test-key"
        
        from agents.market_research_agent import MarketResearchAgent
        from agents.business_consultant_agent import BusinessConsultantAgent
        
        market_agent = MarketResearchAgent()
        business_agent = BusinessConsultantAgent()
        
        # Test system prompt generation
        market_prompt = market_agent.create_system_prompt()
        business_prompt = business_agent.create_system_prompt()
        
        assert len(market_prompt) > 100
        assert len(business_prompt) > 100
        assert "market research" in market_prompt.lower()
        assert "business consultant" in business_prompt.lower()
        
        print("✅ System prompt generation test passed")
        return True
        
    except Exception as e:
        print(f"❌ System prompt generation test failed: {e}")
        return False


def run_all_tests():
    """Run all tests and report results."""
    print("🚚 Food Truck Research Agents - Basic Functionality Tests")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_model_validation,
        test_agent_initialization,
        test_workflow_structure,
        test_retry_handler,
        test_system_prompts
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            print("⚠️  Test failed - stopping execution")
            break
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All basic functionality tests passed!")
        print("\n✨ The system is ready for API-based testing")
        print("Next steps:")
        print("1. Set up API keys in .env file")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Run: python src/main.py")
        return True
    else:
        print("❌ Some tests failed - please fix issues before proceeding")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)