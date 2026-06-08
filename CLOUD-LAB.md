# Cloud Lab: Agent Council RCA

This lab runs a true GitHub Agentic Workflow.

You will create an issue from a prepared scenario. GitHub Actions will run the `gh-aw` workflow, the agent council will inspect the issue and evidence pack, and the workflow will post one final comment.

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
-> DataOps, Cost, and Governance council roles analyze independently
-> the arbiter posts one final issue comment
```

The issue title starts with `Pending participant`. The workflow renames the issue to include the issue author's GitHub handle so participants and facilitators can identify ownership.

## Expected Comment Structure

The final comment should include:

- participant handle
- selected scenario
- consensus root cause
- council comparison table
- recommended next action
- risks and dissent
- missing evidence

## Workshop Rules

- Create only one issue unless the facilitator asks you to create another.
- Do not edit the issue template content before submitting.
- Do not push branches or open pull requests for the cloud lab.
- Treat the agent council output as advice. A human still makes the final decision.
