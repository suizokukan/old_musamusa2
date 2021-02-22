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
    MusaMusa project : musamusa/logging_facilities.py

    Some functions related to logging.

    ___________________________________________________________________________

    * first_log() : first log message
"""
import datetime
import time

import musamusa.global_logger


def first_log():
    """
        first_log()

        Log the first log message.
    """
    musamusa.global_logger.LOGGER.info("{name} v. {version}".format(
        name=musamusa.aboutproject.__projectname__,
        version=musamusa.aboutproject.__version__))
    musamusa.global_logger.LOGGER.info("=== new start === at {timestamp}".format(
        timestamp=datetime.datetime.fromtimestamp(time.time())))
