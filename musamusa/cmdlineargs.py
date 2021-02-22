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
   MusaMusa project : musamusa/cmdlineargs.py

   Command line arguments

   ____________________________________________________________________________

   * read_command_line_arguments() : analyse the command line arguments.
"""
import argparse

import musamusa.aboutproject


def read_command_line_arguments():
    """
        read_command_line_arguments()

        Read the command line arguments.

        (pimydoc)command line options
        ⋅   -h, --help            show this help message and exit
        ⋅   --interface {Linux/CLI}
        ⋅                         choose interface
        ⋅                         (default: linux/cli)
        ⋅   --version             show version number and exit
        ⋅                         (default: False)
        ⋅   --about               show informations about the version, license, author and exit
        ⋅                         (default: False)
        ⋅   --maincfgfile MAINCFGFILE
        ⋅                         name of the main configuration file to be read
        ⋅                         (default: mainconfig.ini)
        ⋅   --logcfgfile LOGCFGFILE
        ⋅                         name of the logging configuration file to be read
        ⋅                         (default: logging.ini)
        ⋅   --checkenv            check Python version and third party packages
        ⋅                         (default: False)
        ⋅

        RETURNED VALUE
                return the argparse object.
    """
    parser = argparse.ArgumentParser(
        description="{0} v. {1}".format(
            musamusa.aboutproject.__projectname__,
            musamusa.aboutproject.__version__
        ),
        epilog="{0} v. {1} ({2}), a project by {3} "
        "({4})".format(
            musamusa.aboutproject.__projectname__,
            musamusa.aboutproject.__version__,
            musamusa.aboutproject.__license__,
            musamusa.aboutproject.__author__,
            musamusa.aboutproject.__email__,
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # -------------------------------------------------------------------------
    # ---- please notice that the arguments are sorted alphabetically ---------
    # -------------------------------------------------------------------------    
    parser.add_argument(
        "--about",
        action="store_true",
        help="show informations about the version, license, author and exit",
    )

    parser.add_argument("--checkenv",
                        action="store_true",
                        help="check Python version and third party packages")
        
    parser.add_argument(
        "--interface",
        action="store",
        default="linux/cli",
        choices=('Linux/CLI',),
        help="choose interface",
    )

    parser.add_argument("--logcfgfile",
                        type=str,
                        default="logging.ini",
                        help="name of the logging configuration file to be read")

    
    parser.add_argument("--maincfgfile",
                        type=str,
                        default="mainconfig.ini",
                        help="name of the main configuration file to be read")
        
    parser.add_argument(
        "--version", action="store_true", help="show version number and exit"
    )
    
    return parser.parse_args()
