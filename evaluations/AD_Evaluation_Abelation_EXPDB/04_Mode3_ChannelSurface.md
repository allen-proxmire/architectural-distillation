# 04 — Mode 3: Channel Surface and Facet Classification

## 1. Overview

Mode 3 constructs the channel interaction surface — the table of which combinations of ZD, A\*, and hybrid constraints are possible, forced, or redundant — and classifies each author's contribution into one of three facet roles: LOAD-BEARING, SUBOPTIMAL, or INERT.

---

## 2. Channel Definitions

### 2.1 ZD Channel
- **Carries**: A(σ) estimates (zero-density bounds on N(σ,T)).
- **Contributors**: 16 authors, 170 hypotheses.
- **Binding segments**: 40 intervals.
- **Role in θ computation**: Provides the A term in the α/β functionals.

### 2.2 A\* Channel
- **Carries**: A\*(σ) estimates (zero-density energy bounds).
- **Contributors**: 2 authors (Heath-Brown, TTY25), 8 hypotheses.
- **Binding segments**: 8 intervals.
- **Role in θ computation**: Provides the A\* term in the α/β functionals.

### 2.3 Hybrid Channel
- **Carries**: The combined α/β computation on each gap-interval.
- **Inputs**: One ZD segment + one A\* segment per gap-interval.
- **Outputs**: θ(σ) per interval; θ\_max globally.
- **Segments**: 46 gap-intervals (common refinement of ZD and A\* partitions).

---

## 3. Channel Interaction Table

Each gap-interval is a (ZD author, A\* author) pair. The 46 intervals produce the following combinations:

| ZD Author \ A\* Author | Heath-Brown | TTY25 | Total ZD intervals |
|---|---|---|---|
| **Ingham** | 2 | 0 | 2 |
| **Guth--Maynard** | 0 | 3 | 3 |
| **Ivic** | 2 | 5 | 7 |
| **TTY25** | 5 | 3 | 8 |
| **Bourgain** | 1 | 1 | 2 |
| **CDV** | 1 | 0 | 1 |
| **Derived** | 6 | 0 | 6 |
| **Pintz** | 19 | 0 | 19 |
| **Heath-Brown** | 1 | 0 | 1 |
| **Total A\* intervals** | **37** | **12** | **49** (note: some intervals counted under multiple partitions) |

### 3.1 Impossible Combinations

The following (ZD, A\*) pairs never occur in the baseline computation:

- **(Montgomery, anything)**: Montgomery's ZD estimates are completely dominated; they never bind.
- **(Ford, anything)**: Same.
- **(Carlson, anything)**: Same.
- **(Huxley, anything)**: Huxley's ZD estimates are dominated by Ivic, TTY25, and others on every interval.
- **(Jutila, anything)**: Same.
- **(Conrey, anything)**: Same.
- **(anything, Ivic)**: Ivic contributes no A\* estimates.
- **(anything, Pintz)**: Pintz contributes no A\* estimates.

### 3.2 Forced Combinations

- **σ ∈ [1/2, 7/10)**: ZD = Ingham, A\* = Heath-Brown. No alternative for either channel.
- **σ ∈ [5/6, 1)**: A\* = Heath-Brown. No alternative. ZD varies (Bourgain, TTY25, derived, Pintz, Heath-Brown).
- **σ ∈ [1011/1012, 1)**: ZD = Heath-Brown, A\* = Heath-Brown. Both channels forced.

### 3.3 Redundant Combinations

- Any gap-interval where both the ZD and A\* authors are INERT produces a θ value that does not participate in θ\_max and could be removed without changing the result.
- The 12 mid-σ intervals (Regime II) where TTY25 controls both channels are internally consistent but collectively INERT for θ\_max.

---

## 4. Facet Classification by Author

### 4.1 Ablation-Based Classification

| Author | Hypotheses | Binding Intervals | θ\_max when removed | Δθ | Classification |
|---|---|---|---|---|---|
| **Heath-Brown** | 7 | 4 (1 ZD + 3 A\*) | 249,999.5 | +249,998 | **LOAD-BEARING** |
| **Pintz** | 20 | 19 ZD | 1.4348 | −0.0652 | SUBOPTIMAL |
| **Ingham** | 1 | 1 ZD | 1.4804 | −0.0196 | SUBOPTIMAL |
| **Huxley** | 8 | 0 | 1.4804 | −0.0196 | SUBOPTIMAL |
| **Jutila** | 1 | 0 | 1.4804 | −0.0196 | SUBOPTIMAL |
| **Conrey** | 1 | 0 | 1.4804 | −0.0196 | SUBOPTIMAL |
| **Guth--Maynard** | 1 | 1 ZD | 1.5000 | 0 | INERT |
| **Ivic** | 111 | 5 ZD | 1.5000 | 0 | INERT |
| **Bourgain** | 4 | 1 ZD | 1.5000 | 0 | INERT |
| **Montgomery** | 1 | 0 | 1.5000 | 0 | INERT |
| **Ford** | 1 | 0 | 1.5000 | 0 | INERT |
| **CDV** | 1 | 1 ZD | 1.5000 | 0 | INERT |
| **Carlson** | 1 | 0 | 1.5000 | 0 | INERT |
| **TTY25** | 21 | 11 (6 ZD + 5 A\*) | 1.5000 | 0 | INERT |

