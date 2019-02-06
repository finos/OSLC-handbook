
# Description
This handbook provides information on how to comply with some of the more common open source licenses under a specific set of use-cases. The goal here is to provide developers and engineers with some "self-serve" information to facilitate the end goal of open source license compliance, particularly for the easy-to-comply with conditions in open source licenses.  This handbook also aims to help identify some of the more complex open source license compliance conditions for which consultation with open source counsel may be needed.

Determining the requirements that need to be met to comply with open source licenses involves:
1) You must know what open source software you are using
2) You must know what license applies to that open source software and the relevant legal interpretation of the license; and
3) How are you using that open source software? This is the “use-case”.

The information in this handbook assumes you have already met #1 in determining what open source software you are using (and under what license). It is the combination of the license (#2) and the use-case (#3) which determines what license conditions are triggered. This is open source license compliance.

One way to think of this is as an if-then statement. For example: IF I am distributing unmodified open source software in binary form (use-case), THEN I must provide a copy of the license (requirement) by (HOW) placing a copy with my distribution.

Some open source license conditions are easy to understand and comply with, while other conditions are open for (legal) interpretation or involve more complex use-cases that cannot be easily categorized. The license compliance requirements in this handbook are summarized for the four most common use-cases as listed below. 

This handbook only provides license compliance information for licenses and use-cases that are easy to understand and summarize succinctly.  Cases where further analysis or consultation with your open source counsel may be needed are noted.  Likewise, if your use-case varies in any way or you are using a different license than those licenses listed here (even if it seems similar) or you have any questions whatsoever about this information or how to properly comply, please contact your open source counsel.

Other terms not related to license compliance are not captured here. For example, choice of law, jurisdiction, statutory references, or passive representations. Some open source licenses provide explicit clarification that no trademark license is granted; as this is essentially a restatement of basic trademark law and does not require any license compliance action, these clauses are not captured here. Likewise, information describing the license grants are not captured here. As always, your open source counsel should familiarize themself with the entire license before relying on the information provided in this handbook.

## Use-case:
Distribution is defined as:

> providing software to another entity, i.e., an individual or organization outside your company or organization. 

This is important as most open source license obligations are triggered by a distribution. Some web-based applications involve the distribution of software (e.g., Javascript). Access via a web-based application is usually not considered a distribution, however some open source licenses have obligations specifically triggered by access to software via a computer network; these are captured via the "other" term type.

1)	UB = Distribution, unmodified, binary form
2)	MB = Distribution, modified, binary form
3)	US = Distribution, unmodified, source form
4)	MS = Distribution, modified, source form

Where "binary" refers to compiled code, binary, executable, non-source form; and "source" refers to the human readable, editable form.

# YAML key definitions
Each license has its own block, even if the compliance profile is exactly the same as another license.
License blocks are arranged alphabetically by licenseID.  See https://github.com/jlovejoy/OSLC-handbook/blob/master/example.yaml for an example of keys and license block formatting.

Key definitions are as follows:

* name = full name of license, corresponds to SPDX License List full names (consistent with tag from SPDX License List XML)
* licenseId = SPDX license identifiers (consistent with tag from SPDX License List XML)
* parent-licenseId = SPDX license identifier for over-arching license where the licenseId here refers to an exception to a license condition or additional permissions beyond those granted in the parent license. In this case, the parent-licenseId and the licenseId would be combined with the SPDX license operator, WITH, to create the complete SPDX license expression
* notes = notes related to the license itself
* resources = external recommended resources for further information on compliance with the particular license. This is limited to only the more complex licenses and trusted resources (e.g., license authors and active community enforcers)
* terms = different types of license terms; each term item has a type (see types below), a description, and may also have a use-case and compliance_notes
  * types:
    * requirement = active obligation that must be met for license compliance for the listed use-case(s)
      * acknowledgment = if there is a requirement to include specific text as an acknowledgement, then that text is included in this field. Do not use quotations for this field. If a name or other similar text is replaceable within the acknowledgment text, it is denoted with double brackets
    * restriction = a restriction or prohibition; applies to all and any use-cases unless specific set of use-cases are identified
    * termination = license termination clause
    * other = other clauses that are neither squarely a requirement, restriction or termination but may be necessary to be aware of for license compliance purposes; applies to all and any use-cases, specific set of use-cases as identified by coding or in description
    * license_versions = information related to how other versions of the same license may be applied
  * description = high-level description to explain the license term, e.g., what do you have to do to meet the requirement, what is the restriction, under what conditions does the license terminate. This field may also include specifics for the use-case where the use-case does not fit into the standard four use-cases as defined
  * use cases = the use case for which the terms (or condition) applies. These are the most common triggers for open source license conditions, but not exhaustive; if the use case or trigger does not fit in one of these categories, then it will be explained in the term description
    * UB = distribution of unmodified binary
    * MB = distribution of modified binary
    * US = distribution of unmodified source
    * MS = distribution of modified source
  *  compliance_notes = specifics of how you need to comply with the term, this is usually present for a requirement, but often not needed or applicable for a restriction
