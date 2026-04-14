# 03 — Mode 2: Extremal Dynamics

## 1. Overview

Mode 2 derives the extremal-dynamics constraints from the α/β machinery. The prime gap exponent θ(σ) is computed on each of 46 gap-intervals as the supremum of two rational functionals α(σ) and β(σ), each depending on the local values of A(σ) and A\*(σ). The global bound is θ\_max = max over all intervals.

This section traces the monotonic climb of θ(σ) toward the extremal vertex and identifies the structural mechanism by which θ\_max = 3/2 is achieved.

---

## 2. The α/β Machinery

On each gap-interval with active zero-density bound A and energy bound A\*:

**U1 (Alpha Functional).**  
α(σ) = 4σ − 2 + 2·(A\*·(1−σ) − 1) / (A\* − A)

**U2 (Beta Functional).**  
β(σ) = 4σ − 2 + (A\*·(1−σ) − 1) / A

**U3 (Local Theta).**  
θ(σ) = max(sup\_σ α(σ), sup\_σ β(σ)) on each interval.

**U4 (Global Theta).**  
θ\_max = max\_i θ\_i = 3/2.

### 2.1 Degeneration Conditions

The α functional has a pole when A\* = A (the denominator A\* − A vanishes). This occurs when the energy bound and the density bound coincide. If Heath-Brown's A\* estimates are removed, the remaining A\* coverage is insufficient: on [1/2, 7/10), no A\* estimate survives, and the system produces θ ~ 250,000 — a numerical artifact of near-degeneracy, not a meaningful bound.

**U5 (Non-Degeneracy Requirement).**  
For the computation to produce finite θ, the condition A\*(σ) > A(σ) must hold strictly on every gap-interval. Heath-Brown's energy estimates are the sole guarantor of this condition on [1/2, 2/3), [2/3, 7/10), and [5/6, 1).

---

## 3. The θ Progression Table

46 gap-intervals, ordered by σ. The "controlling constraint" column identifies which functional (α or β) achieves the supremum.

| # | Interval | θ | ZD Author | A\* Author | Regime |
|---|---|---|---|---|---|
| 1 | [1/2, 2/3) | 1.2000 | Ingham | Heath-Brown | Low-σ |
| 2 | [2/3, 7/10) | 1.2345 | Ingham | Heath-Brown | Low-σ |
| 3 | [7/10, 0.7256) | 1.2364 | Guth--Maynard | TTY25 | Mid-σ |
| 4 | [0.7256, 3/4) | 1.2528 | Guth--Maynard | TTY25 | Mid-σ |
| 5 | [3/4, 19/25) | 1.2528 | Guth--Maynard | TTY25 | Mid-σ |
| 6 | [19/25, 127/167) | 1.2380 | Ivic | TTY25 | Mid-σ |
| 7 | [127/167, 289/380) | 1.2356 | Ivic | TTY25 | Mid-σ |
| 8 | [289/380, 13/17) | 1.2355 | Ivic | TTY25 | Mid-σ |
| 9 | [13/17, 17/22) | 1.2306 | Ivic | TTY25 | Mid-σ |
| 10 | [17/22, 41/53) | 1.2249 | TTY25 | TTY25 | Mid-σ |
| 11 | [41/53, 7/9) | 1.2222 | Ivic | TTY25 | Mid-σ |
| 12 | [7/9, 0.7929) | 1.2193 | TTY25 | TTY25 | Mid-σ |
| 13 | [0.7929, 1867/2347) | 1.2080 | TTY25 | TTY25 | Mid-σ |
| 14 | [1867/2347, 5/6) | 1.2540 | Bourgain | TTY25 | Transition |
| 15 | [5/6, 7/8) | 1.2667 | Bourgain | Heath-Brown | Transition |
| 16 | [7/8, 279/314) | 1.2667 | TTY25 | Heath-Brown | Transition |
| 17 | [279/314, 155/174) | 1.2534 | CDV | Heath-Brown | Transition |
| 18 | [155/174, 9/10) | 1.2543 | Ivic | Heath-Brown | Transition |
| 19 | [9/10, 31/34) | 1.2620 | TTY25 | Heath-Brown | High-σ onset |
| 20 | [31/34, 14/15) | 1.2828 | Derived | Heath-Brown | High-σ onset |
| 21 | [14/15, 2841/3016) | 1.2951 | Derived | Heath-Brown | High-σ onset |
| 22 | [2841/3016, 859/908) | 1.3015 | Derived | Heath-Brown | High-σ onset |
| 23 | [859/908, 23/24) | 1.3210 | Derived | Heath-Brown | High-σ onset |
| 24 | [23/24, 2211487/2274732) | 1.3451 | Pintz | Heath-Brown | Pintz regime |
| 25 | [2211487/2274732, 39/40) | 1.3524 | Derived | Heath-Brown | Pintz regime |
| 26 | [39/40, 40/41) | 1.3718 | TTY25 | Heath-Brown | Pintz regime |
| 27 | [40/41, 41/42) | 1.3725 | TTY25 | Heath-Brown | Pintz regime |
| 28 | [41/42, 59/60) | 1.3850 | Pintz | Heath-Brown | Pintz regime |
| 29 | [59/60, 83/84) | 1.4081 | Pintz | Heath-Brown | Pintz regime |
| 30 | [83/84, 111/112) | 1.4240 | Pintz | Heath-Brown | Pintz regime |
| 31 | [111/112, 143/144) | 1.4355 | Pintz | Heath-Brown | Pintz regime |
| 32 | [143/144, 179/180) | 1.4441 | Pintz | Heath-Brown | Pintz regime |
| 33 | [179/180, 219/220) | 1.4508 | Pintz | Heath-Brown | Pintz regime |
| 34 | [219/220, 263/264) | 1.4561 | Pintz | Heath-Brown | Pintz regime |
| 35 | [263/264, 311/312) | 1.4605 | Pintz | Heath-Brown | Pintz regime |
| 36 | [311/312, 363/364) | 1.4640 | Pintz | Heath-Brown | Pintz regime |
| 37 | [363/364, 419/420) | 1.4670 | Pintz | Heath-Brown | Pintz regime |
| 38 | [419/420, 479/480) | 1.4696 | Pintz | Heath-Brown | Pintz regime |
| 39 | [479/480, 543/544) | 1.4718 | Pintz | Heath-Brown | Pintz regime |
| 40 | [543/544, 611/612) | 1.4737 | Pintz | Heath-Brown | Pintz regime |
| 41 | [611/612, 683/684) | 1.4753 | Pintz | Heath-Brown | Pintz regime |
| 42 | [683/684, 759/760) | 1.4768 | Pintz | Heath-Brown | Pintz regime |
| 43 | [759/760, 839/840) | 1.4781 | Pintz | Heath-Brown | Pintz regime |
| 44 | [839/840, 923/924) | 1.4793 | Pintz | Heath-Brown | Pintz regime |
| 45 | [923/924, 1011/1012) | 1.4804 | Pintz | Heath-Brown | Pintz regime |
| **46** | **[1011/1012, 1)** | **1.5000** | **Heath-Brown** | **Heath-Brown** | **Extremal** |

