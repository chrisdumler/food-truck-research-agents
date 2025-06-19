#!/usr/bin/env python3
"""
Development setup script that checks the structure without requiring external dependencies.
This allows us to validate the code structure before installing all dependencies.
"""

import sys
import os
from pathlib import Path
import importlib.util


def mock_langchain_imports():
    """Mock LangChain imports for structure testing."""
    
    # Create mock classes
    class MockChatOpenAI:
        def __init__(self, **kwargs):
            pass
            
        def invoke(self, messages):
            class MockResponse:
                content = '{"test": "response"}'
            return MockResponse()
    
    class MockChatAnthropic:
        def __init__(self, **kwargs):
            pass
            
        def invoke(self, messages):
            class MockResponse:
                content = '{"test": "response"}'
            return MockResponse()
    
    # Mock the modules
    import sys
    from types import ModuleType
    
    # Mock langchain_openai
    langchain_openai = ModuleType('langchain_openai')
    langchain_openai.ChatOpenAI = MockChatOpenAI
    sys.modules['langchain_openai'] = langchain_openai
    
    # Mock langchain_anthropic
    langchain_anthropic = ModuleType('langchain_anthropic')
    langchain_anthropic.ChatAnthropic = MockChatAnthropic
    sys.modules['langchain_anthropic'] = langchain_anthropic
    
    # Mock langgraph
    langgraph_graph = ModuleType('langgraph.graph')
    langgraph_graph.StateGraph = lambda x: None
    langgraph_graph.START = "START"
    langgraph_graph.END = "END"
    
    langgraph_message = ModuleType('langgraph.graph.message')
    langgraph_message.add_messages = lambda: None
    
    langgraph = ModuleType('langgraph')
    langgraph.graph = langgraph_graph
    
    sys.modules['langgraph'] = langgraph
    sys.modules['langgraph.graph'] = langgraph_graph
    sys.modules['langgraph.graph.message'] = langgraph_message


def test_structure_without_dependencies():
    """Test code structure without external dependencies."""
    print("🏗️  Food Truck Research Agents - Structure Validation")
    print("=" * 60)
    
    # Mock the dependencies
    mock_langchain_imports()
    
    # Add src to path
    src_path = Path(__file__).parent / "src"
    sys.path.insert(0, str(src_path))
    
    tests_passed = 0
    total_tests = 6
    
    print("🧪 Testing code structure...")
    
    try:
        # Test 1: Model imports and validation
        print("1. Testing Pydantic models...")
        from models.research_models import (
            FoodTruckResearchState,
            MarketResearchData,
            AgentResponse,
            RecommendationType
        )
        
        # Test model creation
        state = FoodTruckResearchState(location="Test City")
        assert state.location == "Test City"
        print("   ✅ Pydantic models working")
        tests_passed += 1
        
        # Test 2: Agent structure
        print("2. Testing agent structure...")
        from agents.base_agent import BaseAgent
        from agents.market_research_agent import MarketResearchAgent
        
        # Mock environment
        os.environ["OPENAI_API_KEY"] = "test-key"
        
        agent = MarketResearchAgent()
        assert agent.agent_name == "Market Research Analyst"
        assert callable(agent.create_system_prompt)
        print("   ✅ Agent structure working")
        tests_passed += 1
        
        # Test 3: All agent imports
        print("3. Testing all agent imports...")
        from agents.financial_advisor_agent import FinancialAdvisorAgent
        from agents.operations_consultant_agent import OperationsConsultantAgent
        from agents.business_consultant_agent import BusinessConsultantAgent
        
        agents = [
            MarketResearchAgent(),
            FinancialAdvisorAgent(),
            OperationsConsultantAgent(),
            BusinessConsultantAgent()
        ]
        
        for agent in agents:
            assert hasattr(agent, 'agent_name')
            assert hasattr(agent, 'create_system_prompt')
            
        print("   ✅ All agents importable")
        tests_passed += 1
        
        # Test 4: Retry handler
        print("4. Testing retry handler...")
        from utils.retry_handler import RetryHandler, is_retryable_api_error
        
        handler = RetryHandler()
        assert handler.max_attempts > 0
        assert is_retryable_api_error(Exception("rate limit")) == True
        print("   ✅ Retry handler working")
        tests_passed += 1
        
        # Test 5: System prompts
        print("5. Testing system prompts...")
        for agent in agents:
            prompt = agent.create_system_prompt()
            assert isinstance(prompt, str)
            assert len(prompt) > 50
        print("   ✅ System prompts generated")
        tests_passed += 1
        
        # Test 6: File structure
        print("6. Testing file structure...")
        required_files = [
            "src/models/research_models.py",
            "src/agents/base_agent.py",
            "src/agents/market_research_agent.py",
            "src/agents/financial_advisor_agent.py",
            "src/agents/operations_consultant_agent.py",
            "src/agents/business_consultant_agent.py",
            "src/utils/retry_handler.py",
            "src/main.py",
            "requirements.txt",
            ".env.example"
        ]
        
        missing_files = []
        for file_path in required_files:
            if not Path(file_path).exists():
                missing_files.append(file_path)
        
        if missing_files:
            print(f"   ❌ Missing files: {missing_files}")
        else:
            print("   ✅ All required files present")
            tests_passed += 1
        
    except Exception as e:
        print(f"   ❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"\n📊 Structure Validation Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 Code structure validation successful!")
        print("\n✨ Ready for dependencies installation and full testing")
        print("\nNext steps:")
        print("1. Create virtual environment: python -m venv venv")
        print("2. Activate: source venv/bin/activate (Unix) or venv\\Scripts\\activate (Windows)")
        print("3. Install dependencies: pip install -r requirements.txt")
        print("4. Set up API keys in .env file")
        print("5. Run the application: python src/main.py")
        return True
    else:
        print("❌ Structure validation failed - fix issues before proceeding")
        return False


if __name__ == "__main__":
    success = test_structure_without_dependencies()
    sys.exit(0 if success else 1)