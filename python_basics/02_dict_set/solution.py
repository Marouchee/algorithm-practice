def count(fruits: list[str]) -> dict[str, int]:
    ans = {}
    for item in fruits:
        ans[item] = ans.get(item, 0) + 1
    return ans


def group(students: list[tuple[str, str]]) -> dict[str, list[str]]:
    ans = {}
    for item, ind in students:
        if ind not in ans:
            ans[ind] = [item]
        else:
            ans[ind].append(item)
    return ans


def intersection(a: set[int], b: set[int]) -> set[int]:
    return a & b


def union(a: set[int], b: set[int]) -> set[int]:
    return a | b


def only_left(a: set[int], b: set[int]) -> set[int]:
    return a - b


def distinct_count(nums: list[int]) -> int:
    return len(set(nums))
