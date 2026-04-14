# 05 — Formal-Structural Criteria Verdict

## 1. Evaluation Summary

| Criterion | Verdict | Confidence |
|---|---|---|
| **Minimality** | **FAIL** | High |
| **Locality** | **PASS** | High |
| **Determinism** | **PASS** | High |
| **Generative Sufficiency** | **PASS** | High |
| **Envelope Tightness** | **CONDITIONAL** | Medium |
| **Structural Optimality** | **FAIL** | High |

---

## 2. Criterion 1: Minimality

### Verdict: FAIL

**Definition**: A system is minimal if every constraint participates in determining the output, and removing any single constraint changes the result.

### Evidence

**Constraint census**:
- Total input hypotheses: 178 (170 ZD + 8 A\*)
- Binding constraints: 48 (40 ZD + 8 A\*)
- Non-binding (dominated): 130
- **Redundancy rate: 73.0%**

**Author-level redundancy**:

| Author | Input | Binding | Redundancy |
|---|---|---|---|
| Ivic | 111 | 5 | 95.5% |
| Huxley | 8 | 0 | 100% |
| Bourgain | 4 | 1 | 75.0% |
| Pintz | 20 | 19 | 5.0% |
| TTY25 | 21 | 11 | 47.6% |
| Heath-Brown | 7 | 4 | 42.9% |
| Montgomery | 1 | 0 | 100% |
| Ford | 1 | 0 | 100% |
| Carlson | 1 | 0 | 100% |
| Jutila | 1 | 0 | 100% |
| Conrey | 1 | 0 | 100% |

**Ablation-level redundancy**:
- 8 of 14 testable authors are INERT — removing them has zero effect on θ\_max.
- 5 authors are SUBOPTIMAL — removing them *improves* θ\_max.
- Only 1 author (Heath-Brown) is LOAD-BEARING.

**Structural interpretation**: The system carries massive dead weight. Of 178 constraints, only 2 participate in the extremal vertex. The remaining 176 define interior structure that does not influence the final bound. This is not a minimal system.

**Guth--Maynard structural note**: Removing GM causes the A(σ) envelope to fragment from 40 to 134 intervals while leaving all θ values unchanged. GM's role is purely organizational — it consolidates multiple weaker estimates into a single clean bound on [7/10, 19/25). This is structural simplification, not mathematical contribution to θ\_max.

---

## 3. Criterion 2: Locality

### Verdict: PASS

**Definition**: All constraints are expressed as local inequalities — they bound functions at specific σ values without requiring global information.

### Evidence

Every envelope constraint has the form:
- A(σ) ≤ f(σ) for σ ∈ [a, b), where f is a rational function of σ alone.
- A\*(σ) ≤ g(σ) for σ ∈ [a, b), where g is a rational function of σ alone.

No constraint references:
- The value of A or A\* at a different σ.
- The derivative of A or A\*.
- Any global property of the envelope (e.g., total variation, integral).
- Any relationship between different intervals.

The α/β functionals are also local: they depend only on A(σ) and A\*(σ) at the same σ.

The dependency tree of each hypothesis (tracked by the `dependencies` field) represents a proof-theoretic dependency, not a functional dependency. The numerical computation treats each estimate as an independent constraint.

**Verdict**: Locality holds without qualification.

---

## 4. Criterion 3: Determinism

### Verdict: PASS

**Definition**: The architecture produces a unique output from a given set of inputs. There is no ambiguity, branching, or non-determinism in the computation of θ\_max.

### Evidence

1. **Unique envelope**: The pointwise infimum of a finite collection of continuous functions on compact intervals is uniquely defined. The A(σ) and A\*(σ) envelopes are deterministic.

2. **Unique interval partition**: The common refinement of all hypothesis intervals is uniquely determined by the set of rational endpoints.

3. **Unique stationary points**: The symbolic computation of sup α and sup β via `sympy.solve` on rational functions produces exact algebraic solutions. There are no numerical approximation artifacts.

4. **Unique extremal vertex**: Only one gap-interval achieves θ = 3/2. The second-highest θ is 1.4804 (gap = 0.0196). There is no near-degeneracy.

5. **Reproducibility**: The computation has been verified to produce identical output across multiple runs. The `float(complex(...).real)` patch addresses a sympy representation issue, not a non-determinism.

**Verdict**: Determinism holds. The architecture is a pure function from hypothesis set to θ\_max.

---

## 5. Criterion 4: Generative Sufficiency

### Verdict: PASS

**Definition**: The architecture generates all stated outputs from its inputs without external computation or human intervention.

### Evidence

The pipeline `prove_prime_gap2()` takes no external parameters beyond the hypothesis set. It:

1. Constructs A(σ) from ZD hypotheses (automatic).
2. Constructs A\*(σ) from energy hypotheses (automatic).
3. Computes the common refinement (automatic).
4. Evaluates α and β on each interval (symbolic, automatic).
5. Finds sup of each (symbolic solve + evaluation, automatic).
6. Reports θ\_max = max over all intervals (automatic).

