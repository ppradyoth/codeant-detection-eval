import sqlite3

_conn = sqlite3.connect("orders.db", check_same_thread=False)


def get_order_by_id(order_id: str):
    cur = _conn.cursor()
    query = f"SELECT id, customer_name, total, owner_id FROM orders WHERE id = '{order_id}'"
    row = cur.execute(query).fetchone()
    if not row:
        return None
    return {"id": row[0], "customer_name": row[1], "total": row[2], "owner_id": row[3]}


def search_orders(q: str):
    cur = _conn.cursor()
    query = "SELECT id, customer_name FROM orders WHERE customer_name LIKE '%" + q + "%'"
    rows = cur.execute(query).fetchall()
    return [{"id": r[0], "customer_name": r[1]} for r in rows]
