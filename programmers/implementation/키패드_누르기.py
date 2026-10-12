"""프로그래머스 Lv.1 키패드 누르기 (구현)
https://school.programmers.co.kr/learn/courses/30/lessons/67256

접근: 버튼마다 (열, 아래에서 몇 번째 줄) 좌표를 dict에 두고, 두 엄지의 마지막 버튼을 l_hand, r_hand에 저장한다.
      1·4·7은 왼손, 3·6·9는 오른손. 가운데 열은 상하좌우로만 움직이므로 맨해튼 거리(|x 차| + |y 차|)가
      짧은 손으로 누르고, 같으면 hand로 정한다. 누른 손의 위치를 그 버튼으로 바꾼다.
시간 복잡도: O(N), N = len(numbers)
"""
import random
import time
from collections import deque


def solution(numbers, hand):
    answer = ''
    key_pad = {1:(0,3), 2:(1,3), 3:(2,3), 4:(0,2), 5:(1,2), 6:(2,2), 7:(0,1), 8:(1,1), 9:(2,1), 
              '*': (0,0), 0: (1,0), '#':(2,0)}
    l_hand = '*'
    r_hand = '#'
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            l_hand = num
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            r_hand = num
            answer += 'R'
        else:
            if (abs(key_pad[l_hand][0] - key_pad[num][0]) + abs(key_pad[l_hand][1] - key_pad[num][1])) > (abs(key_pad[r_hand][0] - key_pad[num][0]) + abs(key_pad[r_hand][1] - key_pad[num][1])):
                r_hand = num
                answer += 'R'
            elif (abs(key_pad[l_hand][0] - key_pad[num][0]) + abs(key_pad[l_hand][1] - key_pad[num][1])) < (abs(key_pad[r_hand][0] - key_pad[num][0]) + abs(key_pad[r_hand][1] - key_pad[num][1])):
                l_hand = num
                answer += 'L'
            else:
                if hand == 'right':
                    r_hand = num
                    answer += 'R'
                else:
                    l_hand = num
                    answer += 'L'
        
    return answer


GRID = ["123", "456", "789", "*0#"]


def moves(a, b):
    """좌표 dict 없이, 키패드 격자에서 BFS로 a에서 b까지 칸 수를 센다 (비교용)"""
    pos = {GRID[r][c]: (r, c) for r in range(4) for c in range(3)}
    dist = {pos[a]: 0}
    q = deque([pos[a]])
    while q:
        r, c = q.popleft()
        if (r, c) == pos[b]:
            return dist[(r, c)]
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < 4 and 0 <= nc < 3 and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))


def by_grid_bfs(numbers, hand):
    left, right, out = "*", "#", ""
    for n in map(str, numbers):
        if n in "147":
            side = "L"
        elif n in "369":
            side = "R"
        else:
            dl, dr = moves(left, n), moves(right, n)
            side = "L" if dl < dr else "R" if dr < dl else hand[0].upper()
        if side == "L":
            left = n
        else:
            right = n
        out += side
    return out


if __name__ == "__main__":
    assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
    assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR"
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"
    assert solution([4, 3, 2, 8], "right") == "LRRR"    # 왼손 4, 오른손 2에서 8: 칸 수 2 대 2라 오른손. 직선 거리면 왼손

    random.seed(0)
    for _ in range(20000):
        nums = [random.randint(0, 9) for _ in range(random.randint(1, 20))]
        h = random.choice(["left", "right"])
        assert solution(nums, h) == by_grid_bfs(nums, h), (nums, h)

    big = [random.randint(0, 9) for _ in range(1000)]
    start = time.time()
    solution(big, "left")
    print(f"n=1000: {time.time() - start:.4f}s")
    print("all tests passed")
