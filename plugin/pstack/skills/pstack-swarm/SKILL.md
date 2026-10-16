---
name: pstack-swarm
description: "Fan out N parallel workers, drain them, and return one report."
---

# Swarm

Read [compatibility](../../references/compatibility.md), [delegation](../../references/delegation.md) and [models](../../references/models.md). This workflow explicitly requests parallel delegation. Local workers replace upstream cloud workers. Track Frame, Fan out, Aggregate, Report in the host todo facility or a visible local checklist when no facility exists.

## A. Frame

1. State the done predicate and returned artifact/report.
2. Choose partitioned coverage, identical-brief race or mixed shape. Declare race selection rule before launch: `first pass`, `rank all` or `best-of`. Define evidence of pass and ranking/best criteria. A first-pass race must support cancellation.
3. Set total N from the user or shape. Bound outstanding workers to actual available capacity; queue remaining N without treating a concurrency limit as total coverage.
4. Resolve `swarm workers` from model configuration. Declare each model/effort arm for a model race. Inherited/repeated GPT workers are independent attempts, not provider diversity.
5. Allocate writing isolation and shared runtime resources under delegation.md. Name exact base/check/measurement SHAs in each relevant brief; measurements also specify sample count, one-sample definition and order.

## B. Fan out

Dispatch a bounded concurrent batch and continue until N workers have been launched or an explicit blocker occurs. Each worker receives a stand-alone goal, scope, exact slice/race arm, workspace, required context reads, verification procedure and report contract. Use fresh specialized workers with scoped instructions; full poteto-mode applies only if the assigned playbook needs it. Start from the named local commit/branch, inspecting availability rather than assuming a pushed cloud branch. Report an unavailable base as blocked.

Workers return `PASS`, `ISSUES` or `BLOCKED` with evidence. Proven defects produce ISSUES listing every supported issue, not just the first. Each report identifies exact SHAs/method assigned, files inspected/changed, output paths and unresolved gaps. A dropout leaves N−1 available results and an explicit gap; it never satisfies coverage.

## C. Aggregate

Drain terminal results under the declared selection rule. Reject a result missing required SHAs or method and retry that worker once with a fresh consolidated brief. A second miss is a coverage gap. For partitioned coverage every required slice needs a valid result. For races apply the declared rule, verify the selected evidence and cancel remaining work when applicable, accounting for running processes. A first result without pass evidence does not win.

Review evidence and changed diffs as owner. Keep a compact result table, one-line evidenced issues and explicit gaps/dropouts. Resolve overlap and contradictions against artifacts. Use race selection rather than presenting raw worker dumps.

## D. Report

Return one consolidated in-chat report with results, evidence, issue one-liners, coverage gaps/dropouts and the selection rule when used. A missing slice prevents a whole-coverage PASS even when other workers pass. Include artifact/worktree locations and any retained process ownership necessary for follow-up. Completion is the requested evidenced predicate or an exact BLOCKED report, never a fabricated successful run.
