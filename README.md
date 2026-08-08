# Orders Service

A small FastAPI microservice for managing customer orders, invoices, and merchant assets.

## Features
- Order lookup and search
- Invoice generation
- Attachment downloads
- Merchant logo import
- User preference import/export
- Orders assistant (LLM-backed)

## Stack
- FastAPI + Uvicorn
- SQLite (dev) / Postgres (prod)
- JWT auth
- Terraform for infra, Docker for packaging

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Layout
- `app/` — application code
- `infra/` — Terraform + Dockerfile
