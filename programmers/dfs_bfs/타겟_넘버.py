"""프로그래머스 Lv.2 타겟 넘버 (DFS)
https://school.programmers.co.kr/learn/courses/30/lessons/43165

접근: dfs(i, total)은 i번째 숫자 앞까지 부호를 정했고 합이 total일 때, 끝까지 가서 target이 되는 경우의 수다.
      숫자를 다 쓰면 total == target인지로 1 또는 0을 리턴하고, 아니면 +와 - 두 갈래의 결과를 더해 리턴한다.
시간 복잡도: O(2^n). n <= 20이라 약 100만 가지
"""
import random
import time
from itertools import product


def solution(numbers, target):

    def dfs(i, total):
        if i == len(numbers):
            if total == target:
                return 1
            else:
                return 0
        return dfs(i+1, total + numbers[i]) + dfs(i+1, total - numbers[i])

    answer = dfs(0, 0)
    return answer


def brute_force(numbers, target):
    return sum(sum(s * x for s, x in zip(signs, numbers)) == target
               for signs in product([1, -1], repeat=len(numbers)))


if __name__ == "__main__":
    assert solution([1, 1, 1, 1, 1], 3) == 5
    assert solution([4, 1, 2, 1], 4) == 2
    assert solution([1, 1], 0) == 2
    assert solution([1, 2], 100) == 0          # 만들 수 없는 target

    random.seed(0)
    for _ in range(2000):
        nums = [random.randint(1, 50) for _ in range(random.randint(2, 10))]
        t = max(1, sum(random.choice([1, -1]) * x for x in nums))
        assert solution(nums, t) == brute_force(nums, t), (nums, t)

    big = [random.randint(1, 50) for _ in range(20)]
    start = time.time()
    solution(big, 100)
    print(f"n=20: {time.time() - start:.2f}s")
    print("all tests passed")
