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
   MusaMusa project : musamusa/global_maincfgini.py

   This file only contains the MAINCFGINI and the ORDERS variables.

   ____________________________________________________________________________

   * MAINCFGINI variable
   * ORDERS variable
"""
# MAINCFGINI is a configparser.ConfigParser object.
# to be set by maincfgfile.py:read()
MAINCFGINI = None

# ORDERS is CommandLineOrders object
# a subset of MAINCFGINI
#    (str)               cfgini[orders_category]["orders"]
#    becomes
#    (CommandLineOrders) ORDERS[orders_category]
#
# ORDERS is filled by read_main_cfg_file()
ORDERS = {}
