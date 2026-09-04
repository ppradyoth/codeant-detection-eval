import base64
import json
from urllib.parse import urlparse

import requests
from weasyprint import HTML

ALLOWED_LOGO_HOSTS = ("cdn.merchants.example.com", "assets.example.com")


def generate_invoice(order_id: str, customer_name: str) -> str:
    out = f"/tmp/invoice_{order_id}.pdf"
    HTML("templates/invoice.html").write_pdf(out)
    return out


def _host_allowed(url: str) -> bool:
    host = urlparse(url).hostname or ""
    return any(host.endswith(h) for h in ALLOWED_LOGO_HOSTS)


def fetch_logo(url: str) -> int:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not _host_allowed(url):
        raise ValueError("host not allowed")
    resp = requests.get(url, timeout=5)
    return len(resp.content)


def import_prefs(raw: bytes):
    decoded = base64.b64decode(raw)
    prefs = json.loads(decoded)
    return {"imported": prefs}
