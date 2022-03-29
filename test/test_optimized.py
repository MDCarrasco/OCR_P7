# test/test_optimized.py
# Created at: Mon Mar 28 2022 18:05:29 GMT+0200 (GMT+02:00)
# Copyright 2022 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
test/test_optimized.py
INSERT docstring paragraph

Example:
        INSERT example

Todo:
        * INSERT TODO lines
        *

.. _Google Python Style Guide (reference):
http://google.github.io/styleguide/pyguide.html
"""

# Futures

# Generic/Built-in

# Other Libs
import unittest

# Owned
from optimized import optimized
from share import Share
from wallet import Wallet

__author__ = "Michael Carrasco"
__copyright__ = "2022 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


class OptimizedTester(unittest.TestCase):
    """
    Optimized 0/1 KnapSack problem algorithm tester

    """
    def test_optimized_simple(self):
        self.wallet = Wallet('my_test_wallet', optimized=True, nb_available_shares=3)
        self.assertEqual(self.wallet.max_budget, 50000)
        available_shares = [
            Share("Share-1", "1", "1", cents=True),
            Share("Share-2", "10", "1", cents=True),
            Share("Share-3", "100", "1", cents=True)
        ]
        optimized(self.wallet, available_shares)
        self.assertEqual(self.wallet.total_quantity_bought, 3)
        expected_folder = {
            "Share-1": 1,
            "Share-2": 10,
            "Share-3": 100
        }
        self.assertEqual(self.wallet.folder, expected_folder)
        self.assertEqual(self.wallet.total_cost, 111)
        self.assertEqual(self.wallet.current_budget, 389)
        self.assertEqual(self.wallet.total_profit, 1.11)

    def test_optimized_simple_float(self):
        self.wallet = Wallet('my_test_wallet', optimized=True, nb_available_shares=3)
        self.assertEqual(self.wallet.max_budget, 50000)
        available_shares = [
            Share("Share-1", "0.5", "1.5", cents=True),
            Share("Share-2", "10.22", "12.3", cents=True),
            Share("Share-3", "100.3", "22", cents=True)
        ]
        optimized(self.wallet, available_shares)
        self.assertEqual(self.wallet.total_quantity_bought, 3)
        expected_folder = {
            "Share-1": 0.5,
            "Share-2": 10.22,
            "Share-3": 100.3
        }
        self.assertEqual(self.wallet.folder, expected_folder)
        self.assertEqual(self.wallet.total_cost, 111.02)
        self.assertEqual(self.wallet.current_budget, 388.98)
        self.assertEqual(self.wallet.total_profit, 23.34)

    def test_optimized_complex_float(self):
        self.wallet = Wallet('my_test_wallet', optimized=True, nb_available_shares=9)
        self.assertEqual(self.wallet.max_budget, 50000)
        available_shares = [
            Share("Share - DUPH", "100.01", "12.25", cents=True),
            Share("Share - GTAN", "26.04", "38.06", cents=True),
            Share("Share - USUF", "9.25", "27.69", cents=True),
            Share("Share - CFOZ", "10.64", "38.21", cents=True),
            Share("Share - QLRX", "50.72", "27.47", cents=True),
            Share("Share - HKFP", "230.97", "19.66", cents=True),
            Share("Share - PPPH", "24.06", "38.2", cents=True),
            Share("Share - HLJY", "78.98", "5.54", cents=True),
            Share("Share - CTCR", "160.6", "12.4", cents=True)
        ]
        optimized(self.wallet, available_shares)
        self.assertEqual(self.wallet.total_quantity_bought, 5)

        # Expected_folder values come from the output of utils/knapsack_solver_google.py
        # used with roundings of this test values (the scripts only accepts integers as input)
        # Script results:
        #   Total value (total_profit)                  = 98
        #   Total weight (total_cost)                   : 493
        #   Packed items (indexes in available_shares)  : [1, 4, 5, 6, 8]
        #   Packed_weights (prices in available_shares) : [26, 51, 231, 24, 161]
        self.maxDiff = None
        expected_folder = {
            "Share - GTAN": 26.04,
            "Share - QLRX": 50.72,
            "Share - HKFP": 230.97,
            "Share - PPPH": 24.06,
            "Share - CTCR": 160.6
        }

        self.assertEqual(dict(self.wallet.folder), expected_folder)
        self.assertEqual(self.wallet.total_cost, 492.39)
        self.assertEqual(self.wallet.current_budget, 7.61)
        self.assertEqual(self.wallet.total_profit, 98.35)


if __name__ == "__main__":
    unittest.main()
