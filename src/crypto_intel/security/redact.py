"""Expanded redaction for v0.56 zero-trust."""
import re

PATTERNS = [
    re.compile(r"\b(?:[a-z]{3,8}\s+){11,24}[a-z]{3,8}\b", re.I),  # BIP39-like
    re.compile(r"[5KL][1-9A-HJ-NP-Za-km-z]{50,51}"),  # WIF
    re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),  # AWS
    re.compile(r"ghp_[A-Za-z0-9_]{36}"),  # GitHub PAT
    re.compile(r"[A-Za-z0-9+/]{40,}={0,2}"),  # high entropy / base64
    re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}"),  # Solana-like
    re.compile(r"eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+"),  # JWT
    re.compile(r"[0-9a-fA-F]{64}"),  # hex private key
    re.compile(r"bot[0-9]+:[A-Za-z0-9_\-]{30,}"),  # Telegram
    re.compile(r"(api[_-]?key|secret|private[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}", re.I),
]

def redact(text: str) -> str:
    out = text
    for p in PATTERNS:
        out = p.sub("[REDACTED]", out)
    return out
