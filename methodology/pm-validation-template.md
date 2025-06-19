# PM Validation Template

## Purpose
Final validation response after PM has personally tested the work from a standup report, providing definitive acceptance/rejection and authorization for next steps.

## When to Use
- After PM has completed hands-on testing of reported work
- When converting conditional approval to final acceptance
- For checkpoint validations where human testing is required
- Before authorizing next work requests

## File Naming Convention
`pm-validation-response-[number].md`

## Template Structure

```markdown
# PM Validation Response to Standup Report #[NUMBER]

**Date:** [Date and Time]  
**PM:** [Human PM Name]  
**Work Request:** #[NUMBER] - [Brief Title]  
**Validation Status:** [COMPLETE / IN_PROGRESS / FAILED]

## VALIDATION RESULTS ✅

### Core Functionality: [APPROVED / NEEDS_REVISION / REJECTED]

**[Summary of functionality testing results]**

- **[Feature 1]:** [Test result and status]
- **[Feature 2]:** [Test result and status]  
- **[Integration]:** [Integration testing results]
- **[Performance]:** [Performance observations]
- **[Demo Quality]:** [Overall user experience assessment]

### Issues Identified: [NONE / MINOR / MAJOR]

**[If issues found, list specific problems requiring fixes:]**

- [Specific issue 1 with details]
- [Specific issue 2 with details]
- [Any usability or UI problems]

## OFFICIAL ACCEPTANCE DECISION

**STATUS:** [FULLY_APPROVED / CONDITIONALLY_APPROVED / REJECTED]  
**RATIONALE:** [Clear reasoning for final decision]

## Strategic Assessment

### Technical Success

- [Assessment of technical implementation quality]
- [Evaluation of architecture decisions]
- [Performance and reliability observations]

### Process Success  

- [How well the development process worked]
- [Effectiveness of communication and checkpoints]
- [Quality of requirements and execution]

## Next Phase Authorization

### Work Request #[NEXT_NUMBER]: [Next Title]

**[APPROVED_TO_PROCEED / HOLD / REDIRECT]** with focus on:

1. [Next priority 1]
2. [Next priority 2]
3. [Any follow-up requirements]

### Updated Project Status

- [Project timeline assessment]
- [Progress against original estimates]
- [Revised expectations or scope]

## Key Learnings Validated

### [Learning Category 1]

- [Specific insight or pattern confirmed]
- [Process improvement identified]
- [Methodology effectiveness]

### [Learning Category 2]

- [Another validated learning]
- [Impact on future work]

## Authorization for Next Work Request

**SCOPE:** [Brief description of authorized next work]  
**PRIORITY:** [High/Medium/Low priority level]  
**TIMELINE:** [Estimated timeline based on current patterns]  
**QUALITY GATE:** [Required validation approach for next work]

---

**PM DECISION:** [Clear directive for next action]

**Project Status:** [Overall project health and direction]
```

## Integration with Development Process

**Follows PM Response:** Validation happens after initial PM response and human testing

**Triggers Next Work Request:** Authorization section directly enables next sprint planning

**Creates Quality Audit Trail:** Documents actual validation process and results

**Feeds Process Improvement:** Captures learnings from hands-on testing experience

## Validation Guidelines

### Testing Approach
- **Hands-On Testing:** Actually use the implemented functionality
- **Real Scenarios:** Test with realistic use cases, not just happy path
- **Integration Verification:** Ensure new work integrates properly with existing system
- **User Experience:** Evaluate from end-user perspective

### Decision Criteria
- **Functionality:** Does it work as specified in the work request?
- **Quality:** Does it meet the quality standards in the SLC definition?
- **Integration:** Does it work well with existing features?
- **Demo-Ready:** Is it ready for demonstration or production use?

### Authorization Standards
- **Clear Scope:** Next work request must have well-defined boundaries
- **Realistic Timeline:** Estimates based on observed AI coding patterns
- **Quality Gates:** Appropriate validation checkpoints for next phase
- **Strategic Alignment:** Next work supports overall project goals

This template ensures thorough validation and clear authorization for continued development.
