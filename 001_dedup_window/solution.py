from collections import deque


def dedup(events: list[tuple[int, str]], W: int) -> list[tuple[int, str]]:
    """id별 마지막 처리 시각을 딕셔너리에 저장한다."""
    con = {}
    ans = []
    for t, i in events:
        if i not in con:
            con[i] = t
            ans.append((t, i))
        else:
            if t - con[i] >= W:
                con[i] = t
                ans.append((t, i))
    return ans


def dedup_deque(events: list[tuple[int, str]], W: int) -> list[tuple[int, str]]:
    """처리한 이벤트만 큐에 넣고, 만료된 항목을 먼저 지워 메모리를 윈도 크기로 묶는다."""
    q = deque()
    con = {}
    ans = []

    for t, i in events:
        while q and t - q[0][0] >= W:          # 맨 앞 항목이 만료됐으면
            old_t, old_id = q.popleft()        # 꺼낸 항목을 두 변수로 받기
            del con[old_id]                    # 딕셔너리에서 지우기

        if i not in con:
            con[i] = t
            ans.append((t, i))
            q.append((t, i))                   # deque에 넣기

    return ans
