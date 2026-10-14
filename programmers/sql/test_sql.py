"""프로그래머스 SQL 풀이를 가상 데이터(SQLite)로 실행해 본다. 채점은 프로그래머스(MySQL)에서 통과했다."""
import sqlite3
from datetime import datetime
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
CREATE TABLE APPOINTMENT (
    APNT_YMD TEXT, APNT_NO INTEGER, PT_NO TEXT, MCDP_CD TEXT,
    MDDR_ID TEXT, APNT_CNCL_YN TEXT, APNT_CNCL_YMD TEXT
);
CREATE TABLE USED_GOODS_BOARD (
    BOARD_ID TEXT, WRITER_ID TEXT, TITLE TEXT, CONTENTS TEXT,
    PRICE INTEGER, CREATED_DATE TEXT, STATUS TEXT, VIEWS INTEGER
);
CREATE TABLE USED_GOODS_USER (
    USER_ID TEXT, NICKNAME TEXT, CITY TEXT,
    STREET_ADDRESS1 TEXT, STREET_ADDRESS2 TEXT, TLNO TEXT
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
    ("A009", "Dog", "2025-03-10 09:30:00", "Normal", "Ella", "Spayed Female"),
    ("A010", "Cat", "2025-03-11 10:00:00", "Normal", "Mabel", "Intact Female"),
    ("A011", "Dog", "2025-03-12 11:00:00", "Normal", "Noel", "Intact Male"),
]

OUTS = [
    ("A001", "Dog", "2025-02-01 10:00:00", "Max", "Neutered Male"),
    ("A004", "Cat", "2025-02-15 11:00:00", "Luna", "Spayed Female"),
    ("A090", "Dog", "2025-01-10 15:00:00", "Ghost", "Intact Male"),    # 입소 기록 없음
    ("A080", "Cat", "2025-01-12 17:00:00", "Bella", "Spayed Female"),  # 입소 기록 없음
    ("A003", "Dog", "2025-02-20 09:00:00", "Max", "Neutered Male"),      # 9시 정각: 포함
    ("A006", "Cat", "2025-03-05 19:59:00", "Coco", "Neutered Male"),     # 19시 59분: 포함
    ("A008", "Bird", "2025-03-08 08:59:00", "Kiwi", "Intact Male"),      # 8시 59분: 제외
    ("A009", "Dog", "2025-03-15 20:00:00", "Ella", "Spayed Female"),     # 20시 정각: 제외
    ("A010", "Cat", "2025-03-10 10:30:00", "Mabel", "Spayed Female"),    # 10시 두 번째, 보호 시작(3/11)보다 이른 입양
    ("A011", "Dog", "2025-03-01 07:00:00", "Noel", "Neutered Male"),     # 보호 시작(3/12)보다 이른 입양
]

APPOINTMENTS = [
    ("2022-05-02 09:00:00", 1, "P01", "CS", "D01", "N", None),
    ("2022-05-20 10:00:00", 2, "P02", "CS", "D01", "N", None),
    ("2022-05-01 00:00:00", 3, "P03", "GS", "D02", "N", None),    # 5월 첫 순간: 포함
    ("2022-05-31 23:59:00", 4, "P04", "GS", "D02", "N", None),    # 5월 마지막 순간: 포함, CS와 2건 동률
    ("2022-05-10 11:00:00", 5, "P05", "OS", "D03", "N", None),
    ("2022-04-30 23:59:00", 6, "P06", "PD", "D04", "N", None),    # 4월: 제외
    ("2022-06-01 00:00:00", 7, "P07", "PD", "D04", "N", None),    # 6월: 제외
    ("2021-05-15 12:00:00", 8, "P08", "PD", "D04", "N", None),    # 2021년 5월: 제외
    ("2022-05-03 09:00:00", 9, "P09", "NP", "D05", "N", None),
    ("2022-05-04 09:00:00", 10, "P10", "NP", "D05", "N", None),
    ("2022-05-05 09:00:00", 11, "P11", "NP", "D05", "N", None),
]

GOODS_USERS = [
    ("u1", "하늘", "서울", "", "", ""),
    ("u2", "바다", "부산", "", "", ""),
    ("u3", "구름", "대전", "", "", ""),
    ("u4", "별빛", "광주", "", "", ""),
    ("u5", "노을", "인천", "", "", ""),
]

GOODS_BOARD = [
    ("B01", "u1", "", "", 500000, "2022-10-01", "DONE", 1),
    ("B02", "u1", "", "", 300000, "2022-10-02", "DONE", 1),      # u1 합계 800,000
    ("B03", "u1", "", "", 900000, "2022-10-03", "SALE", 1),      # 판매 중: 제외
    ("B04", "u2", "", "", 700000, "2022-10-04", "DONE", 1),      # u2 정확히 700,000: 포함
    ("B05", "u3", "", "", 699999, "2022-10-05", "DONE", 1),      # u3 1원 모자람: 제외
    ("B06", "u4", "", "", 1000000, "2022-10-06", "RESERVED", 1), # u4 완료 거래 없음: 제외
    ("B07", "u5", "", "", 600000, "2022-10-07", "DONE", 1),
    ("B08", "u5", "", "", 400000, "2022-10-08", "DONE", 1),      # u5 합계 1,000,000
]


