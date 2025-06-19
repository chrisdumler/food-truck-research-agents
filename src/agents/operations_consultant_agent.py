"""
Operations Consultant Agent for analyzing food truck operational requirements.
"""

import json
from typing import Dict, Any
from agents.base_agent import BaseAgent
from models.research_models import AgentResponse, FoodTruckResearchState, OperationsAnalysisData


class OperationsConsultantAgent(BaseAgent):
    """Agent specialized in operational requirements and logistics."""
    
    @property
    def agent_name(self) -> str:
        return "Operations Consultant"
    
    @property  
    def agent_description(self) -> str:
        return "Analyzes operational requirements, permits, logistics, and daily operations for food truck businesses"
    
    def create_system_prompt(self) -> str:
        return """You are an Operations Consultant specializing in food truck business operations.
Your expertise includes:

- Permit and licensing requirements by jurisdiction
- Health department regulations and compliance
- Equipment specifications and requirements
- Staffing needs and operational workflows
- Location restrictions and parking regulations
- Supply chain and logistics planning
- Daily operational procedures and best practices

IMPORTANT: You must respond with a JSON object that matches this exact structure:
{
    "permits_required": ["string array of required permits/licenses"],
    "permit_costs": {
        "business_license": 200.0,
        "food_service_permit": 500.0,
        "mobile_vendor_permit": 1000.0,
        "fire_permit": 150.0,
        "other_permits": 300.0
    },
    "permit_timeline": "string - time needed to obtain permits",
    "health_regulations": ["string array of key health requirements"],
    "location_constraints": ["string array of operational constraints"],
    "equipment_requirements": ["string array of essential equipment"],
    "staffing_needs": {
        "minimum_staff": 2,
        "peak_staff": 4,
        "roles": ["Manager/Cook", "Cashier", "Prep Cook", "Driver"],
        "labor_costs_hourly": {
            "manager": 20.0,
            "cook": 18.0,
            "cashier": 16.0,
            "prep": 15.0
        }
    },
    "daily_operations": ["string array of key daily tasks"],
    "logistics_challenges": ["string array of supply chain considerations"]
}

Focus on location-specific regulations and practical operational considerations.
Consider local health department requirements, parking restrictions, and zoning laws.
Be thorough but practical in your recommendations.

Your analysis will guide implementation planning and operational setup."""
    
    def process_request(self, state: FoodTruckResearchState) -> AgentResponse:
        """Process operations analysis request."""
        try:
            system_prompt = self.create_system_prompt()
            
            # Include previous analysis context
            context = self.format_context_from_state(state)
            user_prompt = self._create_user_prompt(state.location, context)
            
            # Get LLM response
            llm_response = self._safe_llm_call(system_prompt, user_prompt)
            
            # Parse JSON response
            try:
                operations_data_dict = json.loads(llm_response)
                operations_data = OperationsAnalysisData(**operations_data_dict)
            except (json.JSONDecodeError, ValueError) as e:
                # Fallback if JSON parsing fails
                operations_data = self._extract_operations_data_fallback(state.location)
            
            return AgentResponse(
                agent_name=self.agent_name,
                status="SUCCESS",
                message=f"Completed operations analysis for {state.location}",
                data=operations_data,
                next_agent="Business Consultant"
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.agent_name,
                status="ERROR",
                message="Failed to complete operations analysis",
                error_details=str(e)
            )
    
    def _extract_operations_data_fallback(self, location: str) -> OperationsAnalysisData:
        """Fallback method to provide basic operations estimates."""
        return OperationsAnalysisData(
            permits_required=[
                "Business License",
                "Food Service Permit", 
                "Mobile Vendor Permit",
                "Fire Department Permit",
                "Zoning Permit"
            ],
            permit_costs={
                "business_license": 200.0,
                "food_service_permit": 500.0,
                "mobile_vendor_permit": 1000.0,
                "fire_permit": 150.0,
                "other_permits": 300.0
            },
            permit_timeline="4-8 weeks to obtain all permits",
            health_regulations=[
                "Food handler certifications required",
                "Regular health inspections",
                "Temperature monitoring logs",
                "Hand washing stations",
                "Proper food storage protocols"
            ],
            location_constraints=[
                "Distance restrictions from restaurants",
                "Designated parking zones only",
                "Time limits on parking",
                "Noise ordinance compliance",
                "Special event permits needed"
            ],
            equipment_requirements=[
                "Commercial-grade cooking equipment",
                "Refrigeration units",
                "Generator or electrical hookup",
                "Fire suppression system",
                "Hand washing station",
                "Point of sale system",
                "Storage and prep areas"
            ],
            staffing_needs={
                "minimum_staff": 2,
                "peak_staff": 4,
                "roles": ["Manager/Cook", "Cashier", "Prep Cook", "Driver"],
                "labor_costs_hourly": {
                    "manager": 20.0,
                    "cook": 18.0,
                    "cashier": 16.0,
                    "prep": 15.0
                }
            },
            daily_operations=[
                "Pre-service equipment checks",
                "Food prep and inventory",
                "Location setup and permits",
                "Service operations",
                "End-of-day cleaning and storage",
                "Daily sales reporting"
            ],
            logistics_challenges=[
                "Fresh ingredient sourcing",
                "Propane and fuel management",
                "Waste disposal logistics",
                "Equipment maintenance scheduling",
                "Seasonal storage considerations"
            ]
        )