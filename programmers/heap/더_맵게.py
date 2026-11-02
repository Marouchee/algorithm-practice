"""프로그래머스 Lv.2 더 맵게 (힙)
https://school.programmers.co.kr/learn/courses/30/lessons/42626

접근: 모든 값을 최소 힙에 넣고, 가장 작은 값을 꺼낸다.
      K 이상이면 나머지도 모두 K 이상이므로 지금까지 섞은 횟수를 반환한다.
      K 미만이면 두 번째로 작은 값을 꺼내 (가장 작은 값 + 두 번째 × 2)를 다시 넣고 횟수를 1 늘린다.
      힙에 하나만 남았는데 K 미만이면 더 섞을 수 없으므로 -1.
      입력 리스트는 정렬돼 있지 않으므로 heappop 전에 반드시 힙으로 만들어야 한다.
시간 복잡도: 힙 만들기 n log n (heappush n번. heapify를 쓰면 O(n))
            + 섞기 최대 n − 1번 × (heappop 2번 + heappush 1번) = 3n log n → O(n log n)
"""
import heapq
import random
import time


def solution(scoville, K):
    answer = 0
    count = 0
    heap_sco = []
    for item in scoville:
        heapq.heappush(heap_sco, item)
    while True:
        if len(heap_sco) == 1:
            a = heapq.heappop(heap_sco)
            if a < K:
                answer = -1
                break
            else:
                answer = count
                break
        a = heapq.heappop(heap_sco)
        if a < K:
            temp = a + (heapq.heappop(heap_sco)*2)
            heapq.heappush(heap_sco, temp)
            count += 1
        else:
            answer = count
            break

    return answer


def reference(scoville, K):
    """비교용: 정렬된 리스트에서 매번 가장 작은 두 값을 꺼내 섞고 다시 정렬한다 (작은 입력 전용)"""
    s = sorted(scoville)
    count = 0
    while s[0] < K:
        if len(s) == 1:
            return -1
        s = sorted(s[2:] + [s[0] + s[1] * 2])
        count += 1
    return count


if __name__ == "__main__":
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2
    assert solution([1, 2, 3], 11) == 2
    assert solution([1, 1], 100) == -1             # 하나만 남았는데 K 미만
    assert solution([5, 1, 3], 4) == 1             # 정렬 안 된 입력: 힙으로 만들지 않으면 5를 먼저 꺼냄
    assert solution([0, 0], 1) == -1               # 0끼리 섞으면 계속 0
    assert solution([3, 5], 0) == 0                # 처음부터 모두 K 이상

    random.seed(0)
    for _ in range(3000):
        s = [random.randint(0, 10) for _ in range(random.randint(2, 7))]
        K = random.randint(0, 40)
        assert solution(s, K) == reference(s, K), (s, K)

    big = [random.randint(0, 1000000) for _ in range(1000000)]
    start = time.time()
    solution(big, 1000000000)
    print(f"100만 개: {time.time() - start:.2f}s")
    print("all tests passed")
