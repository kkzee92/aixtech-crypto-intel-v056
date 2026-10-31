"""Paper-only demo runner."""
from crypto_intel.strategies.asset_class import score_signal

def run_demo():
    print("AIxTech crypto intel v0.56 — paper-only demo")
    factors = {"strength": 0.62, "vol_tier": 0.45, "vol_forecast": 0.48, "anomaly": 0.2, "correlation": 0.35, "isolation": 0.15, "residual": 0.25, "oi_change": 0.3, "risk_parity": 0.85, "cvar": 0.75, "order_flow": 0.4, "liquidity": 0.7}
    for cls in ["major", "large_alt", "meme", "ai_token"]:
        s = score_signal(cls, "trend", factors)
        print(f"{cls}: score={s}")
    print("Audit seal placeholder — multi-hash lineage OK")