All 46 gap-interval θ values are generated. All A(σ) and A\*(σ) envelope segments are generated. The ablation study itself is fully automated — each of the 17 configurations runs end-to-end without manual intervention.

**Verified outputs**:
- 40 A(σ) intervals with binding authors.
- 8 A\*(σ) intervals with binding authors.
- 46 gap-intervals with θ values.
- θ\_max = 3/2.
- Full ablation table with 17 configurations.
- Per-interval binding analysis with JSON output.

**Verdict**: Generative sufficiency holds. The architecture produces everything claimed.

---

## 6. Criterion 5: Envelope Tightness

### Verdict: CONDITIONAL

**Definition**: The envelope is tight if every binding constraint achieves equality at some point and the bound cannot be improved without new mathematical input.

### Evidence For (PASS components)

**Heath-Brown constraints are tight at the extremal vertex**:
- E40 (A ≤ 6.42√(1−σ) on [1011/1012, 1)): This is the best known ZD estimate near σ = 1. It achieves equality in the sense that θ\_max = 3/2 is a direct consequence of this bound's functional form.
- E\*8 (A\* ≤ 12/(4σ−1) on [5/6, 1)): This is the best known energy estimate in this range.

**The envelope is tight where it matters**: The extremal vertex depends only on Heath-Brown's two constraints, and both are state-of-the-art.

### Evidence Against (FAIL components)

**Interior constraints are loose**:
- The 39 non-extremal A(σ) intervals produce θ values ranging from 1.208 to 1.480 — all strictly below θ\_max = 3/2. Tightening any of these does not improve θ\_max.
- The mid-σ valley (TTY25 zone, θ ~ 1.21) is 20% below θ\_max. This represents substantial slack.

**SUBOPTIMAL constraints indicate negative tightness**:
- Pintz's 19 intervals drive θ up to 1.48 — they are tight in the sense of achieving equality on A(σ), but they are *anti-tight* for the objective: removing them improves θ\_max.
- The Ingham/Huxley/Jutila/Conrey group similarly worsens the bound through their participation in the dependency tree.

**Conditional interpretation**: Tightness holds at the extremal vertex (Heath-Brown) but fails in the bulk of the polytope. The architecture is tight "where it counts" but carries substantial slack everywhere else.

### Quantitative Slack Analysis

| Region | θ range | Slack below θ\_max | Status |
|---|---|---|---|
| Low-σ (Ingham) | 1.20–1.23 | 18–20% | Loose |
| Mid-σ (TTY25) | 1.21–1.25 | 17–19% | Loose |
| Transition | 1.25–1.32 | 12–17% | Moderate |
| Pintz regime | 1.35–1.48 | 1–10% | Approaching tight |
| Extremal (HB) | 1.50 | 0% | **Tight** |

---

## 7. Criterion 6: Structural Optimality

### Verdict: FAIL

**Definition**: The architecture is structurally optimal if it achieves the best possible output with the minimum necessary structure.

### Evidence of Sub-Optimality

**Single point of failure**: The entire computation depends on one author (Heath-Brown) for both the ZD and A\* channels at the extremal vertex. No other author provides estimates that are competitive near σ = 1. This is a structural vulnerability, not an optimal design.

**Massive over-specification**: 178 constraints to determine a 5-dimensional polytope is a 35.6× overdetermination ratio. A structurally optimal system would use O(5–10) constraints.

**Counter-productive constraints**: 5 authors are SUBOPTIMAL — their presence worsens the result. The mechanism is now understood (see 06\_Pintz\_Paradox\_Solved.md): Pintz's tight rational bounds *activate* Heath-Brown's sub-polynomial ZD estimate on [1011/1012, 1) by beating the derived rational bound that would otherwise cover [59/60, 1). The sub-polynomial form produces worse θ despite being a better pointwise ZD estimate. This is a form-mismatch artifact, not a dependency-chain issue.

**Fragmented INERT contributions**: Guth--Maynard's single estimate consolidates 93 intervals into 40, but this consolidation does not improve θ\_max. TTY25's 11 binding intervals provide mid-σ refinement that is invisible to the final bound.

**No feedback mechanism**: The architecture has no way to identify and prune SUBOPTIMAL or INERT constraints. The hypothesis set is assembled once and processed wholesale.

### What Structural Optimality Would Look Like

A structurally optimal version of EXPDB would:
1. Contain exactly the constraints that are LOAD-BEARING or boundary-adjacent.
2. Use ~5–10 total constraints (matching the polytope dimension).
3. Have no SUBOPTIMAL constraints.
4. Have every constraint participate in at least one vertex.
5. Be aware that the α/β functional penalizes sub-polynomial ZD estimates more than rational ones — a structurally optimal system would select estimate *forms* based on their interaction with the objective, not just their pointwise quality.

