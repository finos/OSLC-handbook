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

args = parser.parse_args()

fh = open(args.inputfile, "r", encoding='utf8')

licenses = load(fh, Loader=Loader)

for license in licenses:
    if license["name"]:
        print("# ", license["name"])
    if license["licenseId"]:
        if isinstance(license["licenseId"], list):
            print("- SPDX License ID: ")
            for id in license["licenseId"]:
                print("  - ", id)
        else:
            print("- SPDX License ID: ", license["licenseId"])
    if license["notes"]:
        print("- Notes: ", license["notes"])

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
        print("## Requirements")
        print("|Summary|UB|MB|US|MS|Notes|")
        print("| --- | --- | --- | --- | --- | --- |")

        for req in requirements:
            print("|",req["description"],"|",end="")

            if "use_cases" in req:
                if "UB" in req["use_cases"]:
                    print("X", end="")
                
                print("|", end="")

                if "MB" in req["use_cases"]:
                    print("X", end="")
                
                print("|", end="")

                if "US" in req["use_cases"]:
                    print("X", end="")
                
                print("|", end="")

                if "MS" in req["use_cases"]:
                    print("X", end="")
                
                print("|", end="")
            else:
                print("||||", end="")

            if "compliance_notes" in req:
                print(req["compliance_notes"], end="")
                
            print("|")
    if len(restrictions) > 0:
        print("## Restrictions")
        print("|Summary|Notes|")
        print("| --- | --- |")

        for res in restrictions:
            print("|",res["description"],"|", end="")

            if "compliance_notes" in res:
                print(res["compliance_notes"], end="")

            print("|")
    if len(termination) > 0:
        print("## Termination Provisions")
        print("|Summary|Notes|")
        print("| --- | --- |")

        for termterm in termination:
            print("|",termterm["description"],"|", end="")

            if "compliance_notes" in termterm:
                print(termterm["compliance_notes"], end="")

            print("|")
    if len(lvers) > 0:
        print("## License Versioning")
        print("|Summary|Notes|")
        print("| --- | --- |")

        for lver in lvers:
            print("|",lver["description"],"|", end="")

            if "compliance_notes" in lvers:
                print(lver["compliance_notes"], end="")

            print("|")
    if len(other) > 0:
        print("## Other Terms")
        print("|Summary|Notes|")
        print("| --- | --- |")

        for o in other:
            print("|",o["description"],"|", end="")

            if "compliance_notes" in o:
                print(o["compliance_notes"], end="")

            print("|")