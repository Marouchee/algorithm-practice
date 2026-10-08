"""프로그래머스 Lv.2 가장 큰 수 (정렬)
https://school.programmers.co.kr/learn/courses/30/lessons/42746

접근: 숫자를 문자열로 바꾸고, a + b > b + a이면 a를 앞에 두는 기준으로 정렬해 이어 붙인다.
      정렬 후 맨 앞이 "0"이면 전부 0이므로 "0"을 반환한다.
시간 복잡도: O(n log n). 비교 한 번은 최대 8글자 문자열 비교라 상수
"""
import random
import time
from functools import cmp_to_key
from itertools import permutations


def compare(a, b):
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0


def solution(numbers):
    ans_numbers = []

    for num in numbers:
        ans_numbers.append(str(num))

    ans_numbers.sort(key=cmp_to_key(compare))

    if ans_numbers[0] == "0":
        answer = "0"
    else:
        answer = "".join(ans_numbers)

    return answer


def brute_force(numbers):
    return str(max(int("".join(map(str, p))) for p in permutations(numbers)))


if __name__ == "__main__":
    assert solution([3, 30, 34]) == "34330"
    assert solution([5, 46]) == "546"                       # 마지막 자릿수 규칙의 반례
    assert solution([0, 0]) == "0"                          # "00"이 아니라 "0"
    assert solution([0, 1000]) == "10000"
    assert solution([10, 101]) == "10110"

    random.seed(0)
    for _ in range(1000):
        nums = [random.choice([0, random.randint(0, 9), random.randint(0, 1000)])
                for _ in range(random.randint(1, 6))]
        assert solution(nums) == brute_force(nums), nums

    big = [random.randint(0, 1000) for _ in range(100_000)]
    start = time.time()
    solution(big)
    print(f"n=100,000: {time.time() - start:.2f}s")
    print("all tests passed")
