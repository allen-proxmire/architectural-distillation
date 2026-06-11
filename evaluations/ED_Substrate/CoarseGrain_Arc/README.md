# CoarseGrain Arc — what continuum law does the certified substrate generate?

**Question:** does ED's coarse-graining actually produce a continuum law from the certified substrate — and which one? The cleanest, most falsifiable instance of the program's deepest open thread (*does coarse-graining give the continuum*). Let the data pick the PDE class; diffusion and the corpus Q-C PDE are hypotheses, not assumptions.

**This is the program's first *tested* (not merely *located*) substrate result** — and it can come back "no."

## Verdict (one line)

**The certified ED substrate is a kinetic lattice-gas — ballistic worldlines scattering off ρ-disorder, depositing a slaved ρ field — NOT a diffusion PDE and NOT a closed scalar PDE.** The Q-C / UDM diffusion is a different ED model, at most an over-damped limit. Qualitative verdict solid; quantitative continuum closure is measurement-limited (a dedicated Round-4 study).

## Contents

| File | What |
|---|---|
| `CoarseGrain_ContinuumLimit_Paper.md` | **The paper** — consolidated Rounds 1–3, method, results, verdict, limitations, Round-4 plan |
| `coarsegrain_test.py` | Round 1 — PDE-class regression + single-chain straightness |
| `coarsegrain_round2.py` | Round 2 — `(ρ,φ,J)` transport closure; single-chain drift `v`, diffusion `D` |
| `coarsegrain_round3.py` | Round 3 — merge (collision) operator; directional persistence; scaling |
| `docs/CoarseGrain_Round1_Results.md` | Round-1 results note (superseded by the paper for synthesis) |

## The robust core (survived all three rounds, two self-corrections)

chain/worldline propagator (no branching) → ballistic free-flight + scattering off ρ-disorder → ρ is a *slaved deposition field* → **not diffusion, not a closed ρ-PDE**. R1 read it as drift-diffusion; R2 corrected to ballistic+scattering; R3 falsified R2's "merging breaks continuity" (merging is ~1%, negligible) and located the residual as measurement-limited.

## Status

Rounds 1–3 **done**. Round 4 (matched space-time coarse-graining + ensembles + velocity-resolved lattice-Boltzmann; test whether the over-damped limit is the Q-C/UDM diffusion) is a deliberate numerical study, **not** banked here.
