from parameterized import parameterized
import unittest


def is_leap_year(year):
    """
    Determine if a given year is a Leap Year
    :param year: number
    :return: boolean
    """
    return (year % 400) == 0


class TestIsLeapYear(unittest.TestCase):
    def test_giveYearDivisibleBy400_thenReturnTrue(self):
        self.assertTrue(is_leap_year(2000))

    @parameterized.expand([
        ("year=800", 800),
        ("year=1200", 1200),
        ("year=1600", 1600),
        ("year=1700", 1700),
        ("year=1800", 1800),
        ("year=2100", 2100),
    ])
    def test_givenYearDivisibleBy100ButNot400_thenReturnFalse(self, _, year):
        self.assertFalse(is_leap_year(year))


if __name__ == '__main__':
    unittest.main()