def date_format(value: str, fmt: str) -> str:
    """SQLite에는 MySQL DATE_FORMAT이 없어서 흉내 낸다 (%Y, %m, %d는 strftime과 같다)."""
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S").strftime(fmt)


def hour(value: str) -> int:
    """SQLite에는 MySQL HOUR가 없어서 흉내 낸다."""
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S").hour


def month(value: str) -> str:
    """MySQL MONTH 흉내. MySQL은 5 = '5'를 참으로 보지만 SQLite는 거짓으로 보므로, 문자열 비교 쿼리에 맞춰 문자열로 돌려준다."""
    return str(datetime.strptime(value, "%Y-%m-%d %H:%M:%S").month)


def year(value: str) -> str:
    """MySQL YEAR 흉내 (month와 같은 이유로 문자열)"""
    return str(datetime.strptime(value, "%Y-%m-%d %H:%M:%S").year)


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    con.create_function("DATE_FORMAT", 2, date_format)
    con.create_function("HOUR", 1, hour)
    con.create_function("MONTH", 1, month)
    con.create_function("YEAR", 1, year)
    con.executescript(SCHEMA)
    con.executemany("INSERT INTO ANIMAL_INS VALUES (?, ?, ?, ?, ?, ?)", INS)
    con.executemany("INSERT INTO ANIMAL_OUTS VALUES (?, ?, ?, ?, ?)", OUTS)
    con.executemany("INSERT INTO APPOINTMENT VALUES (?, ?, ?, ?, ?, ?, ?)", APPOINTMENTS)
    con.executemany("INSERT INTO USED_GOODS_USER VALUES (?, ?, ?, ?, ?, ?)", GOODS_USERS)
    con.executemany("INSERT INTO USED_GOODS_BOARD VALUES (?, ?, ?, ?, ?, ?, ?, ?)", GOODS_BOARD)
    return con


con = connect()


def run(name: str) -> list[tuple]:
    return con.execute((HERE / f"{name}.sql").read_text()).fetchall()


if __name__ == "__main__":
    assert run("이름이_없는_동물의_아이디") == [("A002",), ("A005",)]

    rows = run("NULL_처리하기")
    assert len(rows) == 11
    assert rows[1] == ("Cat", "No name", "Spayed Female")              # NULL → 'No name'

    assert run("고양이와_개는_몇_마리_있을까") == [("Cat", 4), ("Dog", 6)]   # Bird 제외
    assert run("동명_동물_수_찾기") == [("Luna", 2), ("Max", 2)]
    assert run("없어진_기록_찾기") == [("A080", "Bella"), ("A090", "Ghost")]
    assert run("오랜_기간_보호한_동물_1") == [
        ("Luna", "2024-11-11 08:00:00"),
        (None, "2024-12-30 16:00:00"),
        (None, "2025-01-03 09:00:00"),
    ]

    assert run("이름에_el이_들어가는_동물_찾기") == [("A009", "Ella"), ("A011", "Noel")]   # 대문자 El 포함, 고양이 Mabel 제외

    rows = run("중성화_여부_파악하기")
    assert rows[0] == ("A001", "Max", "O")        # Neutered
    assert rows[1] == ("A002", None, "O")         # Spayed
    assert rows[2] == ("A003", "Max", "X")        # Intact

    assert run("DATETIME에서_DATE로_형_변환")[0] == ("A001", "Max", "2025-01-05")

    # 이름 11행 중 NULL 2개, Max·Luna 중복 → 7 (COUNT(*)는 11, COUNT(NAME)은 9)
    assert run("중복_제거하기") == [(7,)]

    # Intact → Neutered/Spayed만. A008(Intact → Intact), A001·A004·A009(들어올 때 이미 중성화) 제외
    assert run("보호소에서_중성화한_동물") == [
        ("A003", "Dog", "Max"), ("A006", "Cat", "Coco"), ("A010", "Cat", "Mabel"), ("A011", "Dog", "Noel"),
    ]

    # 보호 시작일 순이면 A010 → A011, 입양일 순이면 거꾸로
    assert run("있었는데요_없었습니다") == [("A010", "Mabel"), ("A011", "Noel")]

    assert run("입양_시각_구하기_1") == [(9, 1), (10, 2), (11, 1), (15, 1), (17, 1), (19, 1)]   # 8시 59분, 20시 정각 제외

    # 건수 오름차순, 동률(CS·GS 2건)은 진료과 코드 오름차순. PD는 5월 예약이 없어 행 자체가 없음
    assert run("진료과별_총_예약_횟수_출력하기") == [("OS", 1), ("CS", 2), ("GS", 2), ("NP", 3)]

    # 완료(DONE)만 합산, 70만 원 이상(경계 포함), 합계 오름차순
    assert run("조건에_맞는_사용자와_총_거래금액_조회하기") == [
        ("u2", "바다", 700000), ("u1", "하늘", 800000), ("u5", "노을", 1000000),
    ]
    print("all tests passed")
