this file will include explanations, instructions for including licenses, etc. 

# Description
  This handbook provides information on how to comply with the identified open source licenses under a specific set of use-cases.

# YAML key definitions
Each license has its own block, even if the compliance profile is exactly the same as another license. License blocks are arranged alphabetically by licenseID.

* name = full name of license, corresponds to SPDX License List full names (consistent with tag from SPDX License List XML) 
* licenseId = SPDX license identifiers (consistent with tag from SPDX License List XML) 
* notes = notes related to the license itself
* resources = 
* terms = different types of license terms; each term item has a type (see types below) and then may have description, use-case, and compliance-notes
  * type
    * requirement = active obligation that must be met for license compliance for the listed use-case(s)
      * acknowledgment = if there is a requirement to include specific text as an acknowledgement, then that text is included in this field. Do not use quotations for this field. If a name or other simliar text is replaceable within the acknowledgement text, it is denoted with double brackets
    * restriction = a restriction or prohibition; applies to all use-cases unless noted otherwise
    * termination = license termination clause 
    * other = other clauses that are neither squarely a requireement, restriction or termination but may be necessary to be aware of for license compliance purposes; applies to all use-cases unless noted otherwise
  * description = high-level description to explain the term, e.g., what do you have to do to meet the requirement, what is the restriction, under what conditions does the license terminat. This field may also include specifics for the use-case where the use-case does not fit into the standard four use-cases as defined below
  * use cases = the use case for which the terms (or condition) applies. These are the most common triggers for open source license conditions, but not exhaustive; if the use case or trigger does not fit in one of these categories, then it will be explained in the term description
    * UB = distribution of unmodified binary
    * MB = distribution of modified binary
    * US = distribution of unmodified source
    * MS = distribution of modified source
  *  compliance_notes = specifics of how you need to comply with the term, this is usually present for a requirement, but often not applicable for a restriction
 
 
