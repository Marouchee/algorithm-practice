def top_k(views: list[str], k: int) -> list[str]:
    count = {}

    for i in views:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    order = sorted(count, key=lambda x: (-count[x], x))

    return order[:k]
