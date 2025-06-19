"""
LangGraph workflow for food truck research agents.
"""

from typing import Dict, Any, Annotated, Optional
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from models.research_models import FoodTruckResearchState, AgentResponse
from agents.market_research_agent import MarketResearchAgent
from agents.financial_advisor_agent import FinancialAdvisorAgent
from agents.operations_consultant_agent import OperationsConsultantAgent
from agents.business_consultant_agent import BusinessConsultantAgent


class WorkflowState(TypedDict):
    """State for the LangGraph workflow."""
    location: str
    market_research: Optional[Dict[str, Any]]
    financial_analysis: Optional[Dict[str, Any]]
    operations_analysis: Optional[Dict[str, Any]]
    business_recommendation: Optional[Dict[str, Any]]
    messages: Annotated[list, add_messages]
    current_agent: str
    status: str
    error_message: str


class FoodTruckResearchWorkflow:
    """LangGraph workflow orchestrating food truck research agents."""
    
    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.1):
        """Initialize the workflow with agent instances."""
        self.market_agent = MarketResearchAgent(model_name, temperature)
        self.financial_agent = FinancialAdvisorAgent(model_name, temperature)
        self.operations_agent = OperationsConsultantAgent(model_name, temperature)
        self.business_agent = BusinessConsultantAgent(model_name, temperature)
        
        # Build the workflow graph
        self.workflow = self._build_workflow()
    
    def _build_workflow(self) -> StateGraph:
        """Build the LangGraph StateGraph workflow."""
        
        # Create the state graph
        workflow = StateGraph(WorkflowState)
        
        # Add agent nodes
        workflow.add_node("market_research_node", self._market_research_node)
        workflow.add_node("financial_analysis_node", self._financial_analysis_node)
        workflow.add_node("operations_analysis_node", self._operations_analysis_node)
        workflow.add_node("business_synthesis_node", self._business_synthesis_node)
        
        # Define the sequential flow
        workflow.add_edge(START, "market_research_node")
        workflow.add_edge("market_research_node", "financial_analysis_node")
        workflow.add_edge("financial_analysis_node", "operations_analysis_node")
        workflow.add_edge("operations_analysis_node", "business_synthesis_node")
        workflow.add_edge("business_synthesis_node", END)
        
        return workflow.compile()
    
    def _market_research_node(self, state: WorkflowState) -> Dict[str, Any]:
        """Execute market research analysis."""
        try:
            # Create research state from workflow state
            research_state = FoodTruckResearchState(
                location=state["location"],
                messages=[str(msg) for msg in state.get("messages", [])]
            )
            
            # Execute market research
            response: AgentResponse = self.market_agent.process_request(research_state)
            
            if response.status == "SUCCESS":
                return {
                    "market_research": response.data.dict() if response.data else {},
                    "current_agent": "Financial Advisor",
                    "status": "success",
                    "messages": state.get("messages", []) + [f"Market Research completed for {state['location']}"]
                }
            else:
                return {
                    "status": "error",
                    "error_message": response.error_details or "Market research failed",
                    "messages": state.get("messages", []) + [f"Market Research failed: {response.message}"]
                }
                
        except Exception as e:
            return {
                "status": "error",
                "error_message": f"Market research node error: {str(e)}",
                "messages": state.get("messages", []) + [f"Market Research error: {str(e)}"]
            }
    
    def _financial_analysis_node(self, state: WorkflowState) -> Dict[str, Any]:
        """Execute financial analysis."""
        try:
            # Create research state with market research context
            research_state = FoodTruckResearchState(
                location=state["location"],
                market_research=state.get("market_research") if state.get("market_research") else None,
                messages=[str(msg) for msg in state.get("messages", [])]
            )
            
            # Execute financial analysis
            response: AgentResponse = self.financial_agent.process_request(research_state)
            
            if response.status == "SUCCESS":
                return {
                    "financial_analysis": response.data.dict() if response.data else {},
                    "current_agent": "Operations Consultant",
                    "status": "success",
                    "messages": state.get("messages", []) + [f"Financial Analysis completed for {state['location']}"]
                }
            else:
                return {
                    "status": "error",
                    "error_message": response.error_details or "Financial analysis failed",
                    "messages": state.get("messages", []) + [f"Financial Analysis failed: {response.message}"]
                }
                
        except Exception as e:
            return {
                "status": "error",
                "error_message": f"Financial analysis node error: {str(e)}",
                "messages": state.get("messages", []) + [f"Financial Analysis error: {str(e)}"]
            }
    
    def _operations_analysis_node(self, state: WorkflowState) -> Dict[str, Any]:
        """Execute operations analysis."""
        try:
            # Create research state with previous context
            research_state = FoodTruckResearchState(
                location=state["location"],
                market_research=state.get("market_research") if state.get("market_research") else None,
                financial_analysis=state.get("financial_analysis") if state.get("financial_analysis") else None,
                messages=[str(msg) for msg in state.get("messages", [])]
            )
            
            # Execute operations analysis
            response: AgentResponse = self.operations_agent.process_request(research_state)
            
            if response.status == "SUCCESS":
                return {
                    "operations_analysis": response.data.dict() if response.data else {},
                    "current_agent": "Business Consultant",
                    "status": "success",
                    "messages": state.get("messages", []) + [f"Operations Analysis completed for {state['location']}"]
                }
            else:
                return {
                    "status": "error",
                    "error_message": response.error_details or "Operations analysis failed",
                    "messages": state.get("messages", []) + [f"Operations Analysis failed: {response.message}"]
                }
                
        except Exception as e:
            return {
                "status": "error",
                "error_message": f"Operations analysis node error: {str(e)}",
                "messages": state.get("messages", []) + [f"Operations Analysis error: {str(e)}"]
            }
    
    def _business_synthesis_node(self, state: WorkflowState) -> Dict[str, Any]:
        """Execute business recommendation synthesis."""
        try:
            # Create complete research state
            research_state = FoodTruckResearchState(
                location=state["location"],
                market_research=state.get("market_research") if state.get("market_research") else None,
                financial_analysis=state.get("financial_analysis") if state.get("financial_analysis") else None,
                operations_analysis=state.get("operations_analysis") if state.get("operations_analysis") else None,
                messages=[str(msg) for msg in state.get("messages", [])]
            )
            
            # Execute business synthesis
            response: AgentResponse = self.business_agent.process_request(research_state)
            
            if response.status == "SUCCESS":
                return {
                    "business_recommendation": response.data.dict() if response.data else {},
                    "current_agent": "Complete",
                    "status": "success",
                    "messages": state.get("messages", []) + [f"Business Recommendation completed for {state['location']}"]
                }
            else:
                return {
                    "status": "error",
                    "error_message": response.error_details or "Business synthesis failed",
                    "messages": state.get("messages", []) + [f"Business Synthesis failed: {response.message}"]
                }
                
        except Exception as e:
            return {
                "status": "error",
                "error_message": f"Business synthesis node error: {str(e)}",
                "messages": state.get("messages", []) + [f"Business Synthesis error: {str(e)}"]
            }
    
    def run_research(self, location: str) -> Dict[str, Any]:
        """Run the complete food truck research workflow."""
        
        # Initialize workflow state
        initial_state: WorkflowState = {
            "location": location,
            "market_research": None,
            "financial_analysis": None,
            "operations_analysis": None,
            "business_recommendation": None,
            "messages": [f"Starting food truck research for {location}"],
            "current_agent": "Market Research Analyst",
            "status": "starting",
            "error_message": ""
        }
        
        try:
            # Execute the workflow
            final_state = self.workflow.invoke(initial_state)
            return final_state
            
        except Exception as e:
            return {
                **initial_state,
                "status": "error",
                "error_message": f"Workflow execution failed: {str(e)}",
                "messages": initial_state["messages"] + [f"Workflow error: {str(e)}"]
            }
    
    def format_results(self, results: Dict[str, Any]) -> str:
        """Format workflow results into a readable report."""
        
        if results.get("status") == "error":
            return f"Research failed: {results.get('error_message', 'Unknown error')}"
        
        location = results.get("location", "Unknown Location")
        report_lines = [
            f"# Food Truck Business Research Report: {location}",
            "=" * 60,
            ""
        ]
        
        # Market Research Section
        market_data = results.get("market_research", {})
        if market_data:
            report_lines.extend([
                "## Market Research Analysis",
                f"**Competition Level:** {market_data.get('competition_level', 'N/A')}",
                f"**Target Customers:** {', '.join(market_data.get('target_customers', []))}",
                f"**Market Size:** {market_data.get('market_size_estimate', 'N/A')}",
                f"**Peak Hours:** {', '.join(market_data.get('peak_hours', []))}",
                f"**Key Opportunities:** {', '.join(market_data.get('opportunities', []))}",
                ""
            ])
        
        # Financial Analysis Section
        financial_data = results.get("financial_analysis", {})
        if financial_data:
            funding = financial_data.get("funding_requirements", 0)
            report_lines.extend([
                "## Financial Analysis",
                f"**Total Funding Required:** ${funding:,.2f}",
                f"**Break-even Timeline:** {financial_data.get('break_even_timeline', 'N/A')}",
                f"**ROI Projection:** {financial_data.get('roi_projection', 'N/A')}",
                ""
            ])
        
        # Operations Section
        operations_data = results.get("operations_analysis", {})
        if operations_data:
            permits = operations_data.get("permits_required", [])
            report_lines.extend([
                "## Operations Requirements",
                f"**Required Permits:** {', '.join(permits)}",
                f"**Permit Timeline:** {operations_data.get('permit_timeline', 'N/A')}",
                f"**Staffing Needs:** {operations_data.get('staffing_needs', {}).get('minimum_staff', 'N/A')} minimum staff",
                ""
            ])
        
        # Business Recommendation Section
        business_data = results.get("business_recommendation", {})
        if business_data:
            recommendation = business_data.get("recommendation", "N/A").upper()
            confidence = business_data.get("confidence_level", "N/A")
            report_lines.extend([
                "## Business Recommendation",
                f"**Recommendation:** {recommendation} (Confidence: {confidence})",
                f"**Key Strengths:** {', '.join(business_data.get('key_strengths', []))}",
                f"**Key Risks:** {', '.join(business_data.get('key_risks', []))}",
                f"**Timeline:** {business_data.get('timeline_recommendation', 'N/A')}",
                ""
            ])
            
            next_steps = business_data.get("next_steps", [])
            if next_steps:
                report_lines.extend([
                    "**Recommended Next Steps:**",
                    *[f"- {step}" for step in next_steps],
                    ""
                ])
        
        return "\n".join(report_lines)