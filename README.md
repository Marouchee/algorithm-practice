# Algorithm Practice

하루 한 문제씩 푸는 Python 코딩 연습 기록입니다. 문제마다 풀이와 테스트를 함께 둡니다.

## 실행

```bash
python3 001_dedup_window/test_solution.py
python3 002_top_k/test_solution.py
python3 003_patrol_robot/test_solution.py
python3 python_basics/01_list/test_solution.py
python3 python_basics/02_dict_set/test_solution.py
python3 python_basics/03_collections/test_solution.py
python3 python_basics/04_sort/test_solution.py
python3 python_basics/05_heap_bisect/test_solution.py
python3 python_basics/06_itertools/test_solution.py
python3 python_basics/07_stdin_recursion/test_solution.py
python3 programmers/hash/완주하지_못한_선수.py
python3 programmers/hash/폰켓몬.py
python3 programmers/hash/전화번호_목록.py
python3 programmers/sort/K번째수.py
python3 programmers/sort/가장_큰_수.py
python3 programmers/sort/H-Index.py
python3 programmers/stack_queue/기능개발.py
python3 programmers/brute_force/모의고사.py
python3 programmers/brute_force/카펫.py
python3 programmers/brute_force/소수_찾기.py
python3 programmers/brute_force/피로도.py
python3 programmers/dfs_bfs/타겟_넘버.py
python3 programmers/dfs_bfs/게임_맵_최단거리.py
python3 programmers/dfs_bfs/네트워크.py
python3 programmers/dfs_bfs/미로_탈출.py
python3 programmers/dfs_bfs/리코쳇_로봇.py
python3 programmers/implementation/신규_아이디_추천.py
python3 programmers/implementation/키패드_누르기.py
python3 programmers/implementation/크레인_인형뽑기_게임.py
python3 programmers/implementation/주차_요금_계산.py
python3 programmers/dp/정수_삼각형.py
python3 programmers/dp/등굣길.py
python3 programmers/shortest_path/배달.py
python3 programmers/heap/야근_지수.py
python3 baekjoon/test_1463_1로_만들기.py
python3 programmers/sql/test_sql.py
(cd sql_basics/01_select_group_join && python3 test_queries.py)
```

## 문제 목록

| # | 날짜 | 문제 | 유형 | 시간 복잡도 |
|---|---|---|---|---|
| 001 | 2026-10-05 | [시간 윈도 내 중복 이벤트 제거](001_dedup_window/problem.md) | 해시, 큐 | O(n) |
| 002 | 2026-10-05 | [조회수 Top K](002_top_k/problem.md) | 해시, 정렬 | O(n + m log m) |
| 003 | 2026-10-23 | [순찰 로봇](003_patrol_robot/problem.md) | 백트래킹 | O(4 · 3^(L-1)), L = min(K, R·C − 1) |

## 프로그래머스

| 날짜 | 문제 | 레벨 | 유형 | 시간 복잡도 |
|---|---|---|---|---|
| 2026-10-06 | [완주하지 못한 선수](programmers/hash/완주하지_못한_선수.py) | Lv.1 | 해시 | O(n) |
| 2026-10-06 | [폰켓몬](programmers/hash/폰켓몬.py) | Lv.1 | 해시 | O(n) |
| 2026-10-07 | [전화번호 목록](programmers/hash/전화번호_목록.py) | Lv.2 | 해시 | O(n) |
| 2026-10-07 | [K번째수](programmers/sort/K번째수.py) | Lv.1 | 정렬 | O(c · n log n) |
| 2026-10-08 | [가장 큰 수](programmers/sort/가장_큰_수.py) | Lv.2 | 정렬 | O(n log n) |
| 2026-10-08 | [H-Index](programmers/sort/H-Index.py) | Lv.2 | 정렬 | O(n log n) |
| 2026-10-10 | [모의고사](programmers/brute_force/모의고사.py) | Lv.1 | 완전탐색 | O(n) |
| 2026-10-10 | [카펫](programmers/brute_force/카펫.py) | Lv.2 | 완전탐색 | O(yellow) |
| 2026-10-10 | [소수 찾기](programmers/brute_force/소수_찾기.py) | Lv.2 | 완전탐색 | O(P · √M) |
| 2026-10-10 | [타겟 넘버](programmers/dfs_bfs/타겟_넘버.py) | Lv.2 | DFS | O(2^n) |
| 2026-10-10 | [게임 맵 최단거리](programmers/dfs_bfs/게임_맵_최단거리.py) | Lv.2 | BFS | O(n · m) |
| 2026-10-12 | [신규 아이디 추천](programmers/implementation/신규_아이디_추천.py) | Lv.1 | 구현 | O(n) |
| 2026-10-12 | [키패드 누르기](programmers/implementation/키패드_누르기.py) | Lv.1 | 구현 | O(N) |
| 2026-10-12 | [네트워크](programmers/dfs_bfs/네트워크.py) | Lv.3 | DFS | O(n²) |
| 2026-10-14 | [크레인 인형뽑기 게임](programmers/implementation/크레인_인형뽑기_게임.py) | Lv.1 | 구현, 스택 | O(M · N) |
| 2026-10-14 | [피로도](programmers/brute_force/피로도.py) | Lv.2 | 완전탐색 | O(n! · n) |
| 2026-10-14 | [미로 탈출](programmers/dfs_bfs/미로_탈출.py) | Lv.2 | BFS | O(n · m) |
| 2026-10-19 | [리코쳇 로봇](programmers/dfs_bfs/리코쳇_로봇.py) | Lv.2 | BFS (미끄러지는 이동) | O(N · M · max(N, M)) |
| 2026-10-19 | [정수 삼각형](programmers/dp/정수_삼각형.py) | Lv.3 | DP | O(n²) |
| 2026-10-19 | [주차 요금 계산](programmers/implementation/주차_요금_계산.py) | Lv.2 | 구현, 해시 | O(n · c + c log c) |
| 2026-10-20 | [기능개발](programmers/stack_queue/기능개발.py) | Lv.2 | 스택/큐 | O(n · D) |
| 2026-10-20 | [등굣길](programmers/dp/등굣길.py) | Lv.3 | DP | O(m · n) |
| 2026-10-23 | [배달](programmers/shortest_path/배달.py) | Lv.2 | 다익스트라 | O(E log E) |
| 2026-10-24 | [야근 지수](programmers/heap/야근_지수.py) | Lv.3 | 힙 | O((W + n) log W) |

