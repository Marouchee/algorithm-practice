"""프로그래머스 Lv.1 K번째수 (정렬)
https://school.programmers.co.kr/learn/courses/30/lessons/42748

접근: 명령마다 i번째~j번째를 잘라(array[i-1:j]) 정렬하고, k번째(인덱스 k-1) 값을 담는다.
시간 복잡도: O(c · n log n). 명령 c개마다 길이 최대 n인 리스트를 정렬한다
"""


def solution(array, commands):
    answer = []

    for i, j, k in commands:
        sliced_list = array[i-1:j]
        sliced_list = sorted(sliced_list)
        answer.append(sliced_list[k-1])

    return answer


if __name__ == "__main__":
    assert solution([50, 60, 70, 80, 90], [[2, 4, 1], [1, 5, 5]]) == [60, 90]
    assert solution([7], [[1, 1, 1]]) == [7]                  # 원소 1개
    assert solution([3, 1, 2], [[1, 3, 1], [1, 3, 3]]) == [1, 3]   # 전체 구간, 첫·마지막
    assert solution([4, 4, 1], [[2, 3, 2]]) == [4]             # 중복 값

    array = [3, 1, 2]
    solution(array, [[1, 3, 1]])
    assert array == [3, 1, 2]                                  # sorted는 원본을 바꾸지 않는다
    print("all tests passed")
