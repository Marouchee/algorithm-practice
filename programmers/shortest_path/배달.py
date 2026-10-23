"""프로그래머스 Lv.2 배달 (다익스트라)
https://school.programmers.co.kr/learn/courses/30/lessons/12978

접근: 아직 확정 안 된 마을 중 지금 알려진 거리가 가장 작은 마을을 heapq로 꺼내 확정하고,
      그 마을의 도로로 이웃 거리를 min으로 갱신한다. 이미 더 짧은 거리로 확정된 마을이 다시 나오면 건너뛴다.
      도로는 양방향이라 그래프에 두 번 넣는다. 1번 마을(거리 0)도 개수에 포함한다.
      (가중치가 다른 그래프라 BFS의 "처음 도착 = 최단"이 성립하지 않는다)
시간 복잡도: O(E log E). 마을마다 도로를 한 번씩만 처리해 push가 최대 2E번이고 push·pop이 각각 O(log 힙 크기)
"""
import heapq
import random
import time


def solution(N, roads, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    for a,b,c in roads:
        graph[a].append([b,c])
        graph[b].append([a,c])

    distance = [500001]*(N+1)

    q=[]
    distance[1] = 0
    heapq.heappush(q, (0,1))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1

    return answer


def floyd(N, roads, K):
    """모든 쌍 최단 거리 (비교용, O(N³))"""
    INF = float("inf")
    d = [[0 if i == j else INF for j in range(N + 1)] for i in range(N + 1)]
    for a, b, c in roads:
        d[a][b] = d[b][a] = min(d[a][b], c)
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return sum(1 for j in range(1, N + 1) if d[1][j] <= K)


def make_roads(n, e):
    roads = [[i, random.randint(1, i - 1), random.randint(1, 10000)] for i in range(2, n + 1)]   # 연결 보장
    while len(roads) < e:
        a, b = random.sample(range(1, n + 1), 2)
        roads.append([a, b, random.randint(1, 10000)])   # 같은 두 마을 사이 도로가 여러 개일 수 있음
    return roads


if __name__ == "__main__":
    assert solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3) == 4
    assert solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4) == 4
    assert solution(1, [], 1) == 1                                    # 1번 마을만
    assert solution(3, [[1, 2, 5], [1, 3, 1], [3, 2, 1]], 2) == 3       # 직접 도로(5)보다 돌아가는 길(2)
    assert solution(2, [[1, 2, 7], [1, 2, 3]], 3) == 2                  # 같은 두 마을 사이 도로 여러 개
    assert solution(4, [[1,3,3],[1,4,8],[3,2,2],[3,4,1]], 4) == 3       # (8, 4)가 힙에 남아 건너뛰는 경우

    random.seed(0)
    for _ in range(2000):
        n = random.randint(2, 12)
        roads = make_roads(n, random.randint(max(n - 1, 0), 30))
        k = random.randint(1, 30000)
        assert solution(n, roads, k) == floyd(n, roads, k), (n, roads, k)

    big = make_roads(50, 2000)
    start = time.time()
    assert solution(50, big, 500000) == floyd(50, big, 500000)
    print(f"N=50, 2,000 roads: {time.time() - start:.3f}s")
    print("all tests passed")
