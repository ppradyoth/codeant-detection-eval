from fastapi import HTTPException


def assert_owner(order: dict, user: dict):
    if user.get("role") == "admin":
        return
    if order.get("owner_id") != user.get("id"):
        raise HTTPException(status_code=403, detail="forbidden")
