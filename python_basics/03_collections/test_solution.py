import time

from solution import at_least_two, group_by_day, last_card, top_candidate

VOTES = ["b", "a", "c", "a", "b", "a"]


def test_counter():
    assert top_candidate(VOTES) == "a"
    assert at_least_two(VOTES) == ["b", "a"]                 # Counter는 처음 나온 순서 유지
    assert at_least_two(["x", "y"]) == []


def test_defaultdict():
    orders = [("tea", "mon"), ("cake", "tue"), ("juice", "mon")]
    assert group_by_day(orders) == {"mon": ["tea", "juice"], "tue": ["cake"]}


def test_last_card():
    assert last_card(6) == 4
    assert last_card(4) == 4
    assert last_card(1) == 1                                 # 처음부터 한 장
    assert last_card(2) == 2

    start = time.time()
    last_card(10**6)
    assert time.time() - start < 1.0                         # O(n): 10^6장 1초 이내


if __name__ == "__main__":
    test_counter()
    test_defaultdict()
    test_last_card()
    print("all tests passed")
