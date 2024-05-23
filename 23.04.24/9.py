from count_chars import count_chars
import pytest

def test_count_chars_empty_string():
    assert count_chars('') == {}

def test_count_chars_single_character_string():
    assert count_chars('a') == {'a': 1}

def test_count_chars_multiple_characters_string():
    assert count_chars('hello') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_count_chars_non_string_input():
    with pytest.raises(TypeError):
        count_chars(123)

def test_count_chars_non_iterable_non_string_input():
    with pytest.raises(TypeError):
        count_chars(123)

def test_count_chars_list_input():
    with pytest.raises(TypeError):
        count_chars([1, 2, 3])

def test_count_chars_mixed_input():
    with pytest.raises(TypeError):
        count_chars(['hello', 123, 'world'])
