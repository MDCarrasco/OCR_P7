# bruteforce.py
# Created at: Wed Mar 03 2021 13:45:39 GMT+0100 (Central European Standard Time)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
bruteforce.py
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
import itertools

# Other Libs

# Owned
from wallet import Wallet
from share_parser import ShareParser

__author__ = "Michael Carrasco"
__copyright__ = "2022 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


def bruteforce():
    """bruteforce.
    """
    my_wallet = Wallet('my_wallet')
    sp = ShareParser()
    available_shares = sp.import_file("./data/simple_data.csv")
    my_wallet.set_combinations(available_shares)
    best_combination = my_wallet.get_best_combination()

    print(f"\nThis is the best combination:"
          f"\n\tName: {best_combination[1]}"
          f"\n\tProfit after 2 years (USD): {best_combination[0]}"
          f"\n\tShares to buy: \n\t\t{best_combination[2]}")


if __name__ == "__main__":
    bruteforce()