### 4.2 Facet Role Definitions

**LOAD-BEARING**: Removing this author causes structural collapse — the computation either fails or produces a meaningless result. Heath-Brown is the only LOAD-BEARING author.

**SUBOPTIMAL**: Removing this author *improves* θ\_max. The mechanism is **envelope activation**: Pintz's tight rational bounds on [41/42, 1011/1012) beat the derived rational bound 6/(303σ − 290), preventing it from extending to σ = 1. This forces the envelope to switch to Heath-Brown's sub-polynomial ZD estimate 6.42√(1−σ) on [1011/1012, 1), which produces θ = 3/2. Without Pintz, the derived rational bound covers [59/60, 1) seamlessly and produces θ = 33/23 ≈ 1.4348 — a better result from a "worse" estimate. The SUBOPTIMAL class demonstrates that pointwise-better A(σ) bounds do not necessarily yield better θ: the α/β functional penalizes sub-polynomial decay more than rational decay.

**INERT**: Removing this author has no effect on θ\_max. Their estimates are either:
- Completely dominated (Montgomery, Ford, Carlson — 0 binding intervals), or
- Binding on interior intervals that do not control θ\_max (Ivic, GM, TTY25, CDV, Bourgain).

---

## 5. The Extremal Vertex

### 5.1 Identification

The extremal vertex of the X5D polytope is uniquely located at:

```
σ ∈ [1011/1012, 1)
ZD channel:  Heath-Brown, A(σ) ≤ 6.42√(1−σ)
A* channel:  Heath-Brown, A*(σ) ≤ 12/(4σ−1)
θ = 3/2
```

### 5.2 Facet Decomposition at the Vertex

At the extremal vertex, exactly **two constraints are active**:
1. E40 (Heath-Brown ZD): A(σ) ≤ 6.42√(1−σ)
2. E\*8 (Heath-Brown A\*): A\*(σ) ≤ 12/(4σ−1)

Both are from Heath-Brown. No other author participates at the extremal vertex.

### 5.3 Vertex Stability Analysis

| Perturbation | Effect on θ\_max |
|---|---|
| Tighten E40 (better ZD near σ=1) | θ\_max decreases |
| Tighten E\*8 (better A\* near σ=1) | θ\_max decreases |
| Remove E40 | θ\_max jumps to 250,000 (collapse) |
| Remove E\*8 | θ\_max jumps to 250,000 (collapse) |
| Tighten any INERT constraint | No effect |
| Remove any SUBOPTIMAL constraint | θ\_max improves to 1.48 or 1.43 |

The vertex is **stable under INERT perturbations** and **fragile under LOAD-BEARING removal**.

---

## 6. Polytope Facet Census

### 6.1 Active Facets at θ\_max

Only 2 of 48 envelope constraints are active at the extremal vertex. The remaining 46 are slack.

### 6.2 Active Facets at θ = 1.4804 (Second Vertex)

If we restrict to the Pintz regime, the second-highest vertex at θ = 1.4804 involves:
- E39 (Pintz ZD): A ≤ 3/(22(42σ−41)) on [923/924, 1011/1012)
- E\*8 (Heath-Brown A\*): A\* ≤ 12/(4σ−1) on [5/6, 1)

This vertex has ZD = Pintz (SUBOPTIMAL) and A\* = Heath-Brown (LOAD-BEARING).

### 6.3 Dimensional Analysis

The X5D polytope has:
- **5 dimensions**: (σ, A, A\*, α, β)
- **48 facet-defining constraints**: 40 from A(σ) + 8 from A\*(σ)
- **46 vertices**: one per gap-interval
- **1 extremal vertex**: [1011/1012, 1)
- **Overdetermination ratio**: 48 constraints / 5 dimensions = **9.6×** (heavily overdetermined)

The polytope is extremely flat: most of its volume is occupied by INERT constraints that define faces far from the extremal vertex.

---

## 7. Channel Surface Topology

The channel surface — the set of all (ZD author, A\* author, θ) triples realized on the envelope — has a simple topology:

1. **Low-σ ridge**: Ingham × Heath-Brown. θ ∈ [1.20, 1.23].
2. **Mid-σ valley**: (GM/Ivic/TTY25) × TTY25. θ ∈ [1.21, 1.25]. Contains the global minimum θ = 1.208.
3. **Transition saddle**: Mixed × Heath-Brown. θ ∈ [1.25, 1.32].
4. **High-σ ramp**: Pintz × Heath-Brown. θ climbs monotonically from 1.35 to 1.48.
5. **Extremal peak**: Heath-Brown × Heath-Brown. θ = 3/2.

The surface has exactly one peak, one valley, and a monotone ramp connecting them. There are no secondary maxima or saddle points in the θ landscape.
