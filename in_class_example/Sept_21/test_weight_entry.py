import pytest

@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected

@pytest.mark.parametrize("input1,, input2, expected", [
    (22, 55, 77),
    (50, 20, 70),
    ])
def test_parse_weight_input(input1, input2, expected):
    from weight_entry import add_number
    answer = add_number(input1, input2)
    assert answer == expected
