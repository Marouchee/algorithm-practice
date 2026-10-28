"""프로그래머스 Lv.2 다리를 지나는 트럭 (스택/큐, 시뮬레이션)
https://school.programmers.co.kr/learn/courses/30/lessons/42583

접근: 1초마다 count를 올리고, 먼저 맨 앞 트럭이 (현재 − 올라간 시각) == bridge_length면 내린다.
      그다음 다리 위 무게 합 current_w_sum + 다음 트럭 무게가 weight 이하면 (무게, 올라간 시각)으로 올린다.
      대기 큐와 다리 큐가 모두 비면 count를 반환한다.
시간 복잡도: O(n · m). n = bridge_length, m = len(truck_weights).
             트럭이 한 대씩만 건너는 최악에도 반복은 n · m + 1번, 한 번 반복은 O(1)
"""
import random
import time
from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_q = deque(truck_weights)
    on_bridge = deque([])

    count = 0
    current_w_sum = 0
    while True:
        count += 1
        if on_bridge:
            if count - on_bridge[0][1] == bridge_length:
                current_w_sum -= on_bridge[0][0]
                on_bridge.popleft()
        if truck_q:
            if current_w_sum + truck_q[0] <= weight:
                truck = truck_q.popleft()
                current_w_sum += truck
                on_bridge.append((truck, count))
        if not truck_q and not on_bridge:
            break

    return count


def reference(bridge_length, weight, truck_weights):
    """비교용: 다리를 길이 bridge_length인 칸 리스트로 두고 1초마다 한 칸씩 민다"""
    bridge = [0] * bridge_length
    waiting = list(truck_weights)
    t = 0
    while waiting or any(bridge):
        t += 1
        bridge.pop(0)
        if waiting and sum(bridge) + waiting[0] <= weight:
            bridge.append(waiting.pop(0))
        else:
            bridge.append(0)
    return t


if __name__ == "__main__":
    assert solution(2, 10, [7, 4, 5, 6]) == 8
    assert solution(100, 100, [10]) == 101
    assert solution(100, 100, [10] * 10) == 110
    assert solution(2, 5, [3, 3]) == 5          # 앞 트럭이 내리는 초에 다음 트럭이 올라감
    assert solution(1, 1, [1, 1, 1]) == 4       # 다리 길이 1

    random.seed(0)
    for _ in range(3000):
        bl = random.randint(1, 6)
        w = random.randint(1, 15)
        trucks = [random.randint(1, w) for _ in range(random.randint(1, 8))]
        assert solution(bl, w, trucks) == reference(bl, w, trucks), (bl, w, trucks)

    start = time.time()
    solution(10000, 10000, [1] * 10000)          # 한 번에 많이 올라가는 경우: 약 2만 번 반복
    print(f"다리 1만·트럭 1만(가벼움): {time.time() - start:.2f}s")
    start = time.time()
    solution(1000, 10, [10] * 1000)              # 한 대씩만 건너는 경우: 약 100만 번 반복
    print(f"다리 1천·트럭 1천(한 대씩): {time.time() - start:.2f}s")
    print("all tests passed")
