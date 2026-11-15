"""S12 개미 걸음: problem.md

접근: 한 걸음마다 칸 색에 따라 회전(흰 → d+1, 검 → d-1, 인덱스는 d%4) → 색 뒤집기 → 이동을 K번 반복한다.
      이동한 바로 다음에 판 밖인지 검사한다. 마지막(K번째) 걸음에서 떠나는 경우도 잡으려면 반복 조건보다 먼저 봐야 한다.
      검은 칸은 끝난 뒤 한 번만 센다.
시간 복잡도: O(T · (K + N²))
"""
T = int(input())

for num in range(T):
    N,K = map(int,input().split())
    board = []
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    r,c,d = map(int, input().split())

    for _ in range(N):
        board.append(list(map(int, input().split())))

    count = 0
    while count < K:
        if board[r][c] == 0:
            d += 1
            board[r][c] = 1
            r += dr[d%4]
            c += dc[d%4]
        else:
            d -= 1
            board[r][c] = 0
            r += dr[d%4]
            c += dc[d%4]

        if r > N-1 or c > N-1 or r < 0 or c < 0:
            r = -1
            c = -1
            break
        count += 1

    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                count += 1

    print(f"#{num+1} {count} {r} {c}")
