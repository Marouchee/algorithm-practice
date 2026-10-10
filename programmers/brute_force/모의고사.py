"""프로그래머스 Lv.1 모의고사 (완전탐색)
https://school.programmers.co.kr/learn/courses/30/lessons/42840

접근: i번 문제에 수포자가 찍는 답은 pattern[i % len(pattern)]이다. 정답과 비교해 맞힌 개수를 세고,
      최고점과 점수가 같은 사람을 1, 2, 3 순서로 모은다 (순서대로 모으므로 정렬이 필요 없다).
시간 복잡도: O(n). n은 문제 수
"""
import random
import time


def solution(answers):
    ans = []

    ans_cnt = {1: 0, 2: 0, 3: 0}

    pattern_1 = [1, 2, 3, 4, 5]
    len_p1 = len(pattern_1)
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    len_p2 = len(pattern_2)
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    len_p3 = len(pattern_3)

    for i in range(len(answers)):
        if answers[i] == pattern_1[i % len_p1]:
            ans_cnt[1] += 1
        if answers[i] == pattern_2[i % len_p2]:
            ans_cnt[2] += 1
        if answers[i] == pattern_3[i % len_p3]:
            ans_cnt[3] += 1

    max_val = max(ans_cnt.values())
    for i in range(1, 4):
        if ans_cnt[i] == max_val:
            ans.append(i)

    return ans


def brute_force(answers):
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [sum(a == p[i % len(p)] for i, a in enumerate(answers)) for p in patterns]
    return [k + 1 for k in range(3) if scores[k] == max(scores)]


if __name__ == "__main__":
    assert solution([1, 2, 3, 4, 5]) == [1]
    assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]
    assert solution([1]) == [1]                   # 문제 1개
    assert solution([4]) == [1, 2, 3]             # 모두 0점이면 전원 동점

    random.seed(0)
    for _ in range(5000):
        a = [random.randint(1, 5) for _ in range(random.randint(1, 30))]
        assert solution(a) == brute_force(a), a

    big = [random.randint(1, 5) for _ in range(10000)]
    start = time.time()
    solution(big)
    print(f"n=10,000: {time.time() - start:.4f}s")
    print("all tests passed")
