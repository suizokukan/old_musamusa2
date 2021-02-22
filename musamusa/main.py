#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    musamusa Copyright (C) 2021 Suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of musamusa.
#    musamusa is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    musamusa is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with musamusa.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
   MusaMusa project : musamusa/main.py

   Main entrypoint into the project : see the entrypoint() function.

   ____________________________________________________________________________

   * entrypoint() : main entrypoint into the project
"""
import sys

from musamusa.cmdlineargs import read_command_line_arguments
import musamusa.aboutproject


def entrypoint():
    """
        entrypoint() function

        main entrypoint into the project

        _______________________________________________________________________

        no ARGS, no RETURNED VALUE
    """
    args = read_command_line_arguments()

    if args.version:
        sys.stdout.write(musamusa.aboutproject.__version__ + "\n")
        # (pimydoc)exit codes
        # ⋅ 1 : (success) print version and exit
        # ⋅ 2 : (success) print about informations and exit
        return 1

    if args.about:
        sys.stdout.write(
            "{0} v. {1} by {2} : see {3}; a {4} project".format(
                musamusa.aboutproject.__projectname__,
                musamusa.aboutproject.__version__,
                musamusa.aboutproject.__author__,
                musamusa.aboutproject.__location__,
                musamusa.aboutproject.__license__,
            )
        )
        # (pimydoc)exit codes
        # ⋅ 1 : (success) print version and exit
        # ⋅ 2 : (success) print about informations and exit
        return 2
