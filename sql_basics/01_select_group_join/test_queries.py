import queries as q
from db import connect

con = connect()


def run(sql: str) -> list[tuple]:
    return con.execute(sql).fetchall()


def test_select():
    assert run(q.S1_1) == [("김하늘",), ("박서연",), ("한지훈",)]
    assert run(q.S1_2) == [("도쿄 항공권", 180000)]
    assert [r[0] for r in run(q.S1_3)] == [12, 10, 9, 8, 6, 4, 1]
    assert run(q.S1_4) == [("최민수",), ("오수아",)]
    assert len(run(q.S1_4_NOT)) == 6
    assert run("SELECT name FROM MEMBERS WHERE city = NULL") == []         # = NULL은 항상 0행


def test_group_by():
    assert run(q.S2_1) == [("ETC", 1), ("FLIGHT", 2), ("HOTEL", 2), ("TOUR", 1)]
    assert run(q.S2_2) == [(5, 6), (1, 5), (3, 5), (2, 2), (6, 2), (7, 1)]
    assert run(q.S2_3) == [(1, 3), (2, 2), (3, 3), (5, 2), (6, 2)]
    assert run("SELECT COUNT(*), COUNT(city) FROM MEMBERS") == [(8, 6)]   # COUNT(열)은 NULL 제외
    assert run(q.S2_5) == [(3, 3), (5, 2), (6, 2)]


def test_join():
    assert run(q.S3_1) == [(3, "이준호", "2026-08-15"), (7, "한지훈", "2026-09-12")]
    assert run(q.S3_2) == [("FLIGHT", 4), ("HOTEL", 3), ("ETC", 2), ("TOUR", 2)]
    assert run(q.S3_3) == [("최민수",), ("윤도윤",)]
    assert run(q.S3_5)[:3] == [(435000, "박서연"), (360000, "이준호"), (339000, "김하늘")]
    assert len(run(q.S3_5)) == 6

    counts = run("""
        SELECT m.name, COUNT(*) AS a, COUNT(o.order_id) AS b
        FROM MEMBERS m LEFT JOIN ORDERS o ON m.member_id = o.member_id
        GROUP BY m.member_id, m.name
    """)
    assert ("최민수", 1, 0) in counts                                       # LEFT JOIN: COUNT(*)는 1, COUNT(열)은 0


if __name__ == "__main__":
    test_select()
    test_group_by()
    test_join()
    print("all tests passed")
