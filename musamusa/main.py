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
   MusaMusa project : musamusa/main.py

   Main entrypoint into the project : see the entrypoint() function.

   ____________________________________________________________________________

   * entrypoint() : main entrypoint into the project
"""
import datetime
import logging
import logging.config
import os.path
import sys

from musamusa.cmdlineargs import read_command_line_arguments
from musamusa.cmdline_checkenv import cmdline_checkenv
import musamusa.global_logger as global_logger
import musamusa.global_maincfgini as global_maincfgini
import musamusa.aboutproject as aboutproject
import musamusa.maincfgfile as maincfgfile


def entrypoint():
    """
        entrypoint() function

        main entrypoint into the project

        _______________________________________________________________________

        no ARGS, no RETURNED VALUE
    """
    # --------------------------------------
    # ---- (1/4) command line arguments ----
    # --------------------------------------    
    args = read_command_line_arguments()

    # --------------------------------------------
    # ---- (2/4) --version, --about, checkenv ----
    # --------------------------------------------  
    if args.version:
        sys.stdout.write(aboutproject.__version__ + "\n")
        # (pimydoc)exit codes
        # ⋅ -1  : (error) missing main configuration file
        # ⋅ -2  : (error) missing logging configuration file
        # ⋅
        # ⋅  1  : (success) print version and exit
        # ⋅  2  : (success) print about informations and exit
        # ⋅  3  : (success) print checkenv informations and exit
        # ⋅
        return 1

    if args.about:
        sys.stdout.write(
            "{0} v. {1} by {2} : see {3}; a {4} project".format(
                aboutproject.__projectname__,
                aboutproject.__version__,
                aboutproject.__author__,
                aboutproject.__location__,
                aboutproject.__license__,
            )
        )
        # (pimydoc)exit codes
        # ⋅ -1  : (error) missing main configuration file
        # ⋅ -2  : (error) missing logging configuration file
        # ⋅
        # ⋅  1  : (success) print version and exit
        # ⋅  2  : (success) print about informations and exit
        # ⋅  3  : (success) print checkenv informations and exit
        # ⋅
        return 2

    if args.checkenv:
        cmdline_checkenv()
        # (pimydoc)exit codes        
        # ⋅ -1  : (error) missing main configuration file
        # ⋅ -2  : (error) missing logging configuration file
        # ⋅
        # ⋅  1  : (success) print version and exit
        # ⋅  2  : (success) print about informations and exit
        # ⋅  3  : (success) print checkenv informations and exit
        # ⋅
        return 3

    # ----------------------------------
    # ---- (3/4) configuration file ----
    # ----------------------------------
    if not maincfgfile.read(args.maincfgfile):
        # (pimydoc)exit codes
        # ⋅ -1  : (error) missing main configuration file
        # ⋅ -2  : (error) missing logging configuration file
        # ⋅
        # ⋅  1  : (success) print version and exit
        # ⋅  2  : (success) print about informations and exit
        # ⋅  3  : (success) print checkenv informations and exit
        # ⋅
        return -1
    
    # -----------------------
    # ---- (4/4) logging ----
    # -----------------------
    logcfgfile = args.logcfgfile

    if not os.path.exists(logcfgfile):
        # (pimydoc)exit codes        
        # ⋅ -1  : (error) missing main configuration file
        # ⋅ -2  : (error) missing logging configuration file
        # ⋅
        # ⋅  1  : (success) print version and exit
        # ⋅  2  : (success) print about informations and exit
        # ⋅  3  : (success) print checkenv informations and exit
        # ⋅
        sys.stdout.write("Error, can't read logging config file : "
                         "where is '{logcfgfile}', namely {fullname} ?\n".format(
                             logcfgfile=logcfgfile,
                             fullname=normpath(logcfgfile)))
        return -2

    logging.config.fileConfig(logcfgfile)
    global_logger.LOGGER = logging.getLogger("activity")

    if not global_maincfgini.MAINCFGINI["logging"].getboolean("authorize logging"):
        logging.disable(sys.maxsize)
        
    import musamusa.logging_facilities
    musamusa.logging_facilities.first_log()
    
