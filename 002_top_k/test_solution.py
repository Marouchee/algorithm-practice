import random
import time

from solution import top_k

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


if __name__ == "__main__":
    test_top_k()
    print("all tests passed")
