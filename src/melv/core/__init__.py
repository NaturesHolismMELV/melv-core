"""
MELV-Core: Core calculation modules

This package contains the core MELV calculations:
- interaction.py: i-factor calculations
- compatibility.py: β-factor calculations
"""

from .interaction import (
    calculate_i_factor,
    analyze_interaction,
    compare_multiple_interactions,
    InteractionResult
)

from .compatibility import (
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
]
