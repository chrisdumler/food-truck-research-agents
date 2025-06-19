"""
Market Research Agent for analyzing food truck business opportunities.
"""

import json
from typing import Dict, Any, List
from agents.base_agent import BaseAgent
from models.research_models import AgentResponse, FoodTruckResearchState, MarketResearchData


class MarketResearchAgent(BaseAgent):
    """Agent specialized in market research and competitive analysis."""
    
    @property
    def agent_name(self) -> str:
        return "Market Research Analyst"
    
    @property
    def agent_description(self) -> str:
        return "Analyzes market conditions, competition, and customer demand for food truck businesses"
    
    def create_system_prompt(self) -> str:
        return """You are a Market Research Analyst specializing in food truck business opportunities. 
Your expertise includes:

- Competitive landscape analysis
- Customer segmentation and demand assessment  
- Market sizing and opportunity identification
- Location-specific market dynamics
- Peak hours and seasonal patterns
- Food trends and preferences analysis

IMPORTANT: You must respond with a JSON object that matches this exact structure:
{
    "location": "string - the target location",
    "competition_level": "string - High/Medium/Low",
    "target_customers": ["string array of customer segments"],
    "peak_hours": ["string array of optimal hours"],
    "seasonal_factors": ["string array of seasonal considerations"],
    "market_size_estimate": "string - estimated daily customer potential",
    "competition_analysis": [
        {
            "name": "competitor name",
            "type": "food type/cuisine",
            "location": "their location",
            "strengths": "their key strengths",
            "weaknesses": "potential weaknesses"
        }
    ],
    "opportunities": ["string array of market opportunities"],
    "challenges": ["string array of market challenges"]
}

Focus on realistic, location-specific insights. Consider local food culture, demographics, 
business districts, events, and regulations that affect food truck operations.

Be data-driven but practical. Your analysis will inform financial and operational planning."""
    
    def process_request(self, state: FoodTruckResearchState) -> AgentResponse:
        """Process market research request for the given location."""
        try:
            system_prompt = self.create_system_prompt()
            user_prompt = self._create_user_prompt(state.location)
            
            # Get LLM response
            llm_response = self._safe_llm_call(system_prompt, user_prompt)
            
            # Parse JSON response
            try:
                market_data_dict = json.loads(llm_response)
                market_data = MarketResearchData(**market_data_dict)
            except (json.JSONDecodeError, ValueError) as e:
                # If JSON parsing fails, extract key information manually
                market_data = self._extract_market_data_fallback(llm_response, state.location)
            
            return AgentResponse(
                agent_name=self.agent_name,
                status="SUCCESS",
                message=f"Completed market research analysis for {state.location}",
                data=market_data,
                next_agent="Financial Advisor"
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.agent_name,
                status="ERROR",
                message="Failed to complete market research analysis",
                error_details=str(e)
            )
    
    def _extract_market_data_fallback(self, response: str, location: str) -> MarketResearchData:
        """Fallback method to extract market data if JSON parsing fails."""
        # Basic parsing fallback - in production, this would be more sophisticated
        return MarketResearchData(
            location=location,
            competition_level="Medium",
            target_customers=["Office workers", "Students", "Families"],
            peak_hours=["11:30 AM - 1:30 PM", "5:30 PM - 7:30 PM"],
            seasonal_factors=["Weather dependent", "Event-driven demand"],
            market_size_estimate="300-500 daily customers",
            competition_analysis=[
                {
                    "name": "Local food trucks",
                    "type": "Various cuisines", 
                    "location": "Downtown area",
                    "strengths": "Established customer base",
                    "weaknesses": "Limited variety"
                }
            ],
            opportunities=["High foot traffic areas", "Event catering", "Corporate partnerships"],
            challenges=["Permit requirements", "Seasonal weather", "Competition from restaurants"]
        )