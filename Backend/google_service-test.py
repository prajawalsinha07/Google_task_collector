# test_google.py

import unittest
from google_service import convert_to_RFC_datetime

class TestRFCDateTimeConversion(unittest.TestCase):

    def test_standard_date(self):
        """ Test standard date conversion """
        self.assertEqual(convert_to_RFC_datetime(2023, 3, 15, 12, 30), '2023-03-15T12:30:00Z')

    def test_leap_year(self):
        """ Test leap year date """
        self.assertEqual(convert_to_RFC_datetime(2020, 2, 29, 0, 0), '2020-02-29T00:00:00Z')

    def test_invalid_date(self):
        """ Test handling of invalid dates """
        with self.assertRaises(ValueError):
            convert_to_RFC_datetime(2023, 2, 29, 0, 0)

if __name__ == '__main__':
    unittest.main()
