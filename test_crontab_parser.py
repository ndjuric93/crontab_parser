import unittest

from crontab_parser import resolve_time_unit, OutOfRangeException


class TestCrontabParser(unittest.TestCase):

    def test_resolve_time_unit_value(self):
        test_value = '15'
        value = resolve_time_unit(
            value=test_value,
            minimum=0,
            maximum=30
        )
        self.assertEqual(test_value, value)

    def test_resolve_time_unit_out_of_range_value(self):
        with self.assertRaises(SystemExit):
            resolve_time_unit('200', 0, 1)

    def test_resolve_time_unit_asterisk(self):
        values = resolve_time_unit('*', 0, 10)
        expected_value = '0 1 2 3 4 5 6 7 8 9 10'
        self.assertEqual(values, expected_value)

    def test_resolve_time_unit_range(self):
        values = resolve_time_unit('0-10', 0, 20)
        expected_value = '0 1 2 3 4 5 6 7 8 9 10'
        self.assertEqual(values, expected_value)

    def test_resolve_time_unit_range_out_of_range_input(self):
        with self.assertRaises(SystemExit):
            resolve_time_unit('1-10', 0, 1)

    def test_resolve_time_unit_range_with_step(self):
        values = resolve_time_unit('0-10/2', 0, 20)
        expected_value = '0 2 4 6 8 10'
        self.assertEqual(values, expected_value)
