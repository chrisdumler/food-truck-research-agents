# Food Truck Research Agents

A multi-agent LangGraph system that uses specialized AI experts to research food truck business opportunities. This project explores multi-agent coordination patterns while producing genuinely useful business research.

## Project Overview

**Research Question:** "Should I start a food truck business in [location]?"

**Multi-Agent Team:**
- **Market Research Analyst** - Competition analysis, demand assessment, customer segments
- **Financial Advisor** - Startup costs, revenue projections, break-even analysis
- **Operations Consultant** - Permits, logistics, daily operations requirements
- **Business Consultant** - Synthesizes findings into actionable recommendations

## Learning Objectives

This project is designed to explore key multi-agent patterns:
- **Agent specialization** with distinct roles and expertise
- **Sequential handoffs** in LangGraph workflows
- **Information synthesis** across multiple expert perspectives
- **Structured output** via Pydantic models
- **Human-in-the-loop** validation and feedback

## SLC Development Approach

Following the [Human-AI Collaborative Development Methodology](./methodology/README.md):

### Simple (Current Phase)
**Goal:** Basic 3-agent sequential workflow
- Linear execution: Market → Financial → Operations → Business Synthesis
- Each agent produces structured research output
- Final consolidated report

**Success Criteria:**
- Agents produce distinct, relevant research
- Clean handoffs between agents  
- Coherent final synthesis
- Working LangGraph implementation

### Lovable (Next Phase)
**Enhancements:**
- Parallel agent execution where possible
- Location-specific research capabilities
- Interactive follow-up questions
- Enhanced report formatting

### Complete (Future Vision)
**Advanced Features:**
- Dynamic agent creation based on research topic
- Multi-round research iterations
- Complex coordination patterns
- Comprehensive business plan generation

## Architecture

```
User Query → Market Research Agent → Financial Advisor → Operations Consultant → Business Consultant → Final Report
```

**Key Components:**
- `src/agents/` - Individual agent implementations
- `src/models/` - Pydantic models for structured outputs
- `src/graph/` - LangGraph workflow orchestration
- `src/main.py` - Entry point and user interface

## Technology Stack

- **LangGraph** - Multi-agent workflow orchestration
- **Pydantic** - Structured data models and validation
- **OpenAI/Anthropic APIs** - LLM backend for agents
- **Python 3.11+** - Development environment

## Getting Started

1. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **API Configuration**
   ```bash
   export OPENAI_API_KEY="your-key-here"
   # or create .env file
   ```

3. **Run Research**
   ```bash
   python src/main.py
   ```

## Development Process

This project follows structured Human-AI collaboration:

1. **Work Requests** - Clear, scoped development tasks
2. **Checkpoint Validation** - Human review at key milestones
3. **Quality Gates** - Testing and validation before acceptance
4. **Iterative Improvement** - Continuous refinement based on feedback

See [methodology documentation](./methodology/) for detailed process templates.

## Current Status

🟡 **In Development** - Simple phase implementation

**Next Milestone:** Complete basic 3-agent sequential workflow with structured outputs

## Contributing

This is a learning project exploring multi-agent patterns. Focus areas:
- Agent coordination and handoff patterns
- LangGraph workflow design
- Structured output and data flow
- Human validation integration

## Project Structure

```
food-truck-research-agents/
├── methodology/           # Development process templates
├── src/
│   ├── agents/           # Individual agent implementations
│   ├── models/           # Pydantic data models
│   ├── graph/            # LangGraph workflow
│   └── main.py           # Application entry point
├── tests/                # Test suite
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

**Learning Focus:** Multi-agent coordination patterns in LangGraph while building something genuinely useful for business research.
