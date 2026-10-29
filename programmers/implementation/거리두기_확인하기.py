"""프로그래머스 Lv.2 거리두기 확인하기 (구현, 격자)
https://school.programmers.co.kr/learn/courses/30/lessons/81302

접근: 대기실마다 P인 칸에서 맨해튼 거리 2 이내의 12칸을 본다. 범위 밖(0 미만, 4 초과)은 건너뛴다.
      거리 1(line_1)에 P가 있으면 위반. 거리 2 일직선(line_2)은 가운데 칸이 X가 아니면 위반.
      거리 2 대각선(line_2_sq)은 사이의 두 칸이 "둘 다 X"여야 지킴이므로, 하나라도 X가 아니면(or) 위반.
      위반이 나오면 flag = 0으로 두고 그 대기실 검사를 끝낸다.
시간 복잡도: O(대기실 수 × 칸 수 × 12) = 5 × 25 × 12 = 1,500번. 세 방향 목록은 차례로(중첩 아님) 돈다
"""
import random
from collections import deque


def solution(places):
    answer = []

    line_1 = [(1,0),(-1,0),(0,1),(0,-1)]
    line_2 = [(2,0),(-2,0),(0,2),(0,-2)]
    line_2_sq = [(1,1),(-1,1),(-1,-1),(1,-1)]
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    for a,b in line_1:
                        x = i+a
                        y = j+b
                        if x<0 or y<0 or x>4 or y>4:
                            continue
                        if place[x][y] == "P":
                            flag = 0
                            break
                    for a,b in line_2:
                        x = i+a
                        y = j+b
                        if x<0 or y<0 or x>4 or y>4:
                            continue
                        if place[x][y] == "P":
                            if place[x-a//2][y-b//2] != "X":
                                flag = 0
                                break
                    for a,b in line_2_sq:
                        x = i+a
                        y = j+b
                        if x<0 or y<0 or x>4 or y>4:
                            continue
                        if place[x][y] == "P":
                            if place[x-a][y] != "X" or place[x][y-b] != "X":
                                flag = 0
                                break
            if flag == 0:
                break
        if flag == 1:
            answer.append(1)
        else:
            answer.append(0)
    return answer


def reference(places):
    """비교용: P마다 X를 벽으로 두고 BFS, 거리 2 안에 다른 P가 닿으면 위반"""
    out = []
    for g in places:
        ok = 1
        for si in range(5):
            for sj in range(5):
                if g[si][sj] != "P":
                    continue
                dist = {(si, sj): 0}
                q = deque([(si, sj)])
                while q:
                    i, j = q.popleft()
                    if dist[(i, j)] == 2:
                        continue
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 5 and 0 <= nj < 5 and (ni, nj) not in dist and g[ni][nj] != "X":
                            dist[(ni, nj)] = dist[(i, j)] + 1
                            if g[ni][nj] == "P":
                                ok = 0
                            q.append((ni, nj))
        out.append(ok)
    return out


if __name__ == "__main__":
    example = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
               ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
               ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
               ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
               ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    assert solution(example) == [1, 0, 1, 1, 1]
    assert solution([["OPOOO", "PXOOO", "OOOOO", "OOOOO", "OOOOO"]]) == [0]   # 대각선, 사이 칸 하나만 X
    assert solution([["POOOO", "OOOOO", "POOOO", "OOOOO", "OOOOO"]]) == [0]   # 두 줄 아래 같은 열
    assert solution([["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOPP"]]) == [0]   # 오른쪽 아래 구석

    random.seed(0)
    for _ in range(5000):
        place = ["".join(random.choice("POX") for _ in range(5)) for _ in range(5)]
        assert solution([place]) == reference([place]), place
    print("all tests passed")
