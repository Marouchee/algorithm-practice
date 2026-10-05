def by_age_then_name(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(people, key=lambda x: (x[1], x[0]))


def by_age_desc_then_name(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(people, key=lambda x: (-x[1], x[0]))


def by_count_desc_then_name(count: dict[str, int]) -> list[str]:
    return sorted(count, key=lambda x: (-count[x], x))
