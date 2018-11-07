this file will include explanations, instructions for including licenses, etc. 

# Description
  This handbook provides information on how to comply with the identified open source licenses under a specific set of use-cases.

# YAML key definitions
Each license has its own block, even if the compliance profile is exactly the same as another license. License blocks are arranged alphabetically by licenseID.

* name = full name of license, corresponds to SPDX License List full names (consistent with tag from SPDX License List XML) 
* licenseId = SPDX license identifiers (consistent with tag from SPDX License List XML) 
* notes = notes related to the license itself
* terms = different types of license terms; each term item has a type (see types below) and then may have description, use-case, and compliance-notes
  * type
    * requirement = active obligation that must be met for license compliance for the listed use-case(s)
      * acknowledgment = if there is a requirement to include specific text as an acknowledgement, then that text is included in this field
    * restriction = a restriction or prohibition; applies to all use-cases unless noted otherwise
    * termination = termination clause 
    * legal = other clauses that a lawyer may want to review; applies to all use-cases unless noted otherwise; also may include additional notes about other terms
  * description = description of the term, e.g., what do you have to do to meet the requirement or what is the restriction
  * use cases = the use case for which the terms (or condition) applies
    * UB = distribution of unmodified binary
    * MB = distribution of modified binary
    * US = distribution of unmodified source
    * MS = distribution of modified source
  *  compliance_notes = notes on specifics of how you need to comply with the term, this is usually present for a requirement, but often not applicable for a restriction
 
 
