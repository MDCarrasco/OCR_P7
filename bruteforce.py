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
from wallet import Wallet
from share_parser import SharesParser

__author__ = "Michael Carrasco"
__copyright__ = "2022 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


def get_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--data", required=True)
    return argument_parser.parse_args()


def bruteforce(data_name):
    """bruteforce.
    """
    my_wallet = Wallet('my_wallet')
    sp = SharesParser()
    available_shares = sp.import_file(f"./data/{data_name}.csv")
    sorted_available_shares_dantzig = sorted(available_shares, key=lambda share: share.profit_amount/share.price, reverse=True)
    print("AlgoTrading bought:")
    for available_share in sorted_available_shares_dantzig:
        share_quantity = (my_wallet.max_budget - my_wallet.max_budget % available_share.price) / available_share.price
        my_wallet.update_total_quantity_bought(share_quantity)
        print(f"Share: {available_share.name}, Quantity: {share_quantity}")
        my_wallet.buy_share(available_share, share_quantity)

    print("\nTotal cost:", my_wallet.get_total_cost())
    print("Total return:", my_wallet.get_total_profit())


def optimized(data_name):
    my_wallet = Wallet('my_wallet')
    sp = SharesParser()
    available_shares = sp.import_file(f"./data/{data_name}.csv")
    my_wallet.prepare_folder_for_optimized()
    folder = my_wallet.get_folder()
    max_budget_in_cts = my_wallet.max_budget * 100
    current_max_budget = 0
    while True:
        current_max_budget_in_cts = current_max_budget * 100
        if current_max_budget_in_cts >= max_budget_in_cts:
            break
        print(current_max_budget)
        print(current_max_budget_in_cts)
        for available_share in available_shares:
            available_share_price_in_cts = available_share.price * 100
            available_profit_amount_in_cts = available_share.profit_amount * 100
            if available_share_price_in_cts < current_max_budget_in_cts:
                folder[str(current_max_budget_in_cts)] = max(
                    folder[str(current_max_budget_in_cts)],
                    folder[str(current_max_budget_in_cts - available_share_price_in_cts)] + available_profit_amount_in_cts
                )
                print(current_max_budget_in_cts, folder[str(current_max_budget_in_cts)])
                break
        current_max_budget += 1

    result = round(folder[str(max_budget_in_cts)], 2)
    print(f"Optimized algo total return: {result}")


if __name__ == "__main__":
    args = get_args()
    bruteforce(args.data)
    optimized(args.data)
