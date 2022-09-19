import pytest

'''
test_tuple = [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
]


@pytest.mark.parametrize("a, b, expected", test_tuple)
def test_add_parametrize(a, b, expected):
    from function import add
    answer = add(a, b)
    assert answer == expected

'''

test_tuple = [
    (85, "Normal"),
    (45, "Borderline Low"),
    (20, "Low")
]
@pytest.mark.parametrize("HDL_input, expected", test_tuple)
def test_check_HDL_Normal(HDL_input, expected):
    from function import check_HDL
    answer = check_HDL(HDL_input)
    assert answer == expected



'''

def test_check_HDL_Normal():
    from function import check_HDL
    answer = check_HDL(85)
    expect_ans = "Normal"
    assert answer == expect_ans
    answer2 = check_HDL(45)
    expect_ans2 = "Borderline Low"
    assert answer2 == expect_ans2
    answer3 = check_HDL(20)
    expect_ans3 = "Low"
    assert answer3 == expect_ans3


def test_check_HDL_BorderlineLow():
    from function import check_HDL
    answer = check_HDL(45)
    expect_ans = "Borderline Low"
    assert answer == expect_ans

def test_check_HDL():
    from function import check_HDL
    answer = check_HDL(20)
    expect_ans = "Low"
    assert answer == expect_ans
'''