# 문법 드릴 05: heapq · bisect

## 5-1. 출력 예측

```python
h = [5, 1, 8, 3]
heapq.heapify(h)
heapq.heappush(h, 0)
a = heapq.heappop(h)
b = heapq.heappop(h)
print(a, b, h[0])   # 0 1 3
```

## 5-2. 최대 힙

`nums = [4, 9, 2, 7]`에서 `heapq`만 써서 큰 수부터 2개 → `[9, 7]`

## 5-3. 튜플 힙

`tasks = [(3, "wash"), (1, "cook"), (2, "shop")]`를 숫자가 작은 순서대로 꺼내 이름만 → `["cook", "shop", "wash"]`

## 5-4. bisect

`scores = [40, 55, 55, 70, 90]` (정렬됨)에서 반복문 없이

- (a) 55점 이상인 사람 수 → `4`
- (b) 정확히 55점인 사람 수 → `2`
- (c) 60점 이상 90점 이하인 사람 수 → `2`

## 5-5. 시간 복잡도

- 크기 k인 힙의 `heappush`, `heappop`: O(log k). 원소가 k개면 층이 약 log₂k개이고, 한 층에 한 번씩 비교한다
- 길이 n인 정렬된 리스트의 `bisect_left`: O(log n)
- 빈 힙에 n개 push 후 n개 pop: O(n log n)
