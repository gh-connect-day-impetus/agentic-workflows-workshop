# Cloud Lab: Agent Council RCA

This lab runs a true GitHub Agentic Workflow.

You will create an issue. GitHub Actions will run the `gh-aw` workflow, Gemini, Claude, and GPT council members will inspect the issue, and Copilot will post the final synthesis.

There are two ways to use the lab:

- **Prepared scenario:** choose one of the three issue templates. The template adds a scenario label and routes the workflow to a curated evidence pack.
- **Free-form experiment:** create a blank issue with your own title and body. If no scenario label is present, the models respond directly to your issue details.

## What You Will Do

1. Open the workshop repo in GitHub.
2. Go to **Issues**.
3. Click **New issue**.
4. First, open one of the three issues already created by the facilitator and inspect its Actions run:
   - open the issue
   - click the linked workflow run in the generated comment, or open the repo's **Actions** tab
   - inspect how the workflow moved through activation, agent execution, and safe outputs
5. Choose one prepared scenario:
   - **Customer 360 Schema Drift RCA**
   - **Cloud Data Job Cost Spike Review**
   - **Data Quality Regression Review**
6. Submit the issue without editing the prepared scenario text.
7. Wait for the agent council comments.
8. Create a second, free-form issue if the facilitator asks you to experiment. Example:

   ```text
   Title: Agentic Workflows goes to Bollywood
   Body: Write a limerick in the style of Shahrukh Khan.
   ```

## What Happens Behind the Scenes

```text
Issue created
-> optional scenario label is applied by a prepared template
-> GitHub Actions starts the compiled gh-aw workflow
-> a pre-agent job comments with the GitHub Actions run link
-> the workflow reads the issue
-> if a scenario label exists, the workflow reads the matching evidence files
-> if no scenario label exists, the workflow uses the issue title and body directly
-> Gemini, Claude, and GPT council members analyze independently
-> each model posts its own council view
-> Copilot posts the final synthesis
```

The issue title starts with `Pending participant`. The workflow renames the issue to include the issue author's GitHub handle so participants and facilitators can identify ownership.

## Expected Comments

The issue should receive these model comments:

- `Agent Council Run Started`
- `Gemini Council View`
- `Claude Council View`
- `GPT Council View`
- `Copilot Final Synthesis`

The first comment links directly to the GitHub Actions run. Use it to inspect the workflow jobs and logs while the agent council is running.

For prepared scenario issues, expect evidence-backed RCA style comments. For free-form issues, expect each model to respond directly to your prompt and then Copilot to compare their outputs.

## Workshop Rules

- Create the scenario issue first, then a free-form issue only when the facilitator asks you to experiment.
- Do not edit the prepared scenario template content before submitting.
- Do not push branches or open pull requests for the cloud lab.
- Treat the agent council output as advice. A human still makes the final decision.
