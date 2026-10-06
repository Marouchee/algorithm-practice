"""프로그래머스 Lv.1 완주하지 못한 선수 (해시)
https://school.programmers.co.kr/learn/courses/30/lessons/42576

접근: 참가자 이름별 개수를 dict에 세고, 완주자마다 1씩 빼서, 값이 1로 남은 이름을 반환한다.
시간 복잡도: O(n). 반복문 3개가 각각 n번, dict 조회·저장은 평균 O(1)
"""


def solution(participant, completion):
    com_dict = {}
    answer = ''

    for item in participant:
        com_dict[item] = com_dict.get(item, 0) + 1

    for item in completion:
        com_dict[item] -= 1

    for item in participant:
        if com_dict[item] == 1:
            answer = item
            break

    return answer


if __name__ == "__main__":
    import random
    import string
    import time

    assert solution(["kim", "lee", "kim"], ["kim", "lee"]) == "kim"      # 동명이인
    assert solution(["a"], []) == "a"
    assert solution(["x", "x", "x"], ["x", "x"]) == "x"
    assert solution(["b", "a", "c"], ["c", "b"]) == "a"

    p = ["".join(random.choices(string.ascii_lowercase, k=5)) for _ in range(10**5)]
    c = p[:]
    random.shuffle(c)
    missing = c.pop()
    start = time.time()
    assert solution(p, c) == missing
    assert time.time() - start < 1.0                                     # 10^5명 1초 이내
    print("all tests passed")
