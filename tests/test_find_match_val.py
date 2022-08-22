import pytest
import sys
sys.path.append("..")
from src.find_1st_match_val import first_match


def test_find_match_has_a_match():
    a = [1, 2, 3]
    b = [3, 4, 5]
    index, value = first_match(a, b)
    assert index > -1, "No matches"


def test_find_match_has_no_match():
    a = [1, 2, 3]
    b = [7, 8, 9]
    index, value = first_match(a, b)
    assert index == -1, "No matches"
