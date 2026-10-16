# Handle all open questions and hypotheses

This PR modifies main.ts to process all open questions and their hypotheses, rather than just one at a time.

## Changes
- Replace single question processing with loop over all open questions
- Add inner loop to process all pending hypotheses for each question
- Maintain proper question and hypothesis status handling
- Improve logging readability with newlines

Link to Devin run: https://app.devin.ai/sessions/729b4bbe71d8452490065690671d623f
