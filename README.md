# MELV-Core: Mathematical Ecology of Cooperation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19029077.svg)](https://doi.org/10.5281/zenodo.19029077)

---

## MELVcore in One Sentence

MELVcore is a mathematical and computational framework that predicts when cooperation emerges in ecological, social, economic, and multi-agent systems by quantifying the energetic balance between resource overlap, service differentiation, and compatibility.

---

## Conceptual Overview

Cooperation is often treated as a moral preference or evolutionary anomaly, yet across biological and artificial systems it appears with striking regularity. MELVcore reframes cooperation as a **thermodynamic attractor** — the energetic basin into which interactive associations naturally settle when interaction costs fall below a critical threshold.

The framework extends classical Lotka–Volterra population dynamics by incorporating energetic burden, resource allocation, and compatibility coupling. These additions allow MELVcore to predict not only whether cooperation or competition will emerge, but also the stability, strength, and perpetuity of cooperative equilibria.

At its core, MELVcore formalizes a simple insight:

> **Cooperation is energetically cheaper than conflict when overlap is low, differentiation is high, and compatibility is sufficient.**

This insight holds across species, organisations, markets, and AI agents. Under normal ecological and social parameters, **78% of simulated systems reach cooperative equilibria** — cooperation is the dominant attractor, the energetic basin into which interactive associations naturally settle when interaction costs are allowed to fall below the critical threshold.

MELVcore differs from classical Lotka–Volterra models in one critical respect: where classical LV treats interaction coefficients as fixed constants, MELV treats them as **dynamic, adaptive variables** that evolve with energetic efficiency. This allows the framework to model the *direction* of system evolution, not just its current state.

---

## Mathematical Summary

MELVcore centres on three coupled quantities:

### i-factor (interaction factor)

```
i = ρ / δ
```

where ρ = resource overlap and δ = service differentiation.

| i value | Regime |
|---|---|
| i < 1.0 | Cooperation — energetically favourable |
| i ≈ 1.0 | Bifurcation threshold |
| i > 1.0 | Competition — energetically costly |

### Energetic cooperation condition

```
(C × TAX) / β < 0.50
```

where:
- **C** = environmental cost burden
- **TAX** = resource allocation fraction
- **β** = compatibility factor

When this inequality holds, cooperation is thermodynamically favoured — not as a moral choice, but as a physical prediction.

### β-factor (compatibility)

```
β = f(physical, service, temporal, φ)
```

where φ (phi) is perpetuity — the long-term sustainability of the cooperative relationship.

### Combined prediction

Cooperation emerges and stabilises when:
- i < 1.0
- (C × TAX) / β < 0.50
- φ × β exceeds the minimum compatibility threshold

These conditions define the **cooperation basin**: the energetic attractor into which systems naturally fall when interaction costs are allowed to decline.

---

## Glossary of Core Terms

**i-factor**
Ratio of resource overlap (ρ) to service differentiation (δ). The central invariant determining whether cooperation or competition emerges. Values below 1.0 favour cooperation; values above 1.0 favour competition.

**β-factor**
Composite measure of compatibility across physical, service, temporal, and sustainability dimensions. Determines how well cooperation functions once it emerges.

**Cooperation basin**
The energetic attractor where cooperative equilibria form — the stable region in parameter space into which interactive associations naturally settle when interaction costs fall below the critical threshold.

**Critical threshold (i ≈ 1.0)**
The bifurcation point separating cooperative and competitive regimes. Confirmed computationally at i = 0.9995 ± 0.029 (R² = 0.9248, p < 10⁻³⁰⁰).

**Perpetuity (φ)**
The long-term sustainability orientation of a cooperative relationship. Approaches 1.0 in mature ecosystems and stable institutions.

**Energetic burden (C × TAX)**
The effective cost of interaction relative to environmental constraints. When divided by β, determines whether a system is above or below the cooperation threshold.

**Service differentiation (δ)**
Degree to which entities provide distinct, non-overlapping functions. Higher differentiation lowers the i-factor and favours cooperation.

**Resource overlap (ρ)**
Degree to which entities compete for the same resources. Higher overlap raises the i-factor and favours competition.

**Thermodynamic attractor**
A stable state toward which systems naturally evolve. In MELV, the cooperation basin is a thermodynamic attractor — not a designed outcome, but an energetically favoured equilibrium.

---

## 🚀 Quick Start (Zero Installation)

**Two ways to explore MELV:**

