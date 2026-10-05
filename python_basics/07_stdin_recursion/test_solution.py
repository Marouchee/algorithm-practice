import io

import solution


def feed(text: str) -> None:
    solution.input = io.StringIO(text).readline              # 표준 입력 대신 문자열을 읽게 함


def test_count_ones():
    feed("3 4\n1 0 1 1\n0 0 1 0\n1 1 1 1\n")
    assert solution.count_ones() == 8
    feed("1 1\n0\n")
    assert solution.count_ones() == 0


def test_read_char_grid():
    feed("2 3\n101\n011\n")
    assert solution.read_char_grid() == [[1, 0, 1], [0, 1, 1]]
    feed("1 3\n305")                                         # 마지막 줄에 '\n'이 없어도 동작
    assert solution.read_char_grid() == [[3, 0, 5]]


if __name__ == "__main__":
    test_count_ones()
    test_read_char_grid()
    print("all tests passed")
