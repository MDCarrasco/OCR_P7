# share_parser.py
# Created at: Wed Mar 03 2021 15:45:08 GMT+0100 (Central European Standard Time)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
share_parser.py
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
import csv
from collections import Counter

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
class SharesParser(object):
    def __init__(self):
        self._file = None
        self._reader = None

    def _reset_parser(self, file_path):
        if self._file:
            self._file.close()
        self._file = open(file_path, 'r')
        self._reader = csv.reader(self._file)
        # skips header line
        next(self._reader)

    @staticmethod
    def _should_parse_row(row):
        if float(row[1]) <= 0.0 or float(row[2]) <= 0.0:
            return False
        return True

    def get_shares_from_file(self, file_path, cents=False) -> list:
        shares      = []
        share_names = []
        self._reset_parser(file_path)
        for row in self._reader:
            if self._should_parse_row(row):
                share_names.append(row[0])
                new_share = Share(row[0], row[1], row[2], cents)
                shares.append(new_share)

        share_names_to_keep = [share_name for share_name, count in Counter(share_names).items() if count == 1]
        shares = [share for share in shares if share.name in share_names_to_keep]
        return shares





