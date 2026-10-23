"""프로그래머스 Lv.3 야근 지수 (힙)
https://school.programmers.co.kr/learn/courses/30/lessons/12927

접근: 제곱의 합을 줄이려면 매시간 가장 큰 남은 작업량을 1 줄인다.
      heapq는 최소 힙이라 음수로 넣어 최대 힙으로 쓰고, 꺼낸 값이 0이면 남은 일이 없으니 멈춘다.
시간 복잡도: O((W + n) log W), W = len(works). 처음 push W번, 시간마다 pop·push 한 번씩이고
             힙 크기는 항상 W라 연산마다 O(log W)
"""
import heapq
import random
import time


def solution(n, works):
    answer = 0
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, -1 * work)

    for _ in range(n):
        x = heapq.heappop(max_heap)
        if x == 0:
            break
        x += 1
        heapq.heappush(max_heap, x)

    while max_heap:
        tmp = -1 * heapq.heappop(max_heap)
        answer = answer + tmp**2

    return answer


def brute(n, works):
    """시간마다 max()로 가장 큰 작업을 찾아 1 줄인다 (비교용, O(n · W))"""
    w = list(works)
    for _ in range(n):
        i = w.index(max(w))
        if w[i] == 0:
            break
        w[i] -= 1
    return sum(x * x for x in w)


if __name__ == "__main__":
    assert solution(4, [4, 3, 3]) == 12
    assert solution(1, [2, 1, 2]) == 6
    assert solution(3, [1, 1]) == 0
    assert solution(1, [1]) == 0                    # 딱 맞게 끝남
    assert solution(10, [5]) == 0                   # 시간이 남음
    assert solution(2, [7, 7, 7]) == 36 + 36 + 49   # 같은 값이 여러 개

    random.seed(0)
    for _ in range(2000):
        works = [random.randint(1, 30) for _ in range(random.randint(1, 8))]
        n = random.randint(1, 200)
        assert solution(n, works) == brute(n, works), (n, works)

    start = time.time()
    solution(1000000, [50000] * 20000)
    print(f"n=1,000,000, works 20,000: {time.time() - start:.2f}s")
    print("all tests passed")
