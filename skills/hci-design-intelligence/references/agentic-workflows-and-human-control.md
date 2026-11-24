# Agentic workflows and human control

Use this reference when designing an AI system that plans, calls tools, changes external state, coordinates multiple agents, or performs a workflow on someone's behalf. The central HCI problem is not whether the system appears autonomous; it is whether people can delegate appropriately, understand consequential state, intervene effectively, and verify the outcome.

## Classify the system before designing it

Distinguish:

- **Assistant:** helps a person perform a task while the person remains the primary actor.
- **Automation:** executes a predefined rule or workflow with limited discretion.
- **Agent:** selects steps and uses tools toward a goal within an authority envelope.
- **Agentic workflow:** combines model decisions, deterministic steps, tools, data, and human checkpoints.
- **Multi-agent system:** allocates work among multiple agents or roles, creating additional handoffs, conflicts, provenance, and coordination failures.
- **Orchestration/control plane:** organizational infrastructure for registering, connecting, observing, governing, changing, and retiring agents and tools.

Do not add an agent because the label is fashionable. Compare it with a direct interface, search, recommendation, assistant, or deterministic workflow. Use agentic behavior only when flexible planning or tool selection creates meaningful user value that justifies added uncertainty, latency, cost, and governance.

## Allocate human and agent work action by action

Decompose the journey into decisions, information retrieval, preparation, external actions, verification, and exceptions. Assign each step deliberately:

| Allocation | Meaning |
|---|---|
| Human-only | A person must make or perform the step |
| Deterministic automation | A defined rule performs it without model discretion |
| Agent observes | The agent retrieves or monitors and reports |
| Agent recommends | The agent proposes an option; a person decides |
| Agent prepares | The agent drafts or configures an action without executing it |
| Agent acts with confirmation | The agent waits at the consequential boundary |
| Agent acts under standing authority | It executes only inside explicit, revocable limits |
| Prohibited | The system must not enable the action for this agent |

Do not classify an entire product as “autonomous.” Choose the maximum autonomy for each action by considering:

- **Consequence:** severity and distribution of harm if wrong.
- **Uncertainty:** limits in inputs, inference, environment, and policy interpretation.
- **Reversibility:** whether people and affected systems can be restored completely and promptly.
- **Reach:** people, accounts, money, data, systems, jurisdictions, and future decisions affected.
- **Detectability:** likelihood and timing of noticing an incorrect or partial outcome.

Use these as structured judgment, not a universal numeric score. Higher consequence, uncertainty, reach, or delayed detection and lower reversibility demand narrower authority, stronger review, independent enforcement, and more capable recovery.

Record the allocation in a Human–Agent Authority Map:

| Task/action | Allocation | Data/tools | Limit | Approval trigger | Visible state | Failure/side effect | Recovery | Verification | Owner |
|---|---|---|---|---|---|---|---|---|---|

## Define the authority envelope

Specify before implementation:

1. The person or organization granting authority and the goal they intend.
2. Allowed tools, resources, data, destinations, recipients, and environments.
3. Actions the agent may propose, prepare, execute, or never perform.
4. Spending, time, volume, privacy, safety, and jurisdictional limits.
5. Conditions requiring preview, confirmation, re-authentication, expert review, or human takeover.
6. Scope duration, expiration, revocation, and whether authority can be delegated to another agent.
7. Observable success, forbidden side effects, rollback, and residual responsibility.

Use least privilege and task-scoped authorization. Approval for one action is not blanket approval for later steps, new recipients, expanded data access, or a changed goal. Renew consent at the point where consequences become material—not repeatedly for harmless internal reasoning.

For identity, authorization, permission, audit, or security-operations details, also read [ai-security-and-secure-interaction.md](ai-security-and-secure-interaction.md). A model must not grant itself authority or serve as the only enforcement point.

## Design the delegation experience

### Before work

- Restate the goal, relevant constraints, and expected deliverable in task language.
- Show the proposed plan or affected resources when choices or consequences are material.
- Identify assumptions, unavailable inputs, permissions, estimated cost/time, and points where the agent will stop.
- Let the person change scope, exclude resources, choose autonomy, or use a manual/non-agent route.

