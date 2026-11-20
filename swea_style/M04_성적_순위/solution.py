"""M04 성적 순위: problem.md

접근: (국어, 영어, 수학, 번호)를 모아 key=(-총점, -수학, -영어, 번호)로 한 번에 정렬하고 K-1번째를 출력한다.
      reverse=True를 쓰지 않아서 번호만 오름차순으로 남는다.
시간 복잡도: O(T · N log N)
"""
T = int(input())

for num in range(T):
    N,K = map(int, input().split())
    grades = []
    for i in range(N):
        a,b,c = map(int, input().split())
        grades.append((a,b,c,i+1))

    grades = sorted(grades, key=lambda x: (-sum(x[0:3]), -x[2], -x[1], x[3]))

    print(f"#{num+1} {grades[K-1][3]} {sum(grades[K-1][:3])}")
