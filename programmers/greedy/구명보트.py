"""프로그래머스 Lv.2 구명보트 (그리디, 투 포인터)
https://school.programmers.co.kr/learn/courses/30/lessons/42885

접근: 몸무게를 정렬하고 left(가장 가벼운 사람), right(가장 무거운 사람)를 양끝에 둔다.
      둘의 합이 limit 이하면 같이 태우고 둘 다 안쪽으로, 아니면 가장 무거운 사람만 혼자 태운다.
      가장 가벼운 사람과도 못 타는 사람은 누구와도 못 탄다. 한 명 남은 경우(left == right)도 보트가 필요해 <=.
      pop(0)으로 빼면 한 번에 O(n)이라 위치만 옮긴다.
시간 복잡도: O(n log n). 정렬 n log n + 투 포인터 n
"""
import random
import time
from functools import lru_cache


def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1
    sorted_people = sorted(people)
    while left <= right:
        if sorted_people[right] + sorted_people[left] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1

    return answer


def brute(people, limit):
    """비교용: 남은 사람 집합(비트마스크)마다 최소 보트 수를 전부 계산한다"""
    n = len(people)

    @lru_cache(maxsize=None)
    def go(mask):
        if mask == 0:
            return 0
        i = (mask & -mask).bit_length() - 1        # 남은 사람 중 번호가 가장 작은 사람
        rest = mask & ~(1 << i)
        best = 1 + go(rest)                         # 혼자 탄다
        for j in range(n):
            if rest >> j & 1 and people[i] + people[j] <= limit:
                best = min(best, 1 + go(rest & ~(1 << j)))
        return best

    return go((1 << n) - 1)


if __name__ == "__main__":
    assert solution([70, 50, 80, 50], 100) == 3
    assert solution([70, 80, 50], 100) == 3
    assert solution([40, 50, 60], 100) == 2      # 한 명 남는 경우 (left == right)
    assert solution([40, 45, 55, 60], 110) == 2
    assert solution([100], 100) == 1

    random.seed(0)
    for _ in range(3000):
        limit = random.randint(40, 240)
        people = [random.randint(40, limit) for _ in range(random.randint(1, 9))]
        assert solution(people, limit) == brute(people, limit), (people, limit)

    big = [random.randint(40, 240) for _ in range(50000)]
    start = time.time()
    solution(big, 240)
    print(f"5만 명: {time.time() - start:.3f}s")
    print("all tests passed")
