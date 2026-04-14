# 01 — Architecture Specification: EXPDB as a 5D Polytope

## 1. System Identity

**System**: EXPDB (Exponent Pair Database) Prime Gap Pipeline  
**Objective**: Compute the optimal bound θ\_max for the exponent θ\_{gap,2} governing prime gaps via Proposition 15.9 of TTY25.  
**Architecture class**: Constrained optimization over a piecewise-rational envelope polytope.  
**Result**: θ\_max = 3/2, achieved at a unique extremal vertex on the interval [1011/1012, 1).

---

## 2. Axioms

### 2.1 Explicit Axioms

**A1 (Zero-Density Hypothesis Framework).**  
For σ ∈ (1/2, 1), the number of zeros N(σ, T) of the Riemann zeta function satisfies  
N(σ, T) ≪ T^{A(σ)(1−σ) + o(1)},  
where A(σ) is a piecewise-rational function assembled from the literature.

**A2 (Zero-Density Energy Framework).**  
An additive-energy analogue A\*(σ) satisfies an analogous bound with stronger decay properties, yielding the energy channel.

**A3 (Envelope Optimality).**  
The functions A(σ) and A\*(σ) are defined as the pointwise infimum of all available estimates at each σ. The best estimate is the one achieving equality on each interval.

**A4 (Prime Gap Reduction).**  
The exponent θ\_{gap,2} is bounded by the supremum over σ of  
max(α(σ), β(σ)),  
where α and β are rational functions of σ, A(σ), and A\*(σ).

### 2.2 Implicit Axioms

**A5 (Interval Partition Compatibility).**  
All estimates are valid on rational-endpoint intervals. The combined envelope inherits a common refinement of all contributing intervals.

**A6 (Monotone Convergence Near σ = 1).**  
As σ → 1, A(σ) → ∞ and A\*(σ) → ∞, but their ratio and interaction through α/β determines whether θ remains finite.

**A7 (Independence of Estimates).**  
Each author's estimates are treated as independent constraints. No estimate depends on another author's result except through the dependency tree tracked by the Hypothesis object.

---

## 3. Operators

| Operator | Symbol | Domain | Action |
|---|---|---|---|
| Zero-density envelope | ZD | σ ∈ [1/2, 1) | Selects pointwise-best A(σ) from all ZD estimates |
| Energy envelope | A\* | σ ∈ [1/2, 1) | Selects pointwise-best A\*(σ) from all energy estimates |
| Alpha functional | α(σ) | Per gap-interval | α = 4σ − 2 + 2(A\*(1−σ) − 1)/(A\* − A) |
| Beta functional | β(σ) | Per gap-interval | β = 4σ − 2 + (A\*(1−σ) − 1)/A |
| Supremum extraction | sup | Per gap-interval | Finds sup of α and β via stationary-point analysis |
| Global maximum | θ\_max | All intervals | θ\_max = max over all intervals of max(sup α, sup β) |

---

## 4. Parameters

| Parameter | Type | Range | Role |
|---|---|---|---|
| σ | Continuous | [1/2, 1) | Abscissa of the zero-density region |
| A(σ) | Piecewise rational | ≥ 0 | Zero-density exponent bound |
| A\*(σ) | Piecewise rational | ≥ 0 | Energy exponent bound |
| θ(σ) | Derived | ≥ 1 | Local prime gap exponent |
| θ\_max | Scalar | = 3/2 | Global optimum (the deliverable) |

---

## 5. Channels

The architecture operates through three information channels:

### 5.1 Zero-Density (ZD) Channel
- **Input**: 170 zero-density estimates from 16 authors.
- **Processing**: Pointwise infimum over all valid estimates at each σ.
- **Output**: 40-interval piecewise envelope A(σ).

### 5.2 Energy (A\*) Channel
- **Input**: 8 zero-density energy estimates from 2 authors (Heath-Brown, TTY25).
- **Processing**: Pointwise infimum.
- **Output**: 8-interval piecewise envelope A\*(σ).

