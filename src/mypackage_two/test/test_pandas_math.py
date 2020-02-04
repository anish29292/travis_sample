import pytest

from mypackage_two.pandas_math import create_empty_dataframe

class TestCreateEmptyDataframe(object):

    def test_on_create_empty_dataframe(self):

        actual = len(create_empty_dataframe(['foo', 'bar'], 20))
        expected = 20
        assert actual == expected
