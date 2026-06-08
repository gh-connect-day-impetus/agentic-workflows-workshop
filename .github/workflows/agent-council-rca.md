---
name: Agent Council RCA

on:
  issues:
    types: [opened, labeled]
  workflow_dispatch:
    inputs:
      issue_number:
        description: Issue number to analyze
        required: true

permissions:
  contents: read
  issues: write

engine: copilot

safe-outputs:
  add-comment:
    target: triggering
    required-labels: ["workshop:agent-council"]
    max: 1
  update-issue:
    target: triggering
    required-labels: ["workshop:agent-council"]
    title:
    max: 1
---

# Agent Council RCA

You are running an agent council for the Agentic Workflows Workshop.

## Operating Rules

- Only act on issues that have the `workshop:agent-council` label.
- Do not edit repository files.
- Do not create branches.
- Do not open pull requests.
- Do not post more than one final issue comment.
- Keep the final comment useful to a developer or data platform lead.

## First Action

Update the issue title so it includes the issue author's GitHub handle.

Use this format:

```text
[Agent Council][<Scenario Short Name>][@<issue-author>] <Readable Scenario Name>
```

Examples:

- `[Agent Council][Schema Drift][@octocat] Customer 360 Pipeline RCA`
- `[Agent Council][Cost Spike][@octocat] Warehouse Query Cost Review`
- `[Agent Council][Data Quality][@octocat] Revenue Dashboard Regression`

Use the `update_issue` safe output for this title update.

## Scenario Routing

Determine the scenario from labels:

- `scenario:customer-360-schema-drift` -> read `evidence/customer-360-schema-drift/`
- `scenario:cloud-cost-spike` -> read `evidence/cloud-cost-spike/`
- `scenario:data-quality-regression` -> read `evidence/data-quality-regression/`

If no supported scenario label is present, comment that the issue is missing a supported scenario label and stop.

## Council Roles

Run the analysis as three independent council roles before synthesizing.

### DataOps Analyst

Focus on pipeline reliability, root cause, operational recovery, test coverage, and blast radius.

### Platform Cost Analyst

Focus on runtime, compute cost, query plan symptoms, SLA risk, and safe optimization options.

### Governance Reviewer

Focus on data contracts, lineage, validation gates, ownership, and prevention controls.

## Arbiter

Compare the three council analyses. Identify consensus and dissent. Prefer a recommendation that is safe, minimal, reversible, and easy for a human maintainer to verify.

## Final Comment Format

Post exactly one issue comment using this structure:

```markdown
## Agent Council RCA

**Participant:** @<issue-author>
**Scenario:** <scenario name>

### Consensus
<1-3 bullets>

### Council Findings
| Council role | Likely cause | Recommended action | Risk or caveat |
|---|---|---|---|
| DataOps Analyst | ... | ... | ... |
| Platform Cost Analyst | ... | ... | ... |
| Governance Reviewer | ... | ... | ... |

### Recommended Next Action
<one clear recommendation>

### Dissent and Missing Evidence
<bullets>

### Human Review
This is an agent council recommendation. A human owner should verify the evidence before production changes.
```

Use the `add_comment` safe output for the final comment.
