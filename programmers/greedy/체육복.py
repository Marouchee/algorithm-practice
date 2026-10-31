"""프로그래머스 Lv.1 체육복 (그리디)
https://school.programmers.co.kr/learn/courses/30/lessons/42862

접근: clothes[i]에 학생 i의 체육복 수를 둔다 (모두 1, 여벌 +1, 도난 −1, 0번 칸은 0).
      여벌도 있고 도난도 당한 학생은 1이 되어 자연스럽게 빌려주지 못한다.
      학생 1부터 차례로 0인 학생을 만나면 앞번호(2벌)부터, 없으면 뒷번호에서 빌린다.
      뒷번호부터 빌리면 그다음 학생이 쓸 여벌을 먼저 가져갈 수 있다 (n=4, lost=[2,4], reserve=[1,3]에서 3명 vs 4명).
      학생 1(앞번호 없음)과 학생 n(뒷번호 없음)은 반복 밖에서 따로 처리한다.
시간 복잡도: O(n)
"""
import random
from itertools import product


def solution(n, lost, reserve):
    answer = 0
    clothes = [1 for _ in range(n+1)]
    clothes[0] = 0
    for i in reserve:
        clothes[i] += 1
    for i in lost:
        clothes[i] -= 1
    if clothes[1] == 0:
        if clothes[2] == 2:
            clothes[2] -= 1
            clothes[1] += 1

    for i in range(2,n):
        if clothes[i] == 0:
            if clothes[i-1] == 2:
                clothes[i-1] -= 1
                clothes[i] += 1
                continue
        if clothes[i] == 0:
            if clothes[i+1] == 2:
                clothes[i+1] -= 1
                clothes[i] += 1

    if clothes[n] == 0:
        if clothes[n-1] == 2:
            clothes[n-1] -= 1
            clothes[n] += 1

    for i in clothes:
        if i >= 1:
            answer += 1
    return answer


def brute(n, lost, reserve):
    """비교용: 여벌이 있는 학생마다 (안 빌려줌 / 앞번호 / 뒷번호) 세 경우를 모두 시도한다"""
    has = [1] * (n + 2)
    for r in reserve:
        has[r] += 1
    for l in lost:
        has[l] -= 1
    lenders = [i for i in range(1, n + 1) if has[i] == 2]
    best = 0
    for choice in product((0, -1, 1), repeat=len(lenders)):
        c = has[:]
        for who, d in zip(lenders, choice):
            if d and 1 <= who + d <= n and c[who + d] == 0:
                c[who + d] = 1
        best = max(best, sum(1 for i in range(1, n + 1) if c[i] >= 1))
    return best


if __name__ == "__main__":
    assert solution(5, [2, 4], [1, 3, 5]) == 5
    assert solution(5, [2, 4], [3]) == 4
    assert solution(3, [3], [1]) == 2
    assert solution(5, [2, 3], [3, 4]) == 4      # 여벌도 있고 도난도 당한 학생 3은 못 빌려줌
    assert solution(4, [2, 4], [1, 3]) == 4      # 앞번호부터 빌려야 함
    assert solution(2, [1], [2]) == 2            # n = 2: 반복 없이 양끝 처리만
    assert solution(2, [2], [1]) == 2

    random.seed(0)
    for _ in range(3000):
        n = random.randint(2, 9)
        lost = random.sample(range(1, n + 1), random.randint(1, n))
        reserve = random.sample(range(1, n + 1), random.randint(1, n))
        assert solution(n, lost, reserve) == brute(n, lost, reserve), (n, lost, reserve)
    print("all tests passed")
