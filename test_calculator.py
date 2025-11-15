"""
Test suite for MELV-Core v0.1

Validates calculations against book examples and October 2025 validation results.

Run with: python test_calculator.py
"""

import sys
sys.path.insert(0, 'src')

import melv
import numpy as np


def test_hornbills_beeaters():
    """Test Chapter 4 example: Namibian hornbills and bee-eaters."""
    print("\n" + "="*60)
    print("TEST 1: Hornbills and Bee-Eaters (Chapter 4)")
    print("="*60)
    
    result = melv.calculate_i_factor(
        overlap=0.3,          # Low resource overlap
        differentiation=0.85   # High service differentiation
    )
    
    print(f"i-factor: {result['i_factor']:.2f}")
    print(f"Regime: {result['regime']}")
    print(f"Expected: i ≈ 0.35, Cooperative")
    
    assert 0.34 < result['i_factor'] < 0.36, f"Expected ~0.35, got {result['i_factor']}"
    assert result['regime'] == "Cooperative", f"Expected Cooperative, got {result['regime']}"
    
    print("✓ PASSED")
    return True


def test_social_media():
    """Test Chapter 14 example: Social media platforms."""
    print("\n" + "="*60)
    print("TEST 2: Social Media Platforms (Chapter 14)")
    print("="*60)
    
    result = melv.calculate_i_factor(
        overlap=0.8,           # High resource overlap (same users)
        differentiation=0.5    # Moderate differentiation
    )
    
    print(f"i-factor: {result['i_factor']:.2f}")
    print(f"Regime: {result['regime']}")
    print(f"Expected: i ≈ 1.60, Competitive")
    
    assert 1.55 < result['i_factor'] < 1.65, f"Expected ~1.60, got {result['i_factor']}"
    assert result['regime'] == "Competitive", f"Expected Competitive, got {result['regime']}"
    
    print("✓ PASSED")
    return True


def test_critical_threshold():
    """Test critical threshold at i ≈ 1.0."""
    print("\n" + "="*60)
    print("TEST 3: Critical Threshold (i ≈ 1.0)")
    print("="*60)
    
    # Just below threshold
    result_coop = melv.calculate_i_factor(
        overlap=0.45,
        differentiation=0.50
    )
    
    # Just above threshold
    result_comp = melv.calculate_i_factor(
        overlap=0.55,
        differentiation=0.50
    )
    
    print(f"Below threshold: i = {result_coop['i_factor']:.2f} → {result_coop['regime']}")
    print(f"Above threshold: i = {result_comp['i_factor']:.2f} → {result_comp['regime']}")
    
    assert result_coop['i_factor'] < 1.0, "Below threshold should be < 1.0"
    assert result_comp['i_factor'] > 1.0, "Above threshold should be > 1.0"
    assert result_coop['regime'] == "Cooperative", "Below threshold should be Cooperative"
    assert result_comp['regime'] == "Competitive", "Above threshold should be Competitive"
    
    print("✓ PASSED")
    return True


def test_uncertainty_quantification():
    """Test bootstrap confidence intervals."""
    print("\n" + "="*60)
    print("TEST 4: Uncertainty Quantification")
    print("="*60)
    
    result = melv.calculate_i_factor(
        overlap=0.3,
        differentiation=0.85,
        uncertainty=0.05,
        bootstrap_n=1000,
        random_state=42  # For reproducibility
    )
    
    ci_lower, ci_upper = result['confidence_interval']
    
    print(f"i-factor: {result['i_factor']:.2f}")
    print(f"95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")
    print(f"Expected: CI width ≈ 0.10-0.20")
    
    ci_width = ci_upper - ci_lower
    assert 0.05 < ci_width < 0.30, f"CI width seems wrong: {ci_width}"
    assert ci_lower < result['i_factor'] < ci_upper, "i-factor not in CI"
    
    print("✓ PASSED")
    return True


def test_beta_calculation():
    """Test β-factor (compatibility) calculation."""
    print("\n" + "="*60)
    print("TEST 5: Beta-factor Calculation")
    print("="*60)
    
    result = melv.calculate_beta(
        physical=0.85,
        service=0.90,
        temporal=0.75,
        perpetuity=0.88
    )
    
    print(f"β: {result['beta']:.2f}")
    print(f"Cooperation potential (φ × β): {result['cooperation_potential']:.2f}")
    print(f"Expected: β ≈ 0.83, φ × β ≈ 0.73")
    
    assert 0.80 < result['beta'] < 0.85, f"Expected ~0.83, got {result['beta']}"
    assert 0.70 < result['cooperation_potential'] < 0.76, \
        f"Expected ~0.73, got {result['cooperation_potential']}"
    
    print("✓ PASSED")
    return True


def test_combined_analysis():
    """Test full MELV analysis combining i-factor and β-factor."""
    print("\n" + "="*60)
    print("TEST 6: Combined Analysis")
    print("="*60)
    
    result = melv.combined_analysis(
        i_factor=0.35,
        beta=0.83,
        perpetuity=0.88
    )
    
    print(f"Prediction: {result['prediction']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Expected: Stable cooperation with High/Moderate confidence")
    
    assert "cooperation" in result['prediction'].lower(), \
        f"Expected cooperation prediction, got {result['prediction']}"
    assert result['confidence'] in ['High', 'Moderate'], \
        f"Expected High or Moderate confidence, got {result['confidence']}"
    
    print("✓ PASSED")
    return True


def run_all_tests():
    """Run complete test suite."""
    print("\n" + "="*70)
    print(" MELV-CORE V0.1 TEST SUITE ".center(70, "="))
    print("="*70)
    print("\nValidating against book examples and October 2025 results...")
    
    tests = [
        test_hornbills_beeaters,
        test_social_media,
        test_critical_threshold,
        test_uncertainty_quantification,
        test_beta_calculation,
        test_combined_analysis
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except AssertionError as e:
            print(f"\n✗ FAILED: {e}")
            results.append(False)
        except Exception as e:
            print(f"\n✗ ERROR: {e}")
            results.append(False)
    
    # Summary
    print("\n" + "="*70)
    print(" TEST SUMMARY ".center(70, "="))
    print("="*70)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"\n✓ ALL TESTS PASSED! ({passed}/{total})")
        print("\nThe MELV calculator is working correctly.")
        print("October 2025 validation results are reproducible.")
        print("\n🚀 READY FOR DEPLOYMENT!")
    else:
        print(f"\n✗ Some tests failed ({passed}/{total} passed)")
        print("\nPlease review failures before deploying.")
    
    print("\n" + "="*70 + "\n")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
