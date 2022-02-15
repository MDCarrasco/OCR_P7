# wallet.py
# Created at: Wed Mar 03 2021 16:09:41 GMT+0100 (Central European Standard Time)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
wallet.py
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
from itertools import combinations
from operator import itemgetter

# Other Libs

# Owned
from share import Share

__author__ = "Michael Carrasco"
__copyright__ = "2022 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


# pylint: disable=too-few-public-methods
class Wallet(object):
    """Wallet.
    """
    def __init__(self, name, max_budget=500):
        """Summary of __init__.

        Args:
            name
            max_budget Default to 500
        """
        self.name = name
        self.max_budget = max_budget
        self._combinations = {}

    def get_best_combination(self):
        best_total_profit_and_combination = 0, None, None
        previous_total_profit_and_combination = 0, None, None
        for combination_name, combination_shares in self._combinations.items():
            current_total_profit_and_combination = self._get_total_profit_and_combination(combination_name, combination_shares)
            comparison_table = [current_total_profit_and_combination, previous_total_profit_and_combination]
            best_total_profit_and_combination = max(comparison_table, key=itemgetter(0))
            previous_total_profit_and_combination = current_total_profit_and_combination

        return best_total_profit_and_combination

    @staticmethod
    def _get_total_profit_and_combination(combination_name, combination_shares):
        total_profit = 0
        for share in combination_shares:
            total_profit += share.profit_amount

        return round(total_profit, 2), combination_name, combination_shares

    def get_combinations(self):
        return self._combinations

    def set_combinations(self, available_shares):
        # this contains all possible combinations of shares from min bugdet (4 dollars) to 500 dollars budget
        for r in range(len(available_shares) + 1):
            combinations_object = combinations(available_shares, r)
            combinations_lst = list(combinations_object)
            i = 1
            for combination in combinations_lst:
                combination_name = f"Combination-{i}"
                shares_combination = []
                total_combination_cost = 0
                for share_obj in combination:
                    total_combination_cost += share_obj.price
                    shares_combination.append(share_obj)
                    i += 1
                if not total_combination_cost > self.max_budget:
                    self._combinations[f"{combination_name}"] = shares_combination
