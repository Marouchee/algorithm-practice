# Algorithm Practice

하루 한 문제씩 푸는 Python 코딩 연습 기록입니다. 문제마다 풀이와 테스트를 함께 둡니다.

## 실행

```bash
python3 001_dedup_window/test_solution.py
python3 002_top_k/test_solution.py
python3 python_basics/01_list/test_solution.py
python3 python_basics/02_dict_set/test_solution.py
python3 python_basics/03_collections/test_solution.py
python3 python_basics/04_sort/test_solution.py
python3 python_basics/05_heap_bisect/test_solution.py
python3 python_basics/06_itertools/test_solution.py
python3 python_basics/07_stdin_recursion/test_solution.py
python3 programmers/hash/완주하지_못한_선수.py
python3 programmers/hash/폰켓몬.py
```

## 문제 목록

| # | 날짜 | 문제 | 유형 | 시간 복잡도 |
|---|---|---|---|---|
| 001 | 2026-10-05 | [시간 윈도 내 중복 이벤트 제거](001_dedup_window/problem.md) | 해시, 큐 | O(n) |
| 002 | 2026-10-05 | [조회수 Top K](002_top_k/problem.md) | 해시, 정렬 | O(n + m log m) |

## 프로그래머스

| 날짜 | 문제 | 레벨 | 유형 | 시간 복잡도 |
|---|---|---|---|---|
| 2026-10-06 | [완주하지 못한 선수](programmers/hash/완주하지_못한_선수.py) | Lv.1 | 해시 | O(n) |
| 2026-10-06 | [폰켓몬](programmers/hash/폰켓몬.py) | Lv.1 | 해시 | O(n) |

## SQL 드릴

| # | 날짜 | 주제 | 다룬 문법 |
|---|---|---|---|
| 01 | 2026-10-07 | [SELECT · GROUP BY · JOIN](sql_basics/01_select_group_join/problem.md) | `WHERE`·`IS NULL`, `COUNT`/`SUM`, `GROUP BY`·`HAVING`, `JOIN`·`LEFT JOIN` |

## 파이썬 문법 드릴

| # | 날짜 | 주제 | 다룬 문법 |
|---|---|---|---|
| 01 | 2026-10-05 | [list](python_basics/01_list/problem.md) | 슬라이싱, 컴프리헨션, 2차원 리스트 생성·전치 |
| 02 | 2026-10-05 | [dict · set](python_basics/02_dict_set/problem.md) | `dict.get` 개수 세기, 그룹 묶기, set 연산자 |
| 03 | 2026-10-06 | [collections](python_basics/03_collections/problem.md) | `Counter.most_common`, `defaultdict(list)`, `deque` 큐 시뮬레이션 |
| 04 | 2026-10-06 | [정렬](python_basics/04_sort/problem.md) | `sort` vs `sorted`, 튜플 비교, `key=lambda` 다중 기준·내림차순 |
| 05 | 2026-10-06 | [heapq · bisect](python_basics/05_heap_bisect/problem.md) | 최대 힙(음수), 튜플 힙, `bisect`로 구간 개수 세기 |
| 06 | 2026-10-06 | [itertools](python_basics/06_itertools/problem.md) | 순열·조합·product 개수, `combinations` 필터, `permutations` + `join` |
| 07 | 2026-10-06 | [표준 입력 · 재귀 한도](python_basics/07_stdin_recursion/problem.md) | `sys.stdin.readline`, 숫자·문자 격자 입력, `setrecursionlimit` |

## 문제마다 지키는 순서

1. 접근을 한 문장으로 쓰고, 쓸 변수 목록을 적는다
2. 코드를 쓴다
3. 예시 하나를 **작성한 코드 그대로** 손으로 따라간다
4. 시간·공간 복잡도를 적는다
5. 테스트를 실행한다
