"""프로그래머스 Lv.2 프로세스 (스택/큐)
https://school.programmers.co.kr/learn/courses/30/lessons/42587

접근: (원래 위치, 우선순위) 쌍을 순서대로 큐에 넣고, 앞에서 꺼낸 프로세스의 우선순위가
      max_pri보다 작으면 뒤로 보내고, 아니면 실행해서 ans_list에 원래 위치를 쌓는다.
      실행할 때마다 큐에 남은 프로세스로 max_pri를 다시 구한다 (한 번만 구하면 낮은 프로세스가 영원히 대기).
      큐가 비면 ans_list에서 location의 인덱스 + 1을 반환한다.
시간 복잡도: O(n²). 실행 사이에 큐를 최대 한 바퀴(n번) 돌고 실행은 n번이라 꺼내기 O(n²),
             실행마다 max_pri를 다시 구하는 비용 O(n) × n번
"""
import random
from collections import deque


def solution(priorities, location):
    answer = 0
    ans_list = []
    process_q = deque([])
    max_pri = 0
    for i in range(len(priorities)):
        process_q.append((i,priorities[i]))
        if priorities[i] > max_pri:
            max_pri = priorities[i]

    while process_q:
        a,b = process_q.popleft()
        if b < max_pri:
            process_q.append((a,b))
        else:
            ans_list.append(a)
            max_pri = 0
            for process in process_q:
                if process[1] > max_pri:
                    max_pri = process[1]

    for i in range(len(ans_list)):
        if ans_list[i] == location:
            answer = i+1

    return answer


def reference(priorities, location):
    """비교용: 꺼낼 때마다 남은 대기 줄 전체와 비교한다"""
    q = deque(enumerate(priorities))
    order = 0
    while q:
        idx, p = q.popleft()
        if any(p < other for _, other in q):
            q.append((idx, p))
            continue
        order += 1
        if idx == location:
            return order


if __name__ == "__main__":
    assert solution([2, 1, 3, 2], 2) == 1
    assert solution([1, 1, 9, 1, 1, 1], 0) == 5
    assert solution([1, 3, 2], 0) == 3
    assert solution([2, 1, 2], 1) == 3          # max_pri를 다시 구하지 않으면 끝나지 않는 예
    assert solution([5], 0) == 1

    random.seed(0)
    for _ in range(5000):
        n = random.randint(1, 10)
        pr = [random.randint(1, 9) for _ in range(n)]
        loc = random.randrange(n)
        assert solution(pr, loc) == reference(pr, loc), (pr, loc)

    worst = list(range(1, 10)) * 11 + [1]       # 길이 100
    assert solution(worst, 0) == reference(worst, 0)
    print("all tests passed")
