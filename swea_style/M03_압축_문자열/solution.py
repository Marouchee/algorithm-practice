"""M03 압축 문자열: problem.md

접근: 글자를 만나면 temp_str에 두고, 뒤따르는 숫자를 temp_num에 문자열로 이어 붙인다(숫자가 없으면 기본값 1).
      다음 글자를 만나면 그 묶음을 횟수만큼 펼쳐 ans에 붙이고, 끝난 뒤 마지막 묶음도 펼친다. 답은 len(ans)와 ans[K-1].
시간 복잡도: O(T · 펼친 길이)
"""
T = int(input())

for num in range(T):
    S,K = input().split()
    K = int(K)
    S = list(S)
    ans = []
    num_l = ['1','2','3','4','5','6','7','8','9','0']

    i=0
    temp_num=1
    temp_str=''
    while i<len(S):
        if S[i] in num_l:
            if temp_num == 1:
                temp_num = ''
            temp_num += S[i]
            i += 1
        elif temp_str == '':
            temp_str = S[i]
            i += 1
        else:
            temp_num = int(temp_num)
            for _ in range(temp_num):
                ans.append(temp_str)
            temp_num=1
            temp_str=''

    temp_num = int(temp_num)
    for _ in range(temp_num):
        ans.append(temp_str)
    temp_num = 1

    print(f"#{num+1} {len(ans)} {ans[K-1]}")
