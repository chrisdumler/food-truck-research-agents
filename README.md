# Food Truck Research Agents

**A demonstration of Human-AI collaborative development methodology for building multi-agent systems.**

This project showcases how a workflow diagram image can be transformed into a working LangGraph multi-agent system through structured collaboration between a human project owner, an AI Product Manager (Pemtu), and a Coding Assistant (Claude Code).

## Project Origin

This project began with a workflow diagram image showing a multi-agent research assistant pattern. Through the Human-AI collaborative development methodology, we:

1. **Analyzed the workflow image** to understand multi-agent coordination patterns
2. **Adapted the concept** to food truck business research as a concrete learning domain
3. **Created structured work requests** using the SLC (Simple, Lovable, Complete) framework
4. **Implemented the system** through methodical PM-to-Coding Agent collaboration
5. **Validated functionality** through human testing and quality gates

The result is a working multi-agent system that demonstrates both the technical patterns and the collaborative process that created it.

## Project Overview

**Research Question:** "Should I start a food truck business in [location]?"

**Multi-Agent Team:**

- **Market Research Analyst** - Competition analysis, demand assessment, customer segments
- **Financial Advisor** - Startup costs, revenue projections, break-even analysis
- **Operations Consultant** - Permits, logistics, daily operations requirements
- **Business Consultant** - Synthesizes findings into actionable recommendations

## Demonstration Objectives

**Primary Goal:** Demonstrate the Human-AI collaborative development methodology in practice

**Technical Learning Areas:**

- **Multi-agent coordination** patterns in LangGraph
- **Agent specialization** with distinct roles and expertise
- **Sequential handoffs** and structured data flow
- **Workflow orchestration** from concept to implementation
- **Quality assurance** through human-in-the-loop validation

**Process Learning Areas:**

- **Structured work requests** using SLC framework
- **Checkpoint validation** and quality gates
- **PM-to-AI communication** patterns
- **Methodology adherence** and process improvement

## Development Methodology Demonstration

This project demonstrates the [Human-AI Collaborative Development Methodology](./methodology/README.md) in action:

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

```text
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

## Project Status

✅ **Phase 1 Complete** - Simple phase successfully implemented and validated

**Demonstrated Capabilities:**

- Working 4-agent sequential workflow (Market → Financial → Operations → Business)
- End-to-end LangGraph implementation with proper state management
- Professional CLI interface with report generation
- Comprehensive error handling and retry logic
- Full methodology compliance including structured communication

**Next Phase:** Ready for Lovable phase enhancements (parallel execution, enhanced research capabilities, interactive features)

## Methodology Demonstration Value

**For Teams Building AI Systems:**

- See structured PM-to-AI collaboration in practice
- Learn multi-agent coordination patterns
- Understand quality gate implementation
- Observe methodology adherence benefits

**For Learning Multi-Agent Development:**

- Working LangGraph StateGraph implementation
- Agent specialization and handoff patterns
- Structured data models with Pydantic
- Error handling and retry logic

**Note:** This is a demonstration project showcasing development methodology rather than a production business tool.

## Project Structure

```text
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

## Project Artifacts

**Code Implementation:** Complete working multi-agent system in `/src`
**Process Documentation:** Full methodology workflow in `/methodology`
**Communication History:** PM-AI collaboration artifacts in `/workflow` (gitignored)
**Validation Results:** Human testing confirmation and quality assessments

---

**Demonstration Focus:** How workflow diagrams become working systems through structured Human-AI collaboration using proven development methodology.
