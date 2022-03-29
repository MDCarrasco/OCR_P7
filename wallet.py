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
from collections import defaultdict
from decimal import Decimal, ROUND_DOWN

# Other Libs

# Owned

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
    def __init__(self, name, max_budget=500, optimized=False, nb_available_shares=None):
        """Summary of __init__.

        Args:
            name
            max_budget Default to 500
        """
        if optimized:
            assert nb_available_shares is not None
        self.name                  = name
        self.current_budget        = max_budget
        self.max_budget            = max_budget if not optimized else max_budget * 100
        self.total_quantity_bought = 0
        self.total_cost            = 0
        self.total_profit          = 0
        self.table                 = None if not optimized else self.__build_table(nb_available_shares)
        self.folder                = defaultdict(int)
        self.optimized             = optimized

    def __build_table(self, nb_available_shares):
        return [[0 for _ in range(self.max_budget + 1)] for _ in range(nb_available_shares + 1)]

    def _buy_share(self, share_name, share_price, share_profit_amount):
        self.folder[share_name] = share_price
        self.current_budget     = float(Decimal(str(self.current_budget)) - Decimal(str(share_price)))
        self.total_cost         = float(Decimal(str(self.total_cost)) + Decimal(str(share_price)))
        self.total_profit       = float(Decimal(str(self.total_profit)) + Decimal(str(share_profit_amount)))

    def buy_share(self, share):
        if self.optimized:
            self._buy_share(share.name, round(share.price / 100, 2), round(share.profit_amount / 100, 2))
        else:
            self._buy_share(share.name, share.price, share.profit_amount)
        self.total_quantity_bought += 1

    def buy_single_shares(self, combination):
        assert sum(share.price for share in combination) <= self.max_budget
        for share in combination:
            self.buy_share(share)

    def __str__(self):
        share_names_and_prices = ""
        for share_name, share_price in self.folder.items():
            share_names_and_prices += f"{share_name} {share_price}\n"
        total_cost   = f"{round(self.total_cost, 2)}\n"
        total_profit = f"{round(self.total_profit, 2)}\n"
        return f"AlgoInvest&Trade bought:\n"\
               f"{share_names_and_prices}" \
               f"Total cost: {total_cost}" \
               f"Total return: {total_profit}"


