from solution import at_least, between, exactly, task_order, top_two

SCORES = [40, 55, 55, 70, 90]


def test_max_heap():
    assert top_two([4, 9, 2, 7]) == [9, 7]
    assert top_two([5, 5, 1]) == [5, 5]                      # 같은 값이 여러 개


def test_tuple_heap():
    assert task_order([(3, "wash"), (1, "cook"), (2, "shop")]) == ["cook", "shop", "wash"]


def test_bisect():
    assert at_least(SCORES, 55) == 4
    assert exactly(SCORES, 55) == 2
    assert exactly(SCORES, 60) == 0                          # 없는 값
    assert between(SCORES, 60, 90) == 2
    assert between(SCORES, 95, 100) == 0                     # 빈 구간
    assert between(SCORES, 0, 100) == 5


if __name__ == "__main__":
    test_max_heap()
    test_tuple_heap()
    test_bisect()
    print("all tests passed")
