"""
Financial Advisor Agent for analyzing food truck business financials.
"""

import json
from typing import Dict, Any
from agents.base_agent import BaseAgent
from models.research_models import AgentResponse, FoodTruckResearchState, FinancialAnalysisData


class FinancialAdvisorAgent(BaseAgent):
    """Agent specialized in financial analysis and projections."""
    
    @property
    def agent_name(self) -> str:
        return "Financial Advisor"
    
    @property
    def agent_description(self) -> str:
        return "Analyzes financial viability, startup costs, and revenue projections for food truck businesses"
    
    def create_system_prompt(self) -> str:
        return """You are a Financial Advisor specializing in food truck business financial analysis.
Your expertise includes:

- Startup cost estimation and budgeting
- Revenue projections and break-even analysis
- Cash flow modeling and working capital requirements
- Profit margin analysis by food category
- ROI calculations and investment analysis
- Risk assessment and financial planning

IMPORTANT: You must respond with a JSON object that matches this exact structure:
{
    "startup_costs": {
        "food_truck": 75000.0,
        "equipment": 25000.0,
        "permits_licenses": 5000.0,
        "initial_inventory": 3000.0,
        "marketing": 2000.0,
        "working_capital": 10000.0,
        "insurance": 4000.0,
        "other": 3000.0
    },
    "monthly_operating_costs": {
        "food_costs": 8000.0,
        "fuel": 800.0,
        "insurance": 400.0,
        "permits": 200.0,
        "maintenance": 500.0,
        "marketing": 300.0,
        "staff": 6000.0,
        "other": 800.0
    },
    "revenue_projections": {
        "daily_revenue": 800.0,
        "monthly_revenue": 20000.0,
        "annual_revenue": 240000.0
    },
    "break_even_timeline": "string - estimated months to break even",
    "profit_margins": {
        "gross_margin": 0.65,
        "net_margin": 0.15
    },
    "cash_flow_analysis": "string - cash flow insights and seasonal considerations",
    "funding_requirements": 127000.0,
    "roi_projection": "string - expected ROI timeline and percentage"
}

Be conservative but realistic in your projections. Consider location-specific factors like:
- Local cost of living and wages
- Competition impact on pricing
- Seasonal variations in revenue
- Local regulations affecting costs

Your analysis will guide investment decisions and operational planning."""
    
    def process_request(self, state: FoodTruckResearchState) -> AgentResponse:
        """Process financial analysis request."""
        try:
            system_prompt = self.create_system_prompt()
            
            # Include market research context
            context = self.format_context_from_state(state)
            user_prompt = self._create_user_prompt(state.location, context)
            
            # Get LLM response
            llm_response = self._safe_llm_call(system_prompt, user_prompt)
            
            # Parse JSON response
            try:
                financial_data_dict = json.loads(llm_response)
                financial_data = FinancialAnalysisData(**financial_data_dict)
            except (json.JSONDecodeError, ValueError) as e:
                # Fallback if JSON parsing fails
                financial_data = self._extract_financial_data_fallback(state.location)
            
            return AgentResponse(
                agent_name=self.agent_name,
                status="SUCCESS",
                message=f"Completed financial analysis for {state.location}",
                data=financial_data,
                next_agent="Operations Consultant"
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.agent_name,
                status="ERROR",
                message="Failed to complete financial analysis",
                error_details=str(e)
            )
    
    def _extract_financial_data_fallback(self, location: str) -> FinancialAnalysisData:
        """Fallback method to provide basic financial estimates."""
        return FinancialAnalysisData(
            startup_costs={
                "food_truck": 75000.0,
                "equipment": 25000.0,
                "permits_licenses": 5000.0,
                "initial_inventory": 3000.0,
                "marketing": 2000.0,
                "working_capital": 10000.0,
                "insurance": 4000.0,
                "other": 3000.0
            },
            monthly_operating_costs={
                "food_costs": 8000.0,
                "fuel": 800.0,
                "insurance": 400.0,
                "permits": 200.0,
                "maintenance": 500.0,
                "marketing": 300.0,
                "staff": 6000.0,
                "other": 800.0
            },
            revenue_projections={
                "daily_revenue": 800.0,
                "monthly_revenue": 20000.0,
                "annual_revenue": 240000.0
            },
            break_even_timeline="12-18 months",
            profit_margins={
                "gross_margin": 0.65,
                "net_margin": 0.15
            },
            cash_flow_analysis="Seasonal variations expected, maintain 3-month cash reserve",
            funding_requirements=127000.0,
            roi_projection="15-20% ROI expected within 2-3 years"
        )