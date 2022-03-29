# optimized.py
# Created at: Wed Mar 03 2021 13:45:39 GMT+0100 (Central European Standard Time)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
optimized.py
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


def optimized(wallet, available_shares):
    """Summary of optimized

    Infos:
        wallet.table = [[0 for _ in range(wallet.max_budget + 1)] for _ in range(len(available_shares) + 1)]
        setup in wallet constructor
    """
    share_count  = len(wallet.table)
    budget_count = len(wallet.table[0])

    for share_idx in range(share_count):
        for budget in range(budget_count):

            if share_idx == 0 or budget == 0:
                continue

            considered_share = available_shares[share_idx - 1]
            prev_made_profit = wallet.table[share_idx - 1]

            if considered_share.price <= budget:
                new_budget = budget - considered_share.price
                wallet.table[share_idx][budget] = max(
                    round(considered_share.profit_amount + prev_made_profit[new_budget], 2),
                    prev_made_profit[budget]
                )
            else:
                wallet.table[share_idx][budget] = prev_made_profit[budget]

    profit = wallet.table[share_count - 1][budget_count - 1]
    budget = wallet.max_budget
    for share_idx in range(share_count, 0, -1):
        prev_made_profit = wallet.table[share_idx - 1]

        if profit <= 0:
            break

        if profit == prev_made_profit[budget]:
            continue
        else:
            considered_share = available_shares[share_idx - 1]
            wallet.buy_share(considered_share)
            profit = round(profit - considered_share.profit_amount, 2)
            budget = budget - considered_share.price


def get_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--data", required=True)
    return argument_parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    share_parser = SharesParser()

    shares    = share_parser.get_shares_from_file(f"./data/{args.data}.csv", cents=True)
    my_wallet = Wallet('my_wallet', optimized=True, nb_available_shares=len(shares))
    optimized(my_wallet, shares)
    print(my_wallet)
