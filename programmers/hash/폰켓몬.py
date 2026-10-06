"""프로그래머스 Lv.1 폰켓몬 (해시)
https://school.programmers.co.kr/learn/courses/30/lessons/1845

접근: 중복을 없앤 종류 수와 고를 수 있는 마릿수(N // 2) 중 작은 값을 반환한다.
시간 복잡도: O(n). set을 만들 때 원소를 n번 넣는다
"""


def solution(nums):
    set_nums = set(nums)

    return min(len(set_nums), len(nums)//2)


if __name__ == "__main__":
    assert solution([5, 5, 5, 7]) == 2
    assert solution([1, 2, 3, 4]) == 2                       # 전부 다른 종류 → N/2가 상한
    assert solution([9, 9]) == 1                             # 한 종류 → 종류 수가 상한
    assert solution([1, 1, 2, 2, 3, 3]) == 3                 # 두 값이 같을 때
    assert isinstance(solution([1, 2]), int)                 # / 대신 // → 정수 반환
    print("all tests passed")