## 백준

| 날짜 | 문제 | 유형 | 시간 복잡도 |
|---|---|---|---|
| 2026-10-12 | [1463 1로 만들기](baekjoon/1463_1로_만들기.py) | DP | O(N) |

## 프로그래머스 SQL

프로그래머스(MySQL)에서 채점을 통과한 쿼리입니다. `test_sql.py`는 가상 데이터(SQLite)로 다시 실행해 봅니다.

| 날짜 | 문제 | 레벨 | 유형 |
|---|---|---|---|
| 2026-10-07 | [이름이 없는 동물의 아이디](programmers/sql/이름이_없는_동물의_아이디.sql) | Lv.1 | IS NULL |
| 2026-10-07 | [NULL 처리하기](programmers/sql/NULL_처리하기.sql) | Lv.2 | IS NULL |
| 2026-10-07 | [고양이와 개는 몇 마리 있을까](programmers/sql/고양이와_개는_몇_마리_있을까.sql) | Lv.2 | GROUP BY |
| 2026-10-07 | [동명 동물 수 찾기](programmers/sql/동명_동물_수_찾기.sql) | Lv.2 | GROUP BY |
| 2026-10-07 | [없어진 기록 찾기](programmers/sql/없어진_기록_찾기.sql) | Lv.3 | JOIN |
| 2026-10-07 | [오랜 기간 보호한 동물(1)](programmers/sql/오랜_기간_보호한_동물_1.sql) | Lv.3 | JOIN |
| 2026-10-08 | [이름에 el이 들어가는 동물 찾기](programmers/sql/이름에_el이_들어가는_동물_찾기.sql) | Lv.2 | String, Date (`LIKE`) |
| 2026-10-08 | [중성화 여부 파악하기](programmers/sql/중성화_여부_파악하기.sql) | Lv.2 | String, Date (`CASE WHEN`) |
| 2026-10-08 | [DATETIME에서 DATE로 형 변환](programmers/sql/DATETIME에서_DATE로_형_변환.sql) | Lv.2 | String, Date (`DATE_FORMAT`) |
| 2026-10-12 | [입양 시각 구하기(1)](programmers/sql/입양_시각_구하기_1.sql) | Lv.2 | GROUP BY (`HOUR`) |
| 2026-10-12 | [있었는데요 없었습니다](programmers/sql/있었는데요_없었습니다.sql) | Lv.3 | JOIN |
| 2026-10-12 | [중복 제거하기](programmers/sql/중복_제거하기.sql) | Lv.2 | SUM, MAX, MIN (`COUNT(DISTINCT)`) |
| 2026-10-12 | [보호소에서 중성화한 동물](programmers/sql/보호소에서_중성화한_동물.sql) | Lv.4 | JOIN (`LIKE`, `AND`·`OR` 괄호) |
| 2026-10-14 | [진료과별 총 예약 횟수 출력하기](programmers/sql/진료과별_총_예약_횟수_출력하기.sql) | Lv.2 | GROUP BY (`MONTH`·`YEAR`, 정렬 2개) |
| 2026-10-15 | [조건에 맞는 사용자와 총 거래금액 조회하기](programmers/sql/조건에_맞는_사용자와_총_거래금액_조회하기.sql) | Lv.3 | JOIN (`GROUP BY`·`HAVING`) |

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
