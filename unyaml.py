#!/usr/bin/env python
import sys
import argparse
from yaml import load, load_all, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

parser = argparse.ArgumentParser(description='Process a license compliance info YAML file into GitHub-flavored Markdown.')
parser.add_argument('inputfile', help='The filename of the input YAML file.')
parser.add_argument('outputfile', help='The filename of the output Markdown file.')

args = parser.parse_args()

nf = open(args.inputfile, "r", encoding='utf8')
of = open(args.outputfile, 'w', encoding='utf-8')

licenses = load(nf, Loader=Loader)
nf.close()

for license in licenses:
    if license["name"]:
        of.write("# " + license["name"] + "\n")
    if license["licenseId"]:
        if isinstance(license["licenseId"], list):
            of.write("- SPDX License ID:\n")
            for id in license["licenseId"]:
                of.write("  - " + id + "\n")
        else:
            of.write("- SPDX License ID: " + license["licenseId"] + "\n")
    if license["notes"]:
        of.write("- Notes: "+ license["notes"] + "\n")

    requirements = []
    restrictions = []
    other = []
    termination = []
    lvers = []

    for term in license["terms"]:
        if term["type"] == "requirement":
            requirements.append(term)
        if term["type"] == "restriction":
            restrictions.append(term)
        if term["type"] == "termination":
            termination.append(term)
        if term["type"] == "license_versions":
            lvers.append(term)
        if term["type"] == "other":
            other.append(term)

    if len(requirements) > 0:
        of.write("## Requirements\n")
        of.write("|Summary|UB|MB|US|MS|Notes|\n")
        of.write("| --- | --- | --- | --- | --- | --- |\n")

        for req in requirements:
            of.write("|" + req["description"] + "|")

            if "use_cases" in req:
                if "UB" in req["use_cases"]:
                    of.write("X")
                
                of.write("|")

                if "MB" in req["use_cases"]:
                    of.write("X")
                
                of.write("|")

                if "US" in req["use_cases"]:
                    of.write("X")
                
                of.write("|")

                if "MS" in req["use_cases"]:
                    of.write("X")
                
                of.write("|")
            else:
                of.write("||||")

            if "compliance_notes" in req and req["compliance_notes"]:
                of.write(req["compliance_notes"])
                
            of.write("|")
    if len(restrictions) > 0:
        of.write("## Restrictions\n")
        of.write("|Summary|Notes|\n")
        of.write("| --- | --- |\n")

        for res in restrictions:
            of.write("|" + res["description"] + "|")

            if "compliance_notes" in res and res["compliance_notes"]:
                of.write(res["compliance_notes"])

            of.write("|")
    if len(termination) > 0:
        of.write("## Termination Provisions\n")
        of.write("|Summary|Notes|\n")
        of.write("| --- | --- |\n")

        for termterm in termination:
            of.write("|" + termterm["description"] + "|")

            if "compliance_notes" in termterm and termterm["compliance_notes"]:
                of.write(termterm["compliance_notes"])

            of.write("|\n")
    if len(lvers) > 0:
        of.write("## License Versioning\n")
        of.write("|Summary|Notes|\n")
        of.write("| --- | --- |\n")

        for lver in lvers:
            of.write("|" + lver["description"] + "|")

            if "compliance_notes" in lvers and lvers["compliance_notes"]:
                of.write(lver["compliance_notes"])

            of.write("|\n")
    if len(other) > 0:
        of.write("## Other Terms\n")
        of.write("|Summary|Notes|\n")
        of.write("| --- | --- |\n")

        for o in other:
            of.write("|" + o["description"] + "|")

            if "compliance_notes" in o and o["compliance_notes"]:
                of.write(o["compliance_notes"])

            of.write("|\n")

of.close()