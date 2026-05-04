# MELV-Core: Mathematical Ecology of Cooperation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)

**Open-source tools for exploring cooperation dynamics — simplified teaching implementation**

> **Note on versions:** This repository implements a pedagogical simplification of the MELV framework using the ratio formulation `i = ρ/δ` (resource overlap / service differentiation). This version emerged from early spreadsheet modelling (2024–2025) and is retained as an accessible educational entry point. It is conceptually valid but does not implement the full 2026 master equation. For the complete mathematical treatment — including temporal dynamics (φ, β, ε) and the near-unity bifurcation — see [AIOS/MELVcore](https://github.com/NaturesHolismMELV/AIOS) and Evans (2026).

This simplified implementation demonstrates when cooperation vs. competition tends to emerge, based on the Modified Energetic Lotka-Volterra (MELV) framework developed over 44 years of research (Evans, 1999; Evans, 2026).

---

## 🚀 Try It Now (Zero Installation)

**Two ways to explore MELV:**

1. **📊 [Interactive Visual Simulator](https://naturesholismmelv.github.io/harmony/)** — Watch cooperation emerge in real-time. Adjust parameters with sliders and see the competition-to-cooperation transition.
2. **🎓 [Tutorial Notebooks](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)** — Learn the mathematics with guided notebooks (click Binder badge above).

---

## Quick Start

```python
import melv

# Calculate i-factor from overlap and differentiation (v1 simplified model)
result = melv.calculate_i_factor(overlap=0.3, differentiation=0.85)

print(f"i-factor: {result['i_factor']:.2f}")
print(f"Regime: {result['regime']}")
# Output:
# i-factor: 0.35
# Regime: Cooperative
```

In this simplified formulation, the **i-factor** (i = ρ/δ) indicates whether cooperation or competition tends to emerge:

- **i < 1.0**: Cooperation regime (differentiation exceeds overlap)
- **i > 1.0**: Competition regime (overlap exceeds differentiation)
- **i ≈ 1.0**: Bifurcation point (system sensitive to small changes)

---

## What is MELV?

The Modified Energetic Lotka-Volterra (MELV) framework mathematically quantifies when cooperation emerges between entities — species, organisations, individuals, or systems.

**The full master equation (Evans, 2026):**

```
i₁₂(t) = i₁₂⁰ × (1 − ε × φ(t) × β(t))
```

Where:
- **φ(t)** — perpetuity: long-run persistence capacity of the interaction
- **β(t)** — compatibility: niche overlap or biochemical affinity
- **ε** — adaptation acceleration: rate of response to interaction mismatches

The master equation is dimensionless, functioning analogously to a refractive index — a pure ratio calibrated prior to domain-specific application. Full cooperative convergence (Cooperation Index CI → 1.0) occurs as i approaches its theoretical maximum near unity, confirmed across 405 agent-based simulation runs (Evans, 2026, DOI: 10.5281/zenodo.19422174).

**This repository** implements the earlier ratio simplification `i = ρ/δ` as an accessible teaching tool. The bifurcation at i = 1.0 in this version is conceptually related to, but mechanistically distinct from, the near-unity bifurcation in the full master equation.

---

## Core Features

### i-Factor Calculations (v1 simplified)

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
    bootstrap_n=1000,
    random_state=42
)
ci_lower, ci_upper = result['confidence_interval']
print(f"95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")
```

### β-Factor (Compatibility)

```python
result = melv.calculate_beta(
    physical=0.85,      # Physical compatibility
    service=0.90,       # Service-need matching
    temporal=0.75,      # Temporal coordination
    perpetuity=0.88     # Sustainability (φ)
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

---

## Installation

### Option 1: Binder (Recommended for First Try)

Click the Binder badge above — runs in your browser with zero installation.

### Option 2: Local Installation

```bash
git clone https://github.com/NaturesHolismMELV/melv-core.git
cd melv-core
pip install -e .
# Or with tutorial dependencies:
pip install -e ".[tutorials]"
```

### Option 3: Just the Package

```bash
pip install git+https://github.com/NaturesHolismMELV/melv-core.git
```

---

## Tutorials

### Tutorial 1: Your First i-Factor Calculation (20 minutes)

Interactive introduction covering:

- Cleaner wrasse mutualism (*Labroides dimidiatus*) — i = 0.24
- Social media platforms — i = 1.60
- Critical threshold at i ≈ 1.0
- Uncertainty quantification with bootstrap confidence intervals
- Hands-on regime scanning

[▶ Run in Binder](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)

---

## Example Results

### Cooperation: Cleaner Wrasse & Client Fish

```python
result = melv.calculate_i_factor(overlap=0.2, differentiation=0.85)
# i = 0.24 → Cooperative
```

Very low resource overlap (cleaners eat parasites; clients eat plankton, algae, small fish) combined with high service differentiation (parasite removal provides critical health benefit; clients provide food source and cleaning station access) gives i well below the threshold. This well-documented mutualism (*Labroides dimidiatus*) is a robust test case for the simplified model.

### Competition: Social Media Platforms

```python
result = melv.calculate_i_factor(overlap=0.8, differentiation=0.5)
# i = 1.60 → Competitive
```

High overlap (same users, advertisers, attention economy) with moderate differentiation creates competitive dynamics consistent with observed platform behaviour.

---

## Validation

This simplified (v1) implementation was validated through early agent-based modelling (2024–2025). The full 2026 validation — 405 simulation runs, Hartigan dip test p ≈ 0 confirming bimodal outcome distribution, Cooperation Index CI reaching 1.0 at i ≥ 0.9995 ± 0.029, ESS invasion recovery 34/34 (100%) — applies to the master equation model and is reported in:

> Evans, L.W. (2026). MELV ABM V2.1. Zenodo. DOI: [10.5281/zenodo.19422174](https://doi.org/10.5281/zenodo.19422174)

---

## Repository Structure

```
melv-core/
├── src/melv/              # Core library (v1 simplified model)
│   └── core/
│       ├── interaction.py    # i-factor calculations (ρ/δ formulation)
│       └── compatibility.py  # β-factor calculations
├── tutorials/             # Interactive notebooks
│   └── 01_first_calculation.ipynb
├── test_calculator.py     # Test suite
├── README.md
├── LICENSE                # MIT License
└── setup.py
```

---

## Running Tests

```bash
python test_calculator.py
```

Six tests cover the core v1 functionality:

- ✓ Cleaner wrasse mutualism (i = 0.24)
- ✓ Social media competition (i = 1.60)
- ✓ Critical threshold boundary
- ✓ Uncertainty quantification
- ✓ Beta calculations
- ✓ Combined analysis

---

## Background: The 44-Year Journey

The MELV framework originates from field observations in Namibia (1981–1983), where hornbill-mongoose mutualism demonstrated cooperation patterns that defied classical competition theory. Bee-flower energetic associations provided a second empirical anchor. After 44 years of development and mathematical formalisation, the framework was published in:

- Evans, L.W. (1999). *Nature's Holism*. iUniverse.
- Evans, L.W. (2026). *Blueprint for Harmony*. Cooperation Press. ISBN 978-969-8992-10-1.

**The core insight: cooperation is not altruism — it is energetic efficiency.**

---

## Citation

If you use this software in your research, please cite:

```
Evans, L.W. (2026). Blueprint for Harmony: A Mathematical Framework for
  Cooperative Systems. Cooperation Press. ISBN 978-969-8992-10-1.
  MELV-Core software: https://github.com/NaturesHolismMELV/melv-core
  ORCID: 0009-0001-0963-1840
```

---

## License

MIT License — see LICENSE file for details.

## Contact

- **Author**: Laurence W. Evans (Zaid)
- **ORCID**: [0009-0001-0963-1840](https://orcid.org/0009-0001-0963-1840)
- **Substack**: [naturesholism.substack.com](https://naturesholism.substack.com)
- **X**: [@NaturesHolism](https://x.com/NaturesHolism)

---

*From observation → theory → validation → implementation → global access*

*The mathematics of cooperation, open to all.* 🌸🐝
