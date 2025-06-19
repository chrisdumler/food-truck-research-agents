# Q&A File Template for PM-Coding Agent Collaboration

## Purpose

This file facilitates questions and answers between coding agents and PMs during work request execution.

## Workflow

1. **Coding Agent** adds questions to the "Questions from Coding Agent" section
2. **PM** reviews questions and provides answers in the "Answers from PM" section  
3. **Coding Agent** reads answers and continues implementation
4. Process repeats as needed until work request is complete

## File Naming Convention

`work-request-[number]-qa.md`

## Template Structure

```markdown
# Work Request #[NUMBER] Q&A

**Work Request:** [Brief title]  
**Status:** [QUESTIONS_PENDING / ANSWERED / COMPLETE]  
**Last Updated:** [Timestamp]

## Questions from Coding Agent
### Q1: [Question category]
[Detailed question text]

### Q2: [Another category]  
[Another question]

## Answers from PM
### A1: [Corresponding answer]
[Detailed answer with any code examples or clarifications]

### A2: [Another answer]
[Another detailed response]

## Resolution Status
- [ ] Question 1 resolved
- [ ] Question 2 resolved
- [ ] All questions answered - coding agent can proceed
```

## Integration with Work Request Process

- Q&A file created when coding agent has questions
- Work request status updated to "BLOCKED" until questions resolved
- Q&A file archived with work request when complete

This creates a clear audit trail of the collaboration process and decision-making.
