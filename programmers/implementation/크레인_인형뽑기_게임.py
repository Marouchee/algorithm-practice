"""프로그래머스 Lv.1 크레인 인형뽑기 게임 (구현, 스택)
https://school.programmers.co.kr/learn/courses/30/lessons/64061

접근: moves의 열마다 위에서부터 내려가 처음 만나는 인형을 꺼내 바구니(deque)에 넣고 그 칸을 0으로 만든다.
      넣은 뒤 바구니 맨 위 두 개(q[top-1], q[top-2])가 같으면 둘 다 꺼내고 2개를 센다. 꺼낸 인형이 있으면 바로 break한다.
시간 복잡도: O(M · N). M은 moves 길이(최대 1,000), N은 격자 크기(최대 30)
"""
import copy
import random
import time
from collections import deque


def solution(board, moves):
    answer = 0
    top = 0

    q = deque([])
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] == 0:
                continue
            q.append(board[i][m-1])
            top = top + 1
            board[i][m-1] = 0

            if top >= 2:
                if q[top-1] == q[top-2]:
                    q.pop()
                    q.pop()
                    top = top - 2
                    answer = answer + 2

            break

    return answer


def by_column_stacks(board, moves):
    """열마다 인형 리스트를 미리 만들어 두고 pop하는 방식 (비교용)"""
    n = len(board)
    cols = [[board[r][c] for r in range(n - 1, -1, -1) if board[r][c]] for c in range(n)]
    basket, popped = [], 0
    for m in moves:
        if not cols[m - 1]:
            continue
        doll = cols[m - 1].pop()
        if basket and basket[-1] == doll:
            basket.pop()
            popped += 2
        else:
            basket.append(doll)
    return popped


def make_board(n, kinds):
    board = [[0] * n for _ in range(n)]
    for c in range(n):
        height = random.randint(0, n)
        for r in range(n - height, n):
            board[r][c] = random.randint(1, kinds)
    return board


if __name__ == "__main__":
    ex = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    assert solution(ex, [1,5,3,5,1,2,1,4]) == 4
    assert solution([[0] * 5 for _ in range(5)], [1, 2, 3]) == 0          # 빈 격자
    assert solution([[0,0],[1,0]], [1, 1]) == 0                           # 빈 열을 다시 뽑아도 바구니 변화 없음
    assert solution([[1,0],[1,0]], [1, 1]) == 2                           # 같은 열에서 연속으로 같은 인형
    assert solution([[0,0,0],[1,2,0],[1,2,0]], [1, 2, 2, 1]) == 4         # 터진 뒤 아래에 있던 인형끼리 다시 맞음

    random.seed(0)
    for _ in range(3000):
        n = random.randint(1, 6)
        board = make_board(n, random.randint(1, 3))
        moves = [random.randint(1, n) for _ in range(random.randint(1, 20))]
        assert solution(copy.deepcopy(board), moves) == by_column_stacks(board, moves), (board, moves)

    big = make_board(30, 100)
    big_moves = [random.randint(1, 30) for _ in range(1000)]
    start = time.time()
    assert solution(copy.deepcopy(big), big_moves) == by_column_stacks(big, big_moves)
    print(f"30x30, moves 1000: {time.time() - start:.3f}s")
    print("all tests passed")
