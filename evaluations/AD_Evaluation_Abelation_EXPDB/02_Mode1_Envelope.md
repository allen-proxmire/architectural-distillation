# 02 — Mode 1: Envelope Constraints

## 1. Overview

Mode 1 derives the envelope inequalities — the set of constraints that any valid A(σ) and A\*(σ) must satisfy. These are the "walls" of the polytope. The EXPDB pipeline constructs two piecewise envelopes from 178 input hypotheses, yielding 40 + 8 = 48 binding segments.

---

## 2. Forbidden Configurations

The following configurations are forbidden by the axioms:

**F1.** A(σ) < 0 for σ ∈ (1/2, 1). (Zero-density exponents are non-negative.)

**F2.** A\*(σ) < A(σ) for any σ. (The energy bound is at least as large as the density bound; otherwise the α functional degenerates.)

**F3.** A(σ) < 2/(1−σ) as σ → 1 without matching A\* growth. (Insufficient density decay near σ = 1 breaks the α/β computation; this is why removing Heath-Brown produces θ ~ 250,000.)

**F4.** A\*(σ) undefined on an interval where A(σ) is defined. (The hybrid channel requires both inputs on every gap-interval.)

---

## 3. Necessary Configurations

**N1.** A\*(σ) must cover [1/2, 1) completely. Currently, only Heath-Brown provides coverage on [1/2, 2/3), [2/3, 7/10), and [5/6, 1). Removing any of these collapses the computation.

**N2.** A(σ) must cover [1/2, 1) completely. Ingham's estimate A(σ) ≤ 3/(2−σ) provides the foundational low-σ coverage.

**N3.** Near σ = 1, A(σ) must grow no faster than O(1/√(1−σ)) for θ to remain finite. Heath-Brown's A(σ) ≤ 6.42√(1−σ) satisfies this.

---

## 4. Envelope Constraints: A(σ) — Zero-Density Channel

40 intervals, enumerated E1–E40 by σ position.

| ID | Interval | Binding Author | Bound | Interior/Extremal |
|---|---|---|---|---|
| E1 | [1/2, 7/10) | Ingham | A ≤ 3/(2−σ) | Interior |
| E2 | [7/10, 19/25) | Guth--Maynard | A ≤ 15/(5σ+3) | Interior |
| E3 | [19/25, 127/167) | Ivic | A ≤ 9/(2(4σ−1)) | Interior |
| E4 | [127/167, 13/17) | Ivic | A ≤ 15/(13σ−3) | Interior |
| E5 | [13/17, 17/22) | Ivic | A ≤ 6/(5σ−1) | Interior |
| E6 | [17/22, 41/53) | TTY25 | A ≤ 2/(3(3σ−2)) | Interior |
| E7 | [41/53, 7/9) | Ivic | A ≤ 9/(7σ−1) | Interior |
| E8 | [7/9, 1867/2347) | TTY25 | A ≤ 9/(8(2σ−1)) | Interior |
| E9 | [1867/2347, 7/8) | Bourgain | A ≤ 3/(2σ) | Interior |
| E10 | [7/8, 279/314) | TTY25 | A ≤ 3/(10σ−7) | Interior |
| E11 | [279/314, 155/174) | CDV | A ≤ 24/(30σ−11) | Interior |
| E12 | [155/174, 9/10) | Ivic | A ≤ 24/(30σ−11) | Interior |
| E13 | [9/10, 31/34) | TTY25 | A ≤ 3/(10σ−7) | Interior |
| E14 | [31/34, 14/15) | Derived | A ≤ 11/(12(4σ−3)) | Interior |
| E15 | [14/15, 2841/3016) | Derived | A ≤ 391/(2493σ−2014) | Interior |
| E16 | [2841/3016, 859/908) | Derived | A ≤ 22232/(163248σ−134765) | Interior |
| E17 | [859/908, 23/24) | Derived | A ≤ 356/(2742σ−2279) | Interior |
| E18 | [23/24, 2211487/2274732) | Pintz | A ≤ 3/(4(6σ−5)) | Interior |
| E19 | [2211487/2274732, 39/40) | Derived | A ≤ 86152/(1447460σ−1311509) | Interior |
| E20 | [39/40, 40/41) | TTY25 | A ≤ 3/(5(8σ−7)) | Interior |
| E21 | [40/41, 41/42) | TTY25 | A ≤ 2/(13σ−10) | Interior |
| E22 | [41/42, 59/60) | Pintz | A ≤ 3/(5(8σ−7)) | Interior |
| E23 | [59/60, 83/84) | Pintz | A ≤ 1/(2(10σ−9)) | Interior |
| E24 | [83/84, 111/112) | Pintz | A ≤ 3/(7(12σ−11)) | Interior |
| E25 | [111/112, 143/144) | Pintz | A ≤ 3/(8(14σ−13)) | Interior |
| E26 | [143/144, 179/180) | Pintz | A ≤ 1/(3(16σ−15)) | Interior |
| E27 | [179/180, 219/220) | Pintz | A ≤ 3/(10(18σ−17)) | Interior |
| E28 | [219/220, 263/264) | Pintz | A ≤ 3/(11(20σ−19)) | Interior |
| E29 | [263/264, 311/312) | Pintz | A ≤ 1/(4(22σ−21)) | Interior |
| E30 | [311/312, 363/364) | Pintz | A ≤ 3/(13(24σ−23)) | Interior |
| E31 | [363/364, 419/420) | Pintz | A ≤ 3/(14(26σ−25)) | Interior |
| E32 | [419/420, 479/480) | Pintz | A ≤ 1/(5(28σ−27)) | Interior |
| E33 | [479/480, 543/544) | Pintz | A ≤ 3/(16(30σ−29)) | Interior |
| E34 | [543/544, 611/612) | Pintz | A ≤ 3/(17(32σ−31)) | Interior |
| E35 | [611/612, 683/684) | Pintz | A ≤ 1/(6(34σ−33)) | Interior |
| E36 | [683/684, 759/760) | Pintz | A ≤ 3/(19(36σ−35)) | Interior |
| E37 | [759/760, 839/840) | Pintz | A ≤ 3/(20(38σ−37)) | Interior |
| E38 | [839/840, 923/924) | Pintz | A ≤ 1/(7(40σ−39)) | Interior |
| E39 | [923/924, 1011/1012) | Pintz | A ≤ 3/(22(42σ−41)) | Interior |
| **E40** | **[1011/1012, 1)** | **Heath-Brown** | **A ≤ 6.42√(1−σ)** | **EXTREMAL** |

