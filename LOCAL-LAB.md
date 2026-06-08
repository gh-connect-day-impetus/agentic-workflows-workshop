# Local Lab: Fix a Tiny Pipeline

This lab uses IDE Agent Mode or Copilot CLI locally. It is not a cloud `gh-aw` run.

The goal is to experience how an agent can inspect code, understand a failing test, make a small patch, and verify the result.

## Setup

Clone the workshop repo:

```bash
git clone https://github.com/<ORG_NAME>/agentic-workflows-workshop.git
cd agentic-workflows-workshop
```

Install `pytest` if your Python environment does not already have it:

```bash
python3 -m pip install -r requirements-dev.txt
```

## Run the Failing Test

From the repo root:

```bash
python3 -m pytest pipeline/tests
```

The test should fail. That is intentional.

## Ask Your Agent

Use IDE Agent Mode or Copilot CLI with a prompt like:

```text
The test under pipeline/tests is failing. Inspect the tiny customer transform pipeline and data file. Make the smallest code change so the transform supports the new loyalty_tier field, handles missing region_code as UNKNOWN, and keeps the output stable. Then rerun the tests.
```

## Verify

After the agent changes the code:

```bash
python3 -m pytest pipeline/tests
git diff
```

You should see a small patch in `pipeline/customer_transform.py`.

## Reflection

Compare this local agent experience with the cloud lab:

- Local Agent Mode is interactive and supervised.
- `gh-aw` is repeatable and event triggered.
- Both are agentic, but only the cloud lab is a true GitHub Agentic Workflow.
