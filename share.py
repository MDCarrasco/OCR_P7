# share.py
# Created at: Wed Mar 03 2021 15:45:08 GMT+0100 (Central European Standard Time)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
share.py
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
class Share(object):
    """Share.
    """
    def __init__(self, name, price, profit_percentage, profit_amount=None):
        """Summary of __init__.

        Args:
            name
            profit_percentage
            profit_amount
        """
        # name
        self.name = name
        # weight
        self.price = float(price)
        self.profit_percentage = float(profit_percentage)
        # value
        self.profit_amount = profit_amount
        if not self.profit_amount:
            self.profit_amount = round(((self.profit_percentage / 100) * self.price), 2)

    def _verbose_str(self):
        return (f"\n\t\tName: {self.name}\n"
                f"\t\tPrice: {self.price}\n"
                f"\t\tProfit percentage after 2 years: {self.profit_percentage}\n"
                f"\t\tProfit amount after 2 years (USD): {self.profit_amount}\n")

    def __str__(self):
        """Summary of __str__.

        Returns:
            str: string representation
        """
        return f"({self.name}, {self.price}, {self.profit_percentage})"

    def __repr__(self):
        return self.__str__()
