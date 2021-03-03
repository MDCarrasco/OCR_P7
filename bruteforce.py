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

# Other Libs

# Owned
from share import Share
from wallet import Wallet

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
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
    shares = []
    shares.append(Share('Share-1', 10, 5))
    shares.append(Share('Share-2', 15, 10))
    shares.append(Share('Share-3', 25, 15))
    shares.append(Share('Share-4', 35, 20))
    shares.append(Share('Share-5', 30, 17))
    shares.append(Share('Share-6', 40, 25))
    shares.append(Share('Share-7', 11, 7))
    shares.append(Share('Share-8', 13, 11))
    shares.append(Share('Share-9', 24, 13))
    shares.append(Share('Share-10', 17, 27))
    shares.append(Share('Share-11', 21, 17))
    shares.append(Share('Share-12', 55, 9))
    shares.append(Share('Share-13', 19, 23))
    shares.append(Share('Share-14', 7, 1))
    shares.append(Share('Share-15', 9, 3))
    shares.append(Share('Share-16', 4, 8))
    shares.append(Share('Share-17', 2, 12))
    shares.append(Share('Share-18', 5, 14))
    shares.append(Share('Share-19', 12, 21))
    shares.append(Share('Share-20', 57, 18))

    for share in shares:


