import time

from solution import dedup, dedup_deque

EXAMPLE = [(1, "a"), (3, "b"), (5, "a"), (11, "a"), (12, "b"), (13, "b"), (20, "a"), (21, "a")]
EXPECTED = [(1, "a"), (3, "b"), (11, "a"), (13, "b"), (21, "a")]


def check(fn):
    assert fn(EXAMPLE, 10) == EXPECTED
    assert fn([(5, "x")], 3) == [(5, "x")]                                  # 원소 1개
    assert fn([(1, "a"), (1, "a")], 1) == [(1, "a")]                        # 같은 시각 중복
    assert fn([(1, "a"), (2, "a"), (3, "a")], 1) == [(1, "a"), (2, "a"), (3, "a")]  # W=1 연속
    assert fn([(1, "a"), (2, "a"), (3, "a")], 3) == [(1, "a")]              # 버린 이벤트는 기준이 아님

    events = [(t, f"u{t}") for t in range(10**5)]
    start = time.time()
    assert len(fn(events, 10)) == 10**5
    assert time.time() - start < 1.0                                        # 10^5개 1초 이내


def test_dedup():
    check(dedup)


def test_dedup_deque():
    check(dedup_deque)


if __name__ == "__main__":
    test_dedup()
    test_dedup_deque()
    print("all tests passed")
