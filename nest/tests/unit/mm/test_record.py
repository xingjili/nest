from unittest import TestCase

from nest.mm.record import show_object


class TestRecord(TestCase):
    def test_show_object(self):
        show_object(1, 2)
