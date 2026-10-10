"""프로그래머스 Lv.2 소수 찾기 (완전탐색)
https://school.programmers.co.kr/learn/courses/30/lessons/42839

접근: 길이 1부터 len(numbers)까지 모든 순열을 int("".join())로 바꿔 set에 넣는다 ("011"과 "11", 같은 숫자 중복 제거).
      set의 각 수가 0, 1이 아니고 2부터 isqrt(수)까지 나누어떨어지는 수가 없으면 소수로 센다.
시간 복잡도: O(P · √M). P는 순열 개수(n = 7이면 13,699개), M은 만들 수 있는 가장 큰 수(√9,999,999 ≈ 3,162)
"""
import random
import time
from math import isqrt
from itertools import permutations


def solution(numbers):
    ans = 0
    all_set = set()
    for i in range(1, len(numbers)+1):
        p_list = list(permutations(numbers,i))
        for item in p_list:
            all_set.add(int("".join(item)))

    for item in all_set:
        flag = 0
        if item == 0 or item == 1:
            continue
        for i in range(2, isqrt(item) + 1):
            if item % i == 0:
                flag = 1
                break
        if flag == 0:
            ans += 1

    return ans


def brute_force(numbers):
    made = {int("".join(p)) for r in range(1, len(numbers) + 1) for p in permutations(numbers, r)}
    return sum(1 for x in made if x > 1 and all(x % d for d in range(2, x)))


if __name__ == "__main__":
    assert solution("17") == 3
    assert solution("011") == 2
    assert solution("0") == 0                 # 0은 소수가 아님
    assert solution("1") == 0                 # 1은 소수가 아님
    assert solution("2") == 1
    assert solution("4") == 0                 # isqrt 끝값을 포함하지 않으면 4를 소수로 셈
    assert solution("9") == 0                 # 같은 이유로 9
    assert solution("00") == 0

    random.seed(0)
    for _ in range(300):
        s = "".join(random.choice("0123456789") for _ in range(random.randint(1, 4)))
        assert solution(s) == brute_force(s), s

    start = time.time()
    assert solution("1234567") == 1336
    print(f"n=7: {time.time() - start:.2f}s")
    print("all tests passed")
