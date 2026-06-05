# Atlas Entry — Event Density Substrate

**Catalog:** ED-Substrate (substrate-mode)
**Paired shadow entry:** #15 — Event Density PDE (continuum, shadow-mode)
**Evaluation type:** Substrate-level AD (extended framework, Phases A1/A2)
**Verdict:** 6 PASS / 0 CONDITIONAL / 0 FAIL *(5/1/0 as originally filed; Determinism upgraded to PASS by the tie-break specification)*
**Pole:** Reach-stratified selection (candidate)
**Filed:** June 2026 · Allen Proxmire

---

## 1. System Summary

The Event Density (ED) substrate is the discrete relational layer underlying the ED framework: micro-events linked by participation channels on a graph, evolving by a local stability-maximizing selection rule under irreversible commitment. It is a **discrete relational architecture** characterized by **finite reach** (influence bounded by decoupling surfaces), **local maximization** (each step commits the maximum-stability candidate in a bounded neighborhood), and **acyclic dynamics** (irreversible accumulation forces fixed-point-only attractors). It is evaluated here as a substrate in its own right — distinct from its coarse-grained PDE shadow (entry #15), which it casts but does not resemble in pole.

---

## 2. Architectural Specification (Step 1)

**Axioms (B1–B7, compressed):**

| Axiom | Commitment |
|---|---|
| B1 | Micro-events — atomic, indivisible; local rate = event density |
| B2 | Channels — participation relations on stable subgraphs, bandwidth-weighted |
| B3 | Adjacency / chains — bandwidth-gated coherent adjacency; chains coarse-grain to particles |
| B4 | Commitment density ρ — local accumulation of committed events (state variable) |
| B5 | Orientation — relational directionality carried by channel structure (non-score-bearing) |
| B6 | Decoupling surfaces — finite-reach horizon; reciprocal participation goes one-sided |
| B7 | P11 irreversibility — every commitment irreversible; forward-only evolution |

**Evolution rule:** Σ(e′) = Coh(e′, s) − Str(e′, ρ_local) − Grad(e′, ∇ρ); chain commits the maximum-Σ candidate. Graph-local, finite-reach. Tie-break: channel-bandwidth-ordering with a B1-distinctness final key (lexicographic, total within each reach stratum) — `Phase_TieBreak_Specification.md`.

**Channel table:**

| Channel | Locality | Linearity | Stability role | Scale |
|---|---|---|---|---|
| Coherence (Coh) | Graph-local, finite reach | Nonlinear | Stabilizing | Local |
| Strain (Str) | Graph-local, finite reach | Nonlinear | Destabilizing | Local |
| Gradient strain (Grad) | Graph-local, finite reach | Nonlinear | Destabilizing / steering | Meso |
| Orientation | Graph-local, chain-propagated | ~Linear (carried) | Neutral / structuring | Meso–global |
| Decoupling | Local boundary, finite reach | Nonlinear (threshold) | Bounding | Local → global partition |

Subspace split: score-bearing {Coh, Str, Grad} coupled by Σ; structural {orientation, decoupling} independent of the rule.

---

## 3. Envelope Summary (Step 2)

**Forbidden patterns:**
- *Structural:* commitment reversal (B7), trans-decoupling reciprocity (B6), broken chain continuity (B3).
- *Dynamical:* sub-maximal commitment (rule); spontaneous orientation reversal — resolved at Step 4 (forbidden within stratum, undefined across).

**Necessary patterns:** maximization footprint on every committed step (N1); monotone ρ-ordering along chains (N2, promotes I4 to established invariant); reach-bounded propagation front (N3); coherence–strain balance at every commitment (N4).

**Envelope inequalities:**
- **ρ(x, t₂) ≥ ρ(x, t₁)** — ρ-monotonicity; sharp at lower bound.
- Σ(e′) ≥ Σ(c) ∀ c ∈ 𝒩 — footprint; sharp by construction.
- d_part(e, e″) ≤ R_decouple(e) — finite reach; boundary-sharp, interior-loose.

**Closure:** closed in the characterized sense — two bounded ghost-state classes (trans-decoupling; non-maximal-path), no uncharacterized slack.

---

## 4. Extremal Dynamics Summary (Step 3)

- **Sharpening fronts** — maximization selects extremes; fronts sharpen (or stay neutral), do not diffuse. Reach-bounded speed, bandwidth-modulated.
- **Self-limiting concentration** — gradient-strain channel caps blow-up.
- **Acyclic attractors** — cycles excluded by ρ-monotonicity + irreversibility; local-maximization fixed points are the sole terminal attractor. (A2 "fixed-point-or-cycle" dichotomy collapses to fixed-point-only.)
- **Partial footprint recoverability** — extensive footprint (commitment set, ρ-profile, maximality certification) preserved by irreversibility; intensive footprint (margins, order, tie resolutions) lost.
- **Orientation located** — Σ is orientation-blind; orientation conservation cannot be a rule property and is routed to Step 4 as a channel-structure question.

---

## 5. Constraint Surface Summary (Step 4)

**Structural faces:** finite-reach/decoupling (SF1, sharp, load-bearing for orientation); forward-only/P11 (SF2, sharp); chain-continuity (SF3, sharp, orientation transport); monotonicity (SF4, sharp).

**Dynamical faces:** maximization footprint (DF1, sharp); sharpening front (DF2, sharp in substrate); acyclic attractor (DF3, sharp, orientation-ambiguous at fixed point); footprint recoverability (DF4, partially sharp).

**Reach-stratified faces:** channel space factorizes into causal cones at decoupling surfaces; constraint surface is a product of per-stratum surfaces glued by one-sided cross-decoupling influence.

**Orientation verdict — STRATIFIED:** orientation conservation holds as a **local invariant within each reach stratum** and is **undefined (not violated) across decoupling surfaces**. Derived (from B3 + B6 + Σ-neutrality), not added as an axiom.

**Determinability boundary = decoupling surface.** Determinable within reach; structurally blind across. Reach horizon and determinability horizon coincide.

**Surface type:** stability-resolved + reach-stratified (defining); commitment-dissipative + locally graph-contractive (subordinate).

---

## 6. Criteria Evaluation (Step 5)

| Criterion | Verdict | Basis |
|---|---|---|
| Minimality | **PASS** | No redundant axiom/channel/term; monotonicity & orientation derived, not posited |
| Locality | **PASS** | Graph-local + finite-reach by axiom; no non-local influence (factorization) |
| Determinism | **PASS** | Components 1–4 PASS; unique-maximizer (Component 4) closed by the tie-break specification (channel-bandwidth-ordering, B1-distinctness final key) |
| Generative Sufficiency | **PASS** | All phenomena from B1–B7 + Σ; orientation derived, never imported |
| Envelope Tightness | **PASS** | Forbidden/necessary clean; only characterized ghost states; closed |
| Structural Optimality | **PASS** | No anomalies; economical surface; reach-stratification forced & multiply-witnessed |

**AD Score: 6 / 6 PASS, 0 CONDITIONAL, 0 FAIL.** *(Originally filed 5/6 with a CONDITIONAL on Determinism; `Phase_TieBreak_Specification.md` filled the open tie-break slot using only B1/B2 structure, closing Component 4 — no new axiom, orthogonal to the stratified-orientation invariant.)*

---

## 7. Pole Assignment (Step 6)

**Candidate pole: reach-stratified selection (substrate-mode).** Defined by: reach-stratified constraint surface, sharpening (non-diffusive) dynamics, acyclic fixed-point-only attractors, local-maximization footprint, finite-reach determinability boundary — none with a continuum analogue. Nearest existing pole: aggregation (shares irreversibility; lacks reach stratification and selection footprint).

**Status: candidate, not confirmed.** AD standard requires recurrence across ≥2 independent entries to establish a pole. ED is the first; confirmation requires a second independent discrete relational substrate (FS substrate is the leading candidate, not yet evaluated).

---

## 8. Substrate–Shadow Relationship

Paired with **#15 — Event Density PDE** (the coarse-grained continuum shadow of this substrate).

- **Key divergence:** the substrate **sharpens** (maximization selects extremes); the PDE shadow **diffuses** (degenerate-parabolic). The diffusion is **manufactured by coarse-graining** — averaging a sharpening selection rule over many steps/chains — not inherited.
- **Different poles:** #15 sits at the diffusive pole; the substrate at the candidate reach-stratified selection pole. **Same physical theory, two levels, two poles.**
- **Inherited features:** locality, irreversible/monotone arrow, aggregation-like accumulation.
- **Atlas convention:** link the two entries explicitly as a **substrate/shadow pair**; record the pole-mismatch; do not assume the substrate inherits the shadow's classification.

---

## 9. Taxonomy Extensions

| Extension | Adds | Placement |
|---|---|---|
| Reach-bounded determination | 4th determinism component for architectures with a determinability boundary | **Core** |
| Ghost-state characterization | Envelope requirement: admissible-but-unreachable regions must be characterized, not merely absent | **Core** |
| Sharpening/diffusive distinction | Dynamical signature separating extremal-selective from averaging dynamics | **Core** |
| Substrate/shadow pole-mismatch | Atlas convention: a theory may hold different poles at substrate and shadow levels | **Core** (convention) |
| Reach-stratified surface type | Constraint-surface type that factorizes at reach boundaries | **Substrate-mode** |

Four core, one substrate-mode. The substrate review returns more to AD's core than to its substrate wing.

---

## 10. Cross-Domain Structural Parallels

FS ↔ ED, **structural form only** — detected by a shared evaluation framework, not a claim of shared subject matter:

- **Determinability boundary ↔ parity barrier** — both are finite-reach horizons where the architecture's determination ends.
- **Finite reach ↔ finite correlation length** — both bound influence locally as a positive structural feature.
- **Sharpening substrate ↔ diffusive shadow** — both are substrates whose continuum projection is smoother than the substrate itself.

**Shared motif (candidate):** finite-reach generative substrate + determinability boundary at the reach horizon + smoother projection shadow. Two instances (FS informal, ED formal); proposed for the atlas pending a confirming second entry.

> **Discipline:** structural analogy only. No claim that ED explains primes or FS explains physics. AD compares architecture, not content.

---

## 11. Open Items

| Item | Type | Status / Resolution |
|---|---|---|
| ~~Tie-breaking rule (unique-maximizer gap)~~ | Architectural | **RESOLVED** — `Phase_TieBreak_Specification.md`: channel-bandwidth-ordering with a B1-distinctness final key; lexicographic, total within each reach stratum; no new axiom. Determinism → PASS, score → 6/6. |
| ~~Orientation: primitive (B5) vs. derivable~~ | Architectural | **RESOLVED — primitive** (`Phase_OrientationPrimitivity_Resolution.md`): longitudinal component derivable from the commitment arrow (B7 + I4 + tie-break), but transverse field content is not supplied by B2–B3, bandwidth, or Σ. B5 retained; Minimality PASS reaffirmed (no score change). |
| Determinability boundary in bits | **Empirical** (open) | Information-theoretic measure of determination lost across a decoupling surface; ED counterpart to FS's quantified parity barrier |

---

## 12. Citation Block

ED-substrate AD evaluation (ten documents, `evaluations/ED_Substrate/`):

1. `Memo_00_ED_Substrate_AD_Scoping.md` — scoping; circularity guard
2. `Phase_A_CriterionMapping.md` — criterion mapping; decision to extend
3. `Phase_A1_SubstrateLevel_AD_Criteria.md` — substrate-level criteria (general class)
4. `Phase_A2_DiscreteExtraction_Modes.md` — discrete extraction modes (general class)
5. `Phase_B_ArchitecturalSpecification.md` — Step 1: architecture
6. `Phase_C_EnvelopeExtraction.md` — Step 2: envelope (Mode 1)
7. `Phase_D_ExtremalDynamics.md` — Step 3: extremal dynamics (Mode 2)
8. `Phase_E_ConstraintSurface.md` — Step 4: constraint surface (Mode 3)
9. `Phase_F_CriteriaEvaluation.md` — Step 5: verdicts (5 PASS / 1 CONDITIONAL)
10. `Phase_G_Generalization.md` — Step 6: generalization, pole, taxonomy
11. `Phase_TieBreak_Specification.md` — architectural closure: tie-break rule; Determinism CONDITIONAL → PASS (6/6)
12. `Phase_OrientationPrimitivity_Resolution.md` — architectural closure: B5 verdict (irreducible/primitive); Minimality PASS reaffirmed

**Paired shadow entry:** `evaluations/AD_Evaluation_EventDensity.md` — entry #15, ED PDE (continuum shadow).

---

*Atlas entry — Event Density substrate. Substrate-mode evaluation; paired with shadow entry #15. Pole: reach-stratified selection (candidate). Score: 6 PASS / 0 CONDITIONAL / 0 FAIL.*
