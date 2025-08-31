# Workflow Directory Organization

This directory contains all PM-to-AI and AI-to-PM communications for structured collaboration. It should be gitignored to keep project history clean while maintaining full audit trails locally.

## Directory Structure

```
workflow/
├── 001-basic-multiagent-setup/
│   ├── work-request-001.md          # PM → AI: Initial work specification
│   ├── work-request-001-qa.md       # AI → PM: Questions (if needed)
│   ├── qa-response-001.md           # PM → AI: Answers to questions
│   ├── standup-report-001.md        # AI → PM: Progress and completion report
│   ├── pm-response-001.md           # PM → AI: Initial assessment and direction
│   └── pm-validation-001.md         # PM → AI: Final acceptance after testing
├── 002-next-sprint/
│   └── [same structure]
└── README.md                        # This file
```

## File Naming Conventions

### Work Requests (PM → AI)
- `work-request-[number].md` - Primary sprint specification
- `qa-response-[number].md` - PM answers to AI questions

### AI Communications (AI → PM)  
- `work-request-[number]-qa.md` - AI questions about work request
- `standup-report-[number].md` - AI progress and completion report

### PM Responses (PM → AI)
- `pm-response-[number].md` - PM assessment and strategic direction
- `pm-validation-[number].md` - PM final acceptance after testing

## Workflow Progression

Each sprint follows this communication flow:

1. **PM creates work-request-[number].md** → AI begins research/implementation
2. **AI creates work-request-[number]-qa.md** (if questions) → PM creates qa-response-[number].md
3. **AI implements with checkpoints** → AI creates standup-report-[number].md
4. **PM reviews and responds** → PM creates pm-response-[number].md
5. **PM tests functionality** → PM creates pm-validation-[number].md
6. **Next sprint begins** → New numbered directory

## Benefits of This Organization

- **Sprint Isolation:** Each sprint has its own directory for clean organization
- **Chronological Flow:** File naming makes communication sequence clear
- **Audit Trail:** Complete record of decisions and progress
- **Gitignore Safe:** Can exclude entire workflow/ directory from version control
- **Template Adherence:** Structure enforces methodology template usage
- **Parallel Sprints:** Could support multiple concurrent work streams if needed

## Integration with Methodology

This structure directly supports the methodology's communication patterns:
- Work Request → Q&A → Implementation → Standup Report → PM Response → PM Validation
- All templates from `/methodology` are used within sprint directories
- Clear handoff points between PM and AI roles
- Full audit trail for process improvement and learning
