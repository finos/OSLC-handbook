this file will include explanations, instructions for including licenses, etc. 

# Description
This handbook provides information on how to comply with some of the more common open source licenses under a specific set of use-cases. The goal here is to provide developers and engineers with some "self-serve" information to facilitate the end goal of open source license compliance, as well as identifying some of the more complex open source license compliance aspects for which consultation with open source counsel may be recommended. 
  
Determining the requirements that need to be met to comply with open source licenses involves: 
1) legal interpretation of the license; and 
2) how the open source software is being used (“use-case”). 
As to the former, some conditions are easy to understand and comply with, while other conditions are open for (legal) interpretation. 
As to the latter, the conditions that need to be met for a given open source license may vary depending on how it is used; for example, whether the open source software is distributed in binary form, distributed in source form, or used in a web-based application. 

One way to think of this is as an if-then statement ... (add bit here from training slides)

The license compliance requirements are summarized for the four most common use-cases as listed below. This document only provides license compliance information for licenses and use-cases that are easy to understand and summarize succinctly.  Cases where further analysis may be needed are flagged and may need consultation with your open source counsel.  Likewise, if your use-case varies in any way or you are using a different license (even if it seems similar) than those licenses listed here or you have any questions whatsoever about this information or how to properly comply, please contact your open source counsel.
  
## Use-case:
Distribution is defined as: 
* providing software to another entity, i.e., an individual or organization outside your company or organization. This is important as most open source license obligations are triggered by a distribution. Access via a web-based application is usually not considered a distribution, but some web-based applications involve the distribution of software (e.g., Javascript) and some open source licenses have obligations specifically triggered by access to software via a computer network.

1)	UB = Distribution, unmodified, binary form 
2)	MB = Distribution, modified, binary form 
3)	US = Distribution, unmodified, source form 
4)	MS = Distribution, modified, source form 

# YAML key definitions
Each license has its own block, even if the compliance profile is exactly the same as another license. 
License blocks are arranged alphabetically by licenseID.

Key definitions are as follows:

* name = full name of license, corresponds to SPDX License List full names (consistent with tag from SPDX License List XML) 
* licenseId = SPDX license identifiers (consistent with tag from SPDX License List XML) 
* notes = notes related to the license itself
* resources = external recommended resources for further information on compliance with the particular license. This is limited to only the more complex licenses and trusted resources (e.g., license authors and active community enforcers)
* terms = different types of license terms; each term item has a type (see types below) and then may have description, use-case, and compliance-notes
  * types:
    * requirement = active obligation that must be met for license compliance for the listed use-case(s)
      * acknowledgment = if there is a requirement to include specific text as an acknowledgement, then that text is included in this field. Do not use quotations for this field. If a name or other simliar text is replaceable within the acknowledgement text, it is denoted with double brackets
    * restriction = a restriction or prohibition; applies to all and any use-cases unless specific set of use-cases are identified
    * termination = license termination clause 
    * other = other clauses that are neither squarely a requireement, restriction or termination but may be necessary to be aware of for license compliance purposes; applies to all and any use-cases, specific set of use-cases as identified by coding or in description
    * license_versions = 
  * description = high-level description to explain the license term, e.g., what do you have to do to meet the requirement, what is the restriction, under what conditions does the license terminate. This field may also include specifics for the use-case where the use-case does not fit into the standard four use-cases as defined
  * use cases = the use case for which the terms (or condition) applies. These are the most common triggers for open source license conditions, but not exhaustive; if the use case or trigger does not fit in one of these categories, then it will be explained in the term description
    * UB = distribution of unmodified binary
    * MB = distribution of modified binary
    * US = distribution of unmodified source
    * MS = distribution of modified source
  *  compliance_notes = specifics of how you need to comply with the term, this is usually present for a requirement, but often not needed or applicable for a restriction
 
 
