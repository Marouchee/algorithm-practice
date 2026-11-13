"""S11 강의실 예약: problem.md

접근: 끝나는 시각이 빠른 수업부터 본다. 직전에 고른 수업의 끝(c_end) 이후에 시작하면(s >= c_end) 고른다.
      이유: 끝이 가장 빠른 수업 A로 최선의 답의 첫 수업 B를 바꿔도, A의 끝 ≤ B의 끝 ≤ 다음 수업의 시작이라 겹치지 않는다.
      (끝, 시작) 튜플로 저장해 정렬하면 끝 기준으로 정렬된다.
시간 복잡도: O(T · N log N) (정렬)
"""
T = int(input())

for num in range(T):
    N = int(input())
    ke = []
    for _ in range(N):
        a,b = map(int, input().split())
        ke.append((b,a))
    
    ke = sorted(ke)

    count = 0
    c_end = 0
    for i in range(N):
        if ke[i][1] >= c_end:
            c_end = ke[i][0]
            count += 1
    
    print(f"#{num+1} {count}")
