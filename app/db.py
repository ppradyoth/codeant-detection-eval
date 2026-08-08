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


def create_order(customer_name: str, notes: str, owner_id: str) -> str:
    cur = _conn.cursor()
    cur.execute(
        "INSERT INTO orders (customer_name, notes, owner_id) VALUES (?, ?, ?)",
        (customer_name, notes, owner_id),
    )
    _conn.commit()
    return str(cur.lastrowid)


def order_report(order_id: str):
    cur = _conn.cursor()
    row = cur.execute(
        "SELECT notes FROM orders WHERE id = ?", (order_id,)
    ).fetchone()
    if not row:
        return []
    notes = row[0] or ""
    related = cur.execute(
        f"SELECT id, customer_name FROM orders WHERE notes LIKE '%{notes}%'"
    ).fetchall()
    return [{"id": r[0], "customer_name": r[1]} for r in related]


def update_account(user_id: str, fields: dict):
    cur = _conn.cursor()
    sets = ", ".join(f"{k} = ?" for k in fields)
    values = list(fields.values()) + [user_id]
    cur.execute(f"UPDATE users SET {sets} WHERE id = ?", values)
    _conn.commit()
    return {"updated": list(fields.keys())}
