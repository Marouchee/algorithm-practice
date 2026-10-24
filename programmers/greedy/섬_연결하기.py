"""프로그래머스 Lv.3 섬 연결하기 (MST, 크루스칼)
https://school.programmers.co.kr/learn/courses/30/lessons/42861

접근: 다리를 비용 오름차순으로 정렬하고 차례로 놓되, 두 섬이 이미 같은 그룹이면 건너뛴다.
      섬마다 그룹 번호(group)를 두고, 다리를 놓으면 b 쪽 그룹 전체를 a의 그룹 번호로 바꾼다.
      바꾸는 도중 group[b]가 바뀌므로 비교할 옛 번호(old)를 반복 전에 저장한다.
시간 복잡도: O(E log E + E · n), E = len(costs). 정렬 + 다리마다 그룹 번호를 n칸 확인.
             n ≤ 100이라 충분하다 (n이 크면 유니온파인드로 합치기를 빠르게 해야 한다)

solution_union_find: 섬마다 가리키는 섬(parent)을 두고, 자기 자신을 가리키는 섬을 대표로 본다.
      합칠 때는 대표의 칸 하나만 바꾸고, find_parent는 따라간 섬들이 대표를 바로 가리키게 고친다(경로 압축).
      시간 복잡도: O(E log E). 정렬이 대부분이다 (섬 10만·다리 20만 0.3초 안팎)
      재귀 find는 사슬이 1,000단계를 넘으면 RecursionError → setrecursionlimit
"""
import random
import sys
import time

sys.setrecursionlimit(10**6)


def solution(n, costs):
    answer = 0

    group = []
    sorted_costs = sorted(costs, key=lambda x: x[2])
    for i in range(n):
        group.append(i)

    for a,b,c in sorted_costs:
        if group[a] == group[b]:
            continue
        old = group[b]
        answer += c
        for i in range(n):
            if group[i] == old:
                group[i] = group[a]

    return answer


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution_union_find(n, costs):
    answer = 0

    group = [i for i in range(n)]
    sorted_costs = sorted(costs, key=lambda x: x[2])

    for a,b,c in sorted_costs:
        if find_parent(group, a) != find_parent(group, b):
            union_parent(group,a,b)
            answer += c

    return answer


def prim(n, costs):
    """연결된 섬에서 가장 싼 다리로 섬을 하나씩 붙인다 (비교용, O(n · E))"""
    joined = {0}
    total = 0
    while len(joined) < n:
        best = min(c for a, b, c in costs if (a in joined) != (b in joined))
        for a, b, c in costs:
            if c == best and (a in joined) != (b in joined):
                joined |= {a, b}
                break
        total += best
    return total


def make_costs(n, extra):
    """무작위 신장 트리로 연결을 보장하고 다리를 extra개 더한다 (같은 연결은 한 번만)"""
    edges = {}
    for v in range(1, n):
        edges[(random.randint(0, v - 1), v)] = random.randint(1, 50)
    for _ in range(extra * 3):
        if len(edges) >= n - 1 + extra:
            break
        a, b = sorted(random.sample(range(n), 2))
        edges.setdefault((a, b), random.randint(1, 50))
    return [[a, b, c] for (a, b), c in edges.items()]


if __name__ == "__main__":
    assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4
    assert solution(4, [[0, 1, 1], [1, 2, 2], [0, 2, 3], [2, 3, 4]]) == 7      # 0-2는 이미 연결돼 건너뜀
    assert solution(1, []) == 0
    assert solution(4, [[0, 1, 1], [2, 3, 1], [1, 2, 5]]) == 7                  # 그룹 두 개를 합칠 때 섬 3까지 바뀌어야 함

    random.seed(0)
    for _ in range(2000):
        n = random.randint(1, 12)
        costs = make_costs(n, random.randint(0, n * 2)) if n > 1 else []
        assert solution(n, costs) == prim(n, costs) == solution_union_find(n, costs), (n, costs)

    chain = [[i, i + 1, 1] for i in range(4998, -1, -1)] + [[0, 4999, 2]]      # 뒤에서부터 이어 붙인 사슬
    assert solution_union_find(5000, chain) == 4999                             # 재귀 한도를 안 올리면 RecursionError

    n = 100000
    big = make_costs(n, 100000)
    start = time.time()
    solution_union_find(n, big)
    print(f"union-find, 섬 10만·다리 {len(big):,}: {time.time() - start:.2f}s")
    print("all tests passed")