---

## 4. Structural Analysis of the Climb

### 4.1 Four Regimes

The θ progression reveals four structurally distinct regimes:

**Regime I: Low-σ (intervals 1–2, σ ∈ [1/2, 7/10))**  
θ ∈ [1.20, 1.23]. Controlled by Ingham (ZD) + Heath-Brown (A\*). These are the classical estimates. θ is moderate because both A and A\* are well-bounded far from σ = 1.

**Regime II: Mid-σ (intervals 3–13, σ ∈ [7/10, 1867/2347))**  
θ ∈ [1.21, 1.25]. This is the TTY25 innovation zone. TTY25 controls both A and A\* on intervals 10, 12, 13. Guth--Maynard and Ivic share the ZD side. θ actually *dips* to a global minimum of 1.2080 at interval 13 — this is the best-constrained region.

**Regime III: Transition (intervals 14–23, σ ∈ [1867/2347, 23/24))**  
θ ∈ [1.25, 1.32]. A\* switches from TTY25 to Heath-Brown at σ = 5/6. The ZD side fragments among Bourgain, CDV, Ivic, TTY25, and derived estimates. θ rises steadily.

**Regime IV: Pintz regime (intervals 24–45, σ ∈ [23/24, 1011/1012))**  
θ ∈ [1.35, 1.48]. Pintz controls the ZD channel with 18 binding intervals. Heath-Brown controls A\*. θ climbs monotonically through Pintz's systematic family of estimates A ≤ 3/(c·(2kσ − (2k−1))), approaching but never reaching 3/2.

**Regime V: Extremal (interval 46, σ ∈ [1011/1012, 1))**  
θ = 3/2 exactly. Heath-Brown controls both channels. This is the unique extremal vertex.

### 4.2 The Pintz Staircase

Pintz's 18 consecutive intervals in Regime IV form a "staircase": each step brings θ closer to 3/2 by a decreasing increment.

| Step | Interval | θ | Δθ from previous |
|---|---|---|---|
| 1 | [41/42, 59/60) | 1.3850 | — |
| 2 | [59/60, 83/84) | 1.4081 | +0.0231 |
| 3 | [83/84, 111/112) | 1.4240 | +0.0159 |
| 4 | [111/112, 143/144) | 1.4355 | +0.0115 |
| ... | ... | ... | decreasing |
| 18 | [923/924, 1011/1012) | 1.4804 | +0.0010 |

