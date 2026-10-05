from solution import count, distinct_count, group, intersection, only_left, union

A = {1, 2, 3, 4}
B = {3, 4, 5}


def test_count():
    fruits = ["pear", "fig", "pear", "plum", "fig", "pear"]
    assert count(fruits) == {"pear": 3, "fig": 2, "plum": 1}
    assert count([]) == {}


def test_group():
    students = [("kim", "A"), ("lee", "B"), ("park", "A")]
    assert group(students) == {"A": ["kim", "park"], "B": ["lee"]}   # 원소가 리스트로 중첩되지 않음
    assert group([("kim", "A")]) == {"A": ["kim"]}


def test_set_operations():
    assert intersection(A, B) == {3, 4}
    assert union(A, B) == {1, 2, 3, 4, 5}
    assert only_left(A, B) == {1, 2}
    assert only_left(B, A) == {5}                            # 방향이 바뀌면 결과도 바뀜
    assert distinct_count([3, 1, 3, 2, 1]) == 3


if __name__ == "__main__":
    test_count()
    test_group()
    test_set_operations()
    print("all tests passed")
