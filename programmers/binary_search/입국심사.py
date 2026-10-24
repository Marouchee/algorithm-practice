"""프로그래머스 Lv.3 입국심사 (이분탐색)
https://school.programmers.co.kr/learn/courses/30/lessons/43238

접근: 시간 T가 정해지면 T분 동안 끝낼 수 있는 사람 수는 심사관마다 T // time을 더한 값이고,
      T가 커지면 이 수는 줄어들지 않는다. 그래서 1 ~ 10**18(심사관 1명, 10억 분, 10억 명) 사이를
      이분탐색해 사람 수가 n 이상이 되는 가장 작은 T를 찾는다.
      n 이상이면 가운데 값을 정답 후보로 저장하고 작은 쪽, 모자라면 큰 쪽에서 계속 찾고 start > end에서 멈춘다.
      (사람 수는 한 번에 여러 명씩 늘 수 있어 "n과 같을 때"를 조건으로 쓰면 안 된다)
시간 복잡도: O(m · log(10**18)), m = len(times). 반복 약 60번, 반복마다 심사관 m명을 더한다
"""
import heapq
import random
import time


def solution(n, times):
    answer = 0
    start = 1
    end = 10**18

    while start <= end:
        count = 0
        mid = (start+end)//2
        for time in times:
            count = count + (mid//time)
        if n <= count:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer


def simulate(n, times):
    """한 사람씩 가장 빨리 끝나는 심사대로 보낸다 (비교용, O(n log m))"""
    desks = [(t, t) for t in times]   # (이 심사대에서 다음 사람이 끝나는 시각, 심사 시간)
    heapq.heapify(desks)
    last = 0
    for _ in range(n):
        finish, t = heapq.heappop(desks)
        last = finish
        heapq.heappush(desks, (finish + t, t))
    return last


if __name__ == "__main__":
    assert solution(6, [7, 10]) == 28
    assert solution(3, [5, 5]) == 10              # 사람 수가 2에서 4로 건너뛰어 정확히 3인 T가 없음
    assert solution(2, [1, 1]) == 1               # 정답이 n * len(times)보다 작음
    assert solution(1, [10**9]) == 10**9
    assert solution(10**9, [10**9]) == 10**18     # 답의 최댓값

    random.seed(0)
    for _ in range(3000):
        times = [random.randint(1, 20) for _ in range(random.randint(1, 6))]
        n = random.randint(1, 60)
        assert solution(n, times) == simulate(n, times), (n, times)

    big = [random.randint(1, 10**9) for _ in range(100000)]
    start = time.time()
    solution(10**9, big)
    print(f"n=10억, 심사관 10만 명: {time.time() - start:.2f}s")
    print("all tests passed")
