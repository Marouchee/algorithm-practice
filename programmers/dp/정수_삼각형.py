"""프로그래머스 Lv.3 정수 삼각형 (DP)
https://school.programmers.co.kr/learn/courses/30/lessons/43105

접근: ans_list[i][j] = 꼭대기에서 (i, j)까지 내려왔을 때의 최대 합.
      위에서 들어오는 칸 (i-1, j-1), (i-1, j) 중 큰 값 + 자기 값. 양 끝(j == 0, j == i)은 들어오는 칸이 하나뿐이다.
      정답은 마지막 줄의 최댓값. (모의고사 때는 모든 경로를 DFS로 돌아 2^(n-1)개 경로에서 시간 초과)
시간 복잡도: O(n²). 안쪽 반복이 줄마다 2, 3, …, n번이라 합이 약 n²/2. n = 500이면 약 12만 5천 번
"""
import random
import sys
import time

sys.setrecursionlimit(10**6)


def solution(triangle):
    answer = 0
    n = len(triangle)
    ans_list=[[triangle[0][0]]]

    for i in range(1,n):
        ans_list.append([])
        for j in range(len(triangle[i])):
            if j == 0:
                ans_list[i].append(ans_list[i-1][0] + triangle[i][0])
            elif j == len(triangle[i]) - 1:
                ans_list[i].append(ans_list[i-1][j-1] + triangle[i][j])
            else:
                ans_list[i].append(max(ans_list[i-1][j-1] + triangle[i][j], ans_list[i-1][j] + triangle[i][j]))
    m = len(ans_list)
    answer = max(ans_list[m-1])

    return answer


def bottom_up(triangle):
    """맨 아래 줄에서 위로 올라가며 두 자식 중 큰 값을 더하는 방식 (비교용). 양 끝 예외가 없다"""
    row = triangle[-1][:]
    for i in range(len(triangle) - 2, -1, -1):
        row = [triangle[i][j] + max(row[j], row[j + 1]) for j in range(i + 1)]
    return row[0]


def all_paths(triangle):
    """모든 경로를 재귀로 확인 (작은 입력 검증용, O(2^n))"""
    def go(i, j):
        if i == len(triangle):
            return 0
        return triangle[i][j] + max(go(i + 1, j), go(i + 1, j + 1))
    return go(0, 0)


def make_triangle(n):
    return [[random.randint(0, 9999) for _ in range(i + 1)] for i in range(n)]


if __name__ == "__main__":
    assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30
    assert solution([[5]]) == 5                      # 한 줄
    assert solution([[1], [2, 3], [4, 5, 6]]) == 10  # 오른쪽 끝 칸은 위 오른쪽 끝에서만 들어옴 (4 + 6)
    assert solution([[0], [0, 0], [0, 0, 0]]) == 0   # 전부 0

    random.seed(0)
    for _ in range(3000):
        t = make_triangle(random.randint(1, 10))
        assert solution(t) == bottom_up(t) == all_paths(t), t

    big = make_triangle(500)
    start = time.time()
    assert solution(big) == bottom_up(big)
    print(f"n=500: {time.time() - start:.3f}s")
    print("all tests passed")
