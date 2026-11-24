# Cyber-physical product–service lifecycles

Use this optional reference for industrial, IoT, cyber-physical, digital-twin, manufacturing-service, or product–service-system work. It is not a default model for ordinary software products.

## Source and scope

`ACADEMIC/INDUSTRIAL CASE` — Robert Woitsch, Anna Sumereder, and Damiano Falcioni, “Model-based data integration along the product & service life cycle supported by digital twinning,” *Computers in Industry* 140 (2022), article 103648, [DOI 10.1016/j.compind.2022.103648](https://doi.org/10.1016/j.compind.2022.103648). Supplied as user-provided text and reviewed 2026-08-31.

The paper proposes a model-based digital-twin environment across design, simulation, manufacturing, and use, illustrated through an industrial paint-production pilot. It is a useful case and conceptual model, not general proof that digital twins improve every service or organization. Preserve the authors' limitation that the pilot was closer to a digital shadow and that the meta-model remained high level.

## HCI and service-design contribution

Treat the product, service, data, organization, physical environment, and customer relationship as one evolving system. Ask:

- Which actors make or depend on decisions at each lifecycle phase?
- What data crosses design, simulation, production, delivery, use, maintenance, and retirement?
- Where do semantics, identifiers, provenance, ownership, or feedback break across phases?
- Which model is descriptive, predictive, simulated, monitored, or operationally controlling?
- How does the interface communicate data origin, freshness, reliability, uncertainty, and human processing?
- What customer value is created beyond internal efficiency, and who carries new labor or risk?
- How will a physical or sandbox experiment create shared understanding before expensive deployment?

## Model the environment

For relevant projects, describe four connected environments:

1. **Domain and organization:** goals, stakeholders, processes, rules, services, business model, and accountability.
2. **Digital models:** process, product, service, lifecycle, and semantic representations at appropriate abstraction levels.
3. **Data and algorithms:** identifiers, events, integrations, simulations, analytics, reliability indicators, and decision logic.
4. **Physical world:** assets, sensors, people, locations, materials, constraints, maintenance, and observable outcomes.

Map information flow and control in both directions. Distinguish a static model, digital shadow, monitoring system, simulation, and operational digital twin rather than using the terms interchangeably.

## Evaluation and trust

Test the continuity between represented and physical state. Validate data accuracy, missingness, delay, provenance, interpretation, and reliability displays. A reliability indicator should support a real decision and be tested for comprehension and calibrated reliance; displaying a number does not establish trustworthiness.

Evaluate:

- operational and service outcomes;
- simulation validity and boundary conditions;
- detection and recovery from sensor, integration, model, or process failure;
- customer and worker experience, workload, accessibility, and control;
- organizational handoffs and ownership;
- sustainability and lifecycle consequences;
- whether benefits transfer beyond the supplied industrial context.

Use service-blueprint and ecosystem-mapping methods for service dependencies, [human-ai-interaction.md](human-ai-interaction.md) for reliance and control, and [ai-agent-evaluation.md](ai-agent-evaluation.md) if an autonomous system acts on the represented state.
