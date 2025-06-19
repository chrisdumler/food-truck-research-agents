"""
Pydantic models for structured data handoffs between food truck research agents.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum


class RecommendationType(str, Enum):
    """Business recommendation types."""
    GO = "go"
    NO_GO = "no_go"
    CONDITIONAL = "conditional"


class MarketResearchData(BaseModel):
    """Market research findings from the Market Research Agent."""
    
    location: str = Field(description="Target location for food truck business")
    competition_level: str = Field(description="High/Medium/Low competition assessment")
    target_customers: List[str] = Field(description="Primary customer segments identified")
    peak_hours: List[str] = Field(description="Optimal operating hours")
    seasonal_factors: List[str] = Field(description="Seasonal considerations affecting business")
    market_size_estimate: str = Field(description="Estimated market size (e.g., '500-1000 daily customers')")
    competition_analysis: List[Dict[str, Any]] = Field(description="List of key competitors with details")
    opportunities: List[str] = Field(description="Market opportunities identified")
    challenges: List[str] = Field(description="Market challenges identified")


class FinancialAnalysisData(BaseModel):
    """Financial analysis from the Financial Advisor Agent."""
    
    startup_costs: Dict[str, float] = Field(description="Breakdown of initial investment costs")
    monthly_operating_costs: Dict[str, float] = Field(description="Monthly recurring expenses")
    revenue_projections: Dict[str, float] = Field(description="Revenue projections (daily/monthly/annual)")
    break_even_timeline: str = Field(description="Estimated time to break even")
    profit_margins: Dict[str, float] = Field(description="Expected profit margins by category")
    cash_flow_analysis: str = Field(description="Cash flow considerations and projections")
    funding_requirements: float = Field(description="Total funding needed to start")
    roi_projection: str = Field(description="Return on investment timeline and percentage")


class OperationsAnalysisData(BaseModel):
    """Operations analysis from the Operations Consultant Agent."""
    
    permits_required: List[str] = Field(description="Required permits and licenses")
    permit_costs: Dict[str, float] = Field(description="Cost breakdown for permits/licenses")
    permit_timeline: str = Field(description="Timeline to obtain all required permits")
    health_regulations: List[str] = Field(description="Key health and safety requirements")
    location_constraints: List[str] = Field(description="Location-specific operational constraints")
    equipment_requirements: List[str] = Field(description="Essential equipment needed")
    staffing_needs: Dict[str, Any] = Field(description="Staffing requirements and roles")
    daily_operations: List[str] = Field(description="Key daily operational considerations")
    logistics_challenges: List[str] = Field(description="Logistics and supply chain considerations")


class BusinessRecommendation(BaseModel):
    """Final business recommendation from the Business Consultant Agent."""
    
    recommendation: RecommendationType = Field(description="Overall business recommendation")
    confidence_level: str = Field(description="High/Medium/Low confidence in recommendation")
    key_strengths: List[str] = Field(description="Key business strengths identified")
    key_risks: List[str] = Field(description="Key business risks identified")
    success_factors: List[str] = Field(description="Critical factors for success")
    next_steps: List[str] = Field(description="Recommended next steps if proceeding")
    timeline_recommendation: str = Field(description="Recommended timeline for launch")
    alternative_suggestions: List[str] = Field(description="Alternative approaches or locations")


class FoodTruckResearchState(BaseModel):
    """Complete state object for the food truck research workflow."""
    
    location: str = Field(description="Target location for research")
    market_research: Optional[MarketResearchData] = Field(default=None, description="Market research findings")
    financial_analysis: Optional[FinancialAnalysisData] = Field(default=None, description="Financial analysis results")
    operations_analysis: Optional[OperationsAnalysisData] = Field(default=None, description="Operations analysis results")
    business_recommendation: Optional[BusinessRecommendation] = Field(default=None, description="Final business recommendation")
    messages: List[str] = Field(default_factory=list, description="Agent communication history")
    current_agent: Optional[str] = Field(default=None, description="Currently active agent")
    
    class Config:
        """Pydantic configuration."""
        arbitrary_types_allowed = True


class AgentResponse(BaseModel):
    """Standard response format for all agents."""
    
    agent_name: str = Field(description="Name of the responding agent")
    status: str = Field(description="SUCCESS or ERROR")
    message: str = Field(description="Human-readable status message")
    data: Optional[Any] = Field(default=None, description="Agent-specific data payload")
    next_agent: Optional[str] = Field(default=None, description="Recommended next agent in workflow")
    error_details: Optional[str] = Field(default=None, description="Error details if status is ERROR")