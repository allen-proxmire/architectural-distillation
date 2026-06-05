# The Substrate Beneath the Shadow
### Finite-Reach Generative Layers and the Determinability Boundary

*An Architectural Distillation note*

Allen Proxmire · June 2026

---

## Preface: what this note is, and is not

This is a conceptual note, not a derivation and not a unification. It observes that two systems Architectural Distillation (AD) has already engaged — **Event Density (ED)**, evaluated as the degenerate-parabolic field architecture in the AD catalog, and the **Factor Skyline (FS)**, the arithmetic project from which AD was originally extracted — share a structural pattern that AD's current taxonomy does not name.

The two systems are **unrelated in content.** ED is a physical ontology; FS is a theory of the multiplicative structure of the integers. ED does not explain prime numbers. FS does not explain physics. Nothing in this note proposes that one derives, predicts, or constrains the other. Any reader looking for a bridge between number theory and physics will not find one here, because there is none being claimed.

What the two systems share is **architecture**, in the precise sense AD uses the word: the structural framework that generates a system's behavior, independent of the system's content. The claim is narrow and, I think, defensible: ED and FS instantiate the same three-part architectural motif, and that motif is a candidate object for AD's own framework. The note states the motif, shows it in each system, and proposes — modestly, as a direction rather than a result — that AD's scope could extend to cover it.

---

## 1. Posture lock

Begin by separating the two things that could be meant by "ED and FS are related."

**They are not related in content.** There is no map from primes to particles, no shared variable, no quantity that appears in both theories. The escape density of the Factor Skyline is a product over primes; the participation measure of Event Density is a bandwidth-weighted phase on a graph. These are different objects in different domains answering different questions. To assert otherwise would be a category error, and this note asserts no such thing.

**They are related in architecture.** Each system, examined structurally, has the same three pieces:

1. A **discrete, finite-reach generative substrate** — a layer of discrete constituents whose interactions reach only finitely far, and which generates the system's structure from the bottom up.
2. A **determinability boundary** — a part of the system's behavior that the finite-reach substrate provably cannot determine. Not "has not yet determined," but *cannot*, as a consequence of the substrate's own finiteness.
3. A **continuous projection shadow** — the familiar continuous law of the system, which is not fundamental but emerges as a coarse-grained or projected image of the discrete substrate. (The term *projection shadow* is used consistently below for this third element, to keep it distinct from the substrate that casts it.)

This is the motif. The remainder of the note exhibits it in each system, names what is shared, and asks what AD should do with it.

A single discipline runs through everything below: the determinability boundary is **measured in one system and structural in the other.** In FS it is a number — a quantity of bits, computed and reproduced. In ED it is a structural feature of the ontology, present by construction but not yet quantified. Keeping this distinction sharp is the whole honesty of the note. The two are the same *kind* of object seen at different resolutions; they are not the same *measurement*, because only one of them has been measured.

---

## 2. The Event Density side

### The substrate

Event Density is a relational ontology built from a small set of primitives. **Micro-events** are discrete acts of becoming; reality is made of them, and the local rate of their production is the event density. Micro-events do not exist in isolation — they **participate** in one another's becoming, and two are **adjacent** when they integrate each other's becoming, share participation bandwidth, and maintain coherent relational timing. A **channel** is a stable subgraph along which micro-events propagate, carrying an edge weight called bandwidth. A **chain** is a sequence of micro-events maintaining coherent participation across its extent — the substrate-level object that, coarse-grained, is a particle.

There is no fundamental field, no fundamental spacetime, no fundamental wavefunction in this picture. Those are emergent. The substrate is discrete and relational, and it generates structure through the participation of micro-events in one another.

### Finite reach

The feature that matters for this note is the substrate's **finite reach**, and ED builds it in explicitly through **decoupling surfaces**. A decoupling surface is a participation threshold where reciprocal participation between two regions becomes *one-sided*: across it, one region can still influence the other, but influence does not return. The cosmic decoupling surface sits at the radius set by the expansion rate; an accelerating chain induces a decoupling surface at a definite distance behind it.

The point is structural, not cosmological. A decoupling surface is the boundary of what a region of the substrate can reach reciprocally. Beyond it, the two-way participation that the substrate's structure depends on simply ends. The substrate is finite-reach not as an approximation or a modeling convenience but as a defining commitment: participation has a horizon, and beyond the horizon the substrate's determinations do not extend.

