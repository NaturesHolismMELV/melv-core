# MELV Mathematical Evolution Simulator

**Interactive visual exploration of cooperation dynamics**

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge)](https://naturesholismmelv.github.io/harmony/)

## 🎮 Try It Now

**[Launch Simulator](https://naturesholismmelv.github.io/harmony/)** - No installation required!

## What Is This?

An interactive web-based simulator that brings the Modified Energetic Lotka-Volterra (MELV) framework to life. Watch cooperation emerge from chaos in real-time!

### Features

🎲 **5 Simulation Modes:**
- 💚 **Mutualism** - Both species benefit (i₁₂ < 0, i₂₁ < 0)
- 🤝 **Cooperation** - Low competition, stable coexistence
- ⚡ **Chaos** - Random parameters, explore unpredictably
- ⚔️ **War** - High competition, one dominates
- 🧠 **AI** - Predictive mode showing likely outcomes

🎛️ **Interactive Controls:**
- Adjust interaction parameters with sliders
- Real-time population graphs
- Chaos level indicator
- Play/pause, reset, speed controls
- Lock parameters during simulation

📊 **Live Visualization:**
- Population dynamics over time
- Cooperation vs competition levels
- System stability indicators
- Mathematical equations displayed

## How It Works

Based on Lotka-Volterra competition equations:

```
dx₁/dt = r₁x₁(1-(x₁+i₁₂x₂)/K₁)
dx₂/dt = r₂x₂(1-(x₂+i₂₁x₁)/K₂)
```

Where:
- **r₁, r₂** = Growth rates
- **K₁, K₂** = Carrying capacities  
- **i₁₂, i₂₁** = Interaction coefficients (the MELV i-factors!)
- **x₁, x₂** = Population sizes

**Key Insight:** When i₁₂ × i₂₁ < 1, cooperation emerges. When > 1, competition dominates.

## Learn More

This simulator complements the rigorous mathematical framework:

📚 **[MELV-Core](https://github.com/NaturesHolismMELV/melv-core)** - Calculate i-factors precisely, with tutorials and scientific validation

🎓 **[Interactive Tutorials](https://mybinder.org/v2/gh/NaturesHolismMELV/melv-core/main?filepath=tutorials%2F01_first_calculation.ipynb)** - Learn the mathematics step-by-step

## Perfect For

- **Visual learners** exploring cooperation vs competition
- **Teaching** MELV concepts interactively
- **Demonstrations** to audiences
- **Quick experimentation** before detailed calculations
- **Building intuition** about parameter effects

## Technical Details

- Pure JavaScript (no backend required)
- Chart.js for visualization
- Tailwind CSS for responsive design
- Mobile-friendly
- GitHub Pages hosted (free!)

## The MELV Framework

Based on 44 years of research by Laurence Evans, the Modified Energetic Lotka-Volterra (MELV) framework mathematically explains when cooperation vs competition emerges.

**Key finding:** Cooperation is not altruism—it's energetic efficiency. When interaction costs (i-factors) fall below critical thresholds, cooperation becomes the optimal strategy.

**Validated:** October 2025 agent-based modeling showed r = -0.944 correlation between i-factor and cooperation emergence.

## Related Work

- **Book:** "Blueprint for Harmony: Why Cooperation Is Nature's Law" (Evans, L., 2026)
- **Code:** [MELV-Core on GitHub](https://github.com/NaturesHolismMELV/melv-core)
- **Citation:** Evans, L. (2026). Blueprint for Harmony. Includes MELV tools.

## Usage

Simply open the [live simulator](https://naturesholismmelv.github.io/harmony/) and:

1. **Choose a mode** (Chaos is great for exploration!)
2. **Press START** to begin simulation
3. **Watch** cooperation or competition emerge
4. **Adjust sliders** to see how parameters affect outcomes
5. **Experiment** with different scenarios

No installation, no accounts, no cost. Just explore!

## License

© 2025 Laurence Evans - Nature's Holism 2025

## Author

**Laurence Evans**
- Organization: Ecotao Enterprises / Nature's Holism
- Book: "Blueprint for Harmony" (February 2026)
- GitHub: [@NaturesHolismMELV](https://github.com/NaturesHolismMELV)

---

**From chaos to cooperation in real-time. That's consciousness acceleration.** 🌸🐝