The staircase converges toward 3/2 but never reaches it. The final step from 1.4804 to 1.5000 requires Heath-Brown's qualitatively different estimate (sub-polynomial vs rational).

### 4.3 Why Removing Heath-Brown Produces θ ~ 250,000

When Heath-Brown is removed:
1. The A\* envelope loses coverage on [1/2, 7/10) and [5/6, 1).
2. On [1/2, 7/10), only TTY25's A\* estimates survive, starting at σ = 7/10. Below that, A\* is undefined or takes a default value.
3. The α functional α = 4σ − 2 + 2(A\*(1−σ) − 1)/(A\* − A) degenerates: when A\* is absent or trivially large, the numerator grows without bound while the denominator (A\* − A) approaches zero.
4. The numerical result θ ~ 250,000 reflects division by a near-zero denominator — a structural collapse, not a meaningful prime gap bound.

This confirms that Heath-Brown's energy estimates are not merely "good" — they are **structurally necessary** for the computation to produce finite output.

### 4.4 The SUBOPTIMAL Paradox (Resolved)

Removing Pintz *improves* θ\_max from 1.5 to 1.4348. Removing Ingham, Huxley, Jutila, or Conrey each improves it to 1.4804. This appears paradoxical: how can removing a constraint improve the bound?

**The mechanism is not dependency-chain contamination.** Heath-Brown's ZD estimate on [1011/1012, 1) has **zero dependencies** — it is a standalone result. Pintz does not feed into it. The paradox operates through **envelope activation**, not algebraic dependency.

**What actually happens:**

1. Without Pintz, a derived rational estimate A(σ) ≤ 6/(303σ − 290) covers the entire interval [59/60, 1). It is a *weaker* pointwise bound than Heath-Brown's 6.42√(1−σ), meaning it gives larger A(σ) values near σ = 1.

2. With Pintz, his 18 tight rational bounds tile [41/42, 1011/1012). They are *better* (smaller) than 6/(303σ − 290) on that range. But they stop at σ = 1011/1012, where Heath-Brown's sub-polynomial estimate 6.42√(1−σ) takes over as the best bound.

3. **Pintz activates Heath-Brown.** By beating the derived rational bound on [41/42, 1011/1012), Pintz prevents that rational bound from extending to σ = 1. This forces the envelope to switch to Heath-Brown's square-root form for the last sliver [1011/1012, 1).

4. The square-root form, when plugged into the α functional, produces α → 3/2 as σ → 1. The rational form 6/(303σ − 290) produces α → 33/23 ≈ 1.4348. **The "better" pointwise ZD estimate produces a worse θ.**

This is a **form mismatch**: the α/β functional penalizes the sub-polynomial decay of √(1−σ) more than the rational decay of 1/(cσ − d). Heath-Brown's estimate is a better zero-density bound in isolation, but a worse input to the prime-gap machinery.

**Confirmed numerically:**
- α on [1011/1012, 1) with Heath-Brown ZD: 1.472 → 1.492 → 1.497 → 1.5 as σ → 1
- α on [59/60, 1) with derived rational ZD: 1.375 → 1.435 (bounded, never reaches 1.5)
- Minimal set (no Pintz, no GM, no Bourgain, etc.): θ\_max = 1.4348 — identical to no-Pintz alone

**The implication:** θ\_max = 3/2 is an assembly artifact. The existing literature contains rational ZD bounds that, if allowed to cover [59/60, 1) without Pintz's intervention, produce θ\_max = 33/23 ≈ 1.4348. The "classical" 3/2 bound is not a hard ceiling — it is a consequence of how the envelope is assembled from heterogeneous estimate families.

---

## 5. Extremal Vertex Characterization

The unique extremal vertex of the X5D polytope:

| Coordinate | Value |
|---|---|
| σ | [1011/1012, 1) |
| A(σ) | Heath-Brown: 6.42√(1−σ) |
| A\*(σ) | Heath-Brown: 12/(4σ−1) |
| α(σ) | Symbolically computed; sup = 1.5 |
| β(σ) | Symbolically computed; sup ≤ 1.5 |
| θ | **3/2** |

**Vertex uniqueness**: No other gap-interval achieves θ = 3/2. The second-largest θ is 1.4804 on [923/924, 1011/1012) (Pintz + Heath-Brown).

**Gap to second vertex**: Δθ = 0.0196, a 1.3% margin. The bound is not tight in the sense that there is significant "daylight" between the extremal vertex and the rest of the polytope.
