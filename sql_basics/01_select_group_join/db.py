"""SQL 드릴용 연습 DB를 메모리(SQLite)에 만든다. 데이터는 가상이다."""
import sqlite3

SCHEMA = """
CREATE TABLE MEMBERS (
    member_id  INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    gender     TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    city       TEXT
);
CREATE TABLE PRODUCTS (
    product_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    category   TEXT NOT NULL,
    price      INTEGER NOT NULL
);
CREATE TABLE ORDERS (
    order_id   INTEGER PRIMARY KEY,
    member_id  INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    amount     INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    status     TEXT NOT NULL
);
"""

MEMBERS = [
    (1, "김하늘", "F", "1995-03-02", "서울"),
    (2, "이준호", "M", "1990-11-15", "부산"),
    (3, "박서연", "F", "1998-07-21", "서울"),
    (4, "최민수", "M", "1987-01-30", None),
    (5, "정다은", "F", "2000-12-05", "대구"),
    (6, "한지훈", "M", "1993-05-17", "서울"),
    (7, "오수아", "F", "1996-09-09", None),
    (8, "윤도윤", "M", "1992-04-11", "광주"),
]

PRODUCTS = [
    (101, "제주 항공권", "FLIGHT", 120000),
    (102, "오사카 호텔", "HOTEL", 95000),
    (103, "다낭 투어", "TOUR", 45000),
    (104, "도쿄 항공권", "FLIGHT", 180000),
    (105, "부산 호텔", "HOTEL", 70000),
    (106, "유심", "ETC", 9000),
]

ORDERS = [
    (1, 1, 101, 2, "2026-08-03", "DONE"),
    (2, 1, 106, 1, "2026-08-03", "DONE"),
    (3, 2, 102, 1, "2026-08-15", "CANCEL"),
    (4, 3, 103, 3, "2026-09-01", "DONE"),
    (5, 3, 104, 1, "2026-09-02", "DONE"),
    (6, 5, 105, 2, "2026-09-10", "DONE"),
    (7, 6, 101, 1, "2026-09-12", "CANCEL"),
    (8, 1, 103, 2, "2026-09-20", "DONE"),
    (9, 2, 104, 2, "2026-10-01", "DONE"),
    (10, 5, 106, 4, "2026-10-02", "DONE"),
    (11, 3, 101, 1, "2026-10-03", "DONE"),
    (12, 6, 102, 2, "2026-10-04", "DONE"),
    (13, 7, 105, 1, "2026-10-05", "DONE"),
]


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    con.executescript(SCHEMA)
    con.executemany("INSERT INTO MEMBERS VALUES (?, ?, ?, ?, ?)", MEMBERS)
    con.executemany("INSERT INTO PRODUCTS VALUES (?, ?, ?, ?)", PRODUCTS)
    con.executemany("INSERT INTO ORDERS VALUES (?, ?, ?, ?, ?, ?)", ORDERS)
    return con
