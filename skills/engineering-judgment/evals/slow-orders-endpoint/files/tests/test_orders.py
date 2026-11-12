import unittest

from app.db import connect
from app.orders import list_orders_for_customer


class ListOrdersTest(unittest.TestCase):
    def setUp(self):
        self.conn = connect()
        c = self.conn
        c.execute("INSERT INTO customers (id, name) VALUES (1, 'Acme')")
        c.execute("INSERT INTO products (id, name, price_cents) VALUES (10, 'Widget', 250), (11, 'Gadget', 1000)")
        c.execute("INSERT INTO orders (id, customer_id, created_at) VALUES (100, 1, '2026-01-01'), (101, 1, '2026-02-01')")
        c.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (100, 10, 4), (101, 10, 1), (101, 11, 2)")

    def test_newest_first_with_totals(self):
        orders = list_orders_for_customer(self.conn, 1)
        self.assertEqual([o["id"] for o in orders], [101, 100])
        self.assertEqual(orders[0]["total_cents"], 2250)
        self.assertEqual(orders[1]["total_cents"], 1000)

    def test_unknown_customer(self):
        self.assertEqual(list_orders_for_customer(self.conn, 999), [])


if __name__ == "__main__":
    unittest.main()
