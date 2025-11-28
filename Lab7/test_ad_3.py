import pytest
from ad_3 import sort_desc


def test_sort_desc():
    data = [3, 1, 4, 2, 5]

    expected = [5, 4, 3, 2, 1]

    result = sort_desc(data)

    assert result == expected, "Lista nie została poprawnie posortowana malejąco"
