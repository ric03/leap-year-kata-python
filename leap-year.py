import unittest

from parameterized import parameterized


def is_leap_year(year):
    """
    Determine if a given year is a Leap Year
    :param year: number
    :return: boolean
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


class TestIsLeapYear(unittest.TestCase):

    @parameterized.expand([
        ("year=400", 400),
        ("year=800", 800),
        ("year=1200", 1200),
        ("year=1600", 1600),
        ("year=2000", 2000),
        ("year=2400", 2400),
    ])
    def test_giveYearDivisibleBy400_thenReturnTrue(self, _, year):
        self.assertTrue(is_leap_year(year))

    @parameterized.expand([
        ("year=1500", 1500),
        ("year=1700", 1700),
        ("year=1800", 1800),
        ("year=1900", 1900),
        ("year=2100", 2100),
    ])
    def test_givenYearDivisibleBy100ButNot400_thenReturnFalse(self, _, year):
        self.assertFalse(is_leap_year(year))

    @parameterized.expand([
        ("year=2008", 2008),
        ("year=2012", 2012),
        ("year=2016", 2016),
        ("year=2020", 2020),
    ])
    def test_givenYearDivisibleBy4ButNot100_thenReturnTrue(self, _, year):
        self.assertTrue(is_leap_year(year))

    @parameterized.expand([
        ("year=1999", 1999),
        ("year=2017", 2017),
        ("year=2018", 2018),
        ("year=2019", 2019),
        ("year=2021", 2021),
        ("year=2022", 2022),
    ])
    def test_givenYearNotDivisibleBy4_thenReturnFalse(self, _, year):
        self.assertFalse(is_leap_year(year))


if __name__ == '__main__':
    unittest.main()
