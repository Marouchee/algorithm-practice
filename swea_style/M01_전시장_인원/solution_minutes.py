"""M01 전시장 인원 (다시 풀기): problem.md

접근: 시각을 0~1439분 정수로 바꾸고, 단체마다 a분부터 b-1분 칸에 인원을 더한다(b분에는 이미 나가고 없음).
      배열을 앞에서부터 훑으며 최댓값보다 **커질 때만** 갱신해 처음 시각을 남긴다. 출력은 f"{h:02d}:{m:02d}".
      solution.py(정렬 + 두 포인터)보다 분기가 적다.
시간 복잡도: O(T · N · L), L = 1440 (하루의 분 수)
"""
T = int(input())

for num in range(T):
    N = int(input())

    in_list = []
    dist = [0 for _ in range(1440)]

    for _ in range(N):
        a,b,c = map(str, input().split())
        a = int(a[:2])*60 + int(a[3:])
        b = int(b[:2])*60 + int(b[3:])
        in_list.append((a, b, int(c)))

    max_people = 0
    max_time = ''

    for a,b,c in in_list:
        for i in range(a,b):
            dist[i] += c

    for i in range(1440):
        if dist[i] > max_people:
            max_people = dist[i]
            max_time = f"{i//60:02d}:{i%60:02d}"

    print(f"#{num+1} {max_people} {max_time}")
