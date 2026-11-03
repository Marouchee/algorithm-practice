"""S01 구간 합 차이: problem.md

접근: 케이스마다 길이 M인 묶음의 합을 모두 구하며 최댓값과 최솟값을 갱신하고, 차이를 모아 마지막에 "#번호 답"으로 출력한다.
      최솟값 초깃값은 묶음 합의 최댓값(10,000 × 1,000)으로 둔다.
시간 복잡도: O(T · (N − M + 1) · M). 묶음 하나의 합(sum + 슬라이스)이 M번 덧셈
"""
T = int(input())
ans = []

for _ in range(T):
    n,m = map(int,input().split())
    a_list = list(map(int,input().split()))

    temp_min = 10000*1000
    temp_max = 0
    for i in range(n-m+1):
        temp = sum(a_list[i:i+m])
        if temp > temp_max:
            temp_max = temp
        if temp < temp_min:
            temp_min = temp
    ans.append(temp_max - temp_min)

for i in range(T):
    print(f"#{i+1} {ans[i]}")
