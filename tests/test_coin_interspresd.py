import pytest
import sys
sys.path.append("..")
from src.coin_interspresed import count_changes

# if __name__ == "__main__":
#     print(count_changes([0, 1, 1, 0, 0, 1]))
#     print(count_changes([0]))
#     print(count_changes([0, 0]))


def test_count_chnges_1():
    assert count_changes([0, 1, 1, 0, 0, 1]) == 2, "Only 2 changes needed"


def test_count_chnges_2():
    assert count_changes([0]) == 0, "No changes needed"


def test_count_chnges_3():
    assert count_changes([0, 0]) == 1, "Only 1 changes needed"
