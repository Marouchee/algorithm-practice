"""프로그래머스 Lv.2 기능개발 (스택/큐)
https://school.programmers.co.kr/learn/courses/30/lessons/42586

접근: 진도와 속도를 deque 두 개에 넣고 하루씩 진행한다. 매일 남은 기능 전부에 속도를 더한 뒤,
      맨 앞이 100 이상인 동안 두 큐를 같이 popleft()하며 센다. 센 값이 0보다 크면 그날 배포 개수로 기록한다.
      (처음에는 `while q_p[0] >= 100`만 써서 마지막 기능을 꺼낸 뒤 빈 큐를 읽어 IndexError. `q_p and`를 앞에 붙여 해결)
시간 복잡도: O(n · D). n은 기능 수, D는 걸리는 날 수(진도 ≥ 1, 속도 ≥ 1이라 최대 99일). 제한에서 약 1만 번
"""
import math
import random
import time
from collections import deque


def solution(progresses, speeds):
    answer = []
    q_p = deque(progresses)
    q_s = deque(speeds)

    while q_p:
        count = 0
        for i in range(len(q_p)):
            q_p[i] += q_s[i]
        while q_p and q_p[0] >= 100:
            q_p.popleft()
            q_s.popleft()
            count += 1
        if count > 0:
            answer.append(count)

    return answer


def by_finish_day(progresses, speeds):
    """기능마다 끝나는 날을 바로 계산하고, 앞 기능보다 늦게 끝나는 기능이 나올 때마다 새 배포를 연다 (비교용, O(n))"""
    answer = []
    release_day = 0
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        if day > release_day:
            answer.append(1)
            release_day = day
        else:
            answer[-1] += 1
    return answer


if __name__ == "__main__":
    assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
    assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]
    assert solution([40, 90, 70], [20, 5, 30]) == [3]          # 뒤 기능이 먼저 끝나도 앞 기능을 기다림
    assert solution([1], [1]) == [1]                           # 99일 걸리는 기능 하나
    assert solution([99, 1], [1, 100]) == [2]                  # 같은 날 끝나는 두 기능

    random.seed(0)
    for _ in range(3000):
        n = random.randint(1, 10)
        progresses = [random.randint(1, 99) for _ in range(n)]
        speeds = [random.randint(1, 100) for _ in range(n)]
        assert solution(progresses, speeds) == by_finish_day(progresses, speeds), (progresses, speeds)

    big_p = [1] * 100
    big_s = [1] * 100
    start = time.time()
    assert solution(big_p, big_s) == [100]
    print(f"n=100, 99일: {time.time() - start:.3f}s")
    print("all tests passed")
