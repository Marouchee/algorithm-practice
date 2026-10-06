S1_1 = "SELECT name FROM MEMBERS WHERE city = '서울' ORDER BY name ASC;"

S1_2 = "SELECT name, price FROM PRODUCTS ORDER BY price DESC LIMIT 1;"

S1_3 = "SELECT order_id, order_date FROM ORDERS WHERE amount >=2 AND status != 'CANCEL' ORDER BY order_date DESC"

S1_4 = "SELECT name FROM MEMBERS WHERE city IS NULL"

S1_4_NOT = "SELECT name FROM MEMBERS WHERE city IS NOT NULL"

S2_1 = "SELECT category, COUNT(*) AS cnt FROM PRODUCTS GROUP BY category ORDER BY category ASC"

S2_2 = "SELECT member_id, SUM(amount) AS sum_amt FROM ORDERS WHERE status != 'CANCEL' GROUP BY member_id ORDER BY sum_amt DESC, member_id ASC"

S2_3 = "SELECT member_id, COUNT(*) AS cnt FROM ORDERS GROUP BY member_id HAVING COUNT(*) >= 2"

S2_5 = "SELECT member_id, COUNT(*) AS cnt FROM ORDERS WHERE order_date >= '2026-09-01' GROUP BY member_id HAVING COUNT(*) >= 2"

S3_1 = """
SELECT o.order_id, m.name, o.order_date
FROM ORDERS o
JOIN MEMBERS m ON m.member_id = o.member_id
WHERE o.status = 'CANCEL';
"""

S3_2 = """
SELECT p.category, COUNT(*) AS cnt
FROM PRODUCTS p
JOIN ORDERS o ON o.product_id = p.product_id
WHERE o.status != 'CANCEL'
GROUP BY p.category
ORDER BY cnt DESC, category ASC;
"""

S3_3 = """
SELECT m.name
FROM MEMBERS m
LEFT JOIN ORDERS o ON m.member_id = o.member_id
WHERE o.member_id IS NULL;
"""

S3_5 = """
SELECT SUM(p.price*o.amount) AS pay_amount,  m.name
FROM ORDERS o
JOIN PRODUCTS p ON p.product_id = o.product_id
JOIN MEMBERS m ON m.member_id = o.member_id
WHERE o.status != 'CANCEL'
GROUP BY m.member_id, m.name
ORDER BY pay_amount DESC;
"""
