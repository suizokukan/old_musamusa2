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
    MusaMusa project : musamusa/maincfgfile.py

    Read the main configuration file.

    ___________________________________________________________________________

    * read()               : wrapper around read_main_cfg_file(),
                             initializing global_maincfgini:MAINCFGINI
    * read_main_cfg_file() : read the main configuration file.
"""
import sys

from musamusa.global_logger import LOGGER
import musamusa.global_maincfgini
import musamusa.cfgini

from musamusa.cfgini import read_cfg_file
from musamusa.cmdlineorders import CommandLineOrders


def read(maincfgfile):
    """
        read()

        Read the main configuration file and initialize 
        musamusa.global_maincfgini.MAINCFGINI

        This function is what executes the --maincfgfile command line option.

        This function doesn't use a logger or rich text output.
        ________________________________________________________________________

        PARAMETER:  (str)maincfgfile : main configg file name

        RETURNED VALUE :
            (bool) success
    """
    (maincfgini_success,
     maincfgerrors,
     musamusa.global_maincfgini.MAINCFGINI,
     musamusa.global_maincfgini.ORDERS) = read_main_cfg_file(maincfgfile)

    if not maincfgini_success:
        sys.stdout.write("[ERRID004] problem with the main config file '{maincfgfile}'; "
                         "errors={maincfgerrors}\n".format(
                             maincfgfile=maincfgfile,
                             maincfgerrors=maincfgerrors))
        return False

    return True


def read_main_cfg_file(filename):
    """
        read_main_cfg_file()

        Read the config file <filename>.

        pimydoc:main config file format
        _______________________________________________________________________

        PARAMETER : (str)filename

        RETURNED VALUE : (bool_success, 
                          (list of str)errors, 
                          configparser.ConfigParser object,
                          CommandLineOrders)
    """
    success, errors, cfgini = read_cfg_file(filename)

    if success:
        # let's check the presence of some values :
        try:
            if cfgini["logging"].getboolean("authorize logging") is None:
                raise KeyError("[logging][authorize logging]")  # missing key.

            orders = cfgini["orders:cli"]["orders"]
            orders = CommandLineOrders(orders_category="orders:cli",
                                       source_string=orders)

            if orders.errors:
                success = False
                errors.append("[ERRID005] Problem with command line orders "
                              "read in '{string}' : "
                              "{errors}.".format(
                                  string=cfgini["orders:cli"]["orders"],
                                  errors=orders.errors))

        except KeyError as err:
            success = False
            errors.append("[ERRID001] Ill-formed config file '{filename}' : "
                          "missing key '{err}'.".format(
                              filename=filename,
                              err=err))

        except ValueError as err:
            success = False
            errors.append("[ERRID003] Ill-formed config file '{filename}' : "
                          "{err}".format(
                              filename=filename,
                              err=err))

    return success, errors, cfgini, orders
