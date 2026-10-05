import heapq
from bisect import bisect_left, bisect_right


def top_two(nums: list[int]) -> list[int]:
    ans = []
    reverse_nums = [-(num) for num in nums]
    heapq.heapify(reverse_nums)
    ans.append(-(heapq.heappop(reverse_nums)))
    ans.append(-(heapq.heappop(reverse_nums)))
    return ans


def task_order(tasks: list[tuple[int, str]]) -> list[str]:
    ans = []
    heapq.heapify(tasks)
    for i in range(len(tasks)):
        ans.append(heapq.heappop(tasks)[1])
    return ans


def at_least(scores: list[int], x: int) -> int:
    return len(scores) - bisect_left(scores, x)


def exactly(scores: list[int], x: int) -> int:
    return bisect_right(scores, x) - bisect_left(scores, x)


def between(scores: list[int], lo: int, hi: int) -> int:
    return bisect_right(scores, hi) - bisect_left(scores, lo)
