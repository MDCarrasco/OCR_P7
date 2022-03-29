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
import argparse

# Other Libs

# Owned
from share_parser import SharesParser
from wallet import Wallet

__author__ = "Michael Carrasco"
__copyright__ = "2022 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


def bruteforce(wallet, available_shares):
    """
    Subset count is 2**len(available_shares) since a share can only either be bought or not bought
    """

    # 1- First task is to find all subsets for a given list of shares
    subsets = [[]]
    for available_share in available_shares:
        subsets += [subset + [available_share] for subset in subsets]
    assert len(subsets) == 2**len(available_shares)

    # 2- Then we remove all subsets that are too expensive (greater than wallet.max_budget)
    subsets = [subset for subset in subsets if sum(share.price for share in subset) <= wallet.max_budget]

    # 3- Then we just have to pick the subset with the best total profit
    best_subset = max(subsets, key=lambda subset: sum(share.profit_amount for share in subset))
    wallet.buy_single_shares(best_subset)


def get_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--data", required=True)
    return argument_parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    share_parser = SharesParser()

    shares    = share_parser.get_shares_from_file(f"./data/{args.data}.csv")
    my_wallet = Wallet('my_wallet')
    bruteforce(my_wallet, shares)
    print(my_wallet)
