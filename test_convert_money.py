import pytest

from convert_money import read_amount


@pytest.mark.parametrize('number, result', [
    (0, 'zero'),
    (1, 'one'),
    (2, 'two'),
    (3, 'three'),
    (4, 'four'),
    (5, 'five'),
    (6, 'six'),
    (7, 'seven'),
    (8, 'eight'),
    (9, 'nine'),
    (10, 'ten'),
    (11, 'eleven'),
    (12, 'twelve'),
    (13, 'thirteen'),
    (14, 'fourteen'),
    (15, 'fifteen'),
    (16, 'sixteen'),
    (17, 'seventeen'),
    (18, 'eighteen'),
    (19, 'nineteen'),
    (20, 'twenty'),
    (21, 'twenty one'),
    (22, 'twenty two'),
    (23, 'twenty three'),
    (24, 'twenty four'),
    (25, 'twenty five'),
    (26, 'twenty six'),
    (27, 'twenty seven'),
    (28, 'twenty eight'),
    (29, 'twenty nine'),
    (30, 'thirty'),
    (31, 'thirty one'),
    (32, 'thirty two'),
    (33, 'thirty three'),
    (34, 'thirty four'),
    (35, 'thirty five'),
    (36, 'thirty six'),
    (37, 'thirty seven'),
    (38, 'thirty eight'),
    (39, 'thirty nine'),
])
def test_read_amount_should_return_the_value_of_said_amount_as_a_string(number, result):
    amount = number

    expected_amount = read_amount(amount)

    assert expected_amount == result
