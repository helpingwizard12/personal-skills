def list_orders_for_customer(conn, customer_id):
    """Return the customer's orders, newest first, each with its line items and total."""
    orders = conn.execute(
        "SELECT id, created_at FROM orders WHERE customer_id = ? ORDER BY created_at DESC",
        (customer_id,),
    ).fetchall()
    result = []
    for order in orders:
        items = conn.execute(
            "SELECT product_id, quantity FROM order_items WHERE order_id = ?", (order["id"],)
        ).fetchall()
        lines = []
        total = 0
        for item in items:
            product = conn.execute(
                "SELECT name, price_cents FROM products WHERE id = ?", (item["product_id"],)
            ).fetchone()
            line_total = product["price_cents"] * item["quantity"]
            total += line_total
            lines.append(
                {"product": product["name"], "quantity": item["quantity"], "line_total_cents": line_total}
            )
        result.append({"id": order["id"], "created_at": order["created_at"], "items": lines, "total_cents": total})
    return result