1. **📊 [Interactive Visual Simulator](https://naturesholismmelv.github.io/harmony/)** — Watch cooperation emerge in real-time. Adjust parameters with sliders and observe chaos → cooperation evolution.
2. **🎓 [Calculation Tutorials](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)** — Learn the mathematics with guided notebooks (click the Binder badge above).

```python
import melv

# Calculate i-factor from overlap and differentiation
result = melv.calculate_i_factor(overlap=0.3, differentiation=0.85)

print(f"i-factor: {result['i_factor']:.2f}")
print(f"Regime: {result['regime']}")
# Output:
# i-factor: 0.35
# Regime: Cooperative
```

---

## Interactive Tools

### Visual Simulator

The [MELV Mathematical Evolution Simulator](https://naturesholismmelv.github.io/harmony/) allows you to:

- 🎲 Watch **chaos → cooperation** evolution live
- 🎛️ Adjust interaction parameters with sliders
- 📊 See population dynamics in real-time graphs
- 🧪 Explore modes: Mutualism, Cooperation, War, AI
- 🔬 Experiment with Lotka–Volterra equations interactively

### Calculation Tutorials

Tutorial 1 (20 minutes) covers:
- Cleaner fish mutualism (i = 0.24)
- Social media platforms (i = 1.60)
- Critical threshold at i ≈ 1.0
- Uncertainty quantification
- Hands-on exploration

[Run in Binder](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)

---

## Core Features

### i-Factor Calculations

```python
# Direct calculation
result = melv.calculate_i_factor(
    overlap=0.3,
    differentiation=0.85
)

# With uncertainty quantification
result = melv.calculate_i_factor(
    overlap=0.3,
    differentiation=0.85,
    uncertainty=0.05,
    bootstrap_n=1000
)
ci_lower, ci_upper = result['confidence_interval']
print(f"95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")
```

### β-Factor (Compatibility)

```python
result = melv.calculate_beta(
    physical=0.85,
    service=0.90,
    temporal=0.75,
    perpetuity=0.88
)

print(f"β = {result['beta']:.2f}")
print(f"Cooperation potential (φ × β) = {result['cooperation_potential']:.2f}")
```

### Combined Analysis

```python
result = melv.combined_analysis(
    i_factor=0.35,
    beta=0.83,
    perpetuity=0.88
)

print(result['prediction'])    # "Stable cooperation"
print(result['confidence'])    # "High"
```

### Example Results

**Cooperation: Cleaner Fish & Client Fish**
```python
result = melv.calculate_i_factor(overlap=0.2, differentiation=0.85)
# i = 0.24 → Cooperative
```
Very low resource overlap combined with high service differentiation (parasite removal) creates strong cooperation. This well-documented mutualism (*Labroides dimidiatus*) demonstrates MELV predictions in action.

**Competition: Social Media Platforms**
```python
result = melv.calculate_i_factor(overlap=0.8, differentiation=0.5)
# i = 1.60 → Competitive
```
High overlap (same users, attention, advertisers) with moderate differentiation creates competitive dynamics and polarisation.

---

## Scientific Validation

MELVcore has undergone multi-method validation across analytical, computational, and empirical domains. Five independent verification approaches in 2025 confirmed the predictive power of the i-factor and the stability of the cooperation threshold.

| Method | Result |
|---|---|
| Agent-based modeling | r = −0.944, p < 10⁻⁶, n = 500 runs |
| Bifurcation analysis | i = 0.9995 ± 0.029, R² = 0.9248, p < 10⁻³⁰⁰ |
| Replicator dynamics | Analytical proof of cooperation emergence below threshold |
| Jacobian stability analysis | Equilibrium stability confirmed in cooperative regimes |
| Service network integration | Ecosystem service coupling and compatibility dynamics validated |

Full validation dataset: [Zenodo DOI: 10.5281/zenodo.19029077](https://doi.org/10.5281/zenodo.19029077)

---

## Applications Across Domains

MELVcore applies to any system where entities interact, share resources, or differentiate services.

**Ecology** — Mutualism, symbiosis, predator–prey transitions, ecosystem service networks.

**Economics** — Market cooperation, sustainable business models, competitive equilibria.

**Organisations** — Team dynamics, inter-departmental collaboration, conflict resolution.

**Social Systems** — Community formation, polarisation analysis, governance structures.

**AI Governance** — Multi-agent alignment, cooperation certification, thermodynamic governance kernels.

---

## Repository Structure

```
melv-core/
├── src/melv/              # Core library
│   └── core/
│       ├── interaction.py    # i-factor calculations
│       └── compatibility.py  # β-factor calculations
├── harmony/               # Interactive simulator (GitHub Pages)
├── tutorials/             # Interactive Jupyter notebooks
├── test_calculator.py     # Test suite
├── README.md              # This file
├── LICENSE                # MIT License
└── setup.py               # Package configuration
```

### Installation

```bash
# Clone and install
git clone https://github.com/NaturesHolismMELV/melv-core.git
cd melv-core
pip install -e .

# Or just the package
pip install git+https://github.com/NaturesHolismMELV/melv-core.git
```

### Tests

```bash
python test_calculator.py
```

All tests should pass:
- ✓ Cleaner fish mutualism (i = 0.24)
- ✓ Social media (i = 1.60)
- ✓ Critical threshold boundary
- ✓ Uncertainty quantification
- ✓ Beta calculations
- ✓ Combined analysis

---

## For Researchers

### Reproducibility
- Full validation dataset on Zenodo (DOI: 10.5281/zenodo.19029077)
- Deterministic calculation functions with transparent parameter definitions
- Open-source test suite with full coverage of core calculations
- Compatible with agent-based modeling frameworks

### Research Integrations
- Supports uncertainty quantification and bootstrapping
- Designed for multi-agent AI governance research
- API compatible with ecological, economic, and social simulation frameworks

### Stability Guarantees
- Core mathematical definitions are stable and versioned
- API changes follow semantic versioning
- Validation suite ensures backward compatibility

### Related Repository: AIOS (MELVcore Governance Platform)

**[NaturesHolismMELV/AIOS](https://github.com/NaturesHolismMELV/AIOS)** is the applied implementation of the MELV framework as a thermodynamic governance kernel for multi-agent AI systems. Where melv-core provides the calculation library, AIOS provides:

- A FastAPI governance platform (416 passing tests)
- Real-time φ/ε assessment for AI agent cooperation
- Domain-specific certification environments (financial, healthcare, autonomous research)
- CLS (Cooperation Level Score) certification with PDF reporting
- MELVcore Claude Code skill for AI-assisted governance

AIOS demonstrates MELV theory in practice: governing AI agent ecosystems using the same thermodynamic principles that govern biological ones.

### Preprint & Academic Outreach
- Preprint available on Zenodo: [DOI: 10.5281/zenodo.19029077](https://doi.org/10.5281/zenodo.19029077)
- arXiv submission in preparation
- ORCID: [0009-0001-0963-1840](https://orcid.org/0009-0001-0963-1840)

---

## Background & Origin Story

MELVcore originates from ecological fieldwork in Namibia (1981–1983), during compulsory military service as a cavalry veterinary assistant. In the bird-rich landscapes of the Namibian savanna, the observation of hornbill–mongoose mutualism — hornbills acting as aerial sentinels, mongooses flushing insects from the soil — revealed cooperation patterns that classical competition theory could not explain.

The foundational insight: cooperation is not altruism. It is energetic efficiency. The cooperation basin is a thermodynamic attractor — complex systems move toward it when interaction costs are allowed to fall below the critical threshold.

The framework was first published in conceptual form in *Nature's Holism* (iUniverse, 1999). Mathematical formalization was completed through human–AI collaboration in 2024–2025, with five independent computational validation streams, and published in *Blueprint for Harmony* (Cooperation Press, 2026).

The framework integrates 44 years of ecological observation, classical Lotka–Volterra theory, and modern complexity science. Its central claim is simple and empirically supported:

> **Cooperation is not altruism. It is physics.**

---

## Citation

```
Evans, L.W. (2026). Blueprint for Harmony: Thermodynamic Foundations of
  Cooperation and Conscious Evolution. Cooperation Press, Cape Town.
  ISBN 978-969-8992-10-1.
  https://www.amazon.com/dp/B0GNLBVHWS

Evans, L.W. (2026). MELVcore: Thermodynamic Governance Kernel for
  Multi-Agent AI Systems [Software]. Zenodo.
  https://doi.org/10.5281/zenodo.19029077
```

---

## License & Contact

**License**: MIT — see LICENSE file for details.

| | |
|---|---|
| **Author** | Laurence W. Evans (Zaid) |
| **Organisation** | Ecotao Enterprises CC, Cape Town, South Africa |
| **Email** | [laurence@ecotao.co.za](mailto:laurence@ecotao.co.za) |
| **Website** | [ecotao.com](https://www.ecotao.com) |
| **Book** | [Blueprint for Harmony](https://www.amazon.com/Blueprint-Harmony-Thermodynamic-Foundations-Cooperation-ebook/dp/B0GNLBVHWS) (2026) |
| **Substack** | [The Thermodynamics of Life](https://naturesholism.substack.com) |
| **X / Twitter** | [@NaturesHolism](https://x.com/NaturesHolism) |
| **ORCID** | [0009-0001-0963-1840](https://orcid.org/0009-0001-0963-1840) |

---

*From observation → theory → validation → implementation → global access*

*Cooperation is not altruism. It is thermodynamics.*
