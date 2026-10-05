from collections import Counter, defaultdict, deque


def top_candidate(votes: list[str]) -> str:
    c = Counter(votes)
    return c.most_common(1)[0][0]


def at_least_two(votes: list[str]) -> list[str]:
    c = Counter(votes)
    return [name for name, cnt in c.items() if cnt > 1]


def group_by_day(orders: list[tuple[str, str]]) -> dict[str, list[str]]:
    dd = defaultdict(list)
    for item, ind in orders:
        dd[ind].append(item)
    return dict(dd)


def last_card(n: int) -> int:
    q = deque()
    for i in range(1, n + 1):
        q.append(i)
    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())
    return q.pop()
