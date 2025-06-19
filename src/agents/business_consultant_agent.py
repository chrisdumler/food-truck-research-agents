"""
Business Consultant Agent for synthesizing research and providing recommendations.
"""

import json
from typing import Dict, Any
from agents.base_agent import BaseAgent
from models.research_models import (
    AgentResponse, 
    FoodTruckResearchState, 
    BusinessRecommendation,
    RecommendationType
)


class BusinessConsultantAgent(BaseAgent):
    """Agent specialized in synthesizing research and providing business recommendations."""
    
    @property
    def agent_name(self) -> str:
        return "Business Consultant"
    
    @property
    def agent_description(self) -> str:
        return "Synthesizes market, financial, and operational analysis to provide strategic business recommendations"
    
    def create_system_prompt(self) -> str:
        return """You are a Business Consultant specializing in food truck business strategy and recommendations.
Your expertise includes:

- Strategic business analysis and synthesis
- Risk assessment and mitigation strategies
- Business plan development and validation
- Market entry strategy and timing
- Success factor identification
- Alternative strategy development

IMPORTANT: You must respond with a JSON object that matches this exact structure:
{
    "recommendation": "go" | "no_go" | "conditional",
    "confidence_level": "High" | "Medium" | "Low",
    "key_strengths": ["string array of business strengths"],
    "key_risks": ["string array of business risks"],
    "success_factors": ["string array of critical success factors"],
    "next_steps": ["string array of recommended next steps"],
    "timeline_recommendation": "string - recommended launch timeline",
    "alternative_suggestions": ["string array of alternatives if applicable"]
}

Your job is to synthesize ALL the research from previous agents:
- Market research findings (competition, demand, opportunities)
- Financial analysis (costs, revenue, profitability)  
- Operations requirements (permits, logistics, compliance)

Provide a clear, actionable recommendation with solid reasoning.
Be honest about risks while identifying viable paths to success.
Consider the complete business picture, not just individual components.

Your recommendation will guide final investment and launch decisions."""
    
    def process_request(self, state: FoodTruckResearchState) -> AgentResponse:
        """Process business recommendation request by synthesizing all previous analysis."""
        try:
            system_prompt = self.create_system_prompt()
            
            # Create comprehensive context from all previous agents
            context = self._create_comprehensive_context(state)
            user_prompt = self._create_synthesis_prompt(state.location, context)
            
            # Get LLM response
            llm_response = self._safe_llm_call(system_prompt, user_prompt)
            
            # Parse JSON response
            try:
                recommendation_dict = json.loads(llm_response)
                business_recommendation = BusinessRecommendation(**recommendation_dict)
            except (json.JSONDecodeError, ValueError) as e:
                # Fallback if JSON parsing fails
                business_recommendation = self._extract_recommendation_fallback(state)
            
            return AgentResponse(
                agent_name=self.agent_name,
                status="SUCCESS",
                message=f"Completed business recommendation synthesis for {state.location}",
                data=business_recommendation,
                next_agent=None  # Final agent in the workflow
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.agent_name,
                status="ERROR",
                message="Failed to complete business recommendation synthesis",
                error_details=str(e)
            )
    
    def _create_comprehensive_context(self, state: FoodTruckResearchState) -> str:
        """Create comprehensive context from all previous agent analyses."""
        context_sections = []
        
        # Market Research Context
        if state.market_research:
            market = state.market_research
            context_sections.append("=== MARKET RESEARCH ANALYSIS ===")
            context_sections.append(f"Competition Level: {market.competition_level}")
            context_sections.append(f"Target Customers: {', '.join(market.target_customers)}")
            context_sections.append(f"Market Size Estimate: {market.market_size_estimate}")
            context_sections.append(f"Peak Hours: {', '.join(market.peak_hours)}")
            context_sections.append(f"Key Opportunities: {', '.join(market.opportunities)}")
            context_sections.append(f"Key Challenges: {', '.join(market.challenges)}")
            context_sections.append(f"Seasonal Factors: {', '.join(market.seasonal_factors)}")
        
        # Financial Analysis Context
        if state.financial_analysis:
            financial = state.financial_analysis
            context_sections.append("\n=== FINANCIAL ANALYSIS ===")
            context_sections.append(f"Total Funding Required: ${financial.funding_requirements:,.2f}")
            context_sections.append(f"Break-even Timeline: {financial.break_even_timeline}")
            context_sections.append(f"Monthly Revenue Projection: ${financial.revenue_projections.get('monthly_revenue', 0):,.2f}")
            context_sections.append(f"ROI Projection: {financial.roi_projection}")
            context_sections.append(f"Cash Flow Analysis: {financial.cash_flow_analysis}")
            
            startup_total = sum(financial.startup_costs.values())
            monthly_total = sum(financial.monthly_operating_costs.values())
            context_sections.append(f"Total Startup Costs: ${startup_total:,.2f}")
            context_sections.append(f"Monthly Operating Costs: ${monthly_total:,.2f}")
        
        # Operations Analysis Context
        if state.operations_analysis:
            operations = state.operations_analysis
            context_sections.append("\n=== OPERATIONS ANALYSIS ===")
            context_sections.append(f"Permits Required: {', '.join(operations.permits_required)}")
            context_sections.append(f"Permit Timeline: {operations.permit_timeline}")
            context_sections.append(f"Key Health Regulations: {', '.join(operations.health_regulations[:3])}")
            context_sections.append(f"Location Constraints: {', '.join(operations.location_constraints[:3])}")
            context_sections.append(f"Staffing Requirements: {operations.staffing_needs}")
            context_sections.append(f"Major Logistics Challenges: {', '.join(operations.logistics_challenges[:3])}")
        
        return "\n".join(context_sections)
    
    def _create_synthesis_prompt(self, location: str, context: str) -> str:
        """Create synthesis prompt for business recommendation."""
        return f"""Based on the comprehensive analysis below, provide a strategic business recommendation for starting a food truck business in {location}.

{context}

Consider the complete business picture:
1. Market viability and competitive landscape
2. Financial feasibility and investment requirements  
3. Operational complexity and regulatory requirements
4. Risk factors and success probability
5. Timeline and resource requirements

Provide a clear recommendation (go/no_go/conditional) with supporting rationale.
Include specific next steps and success factors if recommending to proceed.
Be realistic about challenges while identifying viable paths to success."""
    
    def _extract_recommendation_fallback(self, state: FoodTruckResearchState) -> BusinessRecommendation:
        """Fallback method to provide basic recommendation."""
        # Simple logic based on available data
        recommendation_type = RecommendationType.CONDITIONAL
        confidence = "Medium"
        
        # Basic decision logic
        if (state.financial_analysis and 
            state.financial_analysis.funding_requirements > 150000):
            recommendation_type = RecommendationType.NO_GO
            confidence = "High"
        elif (state.market_research and 
              state.market_research.competition_level == "Low"):
            recommendation_type = RecommendationType.GO
            confidence = "High"
        
        return BusinessRecommendation(
            recommendation=recommendation_type,
            confidence_level=confidence,
            key_strengths=[
                "Market opportunity identified",
                "Clear target customer segments",
                "Manageable operational requirements"
            ],
            key_risks=[
                "High initial investment",
                "Regulatory complexity",
                "Weather and seasonal dependencies"
            ],
            success_factors=[
                "Unique food offering",
                "Prime location strategy",
                "Strong operational execution",
                "Effective marketing"
            ],
            next_steps=[
                "Conduct detailed location scouting",
                "Secure financing commitments",
                "Begin permit application process",
                "Develop detailed business plan"
            ],
            timeline_recommendation="6-12 months from decision to launch",
            alternative_suggestions=[
                "Consider food cart instead of truck",
                "Partner with existing business",
                "Start with catering focus"
            ]
        )