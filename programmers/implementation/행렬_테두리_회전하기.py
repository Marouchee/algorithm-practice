"""프로그래머스 Lv.2 행렬 테두리 회전하기 (구현, 격자)
https://school.programmers.co.kr/learn/courses/30/lessons/77485

접근: 쿼리마다 테두리 칸 좌표를 왼쪽 위에서 시계 방향으로 circuit_list에 담는다
      (위 → 오른쪽 → 아래 → 왼쪽, 왼쪽 변은 x2-x1-1칸만 돌아 시작 칸이 두 번 들어가지 않게 한다).
      그 순서로 값을 vals에 담고, k번째 칸에 vals[k-1]을 넣는다 (k=0이면 vals[-1], 마지막 값).
      옮긴 값 vals의 최솟값을 answer에 쌓는다.
시간 복잡도: O(nm + k(n + m)). n = rows, m = columns, k = len(queries).
             행렬 만들기 nm, 쿼리마다 테두리 최대 2n + 2m - 4칸을 두 번(값 담기, 옮기기) 돈다
"""
import random
import time


def solution(rows, columns, queries):
    answer = []
    n = rows
    m = columns
    board = []
    for i in range(n):
        board.append([])
        for j in range(m):
            board[i].append(i*m + j + 1)

    for query in queries:
        circuit_list = []
        x1 = query[0]-1
        y1 = query[1]-1
        x2 = query[2]-1
        y2 = query[3]-1
        tmp_x = x1
        tmp_y = y1
        circuit_list.append((x1,y1))
        for _ in range(y2-y1):
            tmp_y += 1
            circuit_list.append((tmp_x,tmp_y))
        for _ in range(x2-x1):
            tmp_x += 1
            circuit_list.append((tmp_x,tmp_y))
        for _ in range(y2-y1):
            tmp_y -= 1
            circuit_list.append((tmp_x,tmp_y))
        for _ in range(x2-x1-1):
            tmp_x -= 1
            circuit_list.append((tmp_x,tmp_y))

        vals = []
        for x,y in circuit_list:
            vals.append(board[x][y])
        x,y = circuit_list[0]
        board[x][y] = vals[-1]
        for i in range(1,len(circuit_list)):
            x,y = circuit_list[i]
            board[x][y] = vals[i-1]
        answer.append(min(vals))

    return answer


def reference(rows, columns, queries):
    """비교용: 복사본에서 테두리 칸마다 '어느 칸에서 오는지'를 직접 계산한다"""
    b = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    out = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        old = [row[:] for row in b]
        moved = []
        for r in range(x1, x2 + 1):
            for c in range(y1, y2 + 1):
                if r not in (x1, x2) and c not in (y1, y2):
                    continue
                if r == x1 and c > y1:
                    src = (r, c - 1)        # 위 변: 왼쪽에서 온다
                elif c == y2 and r > x1:
                    src = (r - 1, c)        # 오른쪽 변: 위에서 온다
                elif r == x2 and c < y2:
                    src = (r, c + 1)        # 아래 변: 오른쪽에서 온다
                else:
                    src = (r + 1, c)        # 왼쪽 변: 아래에서 온다
                b[r][c] = old[src[0]][src[1]]
                moved.append(b[r][c])
        out.append(min(moved))
    return out


if __name__ == "__main__":
    assert solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]) == [8, 10, 25]
    assert solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]) == [1, 1, 5, 3]
    assert solution(100, 97, [[1, 1, 100, 97]]) == [1]
    assert solution(3, 4, [[1, 1, 2, 2], [2, 3, 3, 4]]) == [1, 7]     # 겹치지 않는 두 회전

    random.seed(0)
    for _ in range(3000):
        r, c = random.randint(2, 8), random.randint(2, 8)
        qs = []
        for _ in range(random.randint(1, 15)):
            x1, x2 = sorted(random.sample(range(1, r + 1), 2))
            y1, y2 = sorted(random.sample(range(1, c + 1), 2))
            qs.append([x1, y1, x2, y2])
        assert solution(r, c, qs) == reference(r, c, qs), (r, c, qs)

    start = time.time()
    solution(100, 100, [[1, 1, 100, 100]] * 10000)
    print(f"100x100, 가장 큰 테두리 10,000번: {time.time() - start:.2f}s")
    print("all tests passed")
