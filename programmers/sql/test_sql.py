"""프로그래머스 SQL 풀이를 가상 데이터(SQLite)로 실행해 본다. 채점은 프로그래머스(MySQL)에서 통과했다."""
import sqlite3
from pathlib import Path

HERE = Path(__file__).parent

SCHEMA = """
CREATE TABLE ANIMAL_INS (
    ANIMAL_ID TEXT, ANIMAL_TYPE TEXT, DATETIME TEXT,
    INTAKE_CONDITION TEXT, NAME TEXT, SEX_UPON_INTAKE TEXT
);
CREATE TABLE ANIMAL_OUTS (
    ANIMAL_ID TEXT, ANIMAL_TYPE TEXT, DATETIME TEXT,
    NAME TEXT, SEX_UPON_OUTCOME TEXT
);
"""

INS = [
    ("A001", "Dog", "2025-01-05 10:00:00", "Normal", "Max", "Neutered Male"),
    ("A002", "Cat", "2025-01-03 09:00:00", "Normal", None, "Spayed Female"),
    ("A003", "Dog", "2025-02-10 14:00:00", "Sick", "Max", "Intact Male"),
    ("A004", "Cat", "2025-01-20 11:00:00", "Normal", "Luna", "Spayed Female"),
    ("A005", "Dog", "2024-12-30 16:00:00", "Normal", None, "Intact Female"),
    ("A006", "Cat", "2025-03-01 13:00:00", "Normal", "Coco", "Intact Male"),
    ("A007", "Dog", "2024-11-11 08:00:00", "Aged", "Luna", "Neutered Male"),
    ("A008", "Bird", "2025-03-05 12:00:00", "Normal", "Kiwi", "Intact Male"),
]

OUTS = [
    ("A001", "Dog", "2025-02-01 10:00:00", "Max", "Neutered Male"),
    ("A004", "Cat", "2025-02-15 11:00:00", "Luna", "Spayed Female"),
    ("A090", "Dog", "2025-01-10 15:00:00", "Ghost", "Intact Male"),    # 입소 기록 없음
    ("A080", "Cat", "2025-01-12 17:00:00", "Bella", "Spayed Female"),  # 입소 기록 없음
]


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    con.executescript(SCHEMA)
    con.executemany("INSERT INTO ANIMAL_INS VALUES (?, ?, ?, ?, ?, ?)", INS)
    con.executemany("INSERT INTO ANIMAL_OUTS VALUES (?, ?, ?, ?, ?)", OUTS)
    return con


con = connect()


def run(name: str) -> list[tuple]:
    return con.execute((HERE / f"{name}.sql").read_text()).fetchall()


if __name__ == "__main__":
    assert run("이름이_없는_동물의_아이디") == [("A002",), ("A005",)]

    rows = run("NULL_처리하기")
    assert len(rows) == 8
    assert rows[1] == ("Cat", "No name", "Spayed Female")              # NULL → 'No name'

    assert run("고양이와_개는_몇_마리_있을까") == [("Cat", 3), ("Dog", 4)]   # Bird 제외
    assert run("동명_동물_수_찾기") == [("Luna", 2), ("Max", 2)]
    assert run("없어진_기록_찾기") == [("A080", "Bella"), ("A090", "Ghost")]
    assert run("오랜_기간_보호한_동물_1") == [
        ("Luna", "2024-11-11 08:00:00"),
        (None, "2024-12-30 16:00:00"),
        (None, "2025-01-03 09:00:00"),
    ]
    print("all tests passed")
