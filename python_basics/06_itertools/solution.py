from itertools import combinations, permutations


def pairs_within(menu: list[tuple[str, int]], budget: int) -> int:
    com = list(combinations(menu, 2))
    ans = 0
    for i in com:
        if i[0][1] + i[1][1] <= budget:
            ans += 1
    return ans


def two_digit(cards: list[str]) -> list[int]:
    ans = []
    temp = list(permutations(cards, 2))
    for item in temp:
        if item[0] == "0":
            continue
        ans.append(int("".join(item)))
    ans = sorted(ans)
    return ans
