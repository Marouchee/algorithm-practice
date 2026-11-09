"""S07 카드 합 맞추기: problem.md

접근: 마스크 m을 1부터 2^N - 1까지 돌며(0 = 빈 집합 제외), m의 i번 비트가 켜진 카드만 모아 합과 K의 차이를 본다.
      더 작은 차이면 최솟값을 바꾸고 개수를 1로, 같으면 개수를 1 늘린다. 최솟값은 float('inf')에서 시작한다.
시간 복잡도: O(T · N · 2^N). N = 16, T = 10이면 약 1000만 번
"""
T = int(input())

for num in range(T):
    N,K = map(int, input().split())
    cards = list(map(int, input().split()))
    mask = 2**N
    count = 1
    min_val = float('inf')

    for m in range(1, mask):
        temp = []
        for i in range(N):
            if m & (1 << i):
                temp.append(cards[i])
        temp_sum = abs(K-sum(temp))
        if temp_sum == min_val:
            count += 1
        elif temp_sum < min_val:
            min_val = temp_sum
            count = 1
    
    print(f"#{num+1} {min_val} {count}")
