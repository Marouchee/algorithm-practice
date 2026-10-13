"""프로그래머스 Lv.2 피로도 (완전탐색)
https://school.programmers.co.kr/learn/courses/30/lessons/87946

접근: 던전 번호 0~n-1의 모든 순서(permutations)를 만들고, 순서마다 남은 피로도로 들어갈 수 있는 동안 차례로 탐험한다.
      못 들어가는 던전이 나오면 break한다. 그 뒤 순서는 다른 순열에서 이미 확인하므로 건너뛰어도 최댓값이 같다.
시간 복잡도: O(n! · n). n ≤ 8이면 40,320 × 8 ≈ 32만 번
"""
import random
import time
from itertools import permutations


def solution(k, dungeons):
    answer = -1

    temp_list = []
    for i in range(len(dungeons)):
        temp_list.append(i)

    perm = permutations(temp_list)

    for item in perm:
        temp_k = k
        temp_ans = 0
        for j in item:
            if dungeons[j][0] <= temp_k:
                temp_k = temp_k - dungeons[j][1]
                temp_ans += 1
            else:
                break
        if temp_ans > answer:
            answer = temp_ans

    return answer


def by_dfs(k, dungeons):
    """방문 표시 + 재귀로, 지금 들어갈 수 있는 던전만 골라 내려간다 (비교용)"""
    used = [False] * len(dungeons)

    def go(left):
        best = 0
        for i, (need, cost) in enumerate(dungeons):
            if not used[i] and need <= left:
                used[i] = True
                best = max(best, 1 + go(left - cost))
                used[i] = False
        return best

    return go(k)


if __name__ == "__main__":
    assert solution(80, [[80,20],[50,40],[30,10]]) == 3
    assert solution(1, [[2, 1]]) == 0                       # 하나도 못 들어감
    assert solution(10, [[10, 10]]) == 1                    # 피로도가 정확히 0으로 끝남
    assert solution(50, [[40, 30], [10, 10], [10, 10]]) == 3   # 큰 것 먼저면 3개, 작은 것 먼저면 2개
    assert solution(50, [[10, 10], [10, 10], [40, 30]]) == 3   # 입력 순서대로 돌면 2개라 순서를 바꿔야 함

    random.seed(0)
    for _ in range(2000):
        n = random.randint(1, 6)
        dungeons = []
        for _ in range(n):
            cost = random.randint(1, 30)
            dungeons.append([random.randint(cost, 40), cost])
        k = random.randint(1, 80)
        assert solution(k, dungeons) == by_dfs(k, dungeons), (k, dungeons)

    big = [[random.randint(500, 1000), random.randint(1, 500)] for _ in range(8)]
    start = time.time()
    assert solution(5000, big) == by_dfs(5000, big)
    print(f"n=8: {time.time() - start:.3f}s")
    print("all tests passed")
