# AI PM Methodology: Human-AI Collaborative Development Workflow

## Overview

This methodology enables structured, high-quality collaboration between human project managers and AI coding agents. It combines the SLC (Simple, Lovable, Complete) framework with human-in-the-loop quality gates to achieve rapid development with professional results.

## Core Principles

### 1. Structured Communication
- **Templated exchanges** ensure consistent information flow
- **Clear role separation** between PM strategy and AI execution
- **Audit trail creation** for all decisions and progress

### 2. Quality-First Development
- **SLC scoping** prevents scope creep and ensures deliverable features
- **Checkpoint validation** catches issues before they compound
- **Human testing** validates real-world functionality

### 3. Continuous Learning
- **Time tracking** improves estimation accuracy
- **Process assessment** refines methodology over time
- **Knowledge capture** ensures insights aren't lost

## Workflow Process

### Phase 1: Planning & Scoping
**PM Action:** Create work request using SLC framework

1. Use `work-request-template.md` to define sprint
2. Focus on **Simple** (single objective), **Lovable** (user value), **Complete** (full workflow)
3. Include technical context, checkpoints, and acceptance criteria
4. Submit as single prompt to coding agent

### Phase 2: Clarification (If Needed)
**Coding Agent Action:** Ask questions using Q&A template

1. Agent creates `work-request-[number]-qa.md` if clarification needed
2. PM responds with specific answers and guidance
3. Agent waits for complete answers before proceeding

### Phase 3: Implementation
**Coding Agent Action:** Execute work with checkpoint pauses

1. Agent follows SLC scope and technical guidance
2. Pauses at defined checkpoints for PM validation
3. Maintains focus on deliverable outcomes

### Phase 4: Progress Reporting
**Coding Agent Action:** Provide structured status update

1. Use `standup-report-template.md` for comprehensive progress report
2. Include time analysis, challenges, learnings, and artifacts
3. Ask specific questions about decisions or next steps

### Phase 5: Initial Assessment
**PM Action:** Review and provide strategic direction

1. Use `pm-response-template.md` for structured feedback
2. Make acceptance decision (approved/conditional/rejected)
3. Answer agent questions and provide next steps
4. May require human testing before final approval

### Phase 6: Validation Testing
**PM Action:** Hands-on testing and final approval

1. Actually test the implemented functionality
2. Use `pm-validation-template.md` to document results
3. Provide final acceptance decision
4. Authorize next work request if appropriate

## Template Usage Guide

### Work Request Template
**Purpose:** Kick off development sprint  
**Key Sections:**
- **SLC Definition:** Scope with clear boundaries
- **Technical Context:** Current state and constraints  
- **Checkpoints:** Human validation points
- **Coding Agent Instructions:** Process guidance for AI

**Success Factors:**
- Single, clear objective
- Specific technical details
- Realistic time estimates
- Clear acceptance criteria

### Q&A Template
**Purpose:** Clarify requirements during implementation  
**Usage Pattern:**
- Agent identifies questions early in process
- PM provides specific, actionable answers
- Clear resolution tracking

### Standup Report Template
**Purpose:** Comprehensive progress and status update  
**Key Elements:**
- Time investment analysis
- Technical accomplishments
- Challenges and learnings
- Quality assessment
- Next steps and blockers

### PM Response Template
**Purpose:** Strategic direction and decision-making  
**Key Decisions:**
- Accept/reject/conditionally approve work
- Answer specific questions from agent
- Identify next priorities
- Assess process effectiveness

### PM Validation Template
**Purpose:** Final acceptance after hands-on testing  
**Critical Function:**
- Validates real-world functionality
- Provides definitive approval
- Authorizes next phase
- Captures validation learnings

## Communication Patterns

### Standard Sprint Flow
```
Work Request → Implementation → Standup Report → PM Response → PM Validation → Next Work Request
```

### With Clarification
```
Work Request → Q&A → Implementation → Standup Report → PM Response → PM Validation → Next Work Request
```

### With Iteration
```
Work Request → Implementation → Standup Report → PM Response (needs revision) → Implementation → Standup Report → PM Validation
```

## Key Success Factors

### For Project Managers

1. **Clear SLC Scoping**
   - Define single, focused objectives
   - Specify explicit exclusions
   - Set measurable success criteria

2. **Strategic Oversight**
   - Focus on outcomes, not implementation details
   - Maintain project vision and priorities
   - Make timely decisions at checkpoints

3. **Quality Gates**
   - Always test functionality yourself
   - Validate real user experience
   - Don't skip validation steps

### For AI Coding Agents

1. **Follow Templates**
   - Use structured communication formats
   - Provide comprehensive status updates
   - Ask questions when uncertain

2. **Respect Checkpoints**
   - Pause for human validation
   - Don't exceed defined scope
   - Focus on SLC objectives

3. **Quality Focus**
   - Prioritize working functionality
   - Include comprehensive testing
   - Document decisions and tradeoffs

## Methodology Benefits

### Speed & Efficiency
- **96% faster execution** than traditional estimates (based on APL project data)
- **Reduced communication overhead** through structured templates
- **Parallel work streams** enabled by clear scoping

### Quality Assurance
- **Zero regressions** through systematic checkpoint validation
- **Human oversight** at critical decision points
- **Comprehensive testing** built into process

### Knowledge Capture
- **Complete audit trail** of decisions and progress
- **Process improvements** identified and documented
- **Reusable artifacts** for future projects

### Scalability
- **Template-driven** approach enables team adoption
- **Methodology documentation** supports training and onboarding
- **Process refinement** based on systematic feedback

## Estimation Guidelines

### AI Coding Agent Time Patterns
- **Clear requirements + good architecture** = Extremely fast execution
- **Ambiguous scope + poor foundation** = Slower, iterative development
- **Integration complexity** scales execution time
- **UI/UX work** may require more iteration than pure logic

### Typical Sprint Sizes
- **Simple feature:** 1-3 hours
- **Complex integration:** 3-6 hours  
- **New capability:** 6-12 hours
- **Major refactor:** 12+ hours

### Quality vs. Speed Tradeoffs
- **Fast execution** requires excellent upfront scoping
- **High quality** demands human validation checkpoints
- **Process adherence** enables sustainable velocity

## Getting Started

### Prerequisites
- AI coding agent access (Claude Code, Cursor, etc.)
- Version control system (Git recommended)
- Project with existing codebase or clear starting point

### First Sprint Setup
1. Copy all templates to your project documentation
2. Create initial work request using template
3. Submit to coding agent with process instructions
4. Follow workflow through completion
5. Assess and refine for next sprint

### Continuous Improvement
- Track time estimates vs. actuals
- Identify template improvements
- Refine checkpoint criteria
- Document methodology learnings

---

**This methodology transforms AI coding collaboration from ad-hoc interactions into a systematic, high-quality development process that scales across teams and projects.**