### 5.3 Hybrid Channel
- **Input**: A(σ) and A\*(σ) envelopes.
- **Processing**: α/β computation on 46 gap-intervals (common refinement).
- **Output**: θ(σ) on each gap-interval; θ\_max = max over all.

---

## 6. Governing Equations

On each gap-interval [σ\_i, σ\_{i+1}) with active estimates A and A\*:

```
α(σ) = 4σ − 2 + 2·(A*(1−σ) − 1) / (A* − A)
β(σ) = 4σ − 2 + (A*(1−σ) − 1) / A
θ(σ) = max(sup α, sup β)
θ_max = max_i θ(σ_i)
```

The supremum on each interval is computed symbolically via stationary-point analysis (sympy.solve on dα/dσ, dβ/dσ).

---

## 7. The 5D Polytope (X5D)

The EXPDB computation implicitly defines a polytope in 5 dimensions:

| Dimension | Coordinate | Interpretation |
|---|---|---|
| d1 | σ | Position along the critical strip |
| d2 | A(σ) | Zero-density exponent at σ |
| d3 | A\*(σ) | Energy exponent at σ |
| d4 | α(σ) | First gap functional |
| d5 | β(σ) | Second gap functional |

The envelope constraints (A(σ) ≤ f\_i(σ), A\*(σ) ≤ g\_j(σ)) define hyperplane cuts. The feasible region is the intersection of all half-spaces. The extremal vertex is the point maximizing θ = max(α, β) over this polytope.

**Vertex count**: The polytope has 46 vertices (one per gap-interval), but only one achieves θ\_max = 3/2.

**Extremal vertex**: σ ∈ [1011/1012, 1), A(σ) = Heath-Brown ZD, A\*(σ) = Heath-Brown A\*, θ = 3/2.

---

## 8. Contributing Authors and Estimate Types

| Author | Year(s) | Type | Binding Intervals | Facet Role |
|---|---|---|---|---|
| Ingham | 1940 | ZD | 1 (A(σ) on [1/2, 7/10)) | SUBOPTIMAL |
| Huxley | 1972–96 | ZD | 0 binding | SUBOPTIMAL |
| Montgomery | 1971 | ZD | 0 binding | INERT |
| Heath-Brown | 1979, 2017 | ZD + A\* | 1 ZD + 3 A\* | **LOAD-BEARING** |
| Ivic | 1980–2003 | ZD | 5 (mid-σ) | INERT |
| Jutila | — | ZD | 0 binding | SUBOPTIMAL |
| Conrey | 1989 | ZD | 0 binding | SUBOPTIMAL |
| Bourgain | 1995–2002 | ZD | 1 | INERT |
| Ford | 2002 | ZD | 0 binding | INERT |
| Pintz | — | ZD | 19 (high-σ) | SUBOPTIMAL |
| Guth--Maynard | 2024 | ZD | 1 | INERT |
| Chen--Debruyne--Vindas | 2024 | ZD | 1 | INERT |
| Carlson | 1921 | ZD | 0 binding | INERT |
| Tao--Trudgian--Yang | 2024 | ZD + A\* | 6 ZD + 5 A\* | INERT |

---

## 9. Envelope Construction Summary

**A(σ) envelope**:  
- 170 input hypotheses → 40 binding intervals.
- Constructed by `best_zero_density_estimate()`: for each σ, selects the hypothesis with the smallest A(σ) value.
- The interval partition is the common refinement of all hypothesis domains.

**A\*(σ) envelope**:  
- 8 input hypotheses → 8 binding intervals.
- Constructed by `compute_best_energy_bound()`: analogous pointwise selection.
- Much sparser: only Heath-Brown (3 intervals) and TTY25 (5 intervals) contribute.

**Gap computation**:  
- Common refinement of A(σ) and A\*(σ) intervals yields 46 gap-intervals.
- On each, α(σ) and β(σ) are computed symbolically.
- θ\_max = max over all gap-intervals = 3/2.
