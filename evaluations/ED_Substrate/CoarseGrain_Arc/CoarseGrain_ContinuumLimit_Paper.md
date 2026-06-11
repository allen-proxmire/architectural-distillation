# The Continuum Limit of the Certified ED Substrate: a Kinetic Lattice-Gas, not a Diffusion PDE

**Substrate-evaluation paper (Architectural Distillation, ED-Substrate arc).**
Allen Proxmire · June 2026 · *with the certified Σ-rule simulator (`Bits/`)*

---

## Abstract

We ask, empirically and without prior assumption, what continuum law the **certified ED substrate** generates under coarse-graining. The certified substrate is the 13-primitive, two-kernel Σ-rule simulator (the same instrument certified by 20/20 correctness gates for the determinability-boundary measurement). Running it, coarse-graining the event-density field ρ, and applying SINDy-style regression to candidate PDE families, we find: **the substrate is a chain/worldline propagator, and its native continuum is a kinetic lattice-gas — ballistic worldlines scattering off ρ-disorder — not a diffusion PDE.** Three results are robust: (i) ρ is a *slaved deposition field* (`∂_t ρ ∝ φ`, the front density), not an independently-evolving field; (ii) diffusion is decisively excluded (`∇²ρ` carries R² ≈ 0.001–0.004 for `∂_t ρ`); (iii) single fronts free-stream ballistically (`|v|≈1`) on smooth landscapes and scatter diffusively (directional persistence drops to ≈0.36) on rough ones. We could **not** quantitatively verify the closed continuum equation — the transport closure is measurement-limited on this sparse deterministic field — but the *qualitative* characterization is solid, and it cleanly separates the certified Σ-substrate from the corpus's Q-C / UDM **diffusion** PDE, which is at most a downstream (over-damped) limit, not the substrate's direct continuum. The investigation self-corrected twice (Round 2 corrected Round 1; Round 3 corrected Round 2), which we report as a feature of the method. A quantitative Round 4 (ensemble averaging + matched space-time coarse-graining + velocity-resolved BGK) then tested two ambitions and returned **two negatives**: the continuity closure does not clean up even with these fixes, and — decisively — the substrate does **not** generate the corpus's Universal-Mobility (UDM) law (front mobility is concentration-independent, β≈0, not the UDM β≈2), because the strain rule produces *avoidance, not blocking*. Round 5 then resolved that fork: turning on the saturation/extinction mechanism **does** produce concentration-dependent blocking (extinction rate rises 0.03→0.24 with concentration) — the qualitative UDM *ingredient* — but the effective transport still does **not** reproduce the UDM functional form (β≈0, non-monotonic, not β≈2). So UDM is *qualitatively related* to the substrate's saturation regime but is *not quantitatively generated* by it. The arc's overall finding: the certified substrate is **qualitatively generative** (kinetic transport, isotropic equilibrium, saturation degeneracy) and **quantitatively non-generative** (no clean continuum PDE; no UDM law) — the same form-yes / precise-law-no pattern the wider program keeps finding.

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

### 4.4 The quantitative push: kinetic equilibrium clean, but two negatives (Round 4)

Round 4 applied the methodology fixes the earlier rounds lacked — **ensemble averaging** (N=120 identical-IC runs to kill sparsity noise), **matched space-time coarse-graining** (time window Δt = block B), and **velocity-resolved** front populations `f_d` (4 lattice directions) — and tested two quantitative claims.

**Positive — the kinetic equilibrium is clean.** The collision relaxes to a near-**isotropic equilibrium** (`f_d ≈ [0.25, 0.25, 0.26, 0.23]`, anisotropy 0.044) with a **fast relaxation time τ ≈ 1.5 steps**. The BGK *structure* is well-defined and the system sits near its over-damped limit.

**Negative 1 — continuity still does not close.** With ensemble + matched coarsening, the continuity R² rose from ~0.04 to **0.155** at the finest scale (B=2) but **degraded** with coarsening (0.155 → 0.07 → 0.00). The methodology fixes helped marginally and did **not** deliver a verified closed transport equation.

**Negative 2 (decisive) — the substrate does not generate UDM.** The Universal-Mobility hypothesis is that the strain rule (fronts avoid high ρ) is the microscopic origin of the mobility-capacity bound `M(ρ)=M₀(ρ_max−ρ)^β`, β≈2. We measured front mobility against **background concentration** `c` (built up over time, `c`≈0.4→2.5, ensemble-averaged over millions of front-steps):

> mobility is **flat at ≈0.36, concentration-independent** — UDM fit `(1−c/c_max)^β` gives **β ≈ −0.08, R² 0.29**, against the canonical UDM β≈2.

