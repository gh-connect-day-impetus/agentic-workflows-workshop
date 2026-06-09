# Agentic Workflows Workshop

This repository is a hands-on workshop for developers who are familiar with IDE Chat or Agent Mode and want to understand how those ideas become repeatable automation with GitHub Agentic Workflows.

The workshop has two labs:

- **Cloud lab:** a true `gh-aw` workflow runs in GitHub Actions when a participant opens an issue. An agent council analyzes prepared incident scenarios or responds to free-form issue prompts.
- **Local lab:** participants clone the repo, run a tiny failing data pipeline test, and use IDE Agent Mode or Copilot CLI to fix it locally.

## Table of Contents

- [What Is an Agentic Workflow?](#what-is-an-agentic-workflow)
- [How This Workshop Works](#how-this-workshop-works)
- [Repository Layout](#repository-layout)
- [Participant Flow](#participant-flow)
- [Cloud Lab: Agent Council RCA](#cloud-lab-agent-council-rca)
- [Local Lab: Fix a Tiny Pipeline](#local-lab-fix-a-tiny-pipeline)
- [Facilitator Setup](#facilitator-setup)
- [Troubleshooting](#troubleshooting)

## What Is an Agentic Workflow?

An agentic workflow is automation where an AI agent is given a goal, context, tools, and guardrails.

Traditional automation is command driven:

```text
Run tests.
Build artifact.
Deploy package.
```

Agentic automation is goal driven:

```text
Read this incident.
Inspect the evidence.
Compare likely causes.
Recommend the safest next action.
Post a concise issue comment.
```

If you use IDE Chat or Agent Mode, you already know the interactive version:

```text
Developer asks agent -> agent reads repo -> agent suggests or edits code
```

`gh-aw` turns that idea into a repeatable GitHub workflow:

```text
GitHub event -> GitHub Actions -> gh-aw workflow -> AI agent -> safe output
```

The important distinction:

- **IDE Agent Mode / Copilot CLI:** interactive, local, developer-supervised.
- **GitHub Agentic Workflows (`gh-aw`):** event-triggered, repeatable, cloud-run, permission-bounded.

## How This Workshop Works

The repo demonstrates a hybrid model.

```text
Cloud lab:
  Participant opens a prepared scenario issue or a free-form issue
  -> GitHub Actions starts the gh-aw workflow
  -> Gemini, Claude, and GPT council members inspect the issue
  -> Copilot posts a final synthesis after the model-specific comments

Local lab:
  Participant clones this repo
  -> runs a failing Python test
  -> uses IDE Agent Mode or Copilot CLI to fix schema drift locally
  -> reruns tests and inspects the git diff
```

The cloud lab is the true agentic workflow experience. The local lab is the code-editing experience participants already recognize from Agent Mode.

## Repository Layout

```text
.github/
  ISSUE_TEMPLATE/       Prepared issue forms for the cloud lab
  workflows/            gh-aw source workflow
evidence/               Curated incident evidence packs
pipeline/               Tiny local data pipeline with an intentional bug
CONSTANTS.md            Org/repo placeholders to update before publishing
CLOUD-LAB.md            Participant instructions for the cloud lab
LOCAL-LAB.md            Participant instructions for the local lab
```

## Participant Flow

Participants do not need to fork the repo.

1. Open the workshop repo in the EMU organization.
2. Start with [CLOUD-LAB.md](CLOUD-LAB.md).
3. Open one of the existing scenario issues and inspect its Actions run logs.
4. Create one issue from a prepared template.
5. Create one free-form issue to experiment with the workflow.
6. Wait for the agent council comments.
7. Clone the repo locally.
8. Continue with [LOCAL-LAB.md](LOCAL-LAB.md).

## Cloud Lab: Agent Council RCA

The cloud lab has two modes.

Mode 1 uses three one-click issue templates:

- **Customer 360 Schema Drift RCA**
- **Cloud Data Job Cost Spike Review**
- **Data Quality Regression Review**

Each template applies exactly one scenario label:

```text
scenario:customer-360-schema-drift
```

The `gh-aw` workflow reads the issue, selects the matching evidence pack, runs Gemini, Claude, and GPT council sub-agents, then has Copilot post a final synthesis.

Mode 2 is free-form experimentation. Create a blank issue with any title and body. For example:

```text
Title: Agentic Workflows goes to Bollywood
Body: Write a limerick in the style of Shahrukh Khan.
```

If no scenario label is present, the workflow skips evidence-pack routing and asks the models to respond directly to the issue title and body.

Expected output:

```text
Gemini Council View
Claude Council View
GPT Council View
Copilot Final Synthesis
```

## Local Lab: Fix a Tiny Pipeline

The local lab contains a small Python transform that still expects an old field named `customer_tier`. The new input data uses `loyalty_tier` and contains one missing `region_code`.

Participants run:

```bash
python3 -m pytest pipeline/tests
```

The test should fail before the fix. Participants then use IDE Agent Mode or Copilot CLI to make the smallest local code change and rerun the test.

## Facilitator Setup

Before running the workshop:

1. Update [CONSTANTS.md](CONSTANTS.md) with the final EMU org name.
2. Create the repo as `agentic-workflows-workshop` in that org.
3. Enable Issues and Actions.
4. Create required labels:
   - `scenario:customer-360-schema-drift`
   - `scenario:cloud-cost-spike`
   - `scenario:data-quality-regression`
5. Configure `COPILOT_GITHUB_TOKEN`; the workshop uses Copilot's model routing for the Gemini, Claude, GPT, and Copilot council views.
6. Install the `gh-aw` extension locally.
7. Compile the workflow:

   ```bash
   gh extension install github/gh-aw
   gh aw compile agent-council-rca
   ```

8. Commit and push both the Markdown workflow and generated `.lock.yml`.
9. Create one test issue from each template and one blank free-form issue. Confirm four comments appear on each: Gemini, Claude, GPT, and Copilot synthesis.

## Troubleshooting

If an issue does not trigger the workflow:

- Confirm Actions are enabled.
- Confirm the compiled `.lock.yml` was committed.
- Confirm required AI secrets are configured.
- For prepared scenario issues, confirm the scenario labels exist in the repo before the issue is created.

If the local lab does not run:

- Confirm Python 3.9+ is available.
- Install `pytest` if needed:

  ```bash
  python3 -m pip install -r requirements-dev.txt
  ```

- Run tests from the repository root:

  ```bash
  python3 -m pytest pipeline/tests
  ```
