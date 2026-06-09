# Workshop Constants

Update this file before publishing the repository to the EMU organization.

```text
ORG_NAME=gh-connect-day-impetus
REPO_NAME=agentic-workflows-workshop
```

Derived URLs:

```text
REPO_URL=https://github.com/<ORG_NAME>/agentic-workflows-workshop
ISSUES_URL=https://github.com/<ORG_NAME>/agentic-workflows-workshop/issues
ACTIONS_URL=https://github.com/<ORG_NAME>/agentic-workflows-workshop/actions
NEW_ISSUE_URL=https://github.com/<ORG_NAME>/agentic-workflows-workshop/issues/new/choose
```

Required labels:

```text
scenario:customer-360-schema-drift
scenario:cloud-cost-spike
scenario:data-quality-regression
```

Facilitator checklist:

- [ ] Create repo in the EMU org.
- [ ] Enable Issues.
- [ ] Enable Actions.
- [ ] Create required labels before participants create issues.
- [ ] Configure the AI engine secret required by `gh-aw`.
- [ ] Run `gh aw compile agent-council-rca`.
- [ ] Commit the generated `.github/workflows/agent-council-rca.lock.yml`.
- [ ] Test one issue from each scenario template.