### The determinability boundary in ED

This gives ED a determinability boundary, structurally. There are structural dependencies that cannot propagate across a decoupling surface because reciprocal participation has ended; the substrate's determinations do not extend past that horizon. The boundary is not epistemic — it is not about what an observer happens to know. It is architectural: the finite-reach substrate's determinations stop where its reciprocal participation stops.

But — and this is the load-bearing caution — **in ED this boundary is structural, not quantified.** ED tells you the boundary exists and where, in principle, it lies. It does not yet tell you, in bits, how much of the system's behavior falls on the far side of it. There is no measured "determinability gap" for Event Density. The boundary is named by the ontology and located by the decoupling surfaces; its *size* has not been computed. That gap — the absence of a number — is exactly what makes the FS side of this note useful, and exactly what the note's proposal is about.

### The shadow

Coarse-grained over many chain steps, the substrate's dynamics for a participation density reduce to a single continuous law — a quasilinear parabolic equation with a small number of constitutive channels. This is the continuous face that AD evaluated. It is not the substrate; it is the substrate's projection. The familiar continuous equation is the shadow the discrete relational structure casts when you stop tracking individual chain steps and watch the averaged density instead. The same substrate casts other shadows in other regimes — the structures one recognizes as quantum-mechanical, the structures one recognizes as gravitational — but the relevant point here is simply that the continuous law is a projection, not a foundation.

So ED has all three pieces: a discrete finite-reach substrate (micro-events, participation, decoupling surfaces), a determinability boundary (structural, beyond the decoupling surfaces, unquantified), and a continuous shadow (the coarse-grained law).

---

## 3. The Factor Skyline side

### The coverage/escape architecture

The Factor Skyline organizes the integers by their multiplicative structure. Each integer is a column whose width is its least prime factor; the integers thereby stack into a landscape governed by five emergent notions — width, height, activation, coverage, and escape — all deriving from that single primitive.

The generative mechanism is **coverage**. Each prime *p* "activates" at *p²* (the smallest integer whose least prime factor is *p*) and thereafter claims a fixed share of the integers not already claimed by smaller primes. Coverage is cumulative, uniform, and monotone: each activated prime removes its fraction of the remaining space, and the layers do not interfere (distinct primes impose coprime conditions). This is a discrete, finite-reach generative process. At any scale *N*, only the primes up to √*N* have activated; the active coverage layers are a finite set, and each acts locally on the residue structure.

An integer **escapes** if no activated layer claims it — equivalently, if it is prime. Escapes are the narrow columns that slip through every coverage layer. The fraction of integers that escape all layers up to a threshold is the escape density, an exact rational product over primes.

### The shadow

The continuous laws of the primes are projections of this discrete coverage process. The Prime Number Theorem — primes thinning like 1/log *x* — is, in the FS reading, the shadow the escape-density product casts on the number line. The product is discrete, rational, and exact; the logarithm appears only when the product is replaced by its asymptotic envelope. The logarithm is not fundamental to the primes; it is the continuous image of a discrete layered removal. The same is true of the other classical density laws: they are the number-line shadows of a two-dimensional coverage geometry.

This is the FS analogue of ED's coarse-grained equation: a continuous law that is the projection of a discrete finite-reach substrate, not a foundation in its own right.

### The determinability boundary in FS — measured

Here is what FS has that ED does not: the determinability boundary is **a number.**

The coverage layers determine a great deal. Given an integer's residue with respect to the primorial of the small primes, the template fixes whether the position is *open* (coprime to those primes, a candidate for primality) or *covered* (claimed by some small prime). This is the deterministic, finite-reach, coverage-determined layer. It is large, and it is structured.

But coverage cannot do everything. A coverage argument can certify that a position is open — free of small factors — yet it cannot distinguish a genuine prime from a product of large primes, and it cannot determine the *parity* of a number's factorization. This is the **parity barrier**, the classical obstruction in sieve theory: methods built on coverage are blind to whether an integer has an even or odd number of prime factors. Seen from the dynamics side, the same wall is **Sarnak's Möbius disjointness** — the statement that the factorization-parity signal (the Möbius function) is uncorrelated with every low-complexity, finite-memory deterministic system. Two descriptions, one boundary: the coverage substrate cannot reach the parity.

