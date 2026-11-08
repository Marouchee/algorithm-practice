"""S05 도장 맞추기: problem.md

접근: 돌리기 전(0번)에 먼저 비교하고, 같지 않으면 시계 방향으로 90도씩 최대 3번 돌리며 매번 비교한다.
      A[i][j]는 돌린 판의 [j][N-1-i]로 간다. 같아지면 그 횟수를 출력하고 멈추며, 3번 돌려도 다르면 -1.
시간 복잡도: O(T · N²). 케이스마다 입력 2N², 처음 비교 N², 회전 3번 × (복사 N² + 비교 N²)
"""
T = int(input())

for num in range(T):
    N = int(input())
    start = []
    target = []
    for _ in range(N):
        start.append(list(map(int, input().split())))
    for _ in range(N):
        target.append(list(map(int, input().split())))
    
    count = 0
    if start == target:
        print(f"#{num+1} {count}")
    else:
        for _ in range(3):
            temp_list = [[0 for _ in range(N)] for _ in range(N)]
            count += 1
            for i in range(N):
                for j in range(N):
                    temp_list[j][N-i-1] = start[i][j]
            if temp_list == target:
                start = temp_list
                print(f"#{num+1} {count}")
                break
            else:
                start = temp_list
        if start != target:
            print(f"#{num+1} -1")
