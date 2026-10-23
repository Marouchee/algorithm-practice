"""프로그래머스 Lv.3 합승 택시 요금 (다익스트라)
https://school.programmers.co.kr/learn/courses/30/lessons/72413

접근: 합승을 끝내고 갈라지는 지점 i를 1~n 모두 시도해서 s→i + i→a + i→b의 최솟값을 구한다.
      거리는 다익스트라로 구한다. 도로는 양방향이라 그래프에 두 번 넣는다.
      최단 경로는 같은 지점을 두 번 지나지 않아 도로를 최대 n−1 = 199개 쓰므로 최단 요금은 최대 19,900,000.
      초깃값은 이보다 커야 한다 (100,001로 두면 요금이 클 때 갱신이 안 돼 오답).
시간 복잡도: O(n · E log E). 다익스트라 한 번이 O(E log E)이고 3n + 2번 부른다
"""
import heapq
import random
import time


def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]

    for i,j,k in fares:
        graph[i].append([j,k])
        graph[j].append([i,k])

    def dijkstra(start,end):
        q = []
        distance = [2_000_000_000]*(n+1)
        distance[start] = 0
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = i[1] + distance[now]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance[end]

    tmp = 2_000_000_000
    for i in range(1,n+1):
        sm = dijkstra(s,i) + dijkstra(i,a) + dijkstra(i,b)
        if tmp > sm:
            tmp = sm

    answer = min((dijkstra(s,a) + dijkstra(s,b)) , tmp)

    return answer


def floyd(n, s, a, b, fares):
    """모든 쌍 최단 거리 후 갈라지는 지점을 모두 시도 (비교용, O(n³))"""
    INF = float("inf")
    d = [[0 if i == j else INF for j in range(n + 1)] for i in range(n + 1)]
    for x, y, c in fares:
        d[x][y] = d[y][x] = c
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return min(d[s][k] + d[k][a] + d[k][b] for k in range(1, n + 1))


def make_fares(n, extra, max_fare):
    """무작위 신장 트리로 연결을 보장하고 도로를 extra개 더한다 (두 지점 사이 도로는 하나)"""
    edges = {}
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges[(u, v)] = random.randint(1, max_fare)
    for _ in range(extra * 3):
        if len(edges) >= n - 1 + extra:
            break
        u, v = sorted(random.sample(range(1, n + 1), 2))
        edges.setdefault((u, v), random.randint(1, max_fare))
    return [[u, v, c] for (u, v), c in edges.items()]


if __name__ == "__main__":
    assert solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]) == 82
    assert solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]) == 14
    assert solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]) == 18
    assert solution(3, 1, 3, 2, [[1, 2, 80000], [2, 3, 80000]]) == 160000          # 요금 합이 100,001을 넘음
    chain = [[i, i + 1, 100000] for i in range(1, 200)]
    assert solution(200, 1, 200, 199, chain) == 19_900_000                          # 최단 요금 최댓값

    random.seed(0)
    for max_fare in (100, 100000):
        for _ in range(500):
            n = random.randint(3, 12)
            fares = make_fares(n, random.randint(0, n), max_fare)
            s, a, b = random.sample(range(1, n + 1), 3)
            assert solution(n, s, a, b, fares) == floyd(n, s, a, b, fares), (n, s, a, b, fares)

    full = [[u, v, random.randint(1, 100000)] for u in range(1, 201) for v in range(u + 1, 201)]
    start = time.time()
    solution(200, 1, 2, 3, full)
    print(f"n=200, {len(full):,} fares: {time.time() - start:.2f}s")
    print("all tests passed")
