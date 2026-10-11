"""프로그래머스 Lv.1 신규 아이디 추천 (구현)
https://school.programmers.co.kr/learn/courses/30/lessons/72410

접근: 문제의 7단계를 순서대로 문자열 처리한다. 소문자로 바꾸고(lower의 결과를 다시 저장), 허용 문자만 붙이고,
      바로 앞 글자와 함께 마침표인 글자는 건너뛰어 연속 마침표를 하나로 줄인다.
      앞뒤 마침표 제거, 15자 자르기, 3자 채우기 전에 빈 문자열인지 먼저 확인해 [0], [-1]에서 IndexError가 나지 않게 한다.
시간 복잡도: O(n), n = len(new_id)
"""
import random
import re
import time


def solution(new_id):
    temp_ans = new_id.lower()
    
    temp_ans2 = ""
    for ch in temp_ans:
        if ch.islower() or ch.isdigit() or "-" in ch or "_" in ch or "." in ch:
            temp_ans2 += ch
    
    if temp_ans2 != "":
        temp_ans3 = temp_ans2[0]
        for i in range(1, len(temp_ans2)):
            if temp_ans2[i] == "." and temp_ans2[i-1] == ".":
                continue
            temp_ans3 += temp_ans2[i]
    else:
        temp_ans3 = ""
    
    if temp_ans3 != "" and temp_ans3[0] == ".":
        temp_ans3 = temp_ans3[1:]
    if temp_ans3 != "" and temp_ans3[-1] == ".":
        temp_ans3 = temp_ans3[:(len(temp_ans3)-1)]
        
    if temp_ans3 == "":
        temp_ans3 = "a"
        
    if len(temp_ans3) >= 16:
        temp_ans3 = temp_ans3[:15]
        if temp_ans3[-1] == ".":
            temp_ans3 = temp_ans3[:(len(temp_ans3)-1)]
    
    while len(temp_ans3) <= 2:
        temp_ans3 += temp_ans3[-1]
        if len(temp_ans3) == 3:
            break
    
    return temp_ans3


def by_regex(s):
    """정규식으로 같은 7단계를 적은 비교용 풀이"""
    s = re.sub(r"[^a-z0-9\-_.]", "", s.lower())
    s = re.sub(r"\.+", ".", s).strip(".") or "a"
    s = s[:15].rstrip(".")
    while len(s) < 3:
        s += s[-1]
    return s


if __name__ == "__main__":
    assert solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi"   # 대문자를 소문자로 바꿔야 B, T가 남는다
    assert solution("z-+.^.") == "z--"
    assert solution("=.=") == "aaa"           # 3단계 뒤 빈 문자열
    assert solution("123_.def") == "123_.def"
    assert solution("abcdefghijklmn.p") == "abcdefghijklmn"
    assert solution("!") == "aaa"             # 2단계 뒤 빈 문자열
    assert solution("...") == "aaa"
    assert solution("a" * 14 + ".b") == "a" * 14    # 15자로 자른 끝이 마침표
    assert solution("ab" + "." * 20 + "c" * 20) == "ab." + "c" * 12

    alphabet = "abcXYZ019-_.~!@#$%^&*()=+[{]}:?,<>/"
    random.seed(0)
    for _ in range(20000):
        s = "".join(random.choice(alphabet) for _ in range(random.randint(1, 25)))
        assert solution(s) == by_regex(s), s

    big = "".join(random.choice(alphabet) for _ in range(1000))
    start = time.time()
    solution(big)
    print(f"n=1000: {time.time() - start:.4f}s")
    print("all tests passed")
