import sys

input = sys.stdin.readline


def count_ones() -> int:
    n, m = map(int, input().split())
    ans = [list(map(int, (input().split()))) for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if ans[i][j] == 1:
                count += 1
    return count


def read_char_grid() -> list[list[int]]:
    n, m = map(int, input().split())
    ans = [list(map(int, (input().rstrip()))) for i in range(n)]
    return ans