### During work

- Make status meaningful: current objective, completed work, pending steps, blocked state, and whether external changes have occurred.
- Separate internal reasoning from an actionable, privacy-safe activity record. Do not expose hidden chain-of-thought as a substitute for inspectable evidence.
- Support pause, cancellation, correction, takeover, and bounded redirection. Explain what cancellation can and cannot undo.
- Avoid unnecessary interruptions. Request input only when the answer changes authority, risk, outcome, or recovery.

### Before consequential action

- Preview the exact action, target, important content, and irreversible or externally visible effects.
- Place confirmation close to execution and renew it when scope changes.
- Use higher-friction review for destructive, financial, legal, medical, security-sensitive, public, or interpersonal consequences.
- Prefer drafts, simulations, sandboxes, staged execution, and reversible actions where feasible.

### After work

- Report verified outcomes, partial completion, failures, skipped steps, side effects, and remaining obligations.
- Show what changed and where, with provenance sufficient for review.
- Offer rollback, correction, escalation, or a safe manual continuation.
- Never infer success solely from the agent's narrative; verify the state that matters.

## Design multi-agent orchestration

Multiple agents magnify coordination problems. Define:

- each role, capability, owner, trust boundary, data access, and permitted actions;
- routing rules and why a task moves between agents, models, humans, or deterministic services;
- shared versus isolated memory and the provenance of information passed across boundaries;
- conflict resolution, duplicate-action prevention, idempotency, and stopping conditions;
- visible handoffs when identity, capability, policy, cost, or responsibility changes;
- end-to-end ownership so users are not forced to diagnose internal topology;
- lifecycle controls for versioning, evaluation, rollout, monitoring, suspension, and retirement.

Do not make a catalog badge, “trusted” label, or centralized dashboard stand in for evidence. A governed catalog can support discoverability and policy, but every agent still needs task-specific capability evidence, permission review, provenance, monitoring, and a responsible owner.

## Ask HAX and PAIR questions interactively

- **PAIR user needs:** Which flexible part of the workflow benefits from agency, and what simpler baseline was rejected?
- **PAIR mental models:** What will users believe the agent has already done, can see, or is allowed to do?
- **PAIR reliance:** Which action must remain visibly uncertain or independently verified?
- **PAIR feedback and control:** Where can people edit scope, approve, pause, take over, undo, revoke, or escalate?
- **PAIR graceful failure:** What partial or hidden failure could leave the world in an unsafe or misleading state?
- **HAX 1–2:** make capability and performance boundaries clear;
- **HAX 7–10:** support efficient invocation, dismissal, correction, and scoped behavior under uncertainty;
- **HAX 12–17:** expose learning, feedback, controls, and personalization;
- **HAX 18:** communicate material changes to models, tools, authority, or behavior.

Ask at the decision boundary: **What is the most consequential action this agent may take without a person checking it, and what evidence makes that autonomy acceptable?**

## Evaluate and operate the whole system

Use [ai-agent-evaluation.md](ai-agent-evaluation.md). Test not only task quality but authority compliance, matched cases where the agent must not act, permission expansion, wrong-recipient/tool/resource errors, duplicate execution, handoff loss, conflicting agents, partial failure, cancellation, rollback, stale state, inaccessible status, and recovery. Inspect end-to-end traces and verified outcomes across repeated trials.

Monitor capability and regression performance, incidents, intervention and rollback rates, hidden partial failures, unequal outcomes, cost/latency, and whether automation preserves meaningful human control. Reopen review after changes to models, prompts, tools, permissions, data, routing, policy, organizational ownership, or user population.

## Provenance

This is an original HCI synthesis grounded primarily in HAX, PAIR, and the agent-evaluation reference. IBM's [Guide to AI Agents](https://www.ibm.com/think/ai-agents) (first published 2025-05-02, since retitled) is used only as a vendor-authored index covering agent components, architectures, multi-agent systems, frameworks, governance, agentic RAG, and use cases. IBM's [watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) is used only as a product example of a catalog and enterprise control-plane concept. Both are first-party IBM sources but are not independent standards or research proof; product, trust, ROI, productivity, and engagement claims require independent evidence.
