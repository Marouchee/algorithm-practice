from itertools import combinations, permutations, product

from solution import pairs_within, two_digit


def test_counts():
    arr = [1, 2, 3, 4]
    assert len(list(permutations(arr, 2))) == 12
    assert len(list(combinations(arr, 2))) == 6
    assert len(list(product(arr, repeat=2))) == 16


def test_combinations():
    menu = [("coffee", 4), ("cake", 6), ("juice", 5), ("cookie", 2)]
    assert pairs_within(menu, 10) == 5
    assert pairs_within(menu, 1) == 0


def test_permutations():
    assert two_digit(["1", "7", "0"]) == [10, 17, 70, 71]
    assert two_digit(["0", "0", "5"]) == [50, 50]            # 같은 값 카드는 위치가 달라 중복 생성됨


if __name__ == "__main__":
    test_counts()
    test_combinations()
    test_permutations()
    print("all tests passed")
