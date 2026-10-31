"""Multi-hash sealed lineage for v0.56."""
import hashlib
import json

def seal(payload: dict) -> dict:
    raw = json.dumps(payload, sort_keys=True).encode()
    return {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "sha3_256": hashlib.sha3_256(raw).hexdigest(),
        "blake2b": hashlib.blake2b(raw).hexdigest(),
        "sha512": hashlib.sha512(raw).hexdigest(),
        "sha3_512": hashlib.sha3_512(raw).hexdigest(),
        "counter": payload.get("counter", 0),
        "note": "BLAKE3 proxy via blake2b in research mode",
    }
