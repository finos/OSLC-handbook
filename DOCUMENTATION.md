this file will include explanations, instructions for including licenses, etc. 

#Description
  This handbook provides information on how to comply with the identified open source licenses under a specific set of use-cases.

#YAML key definitions
* name = full name of license, corresponds to SPDX License List full names (consistent with tag from SPDX License List XML) 
* licenseId = SPDX license identifiers (consistent with tag from SPDX License List XML) 
* notes = notes related to the license, top-level
* terms = different types of license terms, each term item has a type, description, use-case, and may have compliance-notes or description
  * type
    * requirement = active obligation that must be met for license compliance for the listed use-case(s)
    * restriction = a restriction or prohibition; applies to all use-cases unless noted otherwise
    * termination = termination clause 
    * legal = ther clauses that a lawyer may want to review; applies to all use-cases unless noted otherwise
  * use cases
    * UB = distribution of unmodified binary
    * MB = distribution of modified binary
    * US = distribution of unmodified source
    * MS = distribution of modified source
