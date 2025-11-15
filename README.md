# MELV-Core: Mathematical Ecology of Cooperation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)

**Open-source tools for calculating cooperation dynamics**

Calculate when cooperation vs. competition emerges using the Modified Energetic Lotka-Volterra (MELV) framework. Based on 44 years of research and validated through October 2025 agent-based modeling showing **r = -0.944** correlation between i-factor and cooperation emergence.

## 🚀 Try It Now (Zero Installation)

**Two ways to explore MELV:**

1. **📊 [Interactive Visual Simulator](https://naturesholismmelv.github.io/harmony/)** - Watch cooperation emerge in real-time! Adjust parameters with sliders and see chaos → cooperation evolution.

2. **🎓 [Calculation Tutorials](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)** - Learn the mathematics with guided notebooks (click Binder badge above).

## Quick Start

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

The **i-factor** determines whether cooperation or competition emerges:
- **i < 1.0**: Cooperation regime (synergy through differentiation)
- **i > 1.0**: Competition regime (conflict through overlap)
- **i ≈ 1.0**: Critical threshold (bifurcation point)

## What is MELV?

The Modified Energetic Lotka-Volterra (MELV) framework mathematically quantifies when cooperation emerges between entities (species, organizations, individuals, systems). 

Key insight: **Cooperation emerges when interaction costs fall below a critical threshold**, determined by the balance between:
- **Resource overlap** (ρ): How much entities compete for the same resources
- **Service differentiation** (δ): How much entities provide unique, complementary benefits

The interaction factor **i = ρ/δ** creates a sharp bifurcation at i ≈ 1.0:
- Below threshold: Cooperation is energetically favorable
- Above threshold: Competition dominates

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

While i-factor determines IF cooperation emerges, β-factor determines HOW WELL:

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

## Installation

### Option 1: Binder (Recommended for First Try)
Click the Binder badge above—runs in your browser with zero installation!

### Option 2: Local Installation

```bash
# Clone repository
git clone https://github.com/NaturesHolismMELV/melv-core.git
cd melv-core

# Install package
pip install -e .

# Or install with tutorial dependencies
pip install -e ".[tutorials]"
```

### Option 3: Just the Package

```bash
pip install git+https://github.com/NaturesHolismMELV/melv-core.git
```

## Tutorials

### Tutorial 1: Your First i-Factor Calculation (20 minutes)
Interactive introduction covering:
- Cleaner fish mutualism (i = 0.24)
- Social media platforms (i = 1.60)
- Critical threshold at i ≈ 1.0
- Uncertainty quantification
- Hands-on exploration

[Run in Binder](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)

## Example Results

### Cooperation: Cleaner Fish & Client Fish
```python
result = melv.calculate_i_factor(overlap=0.2, differentiation=0.85)
# i = 0.24 → Cooperative
```

**Interpretation**: Very low resource overlap (completely different food sources - cleaners eat parasites, clients eat other prey) combined with high service differentiation (parasite removal provides life-or-death health benefits, clients provide cleaning station access) creates strong cooperation. This well-documented mutualism (*Labroides dimidiatus*) demonstrates MELV predictions in action.

### Competition: Social Media Platforms
```python
result = melv.calculate_i_factor(overlap=0.8, differentiation=0.5)
# i = 1.60 → Competitive
```

**Interpretation**: High overlap (same users, attention, advertisers) with moderate differentiation creates competitive dynamics and polarization.

## Validation

**October 2025 Agent-Based Modeling:**
- Correlation: r = -0.944 (p < 10⁻⁶)
- Critical threshold: i = 1.01 ± 0.03
- Sample size: n = 500 simulation runs
- Result: Strong validation of theoretical predictions

The framework successfully predicted cooperation emergence with exceptional statistical significance.

## Applications

- **Ecology**: Species interactions, ecosystem dynamics
- **Economics**: Market competition, cooperation strategies
- **Organizations**: Team dynamics, inter-departmental collaboration
- **Social Systems**: Community formation, polarization analysis
- **AI Governance**: Multi-agent systems, alignment strategies

## 🎮 Interactive Visual Simulator

**Want to see cooperation emerge in real-time?**

Try the [MELV Mathematical Evolution Simulator](https://naturesholismmelv.github.io/harmony/) - a companion web app where you can:

- 🎲 Watch **chaos → cooperation** evolution live
- 🎛️ Adjust interaction parameters with sliders
- 📊 See population dynamics in real-time graphs
- 🧪 Explore different modes: Mutualism, Cooperation, War, AI
- 🔬 Experiment with Lotka-Volterra equations interactively

**Perfect for:**
- Visual learners who want to see the math in action
- Teaching MELV concepts interactively
- Quick exploration before diving into calculations
- Demonstrating cooperation emergence to audiences

The simulator complements the tutorials here - use both for complete understanding!

## Background: The 44-Year Journey

This framework originated from ecological observations in Namibia (1981-1983), where hornbills and bee-eaters demonstrated cooperation patterns that defied traditional competition theory. After 44 years of development and mathematical formalization with AI assistance in 2024-2025, the theory now has working implementation and strong empirical validation.

**The mathematics show: Cooperation is not altruism—it's energetic efficiency.**

## Repository Structure

```
melv-core/
├── src/melv/              # Core library
│   └── core/
│       ├── interaction.py    # i-factor calculations
│       └── compatibility.py  # β-factor calculations
├── tutorials/             # Interactive notebooks
├── test_calculator.py     # Test suite (all passing)
├── README.md             # This file
├── LICENSE               # MIT License
└── setup.py              # Package configuration
```

## Development

### Running Tests

```bash
python test_calculator.py
```

All 6 tests should pass:
- ✓ Cleaner fish mutualism (i = 0.24)
- ✓ Social media (i = 1.60)
- ✓ Critical threshold boundary
- ✓ Uncertainty quantification
- ✓ Beta calculations
- ✓ Combined analysis

### Contributing

Contributions welcome! Areas of interest:
- Additional calculation methods
- New tutorials and examples
- Domain-specific modules
- Visualization tools
- Documentation improvements

Please see CONTRIBUTING.md (coming soon) for guidelines.

## Citation

If you use MELV-Core in your research, please cite:

```
Osman, Z. (2026). Blueprint for Harmony: Why Cooperation Is Nature's Law.
  Includes MELV-Core software: https://github.com/NaturesHolismMELV/melv-core
```

## License

MIT License - see LICENSE file for details.

## Contact

- **Author**: Zaid Osman
- **Organization**: Ecotao Enterprises
- **Email**: zaid@ecotao.com
- **Book**: "Blueprint for Harmony" (February 2026)

## Acknowledgments

This platform was built through human-AI collaboration, demonstrating the cooperative principles it calculates. The implementation process itself validated MELV theory: clear module separation (low i-factors) enabled efficient collaboration.

---

**From observation → theory → validation → implementation → global access**

**Calculate cooperation dynamics in 2 minutes. Deploy globally at zero cost.**

**That's consciousness acceleration.** 🌸🐝
