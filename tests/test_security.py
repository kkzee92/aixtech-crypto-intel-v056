from crypto_intel.security.redact import redact
from crypto_intel.security.audit import seal

def test_redact():
    assert "[REDACTED]" in redact("seed phrase word one two three four five six seven eight nine ten eleven twelve")

def test_seal():
    s = seal({"a": 1, "counter": 1})
    assert "sha256" in s and len(s["sha256"]) == 64
