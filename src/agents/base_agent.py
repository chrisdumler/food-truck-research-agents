"""
Base agent class for food truck research agents.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import os
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from models.research_models import AgentResponse, FoodTruckResearchState
from utils.retry_handler import retry_api_call


class BaseAgent(ABC):
    """Base class for all food truck research agents."""
    
    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.1):
        """Initialize the base agent with LLM configuration."""
        self.model_name = model_name
        self.temperature = temperature
        self.llm = self._initialize_llm()
        
    def _initialize_llm(self):
        """Initialize the appropriate LLM based on model name."""
        if "gpt" in self.model_name.lower():
            return ChatOpenAI(
                model=self.model_name,
                temperature=self.temperature,
                api_key=os.getenv("OPENAI_API_KEY")
            )
        elif "claude" in self.model_name.lower():
            return ChatAnthropic(
                model=self.model_name,
                temperature=self.temperature,
                api_key=os.getenv("ANTHROPIC_API_KEY")
            )
        else:
            # Default to OpenAI
            return ChatOpenAI(
                model="gpt-4",
                temperature=self.temperature,
                api_key=os.getenv("OPENAI_API_KEY")
            )
    
    @property
    @abstractmethod
    def agent_name(self) -> str:
        """Return the agent's name."""
        pass
    
    @property
    @abstractmethod
    def agent_description(self) -> str:
        """Return the agent's role description."""
        pass
    
    @abstractmethod
    def create_system_prompt(self) -> str:
        """Create the system prompt for this agent."""
        pass
    
    @abstractmethod
    def process_request(self, state: FoodTruckResearchState) -> AgentResponse:
        """Process a research request and return structured response."""
        pass
    
    def _create_user_prompt(self, location: str, context: Optional[str] = None) -> str:
        """Create user prompt with location and optional context."""
        base_prompt = f"Please analyze the food truck business opportunity in {location}."
        
        if context:
            base_prompt += f"\n\nContext from previous analysis:\n{context}"
            
        base_prompt += "\n\nProvide a comprehensive analysis based on your expertise."
        return base_prompt
    
    @retry_api_call(max_attempts=3, base_delay=1.0)
    def _safe_llm_call(self, system_prompt: str, user_prompt: str) -> str:
        """Make a safe LLM call with error handling and retry logic."""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response = self.llm.invoke(messages)
        
        if not response or not hasattr(response, 'content'):
            raise Exception(f"Invalid response from LLM for {self.agent_name}")
        
        return response.content
    
    def format_context_from_state(self, state: FoodTruckResearchState) -> str:
        """Format context information from previous agents."""
        context_parts = []
        
        if state.market_research:
            context_parts.append("MARKET RESEARCH FINDINGS:")
            context_parts.append(f"- Competition Level: {state.market_research.competition_level}")
            context_parts.append(f"- Target Customers: {', '.join(state.market_research.target_customers)}")
            context_parts.append(f"- Market Size: {state.market_research.market_size_estimate}")
            
        if state.financial_analysis:
            context_parts.append("\nFINANCIAL ANALYSIS:")
            context_parts.append(f"- Funding Required: ${state.financial_analysis.funding_requirements:,.2f}")
            context_parts.append(f"- Break-even Timeline: {state.financial_analysis.break_even_timeline}")
            
        if state.operations_analysis:
            context_parts.append("\nOPERATIONS ANALYSIS:")
            context_parts.append(f"- Permits Required: {', '.join(state.operations_analysis.permits_required)}")
            context_parts.append(f"- Permit Timeline: {state.operations_analysis.permit_timeline}")
            
        return "\n".join(context_parts) if context_parts else ""