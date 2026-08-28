import pytest

from practise2 import binarySearch

@pytest.mark.parametrize(
    "target, expected",
    [
        (2, 1),  # First index of repeated element
        (4, 5),  # Single element present in array
        (6, -1),  # Element missing from array
    ],
)
def test_binary_search(target, expected):
    nums = [1, 2, 2, 2, 3, 4, 5]
    assert binarySearch(nums, target) == expected