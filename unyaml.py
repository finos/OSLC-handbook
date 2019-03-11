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
parser.add_argument('-i', '--inputpath', help='The path containing the input YAML files.')
parser.add_argument('-o', '--outputfile', help='The filename of the output AsciiDoc file.')
parser.add_argument('-nh', '--no-header', help='Exclude .header.adoc file if found in inputpath.')
parser.add_argument('-p', '--preface', help='Path to adoc file to include at the beginning of the document (after TOC). Preface file should begin with "=="-level heading.')
parser.add_argument('-ps', '--postscript', help='Path to adoc file to append to end of document. Postscrit file should begin with "=="-level heading.')

args = parser.parse_args()

of = open(args.outputfile, 'w', encoding='utf-8')
input_file_list = os.listdir(args.inputpath)

# Include the header if it exists and -h! not set
if '.header.adoc' in input_file_list:
    if not args.no_header:
        header_file = open(os.path.join(args.inputpath, ".header.adoc"), "r", encoding='utf8')
        of.write(header_file.read() + "\n\n<<<\n\n")
        input_file_list.remove('.header.adoc')

# Include the preface if one exists
if args.preface:
    preface_file = open(args.preface, "r", encoding='utf8')
    of.write(preface_file.read() + "\n\n<<<\n\n")

of.write("== Licenses\n\n")

# Process each YAML license file
for filename in input_file_list:
    infile = open(os.path.join(args.inputpath, filename), "r", encoding='utf8')

    license = load(infile, Loader=Loader)
    infile.close()

    license = license[0]

    if license["name"]:
        of.write("=== {0}\n".format(license["name"]))
    if license["licenseId"]:
        if isinstance(license["licenseId"], list):
            of.write("SPDX License IDs::\n")
            for id in license["licenseId"]:
                of.write("https://spdx.org/licenses/{id}.html[{id}] +\n".format(id=id))
        else:
            of.write("SPDX License ID:: https://spdx.org/licenses/{id}.html[{id}]\n".format(id=license["licenseId"]))
    if license["notes"]:
        of.write("Notes:: "+ license["notes"] + "\n")
    of.write("\n")

    # Initialize dicts to collect terms, since the YAML format doesn't require 
    # grouping of term types but we want them grouped for output. Keys:
    # * 'terms' is a list of license term dicts containing the keys: type, 
    #   description, use_cases, compliance_notes, and seeAlso.
    # * 'notes_col' is a boolean to capture whether any of the terms of a 
    #   particular type contain a compliance_notes field and therefore whether 
    #   that column should be included in the table.

    conditions = {"notes_col":False, "terms":[]}
    other = {"notes_col":False, "terms":[]}
    termination = {"notes_col":False, "terms":[]}
    lvers = {"notes_col":False, "terms":[]}

    for term in license["terms"]:
        if term["type"] == "condition":
            conditions["terms"].append(term)
            if "compliance_notes" in term and term["compliance_notes"]: conditions["notes_col"] = True
        if term["type"] == "termination":
            termination["terms"].append(term)
            if "compliance_notes" in term and term["compliance_notes"]: termination["notes_col"] = True
        if term["type"] == "license_versions":
            lvers["terms"].append(term)
            if "compliance_notes" in term and term["compliance_notes"]: 
                lvers["otes_col"] = True
        if term["type"] == "other":
            other["terms"].append(term)
            if "compliance_notes" in term and term["compliance_notes"]: 
                other["notes_col"] = True

    if len(conditions["terms"]) > 0:
        of.write("==== Conditions\n")
        of.write('[width="100%", cols="30,5,5,5,5,50a", options="header"]\n')
        of.write("|===\n|Description |UB |MB |US |MS ")
        if conditions["notes_col"]:
            of.write("|Compliance Notes")
        of.write("\n\n")

        for req in conditions["terms"]:
            desc = req["description"]
            ub = us = mb = ms = compliance_notes = ""

            if "use_cases" in req:
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

            if "SeeAlso" in req and req["SeeAlso"]:
                compliance_notes += "\n\nIMPORTANT: {0}".format(req["SeeAlso"])
                
            if conditions["notes_col"]:
                row_format = "|{desc} \n|{ub} \n|{mb} \n|{us} \n|{ms} \n|{compliance_notes} \n\n"
            else:
                row_format = "|{desc} \n|{ub} \n|{mb} \n|{us} \n|{ms} \n\n"

            of.write(row_format.format(desc = desc, ub = ub, mb = mb, us = us, ms = ms, compliance_notes = compliance_notes))

        of.write("|===\n\n")

    if len(termination["terms"]) > 0:
        of.write("==== Termination Provisions\n")
        of.write('[width="100%", options="header"]\n')
        of.write("|===\n|Description ")
        if termination["notes_col"]:
            of.write("|Compliance Notes")
        of.write("\n\n")

        for termterm in termination["terms"]:
            desc = compliance_notes = ""
            desc = termterm["description"]

            if "compliance_notes" in termterm and termterm["compliance_notes"]:
                compliance_notes = "|" + termterm["compliance_notes"]

            of.write("|{desc}\n{compliance_notes}\n\n".format(desc = desc, compliance_notes = compliance_notes))
        of.write("|===\n\n")

    if len(lvers["terms"]) > 0:
        of.write("==== License Versioning\n")
        of.write('[width="100%", options="header"]\n')
        of.write("|===\n|Description ")
        if lvers["notes_col"]:
            of.write("|Compliance Notes")
        of.write("\n\n")

        for lver in lvers["terms"]:
            desc = compliance_notes = ""
            desc = lver["description"]

            if "compliance_notes" in lver and lver["compliance_notes"]:
                compliance_notes = "|" + lver["compliance_notes"]

            of.write("|{desc}\n{compliance_notes}\n\n"
                     .format(desc = desc, compliance_notes = compliance_notes))
        of.write("|===\n\n")
    if len(other["terms"]) > 0:
        of.write("==== Other Terms\n")
        of.write('[width="100%", options="header"]\n')
        of.write("|===\n|Description ")
        if other["notes_col"]:
            of.write("|Compliance Notes")
        of.write("\n\n")

        for o in other["terms"]:
            desc = compliance_notes = ""
            desc = o["description"]

            if "compliance_notes" in o and o["compliance_notes"]:
                compliance_notes = "|" + o["compliance_notes"]

            of.write("|{desc}\n{compliance_notes}\n\n"
                     .format(desc = desc, compliance_notes = compliance_notes))
        of.write("|===\n\n")
    of.write("<<<\n\n")

# Include the postscript if one exists
if args.postscript:
    postscript_file = open(args.postscript, "r", encoding='utf8')
    of.write(postscript_file.read())

of.close()
