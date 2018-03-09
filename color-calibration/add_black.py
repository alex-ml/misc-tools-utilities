#!/usr/bin/python2
#
# Add a synthetic black line to a TI3 file generated by scanin
# (troy_s told me to do that :P)
#
# Copyright (C) 2016 a1ex
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os, sys, re

if len(sys.argv) == 1:
    print "Usage: python2 %s file.ti3" % sys.argv[0]
    raise SystemExit

f = open(sys.argv[1], "r")
inp = f.readlines()
f.close()

black_line = "00B 0 0 0 0 0 0 0 0 0"

for l in inp:
    if l.strip() == black_line:
        print "Synthetic black already there, nothing to do."
        raise SystemExit

f = open(sys.argv[1], "w")

for l in inp:
    m = re.match("NUMBER_OF_SETS +([0-9]+) *$", l)
    if m:
        n = int(m.groups()[0])
        print >> f, "NUMBER_OF_SETS %d" % (n+1)
        continue

    print >> f, l.strip()

    if l.strip() == "BEGIN_DATA":
        print >> f, black_line
        print "Synthetic black added to %s." % sys.argv[1]

f.close()
