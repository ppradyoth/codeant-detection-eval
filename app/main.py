from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import BaseModel

from app import db
from app.auth import current_user
from app.integrations import fetch_logo, generate_invoice, import_prefs
from app.files import download_attachment
from app.llm import assistant_reply

app = FastAPI(title="Orders Service")


class OrderQuery(BaseModel):
    q: str


@app.get("/orders/{order_id}")
def get_order(order_id: str, user=Depends(current_user)):
    order = db.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="not found")
    return order


@app.post("/orders/search")
def search_orders(body: OrderQuery, user=Depends(current_user)):
    return db.search_orders(body.q)


@app.get("/orders/{order_id}/invoice")
def invoice(order_id: str, user=Depends(current_user)):
    order = db.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="not found")
    path = generate_invoice(order_id, order["customer_name"])
    return {"invoice": path}


@app.get("/attachments")
def attachment(name: str, user=Depends(current_user)):
    return download_attachment(name)


@app.post("/merchants/logo")
def merchant_logo(url: str, user=Depends(current_user)):
    return {"bytes": fetch_logo(url)}


@app.post("/prefs/import")
async def prefs_import(request: Request, user=Depends(current_user)):
    raw = await request.body()
    return import_prefs(raw)


@app.post("/assistant")
def assistant(body: OrderQuery, user=Depends(current_user)):
    return {"reply": assistant_reply(body.q, user)}
