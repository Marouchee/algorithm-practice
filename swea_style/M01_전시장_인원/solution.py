"""M01 전시장 인원: problem.md

접근: 입장 (시각, 인원)과 퇴장 (시각, 인원)을 각각 시각 순으로 정렬하고, 두 포인터로 이른 사건부터 처리한다.
      시각이 같으면 퇴장을 먼저 처리한다(b분에는 이미 나가고 없음). 인원이 최댓값보다 **커질 때만** 시각을 바꿔 처음 시각을 남긴다.
      시각은 HH:MM 두 자리라 문자열 비교로 순서가 맞다.
시간 복잡도: O(T · N log N)
"""
T = int(input())

for num in range(T):
    N = int(input())

    in_list = []
    out_list = []
    for _ in range(N):
        a,b,c = map(str, input().split())
        in_list.append((a,int(c)))
        out_list.append((b,int(c)))

    in_list = sorted(in_list)
    out_list = sorted(out_list)

    max_people = 0
    current_people = 0
    max_time = ''
    i=0
    j=0
    while True:
        if i<N and j<N:
            if in_list[i][0] < out_list[j][0]:
                current_people += in_list[i][1]
                if max_people < current_people:
                    max_people = current_people
                    max_time = in_list[i][0]
                i += 1
            elif in_list[i][0] >= out_list[j][0]:
                current_people -= out_list[j][1]
                j += 1
        elif i<N:
            current_people += in_list[i][1]
            if max_people < current_people:
                max_people = current_people
                max_time = in_list[i][0]
            i += 1
        elif j<N:
            current_people -= out_list[j][1]
            j += 1
        else:
            break

    print(f"#{num+1} {max_people} {max_time}")
