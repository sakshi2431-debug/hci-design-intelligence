# AI security and secure interaction

Use this reference when an AI system handles sensitive data, authenticates people or workloads, calls tools, changes external state, supports security operations, or needs a permission, verification, audit, or incident-response experience. Security is a property of the whole sociotechnical system—not the model, a warning dialog, or a guardrail alone.

This is an HCI and product-design reference, not a substitute for threat modeling, security architecture, penetration testing, legal review, or qualified security engineering.

## Start from assets, actors, and consequences

Define:

- people and non-users who could be affected;
- assets, data, services, money, communications, infrastructure, and decisions at risk;
- actors and components crossing trust boundaries;
- allowed actions and the consequences of unauthorized, mistaken, duplicated, delayed, or hidden action;
- likely abuse, prompt injection, compromised content, model error, insider misuse, credential theft, and configuration drift;
- detection, containment, revocation, rollback, recovery, notification, and accountable ownership.

Threat-model the complete flow: user input, system instructions, retrieved documents, memory, models, routers, tools, APIs, databases, logs, human approvals, and downstream recipients. Treat retrieved and user-provided natural language as untrusted input, not authority.

## Keep identities distinct

Model the identities involved instead of collapsing them into a shared “agent” credential:

1. **Human/end-user identity** — who initiated or approved the task.
2. **Application/orchestrator identity** — the service coordinating policy and execution.
3. **Workload identity** — each retriever, gateway, policy service, agent, or other component.
4. **Model/profile identity** — which model, configuration, prompt, and policy produced a plan or output.
5. **Tool/resource identity** — the downstream system receiving the request.
6. **Operator/reviewer identity** — who changed policy, approved an exception, or handled an incident.

Preserve attribution across handoffs. Make it possible to answer who requested, proposed, approved, executed, received, changed, denied, or reversed an action.

## Make policy enforceable outside the model

The model may interpret intent and propose a plan; it must not be the authority that grants itself access. Use deterministic authorization at trust boundaries:

- authenticate the relevant human, application, and workload identities;
- authorize the tool, operation, resource, data class, destination, scope, and context;
- enforce least privilege, short lifetimes, audience/resource restriction, and revocation;
- gate execution at the orchestrator and independently enforce permissions at the tool/API boundary;
- require step-up authentication, confirmation, or review for higher-risk actions;
- deny safely when identity, policy, state, or evidence is insufficient;
- version policy and record the decision and enforcement point.

Do not describe OAuth 2.1 as a final standard. As of 2026-11-23 it is an active IETF working-group Internet-Draft (latest: draft-ietf-oauth-v2-1-17, 2026-10-31), not an RFC. Verify the current OAuth specifications and security best practices before implementation. SPIFFE is one workload-identity option, not a universal requirement; choose mechanisms with security specialists for the actual environment.

## Design permissions people can understand

At the moment of delegation or approval, make clear:

- **who** will act and on whose behalf;
- **what** action is requested;
- **which** data, resource, account, recipient, and environment are affected;
- **why** access is needed and whether a non-agent route exists;
- **when and how long** access lasts;
- whether it is one-time, recurring, background, transferable, or revocable;
- the most important consequence, verification, and recovery route.

Use progressive disclosure: provide a concise decision first and deeper policy details on demand. Avoid vague bundles such as “full access,” hidden scope expansion, coerced consent, and approval fatigue. Ask at consequential boundaries, not after the action and not for every harmless internal step. Support keyboard and assistive technology, clear focus, sufficient time, plain language, localization, and a reviewable history.

An approval UI does not repair an unsafe backend policy. Conversely, an inaccessible or incomprehensible approval can defeat a sound policy by training people to approve reflexively.

## Design security operations for action under pressure

Security operators need context, prioritization, and recovery—not merely more alerts or a conversational layer.

- Organize from situation and consequence to evidence and technical detail; let people drill down without losing context.
- Relate incidents, alerts, entities, assets, policies, and actions through a coherent information architecture.
- Show source, freshness, uncertainty, conflicting evidence, and what the AI transformed or inferred.
- Build verification into the workflow near the recommendation or action.
- Distinguish proposed, approved, running, blocked, partially completed, completed, rolled back, and failed states.
- Make urgency meaningful; do not use alarm styling for routine events.
- Preserve manual paths, expert escalation, collaboration, annotations, and handoff context.
- Reduce repetitive work without automating away the operator's situational awareness or accountability.

Conversational access may reduce navigation effort, but it can also hide the breadth of available evidence, filters, state, and alternative hypotheses. Pair it with inspectable structure and direct manipulation where those support verification.

## Log without creating another hazard

Record correlation identifiers connecting request, model/profile, plan, authorization decision, tool call, outcome, and policy version. Capture enough for audit and incident response, while redacting or excluding secrets, credentials, sensitive prompts, personal data, and unnecessary content. Define access, retention, deletion, integrity, and user-visible history. Never expose hidden chain-of-thought as an audit mechanism; use concise action rationale, evidence, policy decisions, and system events.

## Ask interactively

Use PAIR for mental models, reliance, feedback/control, and graceful failure; use HAX across initial expectations, interaction, error, and change over time. Ask one decision-relevant question at the natural boundary:

**If the model is manipulated or simply wrong, which independently enforced control limits the worst action it could take?**

Then clarify the user-facing consequence: what will the person see, approve, verify, revoke, or recover?

## Evaluate security and usability together

Include representative and adversarial tasks covering:

- correct allow and deny decisions, matched cases where the agent must not act, and scope escalation;
- direct and indirect prompt injection, untrusted retrieval, tool misuse, wrong recipient/resource, duplicate execution, and stale authorization;
- approval comprehension, permission recall, revocation, reauthentication, cancellation, rollback, and recovery;
- alert prioritization, source verification, conflicting evidence, time pressure, interruptions, and handoffs;
- keyboard, screen-reader, low-vision, cognitive, language, and fatigue conditions;
- attribution, audit completeness, sensitive-log handling, policy versioning, incident containment, and credential revocation.

Measure verified security outcomes, task success, time to safe action, false approval/denial, detection and recovery, mental-model accuracy, appropriate reliance, accessibility, and workload. Engagement with a security tool is not a security outcome. Test with representative operators and affected users, and pair usability evidence with technical security testing.

## Provenance and authority

- `PRACTITIONER/VENDOR` — Red Hat, [AI security: Identity and access control](https://www.redhat.com/en/blog/ai-security-identity-and-access-control), published 2026-03-27. Used for system-wide identity separation, independent authorization enforcement, scoped delegation, auditability, and SDLC framing. Product-specific recommendations are not treated as universal requirements.
- `VENDOR EXAMPLE` — Palo Alto Networks, [Security by Design—UX and AI in Modern Cybersecurity](https://www.paloaltonetworks.com/blog/2025/07/security-by-design-ux-ai-modern-cybersecurity/), published 2025-07-24, a blog recap of a vendor podcast. Used only as an example of practitioner concerns (operator context, information architecture, verification), not as evidence. Claims about frictionless AI, adoption, or effectiveness require independent evidence.
- `GOVERNMENT GUIDANCE` — [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) and [SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final). Use for resource-centered zero-trust architecture and identity-based cloud-native access-control context.
- `OPEN STANDARD` — [SPIFFE standards](https://spiffe.io/docs/latest/spiffe-specs/) for workload identity. Verify the selected mechanism and stable specification for the implementation.
- `WORK IN PROGRESS` — [OAuth 2.1 Internet-Draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/), draft -17 dated 2026-10-31 when reviewed on 2026-11-23. The IETF states Internet-Drafts are work in progress and inappropriate to cite as final standards.
