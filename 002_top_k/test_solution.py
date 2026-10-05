import random
import time

from solution import top_k, top_k_heap

VIEWS = ["b", "a", "c", "a", "b", "a", "d"]


def test_top_k():
    assert top_k(VIEWS, 2) == ["a", "b"]
    assert top_k(VIEWS, 3) == ["a", "b", "c"]                # 동점은 사전순
    assert top_k(VIEWS, 10) == ["a", "b", "c", "d"]          # 상품이 k개보다 적음
    assert top_k(["x"], 1) == ["x"]                          # 원소 1개
    assert top_k(["d", "c", "b", "a"], 2) == ["a", "b"]      # 전부 동점

    views = [f"p{random.randrange(10**5)}" for _ in range(10**5)]
    start = time.time()
    assert len(top_k(views, 10)) == 10
    assert time.time() - start < 1.0                         # 10^5개 1초 이내


def test_top_k_heap_distinct_counts():
    # 1단계: 조회 수가 모두 다른 경우만 (동점 처리는 2단계)
    assert top_k_heap(["a", "a", "a", "b", "b", "c"], 2) == ["a", "b"]
    assert top_k_heap(["c", "b", "b", "a", "a", "a"], 2) == ["a", "b"]   # 교체가 일어나는 순서
    assert top_k_heap(["c", "b", "b", "a", "a", "a"], 10) == ["a", "b", "c"]
    assert top_k_heap(["x"], 1) == ["x"]

    views = []
    for i in range(1000):
        views += [f"p{i:04d}"] * (i + 1)
    random.shuffle(views)
    assert top_k_heap(views, 5) == top_k(views, 5)


if __name__ == "__main__":
    test_top_k()
    test_top_k_heap_distinct_counts()
    print("all tests passed")
