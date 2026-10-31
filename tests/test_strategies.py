from crypto_intel.strategies.asset_class import score_signal

def test_score_stress():
    assert score_signal("major", "stress", {"strength": 0.9}) == 0.0

def test_score_normal():
    factors = {"strength": 0.7, "vol_tier": 0.4, "anomaly": 0.1, "correlation": 0.3, "isolation": 0.1, "risk_parity": 0.9, "cvar": 0.8, "liquidity": 0.8}
    s = score_signal("major", "trend", factors)
    assert 0 < s <= 0.08
