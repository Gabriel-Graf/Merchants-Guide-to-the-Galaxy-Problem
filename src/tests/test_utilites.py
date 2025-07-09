import os
import sys

from Solution1.TranslatorExceptions import ProductException

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pytest

from Solution1.Utilities import is_roman, extract_digit, contains_digits, extract_product_name, remove_keywords, \
    print_error


def test_is_roman_valid_and_invalid():
    assert is_roman('XIV')
    assert is_roman('MMXXIII')
    assert not is_roman('XXXX')
    assert not is_roman('IC')
    assert not is_roman('')


def test_extract_digit():
    assert extract_digit(['foo', '23', 'bar']) == 23
    with pytest.raises(ValueError):
        extract_digit(['foo', 'bar'])


def test_contains_digits():
    assert contains_digits(['foo', '23', 'bar'])
    assert not contains_digits(['foo', 'bar'])


def test_extract_product_name_question():
    assert extract_product_name(['how', 'many', 'coins', 'is', 'unu', 'kvin', 'Silver', '?']) == 'Silver'


def test_extract_product_name_definition():
    assert extract_product_name(['unu', 'unu', 'Silver', 'is', '34', 'coins']) == 'Silver'


def test_remove_keywords():
    assert remove_keywords(['a', 'b', 'c'], {'b'}) == ['a', 'c']


def test_print_error(capsys):
    print_error()
    captured = capsys.readouterr()
    assert "I have no idea" in captured.out


def test_extract_product_name_missing_is():
    with pytest.raises(ProductException, match="'is' not found in input"):
        extract_product_name(['unu', 'unu', 'Silver'])


def test_extract_product_name_is_at_start():
    with pytest.raises(ProductException, match="No product name found"):
        extract_product_name(['is', 'Silver', '34', 'coins'])


def test_extract_digit_only_first_number():
    assert extract_digit(['foo', '23', 'bar', '42']) == 23


def test_contains_digits_empty_list():
    assert not contains_digits([])


def test_remove_keywords_no_match():
    assert remove_keywords(['a', 'b', 'c'], {'x', 'y'}) == ['a', 'b', 'c']
