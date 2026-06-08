# Agentic Workflows Workshop

This repository is a hands-on workshop for developers who are familiar with IDE Chat or Agent Mode and want to understand how those ideas become repeatable automation with GitHub Agentic Workflows.

The workshop has two labs:

- **Cloud lab:** a true `gh-aw` workflow runs in GitHub Actions when a participant opens a prepared issue. An agent council analyzes the scenario and comments on the issue.
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
  Participant opens an issue from a prepared template
  -> GitHub Actions starts the gh-aw workflow
  -> specialist council roles inspect the issue and evidence pack
  -> the arbiter posts one final RCA comment

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
3. Create one issue from one of the prepared templates.
4. Wait for the agent council comment.
5. Clone the repo locally.
6. Continue with [LOCAL-LAB.md](LOCAL-LAB.md).

## Cloud Lab: Agent Council RCA

The cloud lab uses three one-click issue templates:

- **Customer 360 Schema Drift RCA**
- **Cloud Data Job Cost Spike Review**
- **Data Quality Regression Review**

Each template applies labels such as:

```text
workshop:agent-council
scenario:customer-360-schema-drift
```

The `gh-aw` workflow reads the issue, selects the matching evidence pack, runs council roles, and comments on the issue.

Expected output:

```text
Agent Council RCA
- consensus root cause
- council comparison table
- recommended next action
- risks and dissent
- missing evidence
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
   - `workshop:agent-council`
   - `scenario:customer-360-schema-drift`
   - `scenario:cloud-cost-spike`
   - `scenario:data-quality-regression`
5. Configure the AI engine secret required by your `gh-aw` setup.
6. Install the `gh-aw` extension locally.
7. Compile the workflow:

   ```bash
   gh extension install github/gh-aw
   gh aw compile agent-council-rca
   ```

8. Commit and push both the Markdown workflow and generated `.lock.yml`.
9. Create one test issue from each template and confirm exactly one council comment appears.

## Troubleshooting

If an issue does not trigger the workflow:

- Confirm the labels exist in the repo before the issue is created.
- Confirm Actions are enabled.
- Confirm the compiled `.lock.yml` was committed.
- Confirm required AI secrets are configured.

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
