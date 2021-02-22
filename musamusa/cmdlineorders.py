#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    MusaMusa Copyright (C) 2021 Suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of MusaMusa.
#    MusaMusa is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MusaMusa is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with MusaMusa.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
    MusaMusa project : musamusa/cmdlineorders.py

    Analyse a source string describing command line orders

    (pimydoc)orders given at launch string format
    ⋅ The string follows the following format: "order1;order2;...".
    ⋅ Spaces are allowed into each order, the unique forbidden character being ';'.
    ⋅
    ⋅ * orders_category = "orders:cli"
    ⋅   - "read_input"
    ⋅
    ⋅   e.g. "read_input;"

    ___________________________________________________________________________

    * CommandLineOrders class : analyse a source string describing
                                command line orders
"""


class CommandLineOrders:
    """
        CommandLineOrders class

        Read orders from a string, check them and store them.

        * __init__(self, orders_category, source_string)
        * __str__(self)
    """
    # known_orders[orders_category] = (list of known orders)
    # for the content, see pimydoc:orders given at launch string format
    known_orders = {"orders:cli": ("read_input",),
                    }

    def __init__(self,
                 orders_category,
                 source_string):
        """
            CommandLineOrders.__str__()

            Extract from the <source_string> the orders belonging to
            <orders_category>.

            <source_string> string format:
             (pimydoc)orders given at launch string format
             ⋅ The string follows the following format: "order1;order2;...".
             ⋅ Spaces are allowed into each order, the unique forbidden character being ';'.
             ⋅
             ⋅ * orders_category = "orders:cli"
             ⋅   - "read_input"
             ⋅
             ⋅   e.g. "read_input;"

            ___________________________________________________________________

            ARGS:
            - orders_category: (str) see pimydoc:orders given at launch string format
            - source_string:   (str) the string to be read
        """
        self.errors = []
        self.orders = []

        if orders_category == "orders:cli":
            known_orders = CommandLineOrders.known_orders[orders_category]
            for _word in source_string.split(";"):
                word = _word.strip()

                if word != "" and word not in known_orders:
                    self.errors.append(f"[ERRID006] Unknown command order '{word}' "
                                       f"read in '{source_string}'; "
                                       f"orders_category is '{orders_category}' but "
                                       f"known orders are {known_orders}")
                elif word != "":
                    self.orders.append(word)

        else:
            self.errors.append(f"[ERRID007] Unknown command line order category "
                               f"'{orders_category}' .")

    def __str__(self):
        """
            CommandLineOrders.__str__()
        """
        if self.errors:
            return "!ERRORS!"+str(self.orders)
        return str(self.orders)
