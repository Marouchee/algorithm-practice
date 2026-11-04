"""S02 꽃가루 모으기: problem.md

접근: 모든 칸을 한 번씩 흔들어 본다. 칸 값 k만큼 네 방향으로 한 칸씩 나아가며 더하고,
      화단 밖(0 미만, N-1·M-1 초과)이 나오면 그 방향은 멈춘다. 가장 큰 합을 "#번호 답"으로 출력한다.
시간 복잡도: O(T · N · M · 4k), k ≤ 9 → 최대 약 360만 번
"""
T = int(input())

for num in range (T):
    N,M = map(int, input().split())
    flowers = []
    ans = 0
    for _ in range(N):
        flowers.append(list(map(int, input().split())))
    
    for i in range(N):
        for j in range(M):
            temp_x = i
            temp_y = j
            k = flowers[i][j]
            temp_sum = k
            for _ in range(k):
                temp_x += 1
                if temp_x > N-1:
                    break
                temp_sum += flowers[temp_x][temp_y]
            temp_x = i
            temp_y = j
            for _ in range(k):
                temp_y += 1
                if temp_y > M-1:
                    break
                temp_sum += flowers[temp_x][temp_y]
            temp_x = i
            temp_y = j
            for _ in range(k):
                temp_x -= 1
                if temp_x < 0:
                    break
                temp_sum += flowers[temp_x][temp_y]
            temp_x = i
            temp_y = j
            for _ in range(k):
                temp_y -= 1
                if temp_y < 0:
                    break
                temp_sum += flowers[temp_x][temp_y]
            if temp_sum > ans:
                ans = temp_sum

    print(f"#{num+1} {ans}")
