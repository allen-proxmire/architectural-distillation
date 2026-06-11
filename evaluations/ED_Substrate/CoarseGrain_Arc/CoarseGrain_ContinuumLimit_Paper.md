# The Continuum Limit of the Certified ED Substrate: a Kinetic Lattice-Gas, not a Diffusion PDE

**Substrate-evaluation paper (Architectural Distillation, ED-Substrate arc).**
Allen Proxmire · June 2026 · *with the certified Σ-rule simulator (`Bits/`)*

---

## Abstract

We ask, empirically and without prior assumption, what continuum law the **certified ED substrate** generates under coarse-graining. The certified substrate is the 13-primitive, two-kernel Σ-rule simulator (the same instrument certified by 20/20 correctness gates for the determinability-boundary measurement). Running it, coarse-graining the event-density field ρ, and applying SINDy-style regression to candidate PDE families, we find: **the substrate is a chain/worldline propagator, and its native continuum is a kinetic lattice-gas — ballistic worldlines scattering off ρ-disorder — not a diffusion PDE.** Three results are robust: (i) ρ is a *slaved deposition field* (`∂_t ρ ∝ φ`, the front density), not an independently-evolving field; (ii) diffusion is decisively excluded (`∇²ρ` carries R² ≈ 0.001–0.004 for `∂_t ρ`); (iii) single fronts free-stream ballistically (`|v|≈1`) on smooth landscapes and scatter diffusively (directional persistence drops to ≈0.36) on rough ones. We could **not** quantitatively verify the closed continuum equation — the transport closure is measurement-limited on this sparse deterministic field — but the *qualitative* characterization is solid, and it cleanly separates the certified Σ-substrate from the corpus's Q-C / UDM **diffusion** PDE, which is at most a downstream (over-damped) limit, not the substrate's direct continuum. The investigation self-corrected twice (Round 2 corrected Round 1; Round 3 corrected Round 2), which we report as a feature of the method.

## 1. Why this question

ED's case is *generativity*: one small primitive set generating the form of physics across domains. The deepest recurring open question — surfaced repeatedly in the substrate-evaluation program (charge's field, gravity's field equation, the determinability boundary) — is whether ED's **coarse-graining actually produces the continuum**, or only ever yields discrete skeletons. The cleanest, most falsifiable instance of that question is the simplest: *take the certified substrate, coarse-grain it, and see what continuum equation it obeys.* This paper answers that, letting the data pick the PDE class, with diffusion and the corpus's Q-C PDE treated as hypotheses, not assumptions.

## 2. Method

The certified Σ-rule substrate evolves node state `(ρ, orientation)` on a fixed participation graph; a front commits (increments ρ by a fixed amount) at its Σ-maximal admissible neighbour and advances. We build an `S×S` grid substrate (`S=121`), seed initial ρ-profiles (uniform/random, Gaussian, step, ring, gradient), seed an ensemble of fronts, evolve, and snapshot the fields each step. We coarse-grain by block-averaging at multiple block sizes, estimate `∂_t ρ, ∂_t φ, ∇ρ, ∇²ρ, |∇ρ|, ∇·J` by finite differences, and regress (least-squares R²) against candidate term-libraries. We instrument the commit log to recover the **front-density** `φ(x,t)` (active fronts per cell), the **front-current** `J(x,t)` (net commit displacement per cell), the **merge sink** `M(x,t)`, and the **directional persistence** `p`. No rule is modified; the certified simulator is used as-is.

## 3. The structural facts that frame everything

Two structural facts (verified directly) reshape the question before any regression:

- **The certified front does not branch.** One seed → exactly one active front after many steps, depositing ρ along a **1-D chain (a worldline)**. The Σ-rule is a *chain propagator, not a field-update rule*. A "ρ-field PDE" is therefore the wrong object for a single front.
- **ρ only changes where a front commits.** ρ is monotone and grows by a fixed increment at each commit, so `∂_t ρ` is the commit-deposition footprint. **ρ is a deposited field slaved to the fronts**, not an independent dynamical field.

## 4. Results

### 4.1 ρ-only PDEs fail; diffusion is excluded (Round 1)

Coarse-graining the ρ field from a front ensemble and regressing `∂_t ρ`:

| IC | diffusion `∇²ρ` | eikonal `|∇ρ|` | diff+eik | PME/UDM |
|---|---|---|---|---|
| uniform | 0.004 | 0.001 | 0.005 | 0.009 |
| gaussian | 0.001 | 0.065 | 0.065 | 0.062 |
| step | 0.001 | 0.094 | 0.095 | 0.095 |
| ring | 0.001 | 0.057 | 0.059 | 0.045 |

**Diffusion is decisively rejected** (R² ≈ 0.001–0.004 across all ICs). No closed ρ-only PDE fits (best ≈ 0.10, a weak transport term). This is structural, per §3: ρ is slaved to the transported front-density, so a closed equation in ρ alone cannot exist.

### 4.2 The worldline: ballistic free-flight + disorder scattering (Rounds 2–3)

Single-chain statistics on controlled landscapes:

| landscape | metric | value | reading |
|---|---|---|---|
| flat / constant ρ | drift `|v|` | **1.00** | ballistic (max speed) |
| ρ-gradient (slope 0.001→0.006) | drift `|v|` | 0.98 → 0.87 | still ballistic; gradient is a weak modulation |
| random ρ | diffusion `D` (MSD=4Dt) | **≈1.26** | scattering off disorder |
| smooth (gaussian/gradient) | persistence `p` | **0.68 / 0.73** | ballistic free-flight |
| random | persistence `p` | **0.36** | collision-dominated |

