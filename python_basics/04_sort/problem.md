# 문법 드릴 04: 정렬 key=lambda · 튜플 비교

## 4-1. 출력 예측

```python
a = [5, 2, 8]
b = a.sort()
print(a, b)                                # [2, 5, 8] None
c = sorted([5, 2, 8], reverse=True)
print(c)                                   # [8, 5, 2]
```

## 4-2. 출력 예측

```python
print((2, "z") < (3, "a"))                 # True
print((2, "z") < (2, "a"))                 # False
print(max([(1, "b"), (3, "a"), (3, "c")])) # (3, 'c')
print((3, "a") > 2)                        # TypeError
```

## 4-3. 기준 두 개로 정렬

`people = [("kim", 30), ("lee", 25), ("park", 30), ("choi", 25)]`

- (a) 나이 오름차순, 같으면 이름 오름차순 → `[("choi", 25), ("lee", 25), ("kim", 30), ("park", 30)]`
- (b) 나이 내림차순, 같으면 이름 오름차순 → `[("kim", 30), ("park", 30), ("choi", 25), ("lee", 25)]`

## 4-4. dict 정렬

`count = {"plum": 2, "pear": 3, "fig": 2}`를 개수 내림차순, 같으면 이름 오름차순으로 정렬한 이름 리스트 → `["pear", "fig", "plum"]`

- 시간 복잡도: 키가 m개일 때 O(m log m)
