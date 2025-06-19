# Work Request Template for PM-to-Coding Agent

## Purpose

Structured sprint specification that provides coding agents with clear scope, context, and success criteria using the SLC (Simple, Lovable, Complete) framework.

## When to Use

- Starting any new development sprint with AI coding agents
- Breaking down larger features into manageable work units
- Ensuring clear communication of requirements and boundaries
- Establishing quality gates and checkpoint validation

## File Naming Convention

`work-request-[number]-[brief-description].md`

## Template Structure

```markdown
# Work Request #[NUMBER]: [Title]

## SPRINT HEADER

```text
SPRINT ID: [PROJECT-NUMBER-description]
DURATION: [X-X hours estimated]
FRAMEWORK: SLC
PM: [Human PM Name]
CODING AGENT: [AI Agent Name/Type]
```

## SLC DEFINITION

### SIMPLE 🎯

**Single Focus:** [One clear, specific objective]

- **Core Function:** [Primary capability being built]
- **Scope Boundary:** [Explicit exclusions - what NOT to build]
- **Success Definition:** [Quantifiable success criteria]

### LOVABLE ❤️

**User Impact:** [How this creates visible value]

- **Visible Outcome:** [What users will experience]
- **Quality Bar:** [Standards for user experience]
- **Demo Value:** [How this contributes to overall project goals]

### COMPLETE ✅

**Full Workflow:** [End-to-end process being implemented]

- **Input/Output:** [Data flow specification]
- **Integration Points:** [How this connects to existing system]
- **Test Scenarios:** [Key test cases that must pass]

## TECHNICAL CONTEXT

### Current State

```text
PROJECT: [Project Name and Path]
BRANCH: [Current branch or branching strategy]
KEY FILES: 
  - [file1.py] ([current state/purpose])
  - [file2.py] ([current state/purpose])
DEPENDENCIES: [Required packages, APIs, etc.]
LAST COMMIT: [Reference point for starting work]
```

### Architecture Constraints

```text
MAINTAIN: [Existing patterns/conventions to preserve]
EXTEND: [Files/modules to enhance]
AVOID: [Technologies, patterns, or approaches to exclude]
VERSION COMPATIBILITY: [Language versions, dependency constraints]
```

## IMPLEMENTATION GUIDANCE

### Expected Approach

```text
PATTERN: [Architectural approach expected]
FILE CHANGES: 
  - CREATE: [New files needed]
  - MODIFY: [Existing files to change]
INTEGRATION: [How to connect to existing system]
ERROR HANDLING: [Expected error scenarios and responses]
```

### AI-Specific Considerations

```text
HALLUCINATION GUARDS: [Specific constraints to prevent AI errors]
CONTEXT LIMITS: [Scope boundaries for AI decision-making]
VERIFICATION POINTS: [Key checkpoints for accuracy]
```

## HUMAN-IN-LOOP CHECKPOINTS

### Checkpoint 1: Foundation ✋

**TRIGGER:** [What milestone triggers this checkpoint]
**VERIFY:** [What PM will test/review]
**DECISION:** [Criteria for proceeding vs. iterating]

### Checkpoint 2: Integration ✋

**TRIGGER:** [Integration milestone description]
**VERIFY:** [Integration testing PM will perform]
**DECISION:** [Go/no-go criteria for final phase]

### Checkpoint 3: Polish ✋

**TRIGGER:** [Final completion milestone]
**VERIFY:** [Final acceptance testing]
**DECISION:** [Acceptance criteria for completion]

## DELIVERY REQUIREMENTS

### Code Quality

- [ ] [Coding standards requirement 1]
- [ ] [Error handling requirement]
- [ ] [Documentation requirement]
- [ ] [Integration requirement]

### Testing Strategy

- [ ] [Test case requirement 1]
- [ ] [Error handling tests]
- [ ] [Integration testing]
- [ ] [Manual testing instructions]

### Handoff Documentation

```text
SUMMARY: [Brief description of what was built]
CHANGES: [Key files modified and why]
TESTING: [How to verify the implementation works]
NEXT STEPS: [Logical follow-on work]
ISSUES: [Known limitations or future considerations]
```

## VERSION CONTROL STRATEGY

### Git Workflow

```text
BRANCH: [Branch naming convention]
COMMITS: 
  1. [Expected commit 1 description]
  2. [Expected commit 2 description]
  3. [Expected commit 3 description]
MERGE CRITERIA: [Requirements before merging]
ROLLBACK PLAN: [How to undo if problems arise]
```

### Protection Points

```text
BEFORE: [Initial checkpoint commit]
DURING: [Checkpoint-based commits]
AFTER: [Final completion commit]
```

## SPECIFIC TEST SCENARIOS

### [Scenario Category 1]

1. [Test case 1 with expected outcome]
2. [Test case 2 with expected outcome]
3. [Test case 3 with expected outcome]

### [Scenario Category 2]

1. [Test case 1 with expected outcome]
2. [Test case 2 with expected outcome]

### Edge Cases

1. [Edge case 1 and expected handling]
2. [Edge case 2 and expected handling]

**Expected Accuracy:** [Performance criteria for test scenarios]

## STATUS: [READY FOR [AGENT NAME]] 🚀

## CODING AGENT INSTRUCTIONS 🤖

**PROCESS:**
1. Read this entire work request carefully
2. If you have questions, create `work-request-[number]-qa.md` using the QA template
3. Wait for PM answers before beginning implementation
4. Follow checkpoint system - pause for PM review at each checkpoint
5. Provide standup report upon completion

**TEMPLATE LOCATIONS:**
- QA Template: `qa-template.md` in this same directory
- Standup Template: `standup-report-template.md` in this same directory

**STATUS UPDATES:**
- Set work request status to "BLOCKED" if waiting for QA responses
- Update status to "IN_PROGRESS" when actively implementing
- Update status to "COMPLETED" when ready for PM review

**COMMUNICATION:**
- Reference this work request ID in all standup reports
- Use checkpoint system for human-in-loop validation
- Ask questions early rather than making assumptions

```

## Integration with Development Process

**Triggers Q&A Process:** If coding agent has questions, create corresponding `work-request-[number]-qa.md`

**Feeds into Standup Reports:** Coding agent references work request ID in all status updates

**Links to PM Responses:** PM responses reference this work request for decision tracking

**Version Control:** Work request becomes part of project documentation and sprint artifacts

## Quality Guidelines

### SLC Framework Usage
- **Simple:** One primary objective only, clear exclusions
- **Lovable:** User-visible value, quality standards
- **Complete:** Full workflow definition, comprehensive testing

### Technical Specifications
- **Concrete:** Specific file names, function signatures, data formats
- **Realistic:** Achievable within estimated timeframe
- **Testable:** Clear acceptance criteria and verification steps

### Communication Clarity
- **Actionable:** Every section provides clear direction
- **Comprehensive:** All context needed for independent execution
- **Structured:** Consistent format for easy parsing by AI agents

This template creates the foundation for successful PM-to-AI collaboration with clear expectations and quality gates.