For the current θ\_max = 3/2 computation, the minimal sufficient set would be:
- Heath-Brown ZD (E40): A ≤ 6.42√(1−σ) on [1011/1012, 1)
- Heath-Brown A\* (E\*8): A\* ≤ 12/(4σ−1) on [5/6, 1)
- One A(σ) estimate covering [1/2, 1011/1012) to complete the envelope
- One A\*(σ) estimate covering [1/2, 5/6) to complete the envelope

That is 4 constraints — a 44.5× reduction from the current 178.

**However**, the Pintz paradox reveals that θ\_max = 3/2 is itself an artifact. A structurally optimal system that excludes Pintz achieves θ\_max = 33/23 ≈ 1.4348 using only rational ZD bounds. The "true" optimal θ from the existing literature may be lower than 3/2.

---

## 8. Constraint Census

### 8.1 By Type

| Category | Count | Binding | Non-binding |
|---|---|---|---|
| Zero-density (ZD) | 170 | 40 | 130 |
| Energy (A\*) | 8 | 8 | 0 |
| **Total** | **178** | **48** | **130** |

### 8.2 By Facet Role

| Role | Authors | Binding constraints | Hypotheses |
|---|---|---|---|
| LOAD-BEARING | 1 (Heath-Brown) | 4 | 7 |
| SUBOPTIMAL | 5 (Pintz, Ingham, Huxley, Jutila, Conrey) | 20 | 31 |
| INERT | 8 (GM, Ivic, Bourgain, Montgomery, Ford, CDV, Carlson, TTY25) | 24 | 140 |

### 8.3 Independent Constraints vs Free Parameters

- **Free parameters**: 5 (the polytope dimension: σ, A, A\*, α, β).
- **Independent binding constraints**: 48 (the envelope segments).
- **Constraints active at θ\_max**: 2 (E40, E\*8).
- **Overdetermination ratio**: 48/5 = **9.6×** (binding only), 178/5 = **35.6×** (total).
- **Effective constraint utilization**: 2/178 = **1.1%**.

---

## 9. Final Verdict

```
+---------------------------+-------------+
| Criterion                 | Verdict     |
+---------------------------+-------------+
| 1. Minimality             | FAIL        |
| 2. Locality               | PASS        |
| 3. Determinism            | PASS        |
| 4. Generative Sufficiency | PASS        |
| 5. Envelope Tightness     | CONDITIONAL |
| 6. Structural Optimality  | FAIL        |
+---------------------------+-------------+
| Overall                   | 3/6 PASS    |
|                           | 1/6 COND    |
|                           | 2/6 FAIL    |
+---------------------------+-------------+
```

### Interpretation

The EXPDB pipeline is a **sound, deterministic, and generatively sufficient** computation. It reliably produces the correct θ\_max = 3/2 from its input hypotheses, and all intermediate results are fully generated.

However, the architecture is **not minimal and not structurally optimal**. It carries 73% redundant constraints, 5 counter-productive author groups, and a single load-bearing author who controls both channels at the extremal vertex. The envelope is tight only at the point that matters (Heath-Brown at σ → 1) and loose everywhere else.

The structural diagnosis: EXPDB is a **historical accumulation**, not an engineered architecture. It preserves every estimate ever published, regardless of whether that estimate contributes to the final bound. This is appropriate for a database (its stated purpose) but architecturally suboptimal for computing θ\_max.

### Recommendations for Structural Improvement

1. **Prune SUBOPTIMAL constraints**: Removing Pintz alone improves θ\_max from 3/2 to 33/23 ≈ 1.4348. The mechanism is now fully understood: Pintz activates Heath-Brown's sub-polynomial ZD estimate by out-competing the derived rational bound on [41/42, 1011/1012). The sub-polynomial form interacts poorly with the α/β functional. See 06\_Pintz\_Paradox\_Solved.md.

2. **Form-aware envelope selection**: The α/β functional penalizes sub-polynomial ZD estimates (√(1−σ) decay) more than rational estimates (1/(cσ−d) decay). A structurally optimal system should select among competing ZD estimates not only by pointwise A(σ) value but also by functional form compatibility with the downstream computation.

3. **Flag INERT constraints**: Mark the 130 non-binding hypotheses so the computation can skip them. This would reduce runtime without changing the result.

4. **Diversify the A\* channel**: The single-author dependency on Heath-Brown for energy estimates is a structural risk. New energy estimates from other authors would improve robustness.

5. **Separate database from computation**: Maintain the full hypothesis database for archival purposes, but extract a minimal sufficient set for each specific computation. The ablation study provides the tool for this extraction.

6. **Investigate whether θ = 33/23 is the true literature bound**: The no-Pintz computation produces θ\_max = 33/23 using only rational ZD bounds. This may represent the actual best bound achievable from the existing zero-density literature when the envelope is assembled optimally. This question has potential paper-level significance.
