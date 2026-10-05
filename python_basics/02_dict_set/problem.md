# 문법 드릴 02: dict.get · set 연산

## 2-1. 개수 세기

`fruits = ["pear", "fig", "pear", "plum", "fig", "pear"]`의 개수를 `Counter` 없이 `dict.get`으로 센다.
→ `{"pear": 3, "fig": 2, "plum": 1}`

## 2-2. 묶기

`students = [("kim", "A"), ("lee", "B"), ("park", "A")]`를 `defaultdict` 없이 반별로 묶는다.
→ `{"A": ["kim", "park"], "B": ["lee"]}`

## 2-3. set

`a = {1, 2, 3, 4}`, `b = {3, 4, 5}`, `nums = [3, 1, 3, 2, 1]`

- (a) 교집합 → `{3, 4}`
- (b) 합집합 → `{1, 2, 3, 4, 5}`
- (c) `a`에만 있는 원소 → `{1, 2}`
- (d) `nums`에서 서로 다른 값의 개수 → `3`

## 2-4. 출력 예측

```python
d = {"x": 1}
print(d.get("y"))      # None
print(d.get("y", 0))   # 0
print(d["y"])          # KeyError: 'y'
```
