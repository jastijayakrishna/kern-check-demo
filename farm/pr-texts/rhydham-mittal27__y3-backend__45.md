# feat: tickets system, test enhancements, parent AI endpoints & shift requests

## Summary
- **Tickets**: New `Ticket` model + service + controller + routes (`/v1/tickets`) — parents/tutors can raise concerns, add comments, and track resolution status
- **Parent AI**: Groq-backed endpoints for study tips (`/v1/parents/ai/study-tips`) and open Q&A (`/v1/parents/ai/ask`)
- **Parent routes**: shift requests, reschedule history, tutor-change requests, attendance verification
- **Tests**: Syllabus coverage tracking, compliance checks, question analysis, covered chapters per cycle
- **ShiftRequest**: Added `effectiveDate` field; coordinator approval flow extended
- **Coordinator**: Reschedule and shift-request management actions added
- **Deps**: Added Groq SDK; updated constants for AI model config

## Test plan
- [ ] `POST /v1/tickets` creates a ticket and returns ticket doc
- [ ] `GET /v1/tickets/my` returns tickets for authenticated user
- [ ] `POST /v1/tickets/:id/comments` appends a comment
- [ ] `POST /v1/parents/ai/study-tips` returns tips array (requires GROQ_API_KEY)
- [ ] `POST /v1/parents/ai/ask` returns answer string
- [ ] Parent shift request creation and listing work
- [ ] Syllabus coverage endpoint returns chapter coverage data

🤖 Generated with [Claude Code](https://claude.com/claude-code)
