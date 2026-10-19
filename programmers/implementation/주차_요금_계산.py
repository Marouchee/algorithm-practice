"""프로그래머스 Lv.2 주차 요금 계산 (구현, 해시)
https://school.programmers.co.kr/learn/courses/30/lessons/92341

접근: in_dict에 지금 주차 중인 차의 입차 시각을 두고, OUT이 오면 (출차 − 입차)를 total_time에 더한 뒤 -1로 표시한다.
      기록이 끝나고도 -1이 아닌 차는 23:59까지 더한다. 누적 시간이 기본 시간 이하면 기본 요금,
      초과하면 기본 요금 + 올림(초과 시간 / 단위 시간) × 단위 요금. 차량 번호 오름차순으로 반환한다.
      (모의고사 때는 입·출차 시각을 덮어쓰기만 해서 누적이 없었고, 정렬 방향·이하 경계·올림을 놓쳤다)
시간 복잡도: O(n · c + c log c). n은 기록 수, c는 차량 수. `car_num not in car_list`가 리스트 검사라 기록마다 O(c)
"""
import math
import random
import time
from collections import defaultdict


def solution(fees, records):
    answer = []
    car_list = []
    in_dict = {}
    total_time = {}

    for item in records:
        time, car_num, status = item.split()
        if car_num not in car_list:
            car_list.append(car_num)
        if status == 'IN':
            in_dict[car_num] = time
        if status == 'OUT':
            diff = (int(time[:2]) - int(in_dict[car_num][:2]))*60 + (int(time[3:]) - int((in_dict[car_num][3:])))
            if car_num in total_time:
                total_time[car_num] += diff
            else:
                total_time[car_num] = diff
            in_dict[car_num] = -1

    car_list = sorted(car_list)
    for item in car_list:
        if in_dict[item] != -1:
            diff = (23 - int(in_dict[item][:2]))*60 + (59 - int((in_dict[item][3:])))
            if item in total_time:
                total_time[item] += diff
            else:
                total_time[item] = diff
            in_dict[item] = -1

    for item in car_list:
        if total_time[item] <= fees[0]:
            answer.append(fees[1])
        else:
            if (total_time[item]-fees[0]) % fees[2] == 0:
                answer.append(((total_time[item]-fees[0])//fees[2])*fees[3] + fees[1])
            else:
                answer.append((((total_time[item]-fees[0])//fees[2])+1)*fees[3] + fees[1])

    return answer


def by_pop(fees, records):
    """분 단위로 한 번 바꾸고, OUT 때 pop으로 주차 중 목록에서 지우는 방식 (비교용)"""
    base_time, base_fee, unit_time, unit_fee = fees
    total, inside = defaultdict(int), {}
    for r in records:
        t, car, status = r.split()
        minutes = int(t[:2]) * 60 + int(t[3:])
        if status == "IN":
            inside[car] = minutes
        else:
            total[car] += minutes - inside.pop(car)
    for car, entered in inside.items():
        total[car] += 23 * 60 + 59 - entered
    return [base_fee + max(0, math.ceil((total[c] - base_time) / unit_time)) * unit_fee for c in sorted(total)]


def make_records(n_cars, n_events):
    cars = random.sample(range(10000), n_cars)
    times = sorted(random.sample(range(1440), min(n_events, 1440)))
    inside, records = set(), []
    for t in times:
        car = random.choice(cars)
        status = "OUT" if car in inside else "IN"
        if status == "OUT":
            inside.discard(car)
        else:
            inside.add(car)
        records.append(f"{t // 60:02d}:{t % 60:02d} {car:04d} {status}")
    return records


if __name__ == "__main__":
    assert solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]) == [14600, 34400, 5000]
    assert solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]) == [0, 591]
    assert solution([1, 461, 1, 10], ["00:00 1234 IN"]) == [14841]
    # 두 번 들어온 차는 누적 60분 = 기본 시간과 같아 기본 요금, 출차 없는 차는 23:59까지
    assert solution([60, 1000, 30, 500], ["09:00 0001 IN", "09:30 0001 OUT", "10:00 0001 IN", "10:30 0001 OUT", "23:00 0002 IN"]) == [1000, 1000]
    assert solution([60, 1000, 30, 500], ["09:00 0001 IN", "10:01 0001 OUT"]) == [1500]   # 1분 초과도 한 단위로 올림

    random.seed(0)
    for _ in range(3000):
        fees = [random.randint(1, 1439), random.randint(0, 100000), random.randint(1, 1439), random.randint(1, 10000)]
        records = make_records(random.randint(1, 5), random.randint(1, 30))
        assert solution(fees, records) == by_pop(fees, records), (fees, records)

    big = make_records(1000, 1000)
    start = time.time()
    assert solution([180, 5000, 10, 600], big) == by_pop([180, 5000, 10, 600], big)
    print(f"1,000 records: {time.time() - start:.3f}s")
    print("all tests passed")
