"""프로그래머스 Lv.2 H-Index (정렬)
https://school.programmers.co.kr/learn/courses/30/lessons/42747

접근: 내림차순 정렬하면 인덱스 i까지 i+1편이 모두 citations[i]번 이상 인용됐다.
      h = i+1은 citations[i] >= i+1일 때 성립하므로, 처음 citations[i] < i+1이 되는 i가 답이다.
      끝까지 성립하면 논문 수가 답이다.
시간 복잡도: O(n log n). 정렬이 지배한다
"""
import random


def solution(citations):
    citations = sorted(citations, reverse = True)

    for i in range(len(citations)):
        if citations[i] < i+1:
            return i

    return len(citations)


def brute_force(citations):
    return max(h for h in range(len(citations) + 1)
               if sum(c >= h for c in citations) >= h)


if __name__ == "__main__":
    assert solution([10, 8, 5, 4, 3]) == 4
    assert solution([10, 8, 5]) == 3          # 끝까지 성립 → 논문 수
    assert solution([10, 8, 1]) == 2          # <= 로 쓰면 3이 나오는 반례
    assert solution([1, 1, 1]) == 1           # < i 로 쓰면 2가 나오는 반례
    assert solution([0]) == 0
    assert solution([0, 0, 0]) == 0
    assert solution([10000] * 1000) == 1000

    random.seed(0)
    for _ in range(5000):
        c = [random.randint(0, 12) for _ in range(random.randint(1, 10))]
        assert solution(c) == brute_force(c), c
    print("all tests passed")
