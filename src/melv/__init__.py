"""
MELV-Core: Mathematical Ecology of Cooperation

Open-source tools for calculating cooperation dynamics using the Modified Energetic
Lotka-Volterra (MELV) framework.

Based on 44 years of research and validated through October 2025 agent-based modeling
showing r = -0.944 correlation between i-factor and cooperation emergence.

Quick Start:
    >>> import melv
    >>> result = melv.calculate_i_factor(overlap=0.3, differentiation=0.85)
    >>> print(f"i = {result['i_factor']:.2f}, regime: {result['regime']}")
    i = 0.35, regime: Cooperative

Author: Zaid Osman (Ecotao Enterprises)
License: MIT
Version: 0.1.0
Repository: https://github.com/YOUR-USERNAME/melv-core
"""

__version__ = "0.1.0"
__author__ = "Zaid Osman"
__license__ = "MIT"

# Import main functions for convenient access
from .core.interaction import (
    calculate_i_factor,
    analyze_interaction,
    compare_multiple_interactions,
    InteractionResult
)

from .core.compatibility import (
    calculate_beta,
    combined_analysis,
    CompatibilityResult
)

__all__ = [
    'calculate_i_factor',
    'analyze_interaction',
    'compare_multiple_interactions',
    'InteractionResult',
    'calculate_beta',
    'combined_analysis',
    'CompatibilityResult',
    '__version__',
]
