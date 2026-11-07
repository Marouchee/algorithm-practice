"""S04 패널 배치: problem.md

접근: 패널의 왼쪽 위 칸 (i, j)를 0 ~ N-M까지 모두 놓아 보고, 자리마다 M×M칸을 더한다.
      합이 지금까지의 최댓값보다 크면 최댓값을 바꾸고 개수를 1로, 같으면 개수를 1 늘린다.
      최댓값과 개수는 0에서 시작한다 (모든 칸이 0이어도 "같음"으로 세어진다).
시간 복잡도: O(T · (M² · (N − M + 1)² + N²)). 덧셈은 M이 N/2 근처일 때 가장 많다
"""
T = int(input())
for num in range(T):
    N,M = map(int, input().split())
    pannel = []
    for _ in range(N):
        pannel.append(list(map(int,input().split())))

    max_val = 0
    count = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_sum = 0
            for a in range(i,i+M):
                for b in range(j,j+M):
                    temp_sum += pannel[a][b]
            if temp_sum > max_val:
                max_val = temp_sum
                count = 1
            elif temp_sum == max_val:
                count += 1

    print(f"#{num+1} {max_val} {count}")