FS quantifies this. Decomposing the information in the skyline's fundamental increment:

- **Total information per integer: ≈ 2.483 bits.** This is the full entropy of the increment that distinguishes prime from composite and records the least prime factor.
- **Template (coverage-determined): ≈ 1.700 bits.** This is the part the finite-reach coverage layers determine, given the primorial residue. It is **scale-invariant** — the same at 10⁴, 10⁵, and 10⁶ — which is what makes it a structural constant of the architecture rather than an artifact of a particular range.
- **Escape (the parity barrier): ≈ 0.265 bits.** This is the residual that no coverage argument can supply — the per-integer information about actual primality that lives on the far side of the determinability boundary. (A further ≈ 0.517 bits is an activation component.)

The decomposition must be read carefully. The residual above the template is ≈ 0.783 bits, but only the **escape component (≈ 0.265 bits) is aligned with the parity barrier** and constitutes the determinability boundary; the activation component (≈ 0.517 bits) is a separate feature of the increment and is *not* part of the boundary. It is the escape component alone that the finite-reach coverage substrate provably cannot reach. The escape figure is also a *peak* rather than a universal constant across all scales, and the robust anchor is its scale-invariant complement, the 1.700-bit template; these are honest hedges from the FS work itself, preserved here.

With those qualifications stated, the essential fact stands: **FS has measured, in bits, how much of its system the finite-reach substrate cannot determine.** The determinability boundary is roughly a quarter of a bit per integer, and it has a name — the parity barrier — and a second face — Sarnak disjointness. It is a quantified finite-reach ceiling.

---

## 4. The shared motif

Set the two systems side by side, content stripped away, architecture only.

| | Event Density | Factor Skyline |
|---|---|---|
| **Finite-reach substrate** | Micro-events, participation, channels; reach bounded by decoupling surfaces | Coverage layers over the integers; reach bounded by the finite set of activated primes (those ≤ √N at scale N) |
| **Determinability boundary** | Beyond decoupling surfaces, reciprocal participation goes one-sided — *structural, unquantified* | Coverage cannot reach factorization parity — *measured, ≈ 0.265 bits; parity barrier / Sarnak* |
| **Continuous shadow** | Coarse-grained parabolic law (and the other domain faces) | PNT and the classical density laws (logarithm as projection) |

The motif is the row structure, not the entries. Each system is a **finite-reach generative substrate** whose **continuous law is a projection shadow**, and each has a **determinability boundary** — a part of itself the finite-reach substrate provably cannot determine.

This is a real structural coincidence and a narrow one. It does not say the substrates are alike in content (they are not). It does not say the boundaries are the same boundary (they are not — one is parity in arithmetic, one is reciprocal reach in physics). It says the *shape* is shared: finite-reach generation, a determinability ceiling, a projected continuous shadow. Three pieces, the same three structural roles, in two unrelated systems.

AD's current taxonomy does not name this shape. AD's poles classify continuum architectures by their dominant channel composition — diffusive, hyperbolic, dispersive, geometric, and so on. Those poles describe systems on the **shadow** side: they are features of continuous laws. The motif here is a relationship *between levels* — between a discrete finite-reach substrate and its continuous shadow, together with the boundary the substrate cannot cross. It is orthogonal to the pole taxonomy. A system's pole describes its shadow; this motif describes the substrate beneath the shadow and the edge of what that substrate can determine.

---

## 5. An AD-level contribution

AD, as it stands, evaluates architectures on the shadow side. Its six criteria — minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality — are applied to the continuous law, and its poles classify that law by channel composition. The Event Density evaluation in the catalog is an evaluation of the *coarse-grained parabolic equation*, the projection shadow, not of the discrete substrate that casts it. To state it plainly: AD's evaluation of ED (#15) was an evaluation of the PDE shadow, not of the discrete substrate that generates it. The substrate level has not been evaluated by AD at all.

The observation of this note suggests a direction: **AD's scope could extend downward, to the discrete generative layer.**

Two of the systems in AD's own orbit — the system from which AD was extracted (FS) and a system AD has evaluated (ED) — are each the continuous shadow of a discrete, finite-reach substrate. AD has been looking at the shadows. The substrates underneath them have a structural feature, the determinability boundary, that the shadow-level analysis does not see and the pole taxonomy does not name. If AD is to be a complete account of architectural structure, the substrate level and its boundary belong in scope.

