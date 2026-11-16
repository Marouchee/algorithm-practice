"""M02 창고 로봇: problem.md

접근: 방향 d를 L → -1, R → +1, 막힘 → +2로 바꾸고 델타 인덱스는 d % 4로 쓴다.
      F: 다음 칸이 밖이거나 선반이면 뒤로 돌고, 아니면 이동한 뒤 P(용량이 남을 때만 집고 '.'으로)·D(모두 배달)를 처리한다.
      남은 택배는 끝난 뒤 바닥의 P만 센다.
시간 복잡도: O(T · (명령 길이 + N · M))
"""
T = int(input())

for num in range(T):
    N,M,K = map(int, input().split())
    R,C,d = map(int, input().split())

    rd = [-1,0,1,0]
    cd = [0,1,0,-1]
    graph=[]
    for _ in range(N):
        graph.append(list(input()))

    orders = list(input())

    x = R-1
    y = C-1
    carry = 0
    ans = 0
    for order in orders:
        if order == 'L':
            d -= 1
        elif order == 'R':
            d += 1
        elif order == 'F':
            nx = x + rd[d%4]
            ny = y + cd[d%4]
            if nx<0 or ny<0 or nx>N-1 or ny>M-1 or graph[nx][ny] == '#':
                d += 2
            else:
                if graph[nx][ny] == 'P' and carry < K:
                    graph[nx][ny] = '.'
                    carry += 1
                elif graph[nx][ny] == 'D':
                    ans += carry
                    carry = 0
                x = nx
                y = ny

    left = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'P':
                left += 1
    print(f"#{num+1} {x+1} {y+1} {ans} {left}")
