#!/usr/bin/env python
# SPDX-License-Identifier: Apache-2.0

import sys, os
import argparse
from yaml import load, load_all, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

parser = argparse.ArgumentParser(description='Process a folder of FOSS license compliance info YAML files into AsciiDoc.')
parser.add_argument('inputpath', help='The path containing the input YAML files.')
parser.add_argument('outputfile', help='The filename of the output AsciiDoc file.')

args = parser.parse_args()

of = open(args.outputfile, 'w', encoding='utf-8')

header = """
Free & Open Source Software License Compliance Guide
====================================================
:Author:    The Fintech Open Source Foundation (FINOS), Jilayne Lovejoy, and other contributors.
:Email:     info@finos.org, opensource@jilayne.com
"""

for filename in os.listdir(args.inputpath):
    infile = open(os.path.join(args.inputpath, filename), "r", encoding='utf8')

    if filename = ".header":
        of.write(header + "\n\n")

    license = load(infile, Loader=Loader)
    infile.close()

    license = license[0]

    if license["name"]:
        of.write("== {0}\n".format(license["name"]))
    if license["licenseId"]:
        if isinstance(license["licenseId"], list):
            of.write("SPDX License IDs::\n")
            for id in license["licenseId"]:
                of.write(id + " +\n")
        else:
            of.write("SPDX License ID:: " + license["licenseId"] + "\n")
    if license["notes"]:
        of.write("Notes:: "+ license["notes"] + "\n")
    of.write("\n")

    conditions = []
    other = []
    termination = []
    lvers = []

    for term in license["terms"]:
        if term["type"] == "condition":
            conditions.append(term)
        if term["type"] == "termination":
            termination.append(term)
        if term["type"] == "license_versions":
            lvers.append(term)
        if term["type"] == "other":
            other.append(term)

    if len(conditions) > 0:
        of.write("=== Conditions\n")
        of.write("[cols=6*,options=header]\n")
        of.write("|===\n|Summary |UB |MB |US |MS |Notes\n\n")

        for req in conditions:
            desc = req["description"]

            if "use_cases" in req:
                ub = us = mb = ms = compliance_notes = ""

                if "UB" in req["use_cases"]:
                    ub = "X"
                if "MB" in req["use_cases"]:
                    mb = "X"
                if "US" in req["use_cases"]:
                    us = "X"
                if "MS" in req["use_cases"]:
                    ms = "X"

            if "compliance_notes" in req and req["compliance_notes"]:
                compliance_notes = req["compliance_notes"]
                
            of.write("|{desc}\n|{ub}\n|{mb}\n|{us}\n|{ms}\n|{compliance_notes}\n"
                     .format(desc = desc, ub = ub, mb = mb, us = us, ms = ms, compliance_notes = compliance_notes))

        of.write("|===\n\n")

    if len(termination) > 0:
        of.write("=== Termination Provisions\n")
        of.write("[cols=2*,options=header]\n")
        of.write("|===\n|Summary |Notes\n\n")

        for termterm in termination:
            desc = compliance_notes = ""
            desc = termterm["description"]

            if "compliance_notes" in termterm and termterm["compliance_notes"]:
                compliance_notes = termterm["compliance_notes"]

            of.write("|{desc}\n|{compliance_notes}\n"
                     .format(desc = desc, compliance_notes = compliance_notes))
        of.write("|===\n\n")
    if len(lvers) > 0:
        of.write("=== License Versioning\n")
        of.write("[cols=2*,options=header]\n")
        of.write("|===\n|Summary |Notes\n\n")

        for lver in lvers:
            desc = compliance_notes = ""
            desc = lver["description"]

            if "compliance_notes" in lver and lver["compliance_notes"]:
                compliance_notes = lver["compliance_notes"]

            of.write("|{desc}\n|{compliance_notes}\n"
                     .format(desc = desc, compliance_notes = compliance_notes))
        of.write("|===\n\n")
    if len(other) > 0:
        of.write("=== Other Terms\n")
        of.write("[cols=2*,options=header]\n")
        of.write("|===\n|Summary |Notes\n")

        for o in other:
            desc = compliance_notes = ""
            desc = o["description"]

            if "compliance_notes" in o and o["compliance_notes"]:
                compliance_notes = o["compliance_notes"]

            of.write("|{desc}\n|{compliance_notes}\n\n"
                     .format(desc = desc, compliance_notes = compliance_notes))
        of.write("|===\n\n")

of.close()