**The certified Σ-substrate does not generate the UDM law.** The physical reason is clean: the strain term produces **avoidance, not blocking** — a front always commits to *some* neighbour every step, so there is no mobility degeneracy. UDM's "mobility vanishes as `c→c_max`" requires a *blocking* / excluded-volume mechanism the substrate (as run) lacks. So **the substrate → UDM → FRAP chain does not close at the certified-substrate level**: UDM is a separate ED posit (Canon P4), not a consequence of these dynamics.

**The one untested mechanism.** Round 4 ran with **no extinction threshold** (fronts never die). The certified substrate also carries a **saturation/extinction** mechanism — fronts extinguish where Σ falls below threshold, which happens in dense, high-ρ regions. *That is exactly the blocking mechanism UDM needs.* It was deliberately **not** tuned in (to avoid fishing for a positive); whether it generates the UDM degeneracy is the Round-5 fork (§8).

### 4.5 The saturation fork: blocking is present, the UDM form is not (Round 5)

Round 5 turned **on** the certified substrate's saturation/extinction threshold (`extinction_threshold=−2.0`, the size-sweep value) — fronts extinguish where Σ falls below threshold, i.e. in dense regions. This is the *blocking* mechanism the strain-avoidance of Round 4 lacked. Measuring extinction and effective mobility against background concentration `c`:

- **Blocking is real.** The extinction rate **rises with concentration**: `0.026 → 0.244` (thr=−2.0) as `c`≈0.1→1.1; `0.026 → 0.141` (thr=−3.0). Fronts die more in denser regions — a genuine concentration-dependent transport degeneracy, the qualitative UDM ingredient.
- **But the UDM form is not reproduced.** The effective mobility `μ_eff = (1−scatter)(1−e)` is **non-monotonic** (`0.24 → 0.36 → 0.25`: scatter-rate drop dominates at low `c`, extinction at high `c`), and the UDM fit `(1−c/c_max)^β` gives **β ≈ 0.05, R² 0.16** (thr=−2.0) — against canonical UDM β ≈ 2.

So **saturation-extinction supplies the blocking UDM needs, but the resulting transport does not have the UDM functional form.** UDM is *qualitatively related* to the substrate's saturation regime (the degeneracy exists) but is *not quantitatively generated* by it (wrong form). Likely reasons: the extinction is a *sharp threshold* (binary die/survive), not a smooth mobility reduction; the committed-ρ grows unbounded so there is no fixed `c_max` where mobility vanishes; and the effective-mobility proxy is confounded (scatter dominates low-`c`, extinction high-`c`). UDM remains a separate ED posit (Canon P4).

## 5. The method self-corrected (and that is the point)

The three rounds form a chain of honest corrections: **R1** read the single chain as drift-diffusion driven by ∇ρ; **R2** showed it is ballistic free-flight + disorder scattering (gradient is a weak modulation), and that ρ-only does not close; **R3** falsified R2's merging diagnosis and located the residual continuity failure as measurement-limited. Each round overturned the previous round's *interpretation* while preserving its *data*. The robust core that survived all three: chain/worldline propagator → ballistic + scattering → slaved ρ → not diffusion.

## 6. Verdict

**The certified ED substrate is a kinetic lattice-gas. Its native continuum is a Boltzmann-class kinetic equation — ballistic worldlines (`v≈1`) scattering off ρ-disorder, with negligible merging (fronts ≈ conserved), depositing a slaved event-density field (`ρ ∝ φ`). It is emphatically not a diffusion PDE, and not a closed scalar PDE in ρ.**

**Consequence for the corpus.** The Q-C Boundary PDE and the Universal (Degenerate-)Mobility law are *closed, diffusion-class* descriptions in ρ. They are therefore **not the certified Σ-substrate's direct continuum limit** — the two are different ED models. Round 4 tested the natural connection (the over-damped limit → UDM) directly and found it **does not hold as run**: front mobility is concentration-independent (β≈0, not UDM β≈2), because the strain rule gives *avoidance, not blocking*. So **UDM is not generated by the certified Σ-dynamics** — it is a separate posit (Canon P4). The one mechanism that could still yield UDM is *saturation/extinction* (fronts dying in dense regions = blocking), untested here and named as the Round-5 fork (§8).