The front is a **ballistic particle scattering off ρ-disorder** (a Lorentz-gas/kinetic picture): free flight at `v≈1`, randomized by landscape roughness. The ρ-*gradient* barely changes the speed; the landscape *roughness*, not its gradient, sets the diffusion. (This corrects Round 1's "drift-diffusion driven by ∇ρ" reading.)

### 4.3 The transport closure: deposition holds, continuity is not cleanly verifiable (Rounds 2–3)

Testing the `(ρ, φ, J)` kinetic closure:

| closure | R² | finding |
|---|---|---|
| deposition `∂_t ρ ~ k·φ` | 0.23–0.34 (k≈0.6) | **holds** — ρ slaved to front density, as predicted |
| continuity `∂_t φ ~ −∇·J` | 0.04–0.09 | not cleanly verified |
| current `J ~ aφ∇ρ − D∇φ` | 0.03–0.19 | weak; drift is *down*-gradient (`a<0`, strain-avoidance) |
| continuity `+` merge sink `M` | 0.038 → **0.038** | merge sink **does not** improve it |

The Round-2 hypothesis — that continuity fails because front number is not conserved (merging) — is **falsified in Round 3**: merging is negligible (`M/φ ≈ 0.01`) and adding `M` produces no improvement. With fronts essentially conserved and merging negligible, the residual low continuity R² is **measurement-limited**, not a physics negative: φ is binary per node, the ensemble is sparse and deterministic, and the coarse-graining mismatches space and time (a front crosses a 4-block cell in ~4 steps, so `∂_t φ` is under-resolved). Consistently, the closure is resolution-sensitive (e.g. Gaussian-IC continuity R² rises 0.046 → 0.112 as blocks coarsen 2→8) — the fingerprint of a measurement artifact, not a conservation failure.

## 5. The method self-corrected (and that is the point)

The three rounds form a chain of honest corrections: **R1** read the single chain as drift-diffusion driven by ∇ρ; **R2** showed it is ballistic free-flight + disorder scattering (gradient is a weak modulation), and that ρ-only does not close; **R3** falsified R2's merging diagnosis and located the residual continuity failure as measurement-limited. Each round overturned the previous round's *interpretation* while preserving its *data*. The robust core that survived all three: chain/worldline propagator → ballistic + scattering → slaved ρ → not diffusion.

## 6. Verdict

**The certified ED substrate is a kinetic lattice-gas. Its native continuum is a Boltzmann-class kinetic equation — ballistic worldlines (`v≈1`) scattering off ρ-disorder, with negligible merging (fronts ≈ conserved), depositing a slaved event-density field (`ρ ∝ φ`). It is emphatically not a diffusion PDE, and not a closed scalar PDE in ρ.**

**Consequence for the corpus.** The Q-C Boundary PDE and the Universal (Degenerate-)Mobility law are *closed, diffusion-class* descriptions in ρ. They are therefore **not the certified Σ-substrate's direct continuum limit** — the two are different ED models. If they connect, it is as a *further, over-damped / many-collision* limit of the kinetic system, not its leading order. Establishing that connection is the natural next study (§8).

**Lean for the program.** The native object being *worldlines with a current* sits on the **geodesic/kinetic side**, not the scalar-diffusion side — consistent with the substrate-evaluation finding that *geometry* (geodesic motion, the emergent metric) is the natural emergence from this substrate. The substrate makes **trajectories first; fields are what their density makes.**

## 7. Limitations (honest)

- We characterized the continuum *qualitatively* (kinetic, not diffusive); we did **not** verify a closed continuum equation *quantitatively*. The transport closure is measurement-limited on a sparse, deterministic, binary-per-node field with mismatched space-time coarse-graining.
- One substrate instantiation (the Σ-rule grid), one regime, modest sizes. A genuine continuum limit requires matched space-time coarsening and ensemble averaging.
- The absolute R² values are not the result; the *contrasts* are — diffusion ≈ 0, deposition ≈ 0.3, persistence regime-split, merging negligible.

## 8. Round-4 (a dedicated study, not banked here)

1. **Matched space-time coarse-graining + ensemble averaging** to *quantitatively* close the kinetic balance where the sparse field could not.
2. **Velocity-resolved lattice-Boltzmann / BGK:** track `f_d(x,t)` (4 lattice velocities), test free-streaming + a relaxation collision operator.
3. **Over-damped limit:** does the closed kinetic equation reduce to the Q-C / UDM **diffusion** PDE at high commit-rate / short mean-free-path? That would *connect* the two ED models rather than leave them separate — and would tie this arc to the FRAP/UDM empirical anchor.
4. **Anisotropy:** quantify the grid/tie-break-induced facet anisotropy of the transport.

---

## Appendix — artifacts

- `coarsegrain_test.py` — Round 1 (PDE-class regression; single-chain straightness).
- `coarsegrain_round2.py` — Round 2 (`(ρ,φ,J)` closure; single-chain drift `v` and diffusion `D`).
- `coarsegrain_round3.py` — Round 3 (merge sink; directional persistence; scaling).
- `docs/CoarseGrain_Round1_Results.md` — the Round-1 results note (superseded by this paper for the synthesis).

*Result: the certified ED substrate generates kinetic lattice-gas continuum dynamics (ballistic worldlines + disorder scattering, slaved ρ), not diffusion and not a closed scalar PDE; the Q-C/UDM diffusion is a different ED model, at most an over-damped limit. Qualitative verdict solid; quantitative closure is a dedicated Round-4 study. No new rules; certified simulator only; the program's first **tested** (not merely located) substrate result.*
