
Thanks for your interest in the Open Source License Handbook!  We welcome input and contributions to this work.  Please review the information below related to ways and how to contribute.

Before you begin, please familiarize yourself with the [DOCUMENTATION.adoc] and other related information.  Check for [https://github.com/finos-osr/OSLC-handbook/issues](open issues) or start a discussion around a new feature idea or a bug.

# Contributor license agreements

Before making your first contribution, please first complete a [https://finosfoundation.atlassian.net/wiki/spaces/FINOS/pages/75530375/Contribution+Compliance+Requirements#ContributionComplianceRequirements-ContributorLicenseAgreement](contributor license agreement) (either a [https://www.finos.org/hubfs/FINOS/governance/FINOS%20CCLA.pdf](CCLA) or [https://www.finos.org/hubfs/FINOS/governance/FINOS%20ICLA.pdf](ICLA)) and send it to legal@finos.org. (We know CLAs are a chore, but we serve a community that places a high value on legal certainty, so we appreciate your patience.)

# Types of contributions

## Improve documentation
We've tried to explain the purpose, structure, and limitations of this handbook as clearly as possible. But if you think improvements can be made or additional information would be helpful, then do let us know by opening an issue with the proposed changes.

## Revise an existing license
Maybe you spot a typo or a better way to word something or make an entry's wording more consistent with like entries.  

## Add a new license
If there is license that is not included here, but you'd like to add the license compliance information to this handbook, great! Please create a new YAML file, following the structure as described in below and as shown in existing license YAML files.  If the new license has similar terms as an existing license included here, please copy the wording or format of the existing license as appropriate to ensure consistency. 

Please only add open source licenses, that is, licenses that meet the [https://opensource.org/osd](Open Source Definition) as defined by the Open Source Initiative (OSI); or the [https://www.gnu.org/philosophy/free-sw.en.html](4 freedoms) as defined by the Free Software Foundation (FSF). 

## Improve and expand the output formats
The `unyaml.py` script compiles the handbook into a single asciidoc file that can be readily converted into html, docbook, and pdf formats (and from docbook to docx, odt, and more). All of the output formats could use a little polishing up. And if there is an additional format you'd like to see, please help us by adding directions or a makefile to generate it.

# YAML key definitions
Each license is contained in its own YAML file, even if the compliance profile is exactly the same as another license.

Key definitions are as follows:

* name = full name of license, corresponds to SPDX License List full names (and key consistent with SPDX for XML, JSON, RDF, and tag/value)
* licenseId = SPDX license identifiers (and key consistent with SPDX for XML, JSON, RDF, and tag/value)
* notes = general notes related to the license itself
* terms = different types of license terms; each term item has a type (see types below), a description, and may also have a use-case, compliance_notes, or seeAlso. 
  * types:
    * condition = condition of the license or active requirement that must be met for license compliance for the listed use-case(s)
      * acknowledgment = if there is a requirement to include specific text as an acknowledgement, then that text is included in this field. Do not use quotations for this field. If a name or other similar text is replaceable within the acknowledgment text, it is denoted with double brackets
    * termination = license termination clause
    * other = other clauses may modify conditions or trigger requirement on different use-cases than the four defined here 
    * license_versions = information related to how other versions of the same license may be applied
  * description = high-level description to explain the license term, e.g., what do you have to do to meet the requirement, what is the condition, under what conditions does the license terminate. This field may also include specifics for the use-case where the use-case does not fit into the standard four use-cases as defined
  * use cases = the use case for which the terms (or condition) applies. These are the most common triggers for open source license conditions, but not exhaustive; if the use case or trigger does not fit in one of these categories, then it will be explained in the term description
    * UB = distribution of unmodified binary
    * MB = distribution of modified binary
    * US = distribution of unmodified source
    * MS = distribution of modified source
  * compliance_notes = specifics of how you need to comply with the term
  * seeAlso = external recommended resources for further information on compliance with the particular license term. This is limited to only the more complex terms and trusted resources (e.g., license authors and active community enforcers)

# How to contribute

First off, clone the repository locally

    clone https://github.com/finos-osr/OSLC-handbook.git

That creates an identical copy of whatever is on the online repository.

## Working with branches

Even if you have push rights to the repository, please never work on the `master` branch. Create a different branch where you can make your modifications and work without fearing to disrupt other's work.

    git checkout -b dev-yourname

It is good practice for each development item to open a specific feature branch and to work on that, so you can commit some of the changes which are ready to be merged while retaining other changes in other areas which are not ready to be pushed.

    git checkout -b dev-yourname-yourfeature

Also, keep your commits **atomic** (one commit, one thing, well described in the firs comment line):

    git add yourmodification.md
    git commit -m "content: Add Contributions section"
    git push

Note, `git add` does not just add *new* files. It also adds old file to the pipeline of files that are to be committed next, in other words, it *stages* them. If you go on modifying the file before committing it, you have three saved versions:

- one is current (unstaged)
- one is the last considered for changing (staged)
- one committed (ready to be pushed, merged)

## Merging your changes

Once you are satisfied with your changes, you can merge them in your main branch and push your branch for merging (eg with a pull request) so that the owners can appreciate your changes. Before merging make sure your branch incorporates the main changes in the `master` branch (note, developers may want to use a separate branch as the main branch and leave master alone).

    git pull
    git checkout dev-yourname

see there is no -b

    git rebase master

syncs your branch with the main branch

    git merge dev-yourname-yourfeature

optional, you can review it with -i flag

    git push  #your commits are now in your branch

Now you can open a pull request asking to incorporate your modifications. As with any open source project, contributions will be reviewed by the project team and may need some modifications to be accepted. The project team will accept or deny your modifications and resolve any conflicts (parts that have been modified by others and by you that cannot be automatically resolved by `git`).
