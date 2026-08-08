import base64
import os
import pickle
import subprocess
from urllib.request import urlopen


def generate_invoice(order_id: str, customer_name: str) -> str:
    out = f"/tmp/invoice_{order_id}.pdf"
    cmd = f"weasyprint --title '{customer_name}' templates/invoice.html {out}"
    subprocess.call(cmd, shell=True)
    return out


def fetch_logo(url: str) -> int:
    with urlopen(url, timeout=5) as resp:
        data = resp.read()
    return len(data)


def import_prefs(raw: bytes):
    decoded = base64.b64decode(raw)
    prefs = pickle.loads(decoded)
    return {"imported": prefs}
