# CoarseGrain Arc — what continuum law does the certified substrate generate?

**Question:** does ED's coarse-graining actually produce a continuum law from the certified substrate — and which one? The cleanest, most falsifiable instance of the program's deepest open thread (*does coarse-graining give the continuum*). Let the data pick the PDE class; diffusion and the corpus Q-C PDE are hypotheses, not assumptions.

**This is the program's first *tested* (not merely *located*) substrate result** — and it can come back "no."

## Verdict (one line)

**The certified ED substrate is QUALITATIVELY generative (kinetic lattice-gas: ballistic worldlines + disorder scattering, isotropic fast-relaxing equilibrium, genuine saturation-driven mobility degeneracy) but QUANTITATIVELY non-generative under the methods tried: NOT diffusion, NO clean closed continuum PDE, and NOT the UDM mobility law (β≈0 not β≈2 — both without blocking [R4] and with saturation-extinction blocking [R5]).** Same form-yes / precise-law-no shape the wider program keeps finding. The program's clearest *tested* (build-and-run, came-back-no) negative.

## Contents

| File | What |
|---|---|
| `CoarseGrain_ContinuumLimit_Paper.md` | **The paper** — consolidated Rounds 1–3, method, results, verdict, limitations, Round-4 plan |
| `coarsegrain_test.py` | Round 1 — PDE-class regression + single-chain straightness |
| `coarsegrain_round2.py` | Round 2 — `(ρ,φ,J)` transport closure; single-chain drift `v`, diffusion `D` |
| `coarsegrain_round3.py` | Round 3 — merge (collision) operator; directional persistence; scaling |
| `coarsegrain_round4.py` | Round 4 — ensemble + matched space-time coarsening; velocity-resolved BGK; UDM (mobility-vs-concentration) test |
| `coarsegrain_round5.py` | Round 5 — saturation/extinction on; extinction-rate + effective-mobility vs concentration; UDM-form test |
| `docs/CoarseGrain_Round1_Results.md` | Round-1 results note (superseded by the paper for synthesis) |

## Status: arc CLOSED (Rounds 1–5)

Qualitative kinetic characterization solid; quantitative continuum closure unachieved; UDM shares the saturation *ingredient* but not its *form*. Further quantitative closure is a dedicated computational-physics project (uncertain payoff), not banked.

## The robust core (survived all three rounds, two self-corrections)

chain/worldline propagator (no branching) → ballistic free-flight + scattering off ρ-disorder → ρ is a *slaved deposition field* → **not diffusion, not a closed ρ-PDE**. R1 read it as drift-diffusion; R2 corrected to ballistic+scattering; R3 falsified R2's "merging breaks continuity" (merging is ~1%, negligible) and located the residual as measurement-limited.

## Status

Rounds 1–3 **done**. Round 4 (matched space-time coarse-graining + ensembles + velocity-resolved lattice-Boltzmann; test whether the over-damped limit is the Q-C/UDM diffusion) is a deliberate numerical study, **not** banked here.
