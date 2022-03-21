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
        self.name                   = name
        self.max_budget             = max_budget
        self._total_quantity_bought = 0
        self._total_cost            = 0
        self._total_profit          = 0
        self._folder                = defaultdict(float)

    def get_total_profit(self):
        return round(self._total_profit, 2)

    def get_folder(self):
        return self._folder

    def set_total_quantity_bought(self, quantity):
        self._total_quantity_bought = quantity

    def update_total_quantity_bought(self, quantity):
        self._total_quantity_bought += quantity

    def get_total_quantity_bought(self):
        return self._total_quantity_bought

    def get_total_cost(self):
        return self._total_cost

    def buy_share(self, share, quantity):
        self._folder[share.name] = quantity
        self.max_budget = self.max_budget % share.price
        self._total_cost += quantity * share.price
        self._total_profit += quantity * share.profit_amount

    def prepare_folder_for_optimized(self):
        for index in range(self.max_budget + 1):
            self._folder[str(index)] = 0
