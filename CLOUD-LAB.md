# Cloud Lab: Agent Council RCA

This lab runs a true GitHub Agentic Workflow.

You will create an issue from a prepared scenario. GitHub Actions will run the `gh-aw` workflow, Gemini, Claude, and GPT council members will inspect the issue and evidence pack, and Copilot will post the final synthesis.

## What You Will Do

1. Open the workshop repo in GitHub.
2. Go to **Issues**.
3. Click **New issue**.
4. Choose one scenario:
   - **Customer 360 Schema Drift RCA**
   - **Cloud Data Job Cost Spike Review**
   - **Data Quality Regression Review**
5. Submit the issue without editing the prepared scenario text.
6. Wait for the agent council comment.

## What Happens Behind the Scenes

```text
Issue created
-> scenario labels are applied
-> GitHub Actions starts the compiled gh-aw workflow
-> the workflow reads the issue and evidence files
-> Gemini, Claude, and GPT council members analyze independently
-> each model posts its own council view
-> Copilot posts the final synthesis
```

The issue title starts with `Pending participant`. The workflow renames the issue to include the issue author's GitHub handle so participants and facilitators can identify ownership.

## Expected Comments

The issue should receive four comments:

- `Gemini Council View`
- `Claude Council View`
- `GPT Council View`
- `Copilot Final Synthesis`

## Workshop Rules

- Create only one issue unless the facilitator asks you to create another.
- Do not edit the issue template content before submitting.
- Do not push branches or open pull requests for the cloud lab.
- Treat the agent council output as advice. A human still makes the final decision.
