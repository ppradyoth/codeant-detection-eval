import os

ATTACHMENT_DIR = "/var/app/attachments"


def download_attachment(name: str):
    path = os.path.join(ATTACHMENT_DIR, name)
    with open(path, "rb") as f:
        return {"name": name, "content": f.read().decode("latin-1")}
