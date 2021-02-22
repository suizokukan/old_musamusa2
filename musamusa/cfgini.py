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
   MusaMusa project : musamusa/cfgini.py

   Some utilities to read .ini files.

   ____________________________________________________________________________

   * read_cfg_file()      : read a .ini file
"""

import os.path
import configparser

from .utils import normpath


def read_cfg_file(filename):
    """
        read_cfg_file()

        Read the config file <filename>.

        This function doesn't use a logger or rich text output.
        _______________________________________________________________________

        PARAMETER : (str)filename

        RETURNED VALUE : (bool_success, (list of str)errors, configparser.ConfigParser object)
    """
    if not os.path.exists(filename):
        return (False,
                ["Where is config file '{filename}', namely '{filename2}' ?".format(
                    filename=filename,
                    filename2=normpath(filename))],
                None)

    success = True
    errors = []
    cfgini = configparser.ConfigParser()

    try:
        cfgini.read(filename)
    except configparser.DuplicateOptionError as err:
        success = False
        errors.append("[ERRID002] Ill-formed config file '{filename}' : duplicate key {err}".format(
            filename=filename,
            err=err))

    return success, errors, cfgini


