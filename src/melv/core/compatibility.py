"""
MELV-Core: Compatibility Factor (β-factor) Calculations

This module implements compatibility calculations for the MELV framework.
While the i-factor determines IF cooperation emerges, the β-factor determines
HOW WELL cooperation functions when it does emerge.

β combines multiple dimensions:
- Physical compatibility (can entities physically interact?)
- Service exchange quality (how well do services match needs?)
- Temporal coordination (do timing patterns align?)
- Perpetuity factor (φ) (how sustainable is the relationship?)

The cooperation potential is: φ × β (perpetuity × compatibility)

Author: Zaid Osman (Ecotao Enterprises)
License: MIT
Version: 0.1.0
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, Optional, Tuple


@dataclass
class CompatibilityResult:
    """
    Results from β-factor calculation.
    
    Attributes:
        beta: Overall compatibility coefficient (0-1)
        physical: Physical compatibility (0-1)
        service: Service exchange quality (0-1)
        temporal: Temporal coordination (0-1)
        perpetuity: Sustainability factor φ (0-1)
        cooperation_potential: φ × β
        interpretation: Human-readable explanation
    """
    beta: float
    physical: float
    service: float
    temporal: float
    perpetuity: Optional[float] = None
    cooperation_potential: Optional[float] = None
    interpretation: str = ""


def calculate_beta(
    physical: float,
    service: float,
    temporal: float,
    perpetuity: Optional[float] = None,
    weights: Optional[Tuple[float, float, float]] = None
) -> Dict:
    """
    Calculate the β-factor (compatibility coefficient).
    
    β quantifies how well entities can cooperate when i < 1.0.
    It combines multiple compatibility dimensions.
    
    Parameters:
        physical: Physical compatibility (0-1)
            Can entities physically interact? Spatial proximity, size matching, etc.
        service: Service exchange quality (0-1)
            How well do provided services match needs?
        temporal: Temporal coordination (0-1)
            Do activity patterns, lifecycles, timescales align?
        perpetuity: Sustainability factor φ (0-1), optional
            How stable/sustainable is the relationship over time?
        weights: Optional (w_physical, w_service, w_temporal) weights
            Default: (0.33, 0.33, 0.34) for equal weighting
    
    Returns:
        Dictionary containing:
            - beta: Overall compatibility (weighted average)
            - physical: Physical compatibility
            - service: Service quality
            - temporal: Temporal coordination
            - perpetuity: φ factor if provided
            - cooperation_potential: φ × β if perpetuity provided
            - interpretation: Human-readable explanation
    
    Examples:
        >>> result = calculate_beta(
        ...     physical=0.85,
        ...     service=0.90,
        ...     temporal=0.75,
        ...     perpetuity=0.88
        ... )
        >>> print(f"β = {result['beta']:.2f}")
        β = 0.83
        >>> print(f"Cooperation potential = {result['cooperation_potential']:.2f}")
        Cooperation potential = 0.73
    """
    
    # Validate inputs
    for name, value in [('physical', physical), ('service', service), ('temporal', temporal)]:
        if not (0 <= value <= 1):
            raise ValueError(f"{name} must be in [0, 1], got {value}")
    
    if perpetuity is not None and not (0 <= perpetuity <= 1):
        raise ValueError(f"perpetuity must be in [0, 1], got {perpetuity}")
    
    # Default weights: equal importance
    if weights is None:
        weights = (0.33, 0.33, 0.34)
    
    # Validate weights
    if len(weights) != 3:
        raise ValueError(f"weights must have 3 values, got {len(weights)}")
    if not np.isclose(sum(weights), 1.0, atol=0.01):
        raise ValueError(f"weights must sum to 1.0, got {sum(weights)}")
    
    # Calculate β as weighted average
    beta = float(
        weights[0] * physical +
        weights[1] * service +
        weights[2] * temporal
    )
    
    # Calculate cooperation potential if perpetuity provided
    cooperation_potential = None
    if perpetuity is not None:
        cooperation_potential = perpetuity * beta
    
    # Generate interpretation
    interpretation = _generate_beta_interpretation(
        beta, physical, service, temporal, perpetuity, cooperation_potential
    )
    
    return {
        'beta': beta,
        'physical': physical,
        'service': service,
        'temporal': temporal,
        'perpetuity': perpetuity,
        'cooperation_potential': cooperation_potential,
        'interpretation': interpretation
    }


def _generate_beta_interpretation(
    beta: float,
    physical: float,
    service: float,
    temporal: float,
    perpetuity: Optional[float],
    coop_potential: Optional[float]
) -> str:
    """Generate human-readable interpretation of β results."""
    
    interpretation = f"β (compatibility) = {beta:.2f}\n\n"
    
    # Overall compatibility assessment
    if beta > 0.8:
        interpretation += "EXCELLENT compatibility: "
    elif beta > 0.6:
        interpretation += "GOOD compatibility: "
    elif beta > 0.4:
        interpretation += "MODERATE compatibility: "
    else:
        interpretation += "LIMITED compatibility: "
    
    # Dimension breakdown
    interpretation += f"\n\nDimension analysis:\n"
    interpretation += f"• Physical: {physical:.2f} - "
    if physical > 0.8:
        interpretation += "Strong physical compatibility\n"
    elif physical > 0.6:
        interpretation += "Good physical match\n"
    else:
        interpretation += "Physical constraints present\n"
    
    interpretation += f"• Service: {service:.2f} - "
    if service > 0.8:
        interpretation += "Excellent service-need matching\n"
    elif service > 0.6:
        interpretation += "Services align reasonably well\n"
    else:
        interpretation += "Service-need mismatch detected\n"
    
    interpretation += f"• Temporal: {temporal:.2f} - "
    if temporal > 0.8:
        interpretation += "Strong temporal synchronization\n"
    elif temporal > 0.6:
        interpretation += "Adequate timing coordination\n"
    else:
        interpretation += "Temporal coordination challenges\n"
    
    # Perpetuity and cooperation potential
    if perpetuity is not None:
        interpretation += f"\nPerpetuit factor (φ) = {perpetuity:.2f} - "
        if perpetuity > 0.8:
            interpretation += "Highly sustainable relationship\n"
        elif perpetuity > 0.6:
            interpretation += "Reasonably sustainable\n"
        else:
            interpretation += "Sustainability concerns\n"
        
        if coop_potential is not None:
            interpretation += f"\nCooperation potential (φ × β) = {coop_potential:.2f}\n"
            if coop_potential > 0.7:
                interpretation += "Strong potential for lasting cooperation"
            elif coop_potential > 0.5:
                interpretation += "Moderate cooperation potential"
            else:
                interpretation += "Limited cooperation potential"
    
    return interpretation


def combined_analysis(
    i_factor: float,
    beta: float,
    perpetuity: Optional[float] = None,
    overlap: Optional[float] = None,
    differentiation: Optional[float] = None
) -> Dict:
    """
    Perform combined MELV analysis with both i-factor and β-factor.
    
    This provides a complete picture:
    - i-factor determines IF cooperation emerges
    - β-factor determines HOW WELL cooperation functions
    - φ × β determines sustainability of cooperation
    
    Parameters:
        i_factor: Interaction efficiency factor
        beta: Compatibility coefficient
        perpetuity: Sustainability factor (optional)
        overlap: Resource overlap (optional, for interpretation)
        differentiation: Service differentiation (optional, for interpretation)
    
    Returns:
        Dictionary containing:
            - i_factor: Interaction efficiency
            - beta: Compatibility
            - perpetuity: Sustainability (if provided)
            - cooperation_potential: φ × β (if perpetuity provided)
            - prediction: Overall regime prediction
            - confidence: Confidence level in prediction
            - interpretation: Detailed analysis
    
    Examples:
        >>> result = combined_analysis(
        ...     i_factor=0.35,
        ...     beta=0.83,
        ...     perpetuity=0.88
        ... )
        >>> print(result['prediction'])
        Stable cooperation
        >>> print(result['confidence'])
        High
    """
    
    # Determine regime from i-factor
    if i_factor < 1.0:
        regime = "Cooperative"
    elif abs(i_factor - 1.0) < 0.05:
        regime = "Critical"
    else:
        regime = "Competitive"
    
    # Calculate cooperation potential
    cooperation_potential = None
    if perpetuity is not None:
        cooperation_potential = perpetuity * beta
    
    # Make prediction
    prediction, confidence = _make_prediction(
        i_factor, beta, perpetuity, cooperation_potential
    )
    
    # Generate comprehensive interpretation
    interpretation = _generate_combined_interpretation(
        i_factor, beta, perpetuity, cooperation_potential,
        regime, prediction, confidence,
        overlap, differentiation
    )
    
    return {
        'i_factor': i_factor,
        'beta': beta,
        'perpetuity': perpetuity,
        'cooperation_potential': cooperation_potential,
        'prediction': prediction,
        'confidence': confidence,
        'interpretation': interpretation
    }


def _make_prediction(
    i_factor: float,
    beta: float,
    perpetuity: Optional[float],
    coop_potential: Optional[float]
) -> Tuple[str, str]:
    """Generate prediction and confidence level."""
    
    # Case 1: Strong cooperation conditions
    if i_factor < 0.7 and beta > 0.7:
        if coop_potential is not None and coop_potential > 0.6:
            return "Stable cooperation", "High"
        elif beta > 0.8:
            return "Stable cooperation", "Moderate"
        else:
            return "Cooperation likely", "Moderate"
    
    # Case 2: Moderate cooperation conditions
    elif i_factor < 1.0 and beta > 0.5:
        if coop_potential is not None and coop_potential > 0.5:
            return "Cooperation with fluctuations", "Moderate"
        else:
            return "Cooperation possible", "Low to Moderate"
    
    # Case 3: Critical threshold
    elif abs(i_factor - 1.0) < 0.1:
        return "Unstable regime (near critical point)", "Low"
    
    # Case 4: Competition
    elif i_factor > 1.0:
        if i_factor < 1.3:
            return "Mild competition", "Moderate"
        else:
            return "Strong competition", "High"
    
    # Case 5: Cooperation with poor compatibility
    else:  # i < 1 but β low
        return "Cooperation possible but inefficient", "Low"


def _generate_combined_interpretation(
    i_factor: float,
    beta: float,
    perpetuity: Optional[float],
    coop_potential: Optional[float],
    regime: str,
    prediction: str,
    confidence: str,
    overlap: Optional[float],
    differentiation: Optional[float]
) -> str:
    """Generate comprehensive interpretation of combined analysis."""
    
    interpretation = "=== COMBINED MELV ANALYSIS ===\n\n"
    
    # i-factor analysis
    interpretation += f"i-factor = {i_factor:.2f} → {regime} regime\n"
    if overlap is not None and differentiation is not None:
        interpretation += f"  (overlap: {overlap:.2f}, differentiation: {differentiation:.2f})\n"
    
    if i_factor < 1.0:
        interpretation += "  ✓ Interaction costs below critical threshold\n"
        interpretation += "  ✓ Cooperation is energetically favorable\n"
    else:
        interpretation += "  ✗ Interaction costs exceed benefits\n"
        interpretation += "  ✗ Competition is energetically favorable\n"
    
    # β-factor analysis
    interpretation += f"\nβ (compatibility) = {beta:.2f}\n"
    if beta > 0.7:
        interpretation += "  ✓ High compatibility for cooperation\n"
    elif beta > 0.5:
        interpretation += "  ~ Moderate compatibility\n"
    else:
        interpretation += "  ✗ Limited compatibility\n"
    
    # Perpetuity and cooperation potential
    if perpetuity is not None:
        interpretation += f"\nφ (perpetuity) = {perpetuity:.2f}\n"
        if coop_potential is not None:
            interpretation += f"Cooperation potential (φ × β) = {coop_potential:.2f}\n"
    
    # Prediction
    interpretation += f"\n=== PREDICTION ===\n"
    interpretation += f"{prediction}\n"
    interpretation += f"Confidence: {confidence}\n\n"
    
    # Explanation
    if i_factor < 1.0 and beta > 0.6:
        interpretation += (
            "Both conditions favor cooperation: low interaction costs (i < 1) "
            "and good compatibility (β > 0.6). Expect cooperative dynamics.\n"
        )
    elif i_factor < 1.0 and beta < 0.6:
        interpretation += (
            "Low interaction costs favor cooperation, but poor compatibility "
            "limits effectiveness. Cooperation may emerge but be inefficient.\n"
        )
    elif i_factor > 1.0:
        interpretation += (
            "High interaction costs (i > 1) create competitive pressure. "
            "Even with good compatibility, cooperation is unlikely to emerge.\n"
        )
    else:
        interpretation += (
            "System near critical threshold. Outcomes highly sensitive to "
            "small parameter changes. Monitor closely for regime shifts.\n"
        )
    
    return interpretation
