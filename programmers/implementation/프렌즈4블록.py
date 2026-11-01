"""프로그래머스 Lv.2 [1차] 프렌즈4블록 (구현, 격자 시뮬레이션)
https://school.programmers.co.kr/learn/courses/30/lessons/17679

접근: 판을 2차원 리스트로 바꾸고 라운드를 반복한다.
      1) 같은 모양 2×2의 네 칸 좌표를 set에 모은다. 한 칸이 2×2 여러 개에 들어가도 한 번만 센다.
         빈칸(0)에서 시작하는 2×2는 건너뛴다.
      2) 모은 칸을 0으로 비운다.
      3) 열마다 아래에서 위로 보며, 빈칸이면 위쪽에서 처음 나오는 블록을 끌어내린다.
         위로 훑는 인덱스는 0에서 멈춰야 한다. -1이 되면 파이썬은 맨 아랫줄을 읽는다.
      set이 비면 끝내고, 라운드마다 set의 크기를 더한다.
시간 복잡도: 라운드 한 번에 2×2 찾기 O(mn) + 떨어뜨리기 O(n · m²).
            라운드마다 4칸 이상 지워지므로 라운드는 mn/4번 이하 → O(m³n²)
"""
import random
import time


def solution(m, n, board):
    answer = 0
    board_list = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            board_list[i][j] = board[i][j]

    while True:
        temp_2x2 = set()
        for i in range(m-1):
            for j in range(n-1):
                if board_list[i][j] == 0:
                    continue
                if board_list[i][j] == board_list[i][j+1] and board_list[i][j+1] == board_list[i+1][j] and board_list[i+1][j] == board_list[i+1][j+1]:
                    temp_2x2.add((i,j))
                    temp_2x2.add((i+1,j))
                    temp_2x2.add((i,j+1))
                    temp_2x2.add((i+1,j+1))
        for x,y in temp_2x2:
            board_list[x][y] = 0
        for j in range(n):
            for i in range(m):
                temp_idx = m-1-i
                if board_list[m-1-i][j] == 0:
                    while temp_idx > 0:
                        temp_idx -= 1
                        if board_list[temp_idx][j] != 0:
                            board_list[m-1-i][j] = board_list[temp_idx][j]
                            board_list[temp_idx][j] = 0
                            break
        if not temp_2x2:
            break
        else:
            answer += len(temp_2x2)

    return answer


def reference(m, n, board):
    """비교용: 열마다 남은 블록만 모아 아래쪽에 다시 채운다"""
    g = [list(row) for row in board]
    total = 0
    while True:
        hit = set()
        for i in range(m - 1):
            for j in range(n - 1):
                c = g[i][j]
                if c != "." and c == g[i][j + 1] == g[i + 1][j] == g[i + 1][j + 1]:
                    hit |= {(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)}
        if not hit:
            return total
        total += len(hit)
        for i, j in hit:
            g[i][j] = "."
        for j in range(n):
            col = [g[i][j] for i in range(m) if g[i][j] != "."]
            col = ["."] * (m - len(col)) + col
            for i in range(m):
                g[i][j] = col[i]


if __name__ == "__main__":
    assert solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]) == 14
    assert solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15
    assert solution(2, 3, ["AAA", "AAA"]) == 6                 # 겹치는 2×2는 한 번만 센다
    assert solution(3, 2, ["AB", "AA", "AA"]) == 4             # 지운 뒤 A, B가 맨 아래로 떨어짐
    assert solution(4, 2, ["AA", "BB", "BB", "AA"]) == 8       # 가운데가 지워져 위아래 A가 만남
    assert solution(2, 2, ["AB", "CD"]) == 0

    random.seed(0)
    for _ in range(5000):
        m, n = random.randint(2, 7), random.randint(2, 7)
        board = ["".join(random.choice("AB") for _ in range(n)) for _ in range(m)]
        assert solution(m, n, board) == reference(m, n, board), (m, n, board)

    for board in (["A" * 30] * 30, ["".join(random.choice("AB") for _ in range(30)) for _ in range(30)]):
        start = time.time()
        solution(30, 30, board)
        print(f"30×30: {time.time() - start:.3f}s")
    print("all tests passed")
