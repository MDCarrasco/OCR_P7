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

# Other Libs

# Owned

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"

# pylint: disable=too-few-public-methods
class Wallet:
    """Wallet.
    """
    def __init__(self, name, total_profit=0, max_budget=500):
        """Summary of __init__.

        Args:
            total_profit
            max_budget Default to 500
        """
        self.name = name
        self.total_profit = total_profit
        self.max_budget = max_budget

    def __str__(self) -> str:
        """Summary of __str__.

        Returns:
            str: string presentation
        """
        return ('\nName: {}\nTotal profit after 2 years (Euro): {}\n'
                '\nMaximum budget (Euro): {}\n'
                .format(self.name, self.total_profit, self.max_budget))