---

## 5. Envelope Constraints: A\*(σ) — Energy Channel

8 intervals, enumerated E\*1–E\*8.

| ID | Interval | Binding Author | Bound | Interior/Extremal |
|---|---|---|---|---|
| E\*1 | [1/2, 2/3) | Heath-Brown | A\* ≤ (10−11σ)/((σ−2)(σ−1)) | Interior |
| E\*2 | [2/3, 7/10) | Heath-Brown | A\* ≤ (18−19σ)/(2(σ−2)(σ−1)) | Interior |
| E\*3 | [7/10, 0.7256) | TTY25 | A\* ≤ 5(19σ−18)/(2(σ−1)(5σ+3)) | Interior |
| E\*4 | [0.7256, 3/4) | TTY25 | A\* ≤ 2(44σ−45)/((σ−1)(2σ+15)) | Interior |
| E\*5 | [3/4, 289/380) | TTY25 | A\* ≤ (220σ−197)/(8(σ−1)(5σ−1)) | Interior |
| E\*6 | [289/380, 0.7929) | TTY25 | A\* ≤ 3(30σ−29)/(5(σ−1)(5σ−1)) | Interior |
| E\*7 | [0.7929, 5/6) | TTY25 | A\* ≤ 4(9σ−10)/(5(σ−1)(4σ−1)) | Interior |
| **E\*8** | **[5/6, 1)** | **Heath-Brown** | **A\* ≤ 12/(4σ−1)** | **EXTREMAL** |

---

## 6. Envelope Geometry Summary

### 6.1 A(σ) Structure
- **40 intervals** from 9 distinct authors + derived estimates.
- **Pintz dominates** the high-σ regime: 19 of 40 intervals lie in [23/24, 1011/1012), all with the family A ≤ 3/(c·(2kσ − (2k−1))) for increasing k. This is a systematic sequence of estimates, not independent constraints.
- **Heath-Brown** holds the single extremal interval [1011/1012, 1) with the only sub-polynomial bound A ≤ 6.42√(1−σ).
- **TTY25** contributes 6 intervals in the mid-range [17/22, 31/34), interleaved with Ivic.

### 6.2 A\*(σ) Structure
- **8 intervals** from 2 authors only.
- **Heath-Brown** provides the structural skeleton: [1/2, 2/3), [2/3, 7/10), [5/6, 1). These three intervals are the only A\* coverage outside the TTY25 range.
- **TTY25** fills the interior [7/10, 5/6) with 5 refined sub-intervals.

### 6.3 Author Coverage Map

```
σ:  1/2          7/10         5/6              1
A:  |--Ingham--|--GM--|--Ivic/TTY25--|..derived..|--Pintz (×19)--|--HB--|
A*: |---Heath-Brown---|-----TTY25 (×5)-----|------Heath-Brown------|
```

---

## 7. Redundancy Census

Of 178 input hypotheses:
- **48 bind** (40 A(σ) + 8 A\*(σ)).
- **130 are strictly dominated** and never achieve equality anywhere on the envelope.
- **Ivic** contributes 111 hypotheses but only 5 binding intervals — **95.5% redundancy**.
- **Pintz** contributes 20 hypotheses with 19 binding intervals — **5% redundancy** (most efficient author).
- **Montgomery, Ford, Carlson, Huxley, Jutila, Conrey**: 0 binding intervals despite 12 combined hypotheses.
