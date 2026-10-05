import heapq


def top_k(views: list[str], k: int) -> list[str]:
    count = {}

    for i in views:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    order = sorted(count, key=lambda x: (-count[x], x))

    return order[:k]


def top_k_heap(views: list[str], k: int) -> list[str]:
    """크기 k 최소 힙으로 상위 k개를 유지한다. 1단계: 조회 수가 모두 다르다고 가정."""
    count = {}

    for i in views:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    order = []
    for item, cnt in count.items():
        if len(order) < k:
            heapq.heappush(order, (cnt, item))
        else:
            if order[0][0] < cnt:
                heapq.heappop(order)
                heapq.heappush(order, (cnt, item))

    order = sorted(order, reverse=True)

    ans = []
    for cnt, item in order:
        ans.append(item)

    return ans
