"""프로그래머스 Lv.2 전화번호 목록 (해시)
https://school.programmers.co.kr/learn/courses/30/lessons/42577

접근: 번호를 모두 set에 넣고, 각 번호의 접두어(자기 자신 제외)가 set에 있는지 확인한다.
시간 복잡도: O(n · L²), L ≤ 20이라 O(n). 번호마다 접두어를 최대 L개 슬라이싱한다
공간: 번호 n개만 set에 저장한다 (접두어를 저장하면 최대 19n개)
"""
import random
import time


def solution(phone_book):
    phone_set = set(phone_book)

    for phone_num in phone_book:
        for i in range(len(phone_num)):
            if phone_num[0:i] in phone_set:
                return False

    return True


if __name__ == "__main__":
    assert solution(["12", "123", "45"]) == False
    assert solution(["123", "12"]) == False                  # 접두어가 뒤에 와도 찾는다
    assert solution(["123", "456", "789"]) == True
    assert solution(["12", "1345", "567", "88"]) == True     # 앞자리만 같고 접두어는 아님
    assert solution(["1"]) == True                           # 자기 자신은 접두어로 치지 않는다
    assert solution(["1", "2"]) == True

    random.seed(1)
    big = list({str(random.randint(10**19, 10**20 - 1)) for _ in range(1_000_000)})
    start = time.time()
    assert solution(big) == True
    print(f"1,000,000 x 20자리: {time.time() - start:.2f}s")
    print("all tests passed")