**Quantitatively, the closure resists.** Across all five rounds, *no* clean closed continuum equation was verified — not as a ρ-PDE (R1), not as a `(ρ,φ,J)` transport system (R2–3), not even with ensemble averaging + matched space-time coarse-graining (R4: continuity R²≈0.15, degrading with scale). The kinetic *equilibrium* is clean (isotropic, τ≈1.5), but the *hydrodynamic closure* is not. And the UDM connection fails both ways: without blocking there is no degeneracy at all (R4, β≈0), and *with* blocking (saturation-extinction, R5) the degeneracy is real but does not take the UDM form (β≈0, not β≈2).

**The honest standing.** The certified substrate is **qualitatively generative** — it produces kinetic transport, an isotropic fast-relaxing equilibrium, and a genuine saturation-driven mobility degeneracy — and **quantitatively non-generative** under the methods tried: no clean closed continuum PDE, and no UDM mobility law. This is the same shape the wider substrate-evaluation program keeps returning — *form/qualitative-structure yes, precise quantitative law no* — now in the continuum-limit register, and as the program's clearest **tested** (build-and-run, came-back-no) negative.

**Lean for the program.** The native object being *worldlines with a current* sits on the **geodesic/kinetic side**, not the scalar-diffusion side — consistent with the substrate-evaluation finding that *geometry* (geodesic motion, the emergent metric) is the natural emergence from this substrate. The substrate makes **trajectories first; fields are what their density makes.**

## 7. Limitations (honest)

- We characterized the continuum *qualitatively* (kinetic, not diffusive); we did **not** verify a closed continuum equation *quantitatively* — even Round-4's ensemble + matched-coarsening fixes left continuity at R²≈0.15 (degrading with scale). The substrate may simply *not* admit a clean local hydrodynamic closure (it never reaches a steady hydrodynamic regime — ρ grows unboundedly as fronts deposit).
- The UDM negative was measured **without** the saturation/extinction mechanism; it refutes UDM-from-strain-avoidance, not UDM-from-saturation (Round 5).
- One substrate instantiation (the Σ-rule grid), modest sizes; the absolute R² are not the result, the *contrasts* are (diffusion≈0; UDM β≈0 not 2; isotropic equilibrium; merging negligible).

## 8. Rounds 4–5 outcome (the arc is closed)

**Round 4 (done).** Kinetic equilibrium clean (isotropic `f_d`, τ≈1.5); continuity still does not close (R²≈0.15, degrading); **substrate ≠ UDM** without blocking (mobility concentration-independent, β≈0 — avoidance, not blocking).

**Round 5 (done).** Saturation/extinction *does* supply blocking (extinction rate rises 0.03→0.24 with `c`), but the effective transport still does **not** take the UDM form (β≈0, non-monotonic). So UDM is *qualitatively related* to the saturation regime but *not quantitatively generated*. The fork resolves to: **UDM shares an ingredient with the substrate's saturation but is not the substrate's continuum law.**

**Beyond (open, not scoped here; lower-confidence).** Whether *any* coarse-graining yields a clean closed PDE for this substrate (it may not — the unbounded-ρ, never-steady regime works against a hydrodynamic limit); a full velocity-resolved Chapman-Enskog derivation; and whether a *different* ED instantiation (e.g. the Q-C PDE model itself) is where UDM is actually generated. The certified Σ-substrate, as the kinetic generator, is characterized; pushing the quantitative closure further is a dedicated computational-physics project with uncertain payoff.

---

## Appendix — artifacts

- `coarsegrain_test.py` — Round 1 (PDE-class regression; single-chain straightness).
- `coarsegrain_round2.py` — Round 2 (`(ρ,φ,J)` closure; single-chain drift `v` and diffusion `D`).
- `coarsegrain_round3.py` — Round 3 (merge sink; directional persistence; scaling).
- `coarsegrain_round4.py` — Round 4 (ensemble + matched space-time coarsening; velocity-resolved BGK; mobility vs background concentration / UDM test).
- `coarsegrain_round5.py` — Round 5 (saturation/extinction on; extinction-rate and effective mobility vs concentration; UDM-form test).
- `docs/CoarseGrain_Round1_Results.md` — the Round-1 results note (superseded by this paper for the synthesis).

*Result (Rounds 1–5): the certified ED substrate is **qualitatively generative** — kinetic lattice-gas (ballistic worldlines + disorder scattering), isotropic fast-relaxing equilibrium, and a genuine saturation-driven mobility degeneracy — and **quantitatively non-generative** under the methods tried: not diffusion, no clean closed continuum PDE, and not the UDM mobility law (β≈0 not β≈2, with or without blocking). The Q-C/UDM diffusion is a different ED model. The arc returns the program's clearest **tested** (build-and-run, came-back-no) negative, in the same form-yes / precise-law-no shape the wider program keeps finding. No new rules; certified simulator only.*
