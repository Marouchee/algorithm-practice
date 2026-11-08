"""S06 회문 줄: problem.md

접근: 길이 l을 2부터 늘려 가며, 가로는 각 행의 슬라이스 board[i][j:j+l], 세로는 각 열의 l칸을 리스트로 모아
      뒤집은 것(`[::-1]`)과 같은지 본다. 더 긴 회문이면 최장 길이를 바꾸고 개수를 1로, 같은 길이면 개수를 1 늘린다.
시간 복잡도: O(T · (N · M³ + M · N³)). 줄마다 구간 약 길이²/2개, 구간마다 비교에 길이만큼
"""
T = int(input())

for num in range(T):
    N,M = map(int, input().split())
    board = []
    count = 0
    max_len = 0
    for _ in range(N):
        board.append(list(input()))
    for l in range(2, M+1):
        for i in range(N):
            for j in range(M-l+1):
                if board[i][j:j+l] == board[i][j:j+l][::-1]:
                    if l > max_len:
                        max_len = l
                        count = 1
                    elif l == max_len:
                        count += 1
    
    for l in range(2, N+1):
        for j in range(M):
            for i in range(N-l+1):
                temp_list = []
                for k in range(l):
                    temp_list.append(board[i+k][j])
                if temp_list == temp_list[::-1]:
                    if l > max_len:
                        max_len = l
                        count = 1
                    elif l == max_len:
                        count += 1
    
    print(f"#{num+1} {max_len} {count}")
