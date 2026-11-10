"""S08 작업 순서: problem.md

접근: 첫 작업은 바깥 반복에서 고르고(준비 시간 없음), 그 뒤는 백트래킹(방문 표시 → 재귀 → 해제)으로 순서를 만든다.
      재귀에 (고른 개수, 직전 작업, 지금까지의 합)을 넘기고, 다음 작업 i를 고를 때 graph[last][i]를 더한다.
      지금까지의 합이 이미 찾은 최솟값 이상이면 더 볼 필요가 없으므로 돌아간다(가지치기).
시간 복잡도: 가지치기가 없으면 O(T · N · N!). 가지치기로 실제로는 훨씬 적게 돈다
"""
T = int(input())

for num in range(T):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    min_val = float('inf')
    
    visit = [False for _ in range(N)]
    N_list = [i for i in range(N)]

    def dfs(depth, last, sum_v):
        global min_val
        if sum_v >= min_val:
            return
        elif depth == N:
            min_val = sum_v
            return
        else:
            for i in range(N):
                if visit[i] == True:
                    continue
                else:
                    sum_v += graph[last][i]
                    visit[i] = True
                    dfs(depth+1, i, sum_v)
                    visit[i] = False
                    sum_v -= graph[last][i]
    
    for start in range(N):
        visit[start] = True
        dfs(1, start, 0)
        visit[start] = False
    
    print(f"#{num+1} {min_val}")
