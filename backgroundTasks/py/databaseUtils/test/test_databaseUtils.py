import unittest

from .._create_price_table import _create_price_table

class databaseUtilsTests(unittest.TestCase):

    def test_create_price_table(self):

        code = "0001"
        frequency = "1d"
        results  = _create_price_table(stock=code, frequency = frequency)

        print (results)