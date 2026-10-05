def last_three(temps: list[int]) -> list[int]:
    return temps[-3:]


def reverse(temps: list[int]) -> list[int]:
    return temps[::-1]


def even_index(temps: list[int]) -> list[int]:
    return temps[::2]


def long_words_upper(words: list[str]) -> list[str]:
    return [word.upper() for word in words if len(word) >= 5]


def make_grid(n: int, m: int) -> list[list[int]]:
    return [[0] * m for i in range(n)]


def transpose(board: list[list[int]]) -> list[list[int]]:
    ans = []
    for j in range(len(board[0])):
        ans.append([board[i][j] for i in range(len(board))])
    return ans


def column_sums(board: list[list[int]]) -> list[int]:
    ans = []
    for j in range(len(board[0])):
        ans.append(sum([board[i][j] for i in range(len(board))]))
    return ans
