"""프로그래머스 Lv.2 카펫 (완전탐색)
https://school.programmers.co.kr/learn/courses/30/lessons/42842

접근: 전체 칸 수 area = brown + yellow. 세로 h를 3부터 올리며 area가 h로 나누어떨어지면 w = area // h로 두고,
      안쪽 직사각형 (w-2) × (h-2)가 yellow와 같으면 답이다. h를 작은 쪽부터 보므로 처음 찾은 답은 w >= h다.
시간 복잡도: O(yellow). h - 2 <= yellow라 range 끝을 yellow + 3으로 잡았다
             (실제로는 h <= w인 답에서 멈추므로 최대 약 sqrt(brown + yellow)번 돈다)
"""
import time


def solution(brown, yellow):
    area = brown + yellow

    for h in range(3, yellow + 3):
        if area % h != 0:
            continue
        w = area // h
        if yellow != (h-2)*(w-2):
            continue
        answer = [w, h]
        break

    return answer


if __name__ == "__main__":
    assert solution(10, 2) == [4, 3]
    assert solution(8, 1) == [3, 3]                  # yellow 최솟값
    assert solution(24, 24) == [8, 6]                # h=3, 4는 나누어떨어지지만 노란 칸 조건에서 걸러진다
    assert solution(5000, 1560001) == [1251, 1251]   # 정사각형, 반복이 가장 긴 입력

    # 제한 안의 모든 유효 입력 (w >= h >= 3, brown <= 5,000, yellow <= 2,000,000)
    start = time.time()
    count = 0
    for h in range(3, 1300):
        for w in range(h, 2600):
            b, y = 2*w + 2*h - 4, (w-2)*(h-2)
            if b > 5000 or y > 2_000_000:
                break
            assert solution(b, y) == [w, h], (b, y)
            count += 1
    print(f"valid inputs {count}: {time.time() - start:.2f}s")
    print("all tests passed")
