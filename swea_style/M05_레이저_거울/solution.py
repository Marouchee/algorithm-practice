"""M05 레이저 거울: problem.md

접근: 방향 0~3(위·오른쪽·아래·왼쪽) + 델타 배열. 반사는 표 두 개(`/`: [1, 0, 3, 2], `\\`: [3, 2, 1, 0])로 d를 바꾼다.
      shoot(x, y, d)는 판 안에 있고 벽이 아닌 동안 처음 밟는 칸만 세고 한 칸씩 이동한다.
      네 변의 2(N + M)개 출발점에서 모두 쏘아 최댓값을 구한다.
      (시험 때는 같은 블록을 출발 변마다 4번 복사해 썼고, 다음 날 함수 하나로 다시 썼다.)
시간 복잡도: O(T · (N + M) · N · M)
"""
T = int(input())

for num in range(T):
    N,M = map(int, input().split())
    board = []
    nc = [-1,0,1,0]
    mc = [0,1,0,-1]
    ans = 0
    slash = [1,0,3,2]
    back = [3,2,1,0]
    for _ in range(N):
        board.append(list(input()))

    def shoot(x,y,d):
        visit = [[-1 for _ in range(M)] for _ in range(N)]
        tmp = 0
        while True:
            if x<0 or y<0 or x>N-1 or y>M-1:
                break
            if board[x][y] == '#':
                break
            elif board[x][y] == '/':
                d = slash[d]
                if visit[x][y] != 1:
                    visit[x][y] = 1
                    tmp += 1
                x += nc[d]
                y += mc[d]
            elif board[x][y] == '\\':
                d = back[d]
                if visit[x][y] != 1:
                    visit[x][y] = 1
                    tmp += 1
                x += nc[d]
                y += mc[d]
            else:
                if visit[x][y] != 1:
                    visit[x][y] = 1
                    tmp += 1
                x += nc[d]
                y += mc[d]
        
        return tmp

    for j in range(M):
        tmp_ans1 = shoot(0,j,2)
        tmp_ans2 = shoot(N-1,j,0)
        ans = max(tmp_ans1, tmp_ans2, ans)

    for i in range(N):
        tmp_ans1 = shoot(i,0,1)
        tmp_ans2 = shoot(i,M-1,3)
        ans = max(tmp_ans1, tmp_ans2, ans)

    print(f"#{num+1} {ans}")
