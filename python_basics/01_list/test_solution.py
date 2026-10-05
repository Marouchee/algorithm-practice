from solution import (
    column_sums,
    even_index,
    last_three,
    long_words_upper,
    make_grid,
    reverse,
    transpose,
)

TEMPS = [12, 15, 9, 20, 18, 7, 25]
BOARD = [[1, 2, 3], [4, 5, 6]]


def test_slicing():
    assert last_three(TEMPS) == [18, 7, 25]
    assert last_three([1, 2, 3, 4]) == [2, 3, 4]             # 길이가 달라도 동작
    assert reverse(TEMPS) == [25, 7, 18, 20, 9, 15, 12]
    assert even_index(TEMPS) == [12, 9, 18, 25]              # 인덱스 0도 짝수


def test_comprehension():
    words = ["apple", "kiwi", "banana", "fig", "cherry"]
    assert long_words_upper(words) == ["APPLE", "BANANA", "CHERRY"]
    assert long_words_upper([]) == []


def test_grid_rows_are_independent():
    grid = make_grid(3, 4)
    grid[1][2] = 5
    assert grid == [[0, 0, 0, 0], [0, 0, 5, 0], [0, 0, 0, 0]]
    assert grid[0] is not grid[1]                            # [[0]*4]*3 함정 방지


def test_2d_traversal():
    assert transpose(BOARD) == [[1, 4], [2, 5], [3, 6]]
    assert column_sums(BOARD) == [5, 7, 9]
    assert transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]   # 3행 2열
    assert column_sums([[1, 2], [3, 4], [5, 6]]) == [9, 12]


if __name__ == "__main__":
    test_slicing()
    test_comprehension()
    test_grid_rows_are_independent()
    test_2d_traversal()
    print("all tests passed")
