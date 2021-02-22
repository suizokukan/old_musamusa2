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

# TODO
import musamusa.global_maincfgini
import musamusa.cfgini

def read(maincfgfile):
    """
        read()

        Read the configuration file and initialize nikw.cfgini.MAINCFGINI

        This function is what executes the --maincfgfile command line option.

        This function doesn't use a logger or rich text output.
        ________________________________________________________________________

        PARAMETER:  (str)maincfgfile : main configg file name

        RETURNED VALUE :
            (bool) success
    """
    (maincfgini_success,
     maincfgerrors,
     musamusa.global_maincfgini.MAINCFGINI) = musamusa.cfgini.read_main_cfg_file(maincfgfile)

    if not maincfgini_success:
        print("[ERRID004] problem with the main config file '{maincfgfile}'; "
              "errors={maincfgerrors}".format(
                  maincfgfile=maincfgfile,
                  maincfgerrors=maincfgerrors))
        return False

    return True

