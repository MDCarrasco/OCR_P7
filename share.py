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
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"

# pylint: disable=too-few-public-methods
class Share:
    """Share.
    """
    def __init__(self, name, profit_percentage, profit_amount):
        """Summary of __init__.

        Args:
            name
            profit_percentage
            profit_amount
        """
        self.name = name
        self.profit_percentage = profit_percentage
        self.profit_amount = profit_amount

    def __str__(self) -> str:
        """Summary of __str__.

        Returns:
            str: string presentation
        """
        return ('\nName: {}\nProfit percentage after 2 years: {}\n'
                '\nProfit amount after 2 years: {}\n'
                .format(self.name, self.profit_percentage, self.profit_amount))
