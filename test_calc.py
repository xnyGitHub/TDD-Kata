"""Pytests for calc.py"""
from calc import add


def test_add():
    """Test add an empty string | "" == 0"""
    result = add("")
    assert result == 0


def test_add_return_num():
    """Test add with one number | "1" == 1"""
    result = add("1")
    assert result == 1


def test_add_two_numbers_return_sum():
    """Test add with two numbers | "1,2" == 3"""
    result = add("1,2")
    assert result == 3


def test_add_random_amount_of_numbers_return_sum():
    """Test add with multiple numbers | "1,2,5,8,4,3" == 23"""
    result = add("1,2,5,8,4,3")
    assert result == 23


def test_add_numbers_with_new_lines():
    """Test add with numbers and new lines | "1\n2,3" == 6"""
    result = add("1\n2,3")
    assert result == 6


def test_add_user_defined_delimiters_return_sum():
    """Teest add numbers with new lines and delimiters | "//;\n1;2" == 3"""
    result = add("//;\n1;2")
    assert result == 3


def test_add_with_negative_numbers():
    """Test add with negative number | "-1,2" == "Negatives are not allowed ['-1']" """
    result = add("-1,2")
    assert result == "Negatives are not allowed ['-1']"


def test_numbers_bigger_than_1000():
    """Test add with number bigger then 1000 | "1000,2" == 2"""
    result = add("1000,2")
    assert result == 2


def test_add_user_defined_delimiters_of_any_length_return_sum():
    """Test add with delimiters of anny length | "//[***]\n1***2***3" == 6"""
    result = add("//[***]\n1***2***3")
    assert result == 6


def test_add_user_defined_multiple_delimiters_return_sum():
    """Test add multiple delimiters | "//[*][%]\n1*2%3" == 6"""
    result = add("//[*][%]\n1*2%3")
    assert result == 6


def test_add_user_defined_multiple_delimiters_of_any_length_return_sum():
    """Test add multiple delimiters of any length | "//[[[[***][%]\n1***2%%%%***%3" == 6"""
    result = add("//[[[[***][%]\n1***2%%%%***%3")
    assert result == 6