And here is the part that makes the extension concrete rather than merely gestural: **the determinability boundary is a measurable structural quantity.** FS demonstrates this. The boundary is not a vague "there are things the system can't do" — it is roughly 0.265 bits per integer, scale-invariant in its template complement, with a named mechanism. AD already has a quantitative instinct: the overdetermination ratio (independent constraints over free parameters) is a number AD computes to gauge architectural rigidity. The determinability boundary could be a second such number — a measure, in bits, of how much of a system's behavior lies beyond what its finite-reach substrate can determine. Overdetermination measures how tightly the architecture is constrained from above; the determinability boundary measures how much escapes it from below.

So the proposal, stated modestly:

- The **finite-reach substrate with a projection shadow** is a candidate architectural object for AD — a structural configuration AD should be able to recognize and evaluate, distinct from the shadow-level pole.
- The **determinability boundary** is a candidate measurable invariant — sharply measured in FS (≈ 0.265 bits), structurally present in ED (the decoupling-surface boundary), awaiting quantification in the latter.
- Whether this rises to a new **pole** in AD's strict sense, or sits as a cross-cutting **invariant** orthogonal to the existing poles, is open. The pole taxonomy is channel-based and lives on the shadow; this motif lives a level down. My own inclination is that it is an *invariant* rather than a pole — a property a substrate-shadow pair can have, measurable across domains — but that classification question is exactly the kind of thing the AD framework exists to settle, and I leave it open rather than assert it.

The single most useful thing this note points at is a *task*: **measure ED's determinability boundary in bits.** FS shows it can be done — that a finite-reach substrate's determinability ceiling is a computable quantity. ED has the boundary structurally but no number. Computing it — quantifying how much of the substrate's behavior falls beyond its decoupling surfaces — would turn the shared motif from an observed shape into a measured one on both sides, and would test whether the determinability boundary is a genuine cross-domain invariant or only a suggestive rhyme. That measurement is the natural next step, and it is the kind of step AD is built to motivate.

Stated as a deliverable: **the practical next step is to quantify ED's determinability boundary, if possible, in the same information-theoretic terms used in FS** — a number of bits, computed from the substrate, measuring how much of the system's behavior falls beyond the reach of its decoupling surfaces. If that number exists and can be found, the motif is measured on both sides. If it cannot, the asymmetry between the two systems is itself a finding worth recording.

---

## 6. Scope, cautions, and what is not being claimed

Because the temptation to over-read a cross-domain pattern is real, the cautions deserve their own section.

**No unification.** This note does not unify physics and number theory, does not claim a common origin for ED and FS, and does not propose that either field's results bear on the other. The systems are independent. The pattern is architectural.

**No derivation.** Nothing here is derived. The motif is *observed* in two systems, not proven to hold of any third, and not shown to follow from any deeper principle. It is a structural description, and structural descriptions of this kind are noticings, not theorems.

**Measured versus structural, held apart.** The determinability boundary is measured in FS and structural in ED. These are not the same epistemic status, and the note does not pretend they are. FS's ≈ 0.265 bits is a computed, reproduced quantity. ED's boundary is a feature of the ontology with no number attached. The claim that they are "the same kind of object" is a claim about *kind*, not about *measurement*; until ED's boundary is quantified, the symmetry between the two sides is a structural analogy, and analogies are to be held loosely until they are made to pay. Structural analogies are invitations to measure, not conclusions.

**A candidate, not a fixture.** The proposal that AD's scope extends to the substrate level, and that the determinability boundary is a cross-domain invariant, is offered as a direction worth testing — not as an established part of the framework. It earns its place only if the ED-side measurement can be carried out and if the motif survives examination in further systems. One measured instance and one structural instance is enough to notice a pattern; it is not enough to canonize one.

What remains, when all the cautions are applied, is small and I think solid: two systems AD has engaged are each a finite-reach generative substrate casting a continuous shadow, each has a part it cannot determine, and in one of them that part has been measured. That is a shared architectural shape AD does not currently name, and it is worth naming — carefully, and without letting it carry more weight than two examples can bear.

---

*This note is a conceptual proposal within the Architectural Distillation framework. It references the Event Density evaluation in the AD catalog and the Factor Skyline project from which AD was extracted. It makes no claim that Event Density and the Factor Skyline are related in content; the relationship asserted is architectural only.*
