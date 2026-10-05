# 문법 드릴 03: Counter · defaultdict · deque

## 3-1. Counter

`votes = ["b", "a", "c", "a", "b", "a"]`

- (a) 가장 많이 득표한 후보의 이름 → `"a"`
- (b) 2표 이상 받은 후보 이름 리스트 → `["b", "a"]`

## 3-2. defaultdict

`orders = [("tea", "mon"), ("cake", "tue"), ("juice", "mon")]`를 `if/else` 없이 요일별로 묶는다.
→ `{"mon": ["tea", "juice"], "tue": ["cake"]}`

## 3-3. 출력 예측

```python
q = deque([10, 20, 30])
q.append(40)
x = q.popleft()
q.appendleft(5)
y = q.pop()
print(x, y, list(q))   # 10 40 [5, 20, 30]
```

## 3-4. 마지막 카드

카드 `1`부터 `n`까지가 위에서부터 순서대로 쌓여 있다. 한 장 남을 때까지 (1) 맨 위 카드를 버리고 (2) 그다음 맨 위 카드를 맨 아래로 옮긴다. 마지막 카드를 구한다. `n = 6`이면 `4`.

- 시간 복잡도: `deque.popleft()`를 쓰면 O(n), `list.pop(0)`을 쓰면 뒤 원소를 매번 한 칸씩 당겨 O(n²)
