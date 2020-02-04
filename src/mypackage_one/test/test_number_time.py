import pytest

from mypackage_one.number_time import add_twenty_to_anything


class TestAddTwentyToAnything(object):

    def test_on_add_twenty_to_anything(self):

        actual = add_twenty_to_anything(5)
        expected = 25
        assert actual == expected
        
    def test_on_add_twenty_to_any(self):

        actual = add_twenty_to_anything(50)
        expected = 70
        assert actual == expected
