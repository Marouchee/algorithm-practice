from solution import by_age_desc_then_name, by_age_then_name, by_count_desc_then_name

PEOPLE = [("kim", 30), ("lee", 25), ("park", 30), ("choi", 25)]


def test_two_keys():
    assert by_age_then_name(PEOPLE) == [("choi", 25), ("lee", 25), ("kim", 30), ("park", 30)]
    assert by_age_desc_then_name(PEOPLE) == [("kim", 30), ("park", 30), ("choi", 25), ("lee", 25)]
    assert PEOPLE[0] == ("kim", 30)                          # sorted는 원본을 바꾸지 않음


def test_dict_sort():
    assert by_count_desc_then_name({"plum": 2, "pear": 3, "fig": 2}) == ["pear", "fig", "plum"]
    assert by_count_desc_then_name({"ax": 9, "bb": 1}) == ["ax", "bb"]   # 글자 순서로는 통과 못 하는 반례
    assert by_count_desc_then_name({}) == []


if __name__ == "__main__":
    test_two_keys()
    test_dict_sort()
    print("all tests passed")
