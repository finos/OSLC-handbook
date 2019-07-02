Overview
========

This handbook provides information on how to comply with some common
open source licenses under a specific set of use-cases. The goal here is
to provide developers and engineers with some "self-serve" information
to facilitate the end goal of open source license compliance,
particularly for the easy-to-comply with conditions in open source
licenses. This handbook also aims to help identify some of the more
complex open source license compliance conditions for which consultation
with open source counsel may be needed.

Open source license compliance explained
----------------------------------------

Determining the requirements that need to be met to comply with open
source licenses involves the following:

1.  You must know what open source software you are using;

2.  You must know what license applies to that open source software and
    the relevant legal interpretation of the license; and

3.  You must know how you using that open source software. This is the
    “use-case”.

The information in this handbook assumes you have already determined
what open source software you are using and under what license (\#1 and
\#2). It is the combination of the license (\#2) and the use-case (\#3)
which determines what license conditions are triggered. This is open
source license compliance.

One way to think of this is as an if-then statement. For example: IF I
am distributing unmodified open source software in binary form
(use-case), THEN I must provide a copy of the license (requirement) by
(HOW) placing a copy with my distribution.

Scope of this handbook
----------------------

Some open source license conditions are easy to understand and comply
with, while other conditions are open for (legal) interpretation or
involve more complex use-cases that cannot be easily categorized. The
license compliance requirements in this handbook are summarized for the
four most common use-cases as listed below. License terms or conditions
where further analysis or consultation with your open source counsel may
be needed are noted. For these license terms or conditions, external
references that may be helpful are provided in the seeAlso key.
Likewise, if your use-case varies in any way or you are using a
different license than those licenses listed here (even if it seems
similar) or you have any questions about this information or how to
properly comply, please contact your open source counsel.

Other terms not related to license compliance are not captured here. For
example, choice of law, jurisdiction, statutory references, or licensee
representations. Some open source licenses provide explicit
clarification that no trademark license is granted; as this is
essentially a restatement of basic trademark law and does not require
any license compliance action, these clauses are not captured here.
Likewise, information describing the license grants are not captured
here. As always, your open source counsel should familiarize themself
with the entire license before relying on the information provided in
this handbook.

Use Cases
---------

>     providing software to another entity, i.e., an individual or organization outside your company or organization.

This is important as most open source license obligations are triggered
by a distribution. Some web-based applications involve the distribution
of software (e.g., Javascript). Access via a web-based application is
usually not considered a distribution, however some open source licenses
have obligations specifically triggered by access to software via a
computer network; these are captured via the "other" term type.

1.  UB = Distribution, unmodified, binary form

2.  MB = Distribution, modified, binary form

3.  US = Distribution, unmodified, source form

4.  MS = Distribution, modified, source form

Where "binary" refers to compiled code, binary, executable, non-source
form; and "source" refers to the human readable, editable form.

Copyright and License Notice
----------------------------

© 2019 Fintech Open Source Foundation, Jilayne Lovejoy, and other
contributors. This document is licensed under the terms of the [Creative
Commons Attribution-ShareAlike (CC By-SA) License, version
4.0](https://creativecommons.org/licenses/by-sa/4.0/). It is offered
as-is and as-available, without representation or warranty of any kind,
whether express, implied, statutory, or other. The original version of
this document is available at
<https://github.com/finos-osr/OSLC-handbook/>. Any modified version must
indicate modifications. This notice and disclaimer must be retained on
any copies and derivative works.

Licenses
========

BSD Zero Clause License
-----------------------

SPDX License ID  
[0BSD](https://spdx.org/licenses/0BSD.html)

Notes  
This is a blanket license with no conditions.

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>This license places no conditions whatsoever on using, copyring, modifying or distributing the software for any purpose.</p></td>
</tr>
</tbody>
</table>

GNU Affero General Public License 3.0
-------------------------------------

SPDX License IDs  
[AGPL-3.0-only](https://spdx.org/licenses/AGPL-3.0-only.html)  
[AGPL-3.0-or-later](https://spdx.org/licenses/AGPL-3.0-or-later.html)  

Notes  
AGPL-3.0 is the same license as GPL-3.0, but with an additional term in
section 13 which imposes a requirement for a modified version accessed
via remote computer network. AGPL-3.0 provides the option to use either
that version of the license only or to make it available under any later
version of that license. This is denoted in the standard license header
and by using AGPL-3.0-only or AGPL-3.0-or-later.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>It must be an actual copy of the license not a website link</p></td>
</tr>
<tr class="even">
<td><p>Retain notices on all files</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Source files usually have a standard license header that includes a copyright notice and disclaimer of warranty. This is also where you determine if the license is “or later” or the specific version only</p></td>
</tr>
<tr class="odd">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Modified files must have “prominent notices that you changed the files” and a date</p></td>
</tr>
<tr class="even">
<td><p>Modifications or derivative work must be licensed under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Strong copyleft or reciprocal, project-based license meaning that derivative works must also be under AGPL-3.0. For more information about AGPL-3.0 compliance and this condition in particular (which is the same as for GPL-3.0), see the references provided or consult with your open source legal counsel.</p></td>
</tr>
<tr class="odd">
<td><p>Provide corresponding source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Corresponding Source = all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. Options for providing source = with binary, written offer, or via a network server. See section 6 for more details. For more information about AGPL-3.0 compliance and this condition in particular, see the references provided or consult your open source legal counsel.</p></td>
</tr>
<tr class="even">
<td><p>No additional restrictions</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You may not impose any further restrictions on the exercise of the rights granted under this license.</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License automatically terminates if you do not comply with the terms of the license</p></td>
</tr>
<tr class="even">
<td><p>License terminates if you initiate litigation claiming use of the program under this license violates a patent</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license or that version only, as specified. If no license version is specificed, then you may use any version ever published by the FSF.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide information necessary to install modified versions on <em>User Products</em></p></td>
<td><p>If convey object code in, with, or specificially for use in a User Product and the right of possession for the User Product is tranferred as part of the conveyance, then the corresponding source code must include Installation Information (methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source) (see section 6 for more details)</p></td>
</tr>
</tbody>
</table>

Apache Software License 1.1
---------------------------

SPDX License ID  
[Apache-1.1](https://spdx.org/licenses/Apache-1.1.html)

Notes  
Apache-1.1 and Entessa are essentially the same license (as per SPDX
License List Matching Guidelines). Because the OSI approved them
separately, they are listed separately (here and on the SPDX License
List).

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="odd">
<td><p>Acknowledgement must be included in end-user documentation, in software or wherever third-party acknowledgments appear</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Name of project cannot be used for derived products without permission</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

Apache Software License 2.0
---------------------------

SPDX License ID  
[Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Does not specify format for providing copy of license</p></td>
</tr>
<tr class="even">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Modified files must include &quot;prominent notices&quot; of the modifications</p></td>
</tr>
<tr class="odd">
<td><p>Retain all notices</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Copyright notices and other notices do not have to be reproduced for binary distribution</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Any patent claims accusing the work by a licensee results in termination of all patent licenses to the licensee.</p></td>
</tr>
</tbody>
</table>

Artistic License 1.0 (Perl)
---------------------------

SPDX License ID  
[Artistic-1.0-Perl](https://spdx.org/licenses/Artistic-1.0-Perl.html)

Notes  
This is the Artistic License 1.0 found on the Perl site, which is
different (particularly, clauses 5, 6, 7 and 8) than the Artistic
License 1.0 w/clause 8 found on the OSI site. This license has specific
use cases and conditions that are difficult to summarize; please see
sections 5-8 and relevant definitions for more details.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Retain all notices</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>Copyright notices and other notices</p></td>
</tr>
<tr class="even">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Modified files must have &quot;prominent notice&quot; in each file stating how the file was modified and when</p></td>
</tr>
<tr class="odd">
<td><p>Provide access to modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Do at least one of the following: place modification in the public domain or otherwise make them freely available; OR rename non-standard executables; OR &quot;make other distribution arrangements&quot; with the copyright holder (see section 3 for more details).</p></td>
</tr>
<tr class="even">
<td><p>Access to source</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Do at least one of the following: provide a Standard Version of the executables and library files; OR provide source for your modifications; OR give non-standard executables non-standard name and document the differences with instructions on where to get the Standard Version; OR &quot;make other distribution arrangements&quot; with the copyright holder (see section 4 for more details)</p></td>
</tr>
<tr class="odd">
<td><p>You may distribute this package as part of a larger (commercial) distribution, but cannot charge a fee for the standalone package. You may charge a reasonable fee for copying or support.</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The following are not considered part of the package or do not fall under copyright of this package and subject to the license: scripts and library files supplied as input to or produced as output from the program; C subroutines (or comparably compiled subroutines in other languages) supplied by you and linked into this Package in order to emulate subroutines and variables of the language defined by this package; aggregation of this package with other software where the package is embedded and the interfaces are not visible to the end user (see sections 6, 7, and 8 for more details)</p></td>
</tr>
</tbody>
</table>

Artistic License 2.0
--------------------

SPDX License ID  
[Artistic-2.0](https://spdx.org/licenses/Artistic-2.0.html)

Notes  
This license has specific use cases and conditions that are difficult to
summarize; please see sections 4-9 and relevant definitions for more
details.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Retain all notices</p></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>Copyright notices and other notices</p></td>
</tr>
<tr class="even">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Document how the modified version differs from the standard version</p></td>
</tr>
<tr class="odd">
<td><p>Provide access to modified version</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Do at least one of the following: make modified version available to copyright holder under same license; OR ensure modified version does not prevent user from installing or running standard version and use different name; OR allow any recipients of modified version to make source available to others under same license or a similarly free/open license (see section 4 for more details)</p></td>
</tr>
<tr class="even">
<td><p>Access to source</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td></td>
<td><p>Provide complete instructions on how to get source for standard version; instructions must be kept current for your distribution</p></td>
</tr>
<tr class="odd">
<td><p>You may distribute this package as part of a larger (commercial) distribution, but cannot charge a licensing fee for the standalone package. You may charge distributor fees or licensing fees for other components in the distribution.</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Any patent claims accusing the work by a licensee results in termination of all licenses to the licensee</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Modified or standard versions linked with other works; embedding the package in a larger work of your own; or stand-alone binary or bytecode versions of applications that include the package may be distributed without restriction provided the result does not expose a direct interface to the package. See sections 8 for more details.</p></td>
</tr>
<tr class="even">
<td><p>Works that merely extend or make use of the package do not cause the package to be a modified version, are not considered parts of the package itself, and are not subject to the terms of this license. See section 9 for more details.</p></td>
</tr>
</tbody>
</table>

BSD 2-Clause "Simplified" License
---------------------------------

SPDX License ID  
[BSD-2-Clause](https://spdx.org/licenses/BSD-2-Clause.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
</tbody>
</table>

BSD 3-Clause "New" or "Revised" License
---------------------------------------

SPDX License ID  
[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
</tbody>
</table>

BSD-4-Clause (University of California-Specific)
------------------------------------------------

SPDX License ID  
[BSD-4-Clause-UC](https://spdx.org/licenses/BSD-4-Clause-UC.html)

Notes  
The advertising clause was rescinded by the University of California in
1999 for all material under BSD-4-Clause with University of California
copyright notice. Thus, you do not need to comply with the
advertising/acknowledgment requirement, which makes the license
essentially BSD-3-Clause.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
</tbody>
</table>

BSD 4-Clause "Original" or "Old" License
----------------------------------------

SPDX License ID  
[BSD-4-Clause](https://spdx.org/licenses/BSD-4-Clause.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="odd">
<td><p>Advertising materials &quot;mentioning the features or use of this software&quot; must include acknowledgment</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Boost Software License 1.0
--------------------------

SPDX License ID  
[BSL-1.0](https://spdx.org/licenses/BSL-1.0.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For distributions “of machine-executable object code generated by a source language processor” (i.e., UB and MB use cases), these requirements need not be met. However, you might consider the need to identify the presence of software under BSL-1.0 for other reasons, especially if you have an agreement that wraps around this code/license.</p></td>
</tr>
</tbody>
</table>

Common Development and Distribution License 1.0
-----------------------------------------------

SPDX License ID  
[CDDL-1.0](https://spdx.org/licenses/CDDL-1.0.html)

Notes  
Versions 1.0 and 1.1 are essentially the same, except v1.1 adds a patent
infringement clause and choice of law.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Provide source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>You must inform recipients of how they can obtain source code “in a reasonable manner on or through a medium customarily used for software exchange”, including your modifications, if any</p></td>
</tr>
<tr class="odd">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Provide notice of your modifications that identifies you as the contributor of the modification</p></td>
</tr>
<tr class="even">
<td><p>Modifications under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>File-level reciprocal license meaning that modifications to any file or new files that contain part of original software are governed by the terms of this license. Larger works may be created by combining covered software with code not governed by this license, so long as you comply with this license for the covered software (see sections 1.6, 1.9, and 3.6 for more information)</p></td>
</tr>
<tr class="odd">
<td><p>No additional restrictions</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You may not impose any terms on source code that alters or restricts recipient’s rights under this license</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License terminates upon failure to comply with license after a 30 day cure period</p></td>
</tr>
<tr class="even">
<td><p>Any patent claims accusing the software by a licensee results in termination of patent licenses to the licensee, with a 60 day cure (see section 6.2 for more details)</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of of same version or any later version of the license, unless the version you received states otherwise.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>You may offer and charge a fee for warranty, support, indemnity or liability obligations to recipients. However, you must make it clear that any such offer is offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.4 for more details.</p></td>
</tr>
<tr class="even">
<td><p>You may distribute binary versions under a different license, so long as you do not limit or alter the recipient’s right in the source code under this license. You must make it clear that any differing terms are offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make (see section 3.6 for more details).</p></td>
</tr>
</tbody>
</table>

Common Development and Distribution License 1.1
-----------------------------------------------

SPDX License ID  
[CDDL-1.1](https://spdx.org/licenses/CDDL-1.1.html)

Notes  
Versions 1.0 and 1.1 are essentially the same, except v1.1 adds a patent
infringement clause and choice of law.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Provide source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>You must inform recipients of how they can obtain source code “in a reasonable manner on or through a medium customarily used for software exchange”, including your modifications, if any</p></td>
</tr>
<tr class="odd">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Provide notice of your modifications that identifies you as the contributor of the modification</p></td>
</tr>
<tr class="even">
<td><p>Modifications under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>File-level reciprocal license meaning that modifications to any file or new files that contain part of original software are governed by the terms of this license. Larger works may be created by combining covered software with code not governed by this license, so long as you comply with this license for the covered software (see sections 1.6, 1.9, and 3.6 for more details)</p></td>
</tr>
<tr class="odd">
<td><p>No additional restrictions</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You may not impose any terms on source code that alters or restricts recipient’s rights under this license</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License terminates upon failure to comply with license after a 30 day cure period</p></td>
</tr>
<tr class="even">
<td><p>Any patent claims accusing the software by a licensee results in termination of patent licenses to the licensee, with a 60 day cure. If such claim is resolved (such as by license or settlement) prior to the initiation of patent infringement litigation, then the reasonable value of the licenses granted by such parties in this license shall be taken into account in determining the amount or value of any payment or license (see section 6.2 and 6.3 for more details).</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license, unless the version you received states otherwise.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>You may offer and charge a fee for warranty, support, indemnity or liability obligations to recipients. However, you must make it clear that any such offer is offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make (see section 3.4 for more details)</p></td>
</tr>
<tr class="even">
<td><p>You may distribute binary versions under a different license, so long as you do not limit or alter the recipient’s right in the source code under this license. You must make it clear that any differing terms are offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make (see section 3.6 for more details)</p></td>
</tr>
</tbody>
</table>

Entessa Public License 1.0
--------------------------

SPDX License ID  
[Entessa](https://spdx.org/licenses/Entessa.html)

Notes  
Apache-1.1 and Entessa are essentially the same license (as per SPDX
License List Matching Guidelines). Because the OSI approved them
separately, they are listed separately (here and on the SPDX License
List).

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="odd">
<td><p>Acknowledgement must be included in end-user documentation, in software or wherever third-party acknowledgments appear</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Name of project cannot be used for derived products without permission</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

Eclipse Public License 1.0
--------------------------

SPDX License ID  
[EPL-1.0](https://spdx.org/licenses/EPL-1.0.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>A copy of the license must be included with each copy of the program. While there is no explicit language requiring a copy of the license for a binary distribution, one would need to identify this license to meet other requirements, thus some reference to the license is practically necessary.</p></td>
</tr>
<tr class="even">
<td><p>Retain notices</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You must retain license notices with every source code distribution or include notices in another likely location</p></td>
</tr>
<tr class="odd">
<td><p>Provide source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Must inform recipients how to obtain source code by reasonable manner via a &quot;medium customarily used for software exchange&quot;</p></td>
</tr>
<tr class="even">
<td><p>Notice of contributions</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Include a note that identifies contributor as the originator of its contribution</p></td>
</tr>
<tr class="odd">
<td><p>Modifications under same license</p></td>
<td></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>File-level reciprocal license meaning that modifications to any file or new files that contain part of original software are governed by the terms of this license. This does not include additional separate software modules that are distributed with the program and are not derivative works of the program (see sections 1 and 3 for more details)</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License terminates upon failure to comply with &quot;material terms or conditions&quot; and failure to cure in a reasonable period of time after becoming aware of noncompliance</p></td>
</tr>
<tr class="even">
<td><p>Any patent claims accusing the software by a licensee results in termination of patent licenses to the licensee</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>You may distribute binary versions under a different license, provided you disclaim contributors from warranties, liability, and defend contributors against any third party claims brought as a result of your distribution. Clarify that any provisions offered by you are offered by you only (see section 3 and 4 for details)</p></td>
</tr>
</tbody>
</table>

Eclipse Public License 2.0
--------------------------

SPDX License ID  
[EPL-2.0](https://spdx.org/licenses/EPL-2.0.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide license</p></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Accompany the program with a statement that the source code if available under the license. For source code distributions, must provide a copy of the license.</p></td>
</tr>
<tr class="even">
<td><p>Provide source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Must inform recipients how to obtain source code by reasonable manner via a &quot;medium customarily used for software exchange&quot;</p></td>
</tr>
<tr class="odd">
<td><p>Modifications under same license</p></td>
<td></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>File-level reciprocal license meaning that modifications to any file or new files that contain part of original software are governed by the terms of this license. This does not include additional separate software modules that are distributed with the program and are not derivative works of the program (see sections 1 and 3.2 for more details)</p></td>
</tr>
<tr class="even">
<td><p>Retain notices</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You must retain license notices with every source code distribution or include notices in another likely location</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License terminates upon failure to comply with &quot;material terms or conditions&quot; and failure to cure in a reasonable period of time after becoming aware of noncompliance</p></td>
</tr>
<tr class="even">
<td><p>Any patent claims accusing the software by a licensee results in termination of patent licenses to the licensee</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>You may distribute program under a different license, provided you disclaim contributors from warranties, liability, and defend contributors against any third party claims brought as a result of your distribution. Clarify that any provisions offered by you are offered by you only (see section 3 for details)</p></td>
</tr>
<tr class="even">
<td><p>You may distribute under an enumerated <em>Secondary License</em> if authorized by the initial Contributor or combined with code under that Secondary License (see section 3.2 for more details)</p></td>
</tr>
</tbody>
</table>

GNU General Public License 2.0
------------------------------

SPDX License IDs  
[GPL-2.0-only](https://spdx.org/licenses/GPL-2.0-only.html)  
[GPL-2.0-or-later](https://spdx.org/licenses/GPL-2.0-or-later.html)  

Notes  
GPL-2.0 provides the option to use either that version of the license
only or to make it available under any later version of that license.
This is denoted in the standard license header and by using GPL-2.0-only
or GPL-2.0-or-later

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>It must be an actual copy of the license not a website link</p></td>
</tr>
<tr class="even">
<td><p>Retain notices on all files</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Source files usually have a standard license header that includes a copyright notice and disclaimer of warranty. This is also where projects typically indicate if the -or-later version option is available.</p></td>
</tr>
<tr class="odd">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Modified files must have “prominent notices that you changed the files” and a date</p></td>
</tr>
<tr class="even">
<td><p>Modifications or derivative work must be licensed under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Strong copyleft or reciprocal, project-based license meaning that derivative works must also be under GPL-2.0. For more information about GPL-2.0 compliance and this condition in particular, see the references provided or consult your open source legal counsel.</p></td>
</tr>
<tr class="odd">
<td><p>Provide corresponding source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Corresponding Source = all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. Options for providing source = with binary, written offer (see section 3 for more details). For more information about GPL-2.0 compliance and this condition in particular, see the references provided or consult your open source legal counsel.</p></td>
</tr>
<tr class="even">
<td><p>No additional restrictions</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You may not impose any further restrictions on the exercise of the rights granted under this license.</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License automatically terminates if you do not comply with the terms of the license</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license or that version only, as specified. If no license version is specified, then you may use any version ever published by the FSF.</p></td>
</tr>
</tbody>
</table>

GNU General Public License 3.0
------------------------------

SPDX License IDs  
[GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html)  
[GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)  

Notes  
GPL-3.0 provides the option to use either that version of the license
only or to make it available under any later version of that license.
This is denoted in the standard license header and by using GPL-3.0-only
or GPL-3.0-or-later. For a comparison of GPL-3.0 to GPL-2.0, see
[Copyleft Guide: Understanding GPLv3 As An Upgraded
GPLv2](http://copyleft.org/guide/comprehensive-gpl-guidech10.html#x13-610009)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>It must be an actual copy of the license not a website link</p></td>
</tr>
<tr class="even">
<td><p>Retain notices on all files</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Source files usually have a standard license header that includes a copyright notice and disclaimer of warranty. This is also were you determine if the license is “or later” or the specific version only</p></td>
</tr>
<tr class="odd">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Modified files must have “prominent notices that you changed the files” and a date</p></td>
</tr>
<tr class="even">
<td><p>Modifications or derivative work must be licensed under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Strong copyleft or reciprocal, project-based license meaning that derivative works must also be under GPL-3.0. For more information about GPL-3.0 compliance and this condition in particular, see the references provided or consult with your open source legal counsel.</p></td>
</tr>
<tr class="odd">
<td><p>Provide corresponding source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Corresponding Source = all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. Options for providing source = with binary, written offer, or via a network server (see section 6 for more details). For more information about GPL-3.0 compliance and this condition in particular, see the references provided or consult your open source legal counsel.</p></td>
</tr>
<tr class="even">
<td><p>May not prohibit circumvention of technological measures that prevent users from exercising rights under the license (see section 3 for more details)</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>No additional restrictions</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You may not impose any further restrictions on the exercise of the rights granted under this license.</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License automatically terminates if you do not comply with the terms of the license</p></td>
</tr>
<tr class="even">
<td><p>License terminates if you initiate litigation claiming use of the program under this license violates a patent</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license or that version only, as specified. If no license version is specificed, then you may use any version ever published by the FSF.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Author may include <em>additional permissions</em> making exceptions from license terms. You may remove additional permission when you convey the work.</p></td>
<td><p>Contributors may add certain additional restrictions for their contributions, including disclaimers, legal notices, limitation of trademark and publicity rights, extension of indemnification received by licensor.</p></td>
</tr>
<tr class="even">
<td><p>Provide information necessary to install modified versions on <em>User Products</em></p></td>
<td><p>If convey object code in, with, or specificially for use in a User Product and the right of possession for the User Product is tranferred as part of the conveyance, then the corresponding source code must include Installation Information (methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source) (see section 6 for more details)</p></td>
</tr>
</tbody>
</table>

ISC License
-----------

SPDX License ID  
[ISC](https://spdx.org/licenses/ISC.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>This information must appear &quot;in all copies&quot;</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>This information must appear &quot;in all copies&quot;</p></td>
</tr>
</tbody>
</table>

GNU Library General Public License 2.0
--------------------------------------

SPDX License IDs  
[LGPL-2.0-only](https://spdx.org/licenses/LGPL-2.0-only.html)  
[LGPL-2.0-or-later](https://spdx.org/licenses/LGPL-2.0-or-later.html)  

Notes  
LGPL-2.0 and LGPL-2.1 are the same substantive license except for the
addition of section 6(b) in LGPL-2.1.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>It must be an actual copy of the license not a website link</p></td>
</tr>
<tr class="even">
<td><p>Retain notices on all files</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Source files usually have a standard license header that includes a copyright notice and disclaimer of warranty. This is also were you determine if the license is “or later” or the specific version only</p></td>
</tr>
<tr class="odd">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Modified files must have “prominent notices that you changed the files” and a date</p></td>
</tr>
<tr class="even">
<td><p>Modifications or derivative work must be licensed under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Derivative works of the library must also be under LGPL (this usually includes statically linked code).</p></td>
</tr>
<tr class="odd">
<td><p>Provide corresponding source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>complete source code = all the source code for all modules it contains, plus any associated interface definition files, plus the scripts used to control compilation and installation of the library (see section 4 or section 6, as applicable).</p></td>
</tr>
<tr class="even">
<td><p>No additional restrictions</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You may not impose any further restrictions on the exercise of the rights granted under this license.</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License automatically terminates if you do not comply with the terms of the license</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license or that version only, as specified. If no license version is specificed, then you may use any version ever published by the FSF.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows dynamic linking of code with “a work that uses the Library” under a different license, under certain conditions.</p></td>
<td><p>Terms of the other license must permit reverse engineering and debugging; must provide a copy of the license and prominent notice that the Library is used; must provide source code via one of the options in section 6 of the license. Also must include any data and utility programs needed for reproducing the executable, but this need not include anything that is normally distributed with the major components of the operating system. For more information about LGPL-2.0 compliance and this condition in particular, see the references provided or consult your open source legal counsel.</p></td>
</tr>
</tbody>
</table>

GNU Lesser General Public License 2.1
-------------------------------------

SPDX License IDs  
[LGPL-2.1-only](https://spdx.org/licenses/LGPL-2.1-only.html)  
[LGPL-2.1-or-later](https://spdx.org/licenses/LGPL-2.1-or-later.html)  

Notes  
LGPL-2.0 and LGPL-2.1 are the same substantive license except for the
addition of section 6(b) in LGPL-2.1.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>It must be an actual copy of the license not a website link</p></td>
</tr>
<tr class="even">
<td><p>Retain notices on all files</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Source files usually have a standard license header that includes a copyright notice and disclaimer of warranty. This is also were you determine if the license is “or later” or the specific version only</p></td>
</tr>
<tr class="odd">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Modified files must have “prominent notices that you changed the files” and a date</p></td>
</tr>
<tr class="even">
<td><p>Modifications or derivative work must be licensed under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Derivative works of the library must also be under LGPL (this usually includes statically linked code).</p></td>
</tr>
<tr class="odd">
<td><p>Provide corresponding source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>complete source code = all the source code for all modules it contains, plus any associated interface definition files, plus the scripts used to control compilation and installation of the library (see section 4 or section 6, as applicable).</p></td>
</tr>
<tr class="even">
<td><p>No additional restrictions</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You may not impose any further restrictions on the exercise of the rights granted under this license.</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License automatically terminates if you do not comply with the terms of the license</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license or that version only, as specified. If no license version is specificed, then you may use any version ever published by the FSF.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows dynamic linking of code with “a work that uses the Library” under a different license, under certain conditions.</p></td>
<td><p>Terms of the other license must permit reverse engineering and debugging; must provide a copy of the license and prominent notice that the Library is used; must provide source code via one of the options in section 6 of the license. Also must include any data and utility programs needed for reproducing the executable, but this need not include anything that is normally distributed with the major components of the operating system. For more information about LGPL-2.1 compliance and this condition in particular, see the references provided or consult your open source legal counsel.</p></td>
</tr>
</tbody>
</table>

GNU Lesser General Public License 3.0
-------------------------------------

SPDX License IDs  
[LGPL-3.0-only](https://spdx.org/licenses/LGPL-3.0-only.html)  
[LGPL-3.0-or-later](https://spdx.org/licenses/LGPL-3.0-or-later.html)  

Notes  
LGPL-3.0 incorporates the terms of GPL-3.0 and supplements the parent
license with the terms listed here.

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of of same version or any later version of the license or that version only, as specified. If no license version is specificed, then you may use any version ever published by the FSF.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>If you modify the library so that it does not function without data or function supplied by your application, the modified library can only be distributed under the terms of GPL-3.0. This restriction does not apply if the data or function is supplied as an argument.</p></td>
<td><p>Object code incorporating header file material from the library that is not limited to numerical parameters, data structure layouts and accessors or small macros, inline functions and templates of fewer than ten lines must include a prominent notice that the library is used, its use is covered by LGPL-3.0, and provide a copy of the license (see section 3 for more details)</p></td>
</tr>
<tr class="even">
<td><p>Allows distribution of combined LGPL-3.0 and other code under under a different license, under certain conditions.</p></td>
<td><p>Allows use of a &quot;suitable shared library mechanism&quot; (including dynamic linking) to combine the LGPL-3.0 code with non-LGPL-3.0 code, so long as the source code is provided to allow the user to recombine or relink the application with a modified version of the LGPL-3.0 library. This must include installation information as defined in GPL-3.0, if necessary to install and execute a modified version of the combined work (see sections 4d and 4e for more details). For more information about LGPL-3.0 compliance and this condition in particular, see the references provided or consult your open source legal counsel.</p></td>
</tr>
</tbody>
</table>

libpng License
--------------

SPDX License ID  
[Libpng](https://spdx.org/licenses/Libpng.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Modified verions must be &quot;plainly marked as such&quot; and not misrepresented as the original software</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Copyright notices may not be removed or altered for any source distribution</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The origin of the code must not be misrepresented</p></td>
</tr>
</tbody>
</table>

CMU License
-----------

SPDX License ID  
[MIT-CMU](https://spdx.org/licenses/MIT-CMU.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, provide this information &quot;in supporting documentation&quot;</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, provide this information &quot;in supporting documentation&quot;</p></td>
</tr>
</tbody>
</table>

MIT License
-----------

SPDX License ID  
[MIT](https://spdx.org/licenses/MIT.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>This information &quot;shall be included in all copies or substantial portions of the Software&quot;. Some people interpret MIT as not implicating these requirements for binary distribution (e.g., UB and MB), but this is not the prevailing view and best practice is to include it.</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>This information &quot;shall be included in all copies or substantial portions of the Software&quot;.Some people interpret MIT as not implicating these requirements for binary distribution (e.g., UB and MB), but this is not the prevailing view and best practice is to include it.</p></td>
</tr>
</tbody>
</table>

Mozilla Public License 1.0
--------------------------

SPDX License ID  
[MPL-1.0](https://spdx.org/licenses/MPL-1.0.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You must include a copy of the license with every source code distribution</p></td>
</tr>
<tr class="even">
<td><p>Retain notices</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You must retain license notices with every source code distribution or include notices in another likely location</p></td>
</tr>
<tr class="odd">
<td><p>Provide source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Provide source code on same media as binary or make available via other electronic distribution mechanism for 12 months after initial availability or at least 6 months after a subsequent version has been made available. See section 3.2 for more details.</p></td>
</tr>
<tr class="even">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Document changes you made and date; include a prominent statement as to the origin of the original code. See section 3.3 for more details.</p></td>
</tr>
<tr class="odd">
<td><p>Modifications under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>File-level reciprocal license meaning that modifications to any file or new files that contain part of original software are governed by the terms of this license. Larger works may be created by combining covered software with code not governed by this license, so long as you comply with this license for the covered software (see sections 1.10 and 3.7 for more details)</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License terminates upon failure to comply with license after a 30 day cure period</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of of same version or any later version of the license.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide notice in a file called &quot;LEGAL&quot; containing any third party intellectual property rights for particular functionality or code, including if your modifications are an application programming intereface and you own or control patents which are reasonably necessary to implement the API. See section 3.4 for more details.</p></td>
</tr>
<tr class="even">
<td><p>You may offer and charge a fee for warranty, support, indemnity or liability obligations to recipients. However, you must make it clear that any such offer is offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.5 for more details.</p></td>
</tr>
<tr class="odd">
<td><p>You may distribute binary versions under a different license, so long as you do not limit or alter the recipient’s right in the source code under this license. You must make it clear that any differing terms are offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.6 for more details.</p></td>
</tr>
<tr class="even">
<td><p>If it is impossible for you to comply with any of the terms of this license due to statute or regulation then you must comply with the terms of this License to the maximum extent possible; and describe the compliance limitations and the code they affect and include such description in all distributions of the source code (see section 3.4 for more details)</p></td>
</tr>
</tbody>
</table>

Mozilla Public License 1.1
--------------------------

SPDX License ID  
[MPL-1.1](https://spdx.org/licenses/MPL-1.1.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You must include a copy of the license with every source code distribution</p></td>
</tr>
<tr class="even">
<td><p>Retain notices</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You must retain license notices with every source code distribution or include notices in another likely location</p></td>
</tr>
<tr class="odd">
<td><p>Provide source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Provide source code on same media as binary or make available via other electronic distribution mechanism for 12 months after initial availability or at least 6 months after a subsequent version has been made available. See section 3.2 for more details.</p></td>
</tr>
<tr class="even">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Document changes you made and date; include a prominent statement as to the origin of the original code. See section 3.3 for more details.</p></td>
</tr>
<tr class="odd">
<td><p>Modifications under same license</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>File-level reciprocal license meaning that modifications to any file or new files that contain part of original software are governed by the terms of this license. Larger works may be created by combining covered software with code not governed by this license, so long as you comply with this license for the covered software (see sections 1.9 and 3.7 for more details)</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License terminates upon failure to comply with license after a 30 day cure period</p></td>
</tr>
<tr class="even">
<td><p>Any patent claims accusing the software by a licensee results in termination of all licenses to the licensee, with a 60 day cure. Any patent claims by a licensee accusing any contributor results in termination of all of that contributor’s patent licenses (see section 8.2 and 8.3 for more details).</p></td>
</tr>
<tr class="odd">
<td><p>If you initiate a patent infringement litigation against the initial developer or a contributor alleging that any software, hardware or device other than a contributor’s version infringed any patent, then the license from such parties terminates (see section 8.2 for more details).</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of of same version or any later version of the license.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide notice in a file called, LEGAL, of any third party intellectual property rights for particular functionality or code, including if your modifications are an application programming intereface and you own, control, or have knowledge of any patent licenses which are reasonably necessary to implement the API. See section 3.4 for more details.</p></td>
</tr>
<tr class="even">
<td><p>You may offer and charge a fee for warranty, support, indemnity or liability obligations to recipients. However, you must make it clear that any such offer is offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.5 for more details.</p></td>
</tr>
<tr class="odd">
<td><p>You may distribute binary versions under a different license, so long as you do not limit or alter the recipient’s right in the source code under this license. You must make it clear that any differing terms are offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.6 for more details.</p></td>
</tr>
<tr class="even">
<td><p>You may distribute binary versions under a different license, so long as you do not limit or alter the recipient’s right in the source code under this license. You must make it clear that any differing terms are offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.6 for more details.</p></td>
</tr>
</tbody>
</table>

Mozilla Public License 2.0
--------------------------

SPDX License ID  
[MPL-2.0](https://spdx.org/licenses/MPL-2.0.html)

Notes  
This license includes a license-compatibility provision related to use
of the code with the GPL-2.0-or-later, LGPL-2.1-or-later, and
GPL-3.0-or-later which is difficult to capture, please see sections
1.12, 2.4, 3.3, and 10.4 for more details.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You must inform recipients that source code is goverened by this licenses and how to obtain a copy</p></td>
</tr>
<tr class="even">
<td><p>Modifications under same license</p></td>
<td></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>File-level reciprocal license meaning that modifications to any file or new files that contain part of original software are governed by the terms of this license. Larger works may be created by combining covered software with code not governed by this license, so long as you comply with this license for the covered software (see sections 1.10 and 3.3 for more details)</p></td>
</tr>
<tr class="odd">
<td><p>Retain notices</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>You must retain license notices with every source code distribution or include notices in another likely location</p></td>
</tr>
<tr class="even">
<td><p>Provide source code</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Must inform recipients how to obtain source code by reasonable means in a timely manner and at no cost more than the cost of distribution to the recipient.</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>License terminates upon failure to comply with license unless certain conditions are met by you and contributor (see section 5.1 for more details)</p></td>
</tr>
<tr class="even">
<td><p>Any patent claims accusing the software by a licensee results in termination of all licenses to the licensee</p></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license.</p></td>
</tr>
</tbody>
</table>

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>You may distribute binary versions under a different license, so long as you do not limit or alter the recipient’s right in the source code under this license.</p></td>
</tr>
<tr class="even">
<td><p>You may offer and charge a fee for warranty, support, indemnity or liability obligations to recipients. However, you must make it clear that any such offer is offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.5 for more details.</p></td>
</tr>
<tr class="odd">
<td><p>You may distribute binary versions under a different license, so long as you do not limit or alter the recipient’s right in the source code under this license. You must make it clear that any differing terms are offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.6 for more details.</p></td>
</tr>
</tbody>
</table>

Microsoft Public License
------------------------

SPDX License ID  
[Ms-PL](https://spdx.org/licenses/Ms-PL.html)

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Include a complete copy of license with source code distributions</p></td>
</tr>
<tr class="even">
<td><p>Retain all notices</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Retain all notices present in software</p></td>
</tr>
<tr class="odd">
<td><p>Source code under same license</p></td>
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Distributions of &quot;any portion of the software in source code form&quot; must be under this license</p></td>
</tr>
<tr class="even">
<td><p>Comply with this license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
<td></td>
<td><p>Object or compiled code distributions must be under a license that complies with this license</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Any patent claims by licensee against any contributor accusing the software result in termination of all patent licenses from that contributor</p></td>
</tr>
</tbody>
</table>

University of Illinois/NCSA Open Source License
-----------------------------------------------

SPDX License ID  
[NCSA](https://spdx.org/licenses/NCSA.html)

Notes  
NCSA is essentially an MIT grant with BSD-3-Clause conditions, thus
compliance is the same as BSD-3-Clause.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
</tbody>
</table>

OpenSSL License
---------------

SPDX License ID  
[OpenSSL](https://spdx.org/licenses/OpenSSL.html)

Notes  
This license is actually a set of two licenses, which have similar text
and requirements but different copyright holders and therefore different
acknowledgment text. Some requirements to include acknowledgements may
only apply if you are using that part of the project written by a
specific copyright holder.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="odd">
<td><p>Acknowledgement must be included for any redistribution</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Include acknowledgement in advertising mentioning features or use</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>Include acknowledgement in advertising mentioning features or use. &quot;The word <em>cryptographic</em> can be left out if the rouines from the library being used are not cryptographic related&quot;.</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Include acknowledgement If you include any Windows specific code (or a derivative thereof) from the apps directory (application code)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>Name of project cannot be used for derived products without permission</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

PHP License v3.0
----------------

SPDX License ID  
[PHP-3.0](https://spdx.org/licenses/PHP-3.0.html)

Notes  
PHP-3.0 and PHP-3.01 are the same license, but for a slight variation in
the acknowledment text.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="odd">
<td><p>Name of project cannot be used for derived products without permission</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Acknowlegment must be retained in all redistributions</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license.</p></td>
</tr>
</tbody>
</table>

PHP License v3.01
-----------------

SPDX License ID  
[PHP-3.01](https://spdx.org/licenses/PHP-3.01.html)

Notes  
PHP-3.0 and PHP-3.01 are the same license, but for a slight variation in
the acknowledment text.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="odd">
<td><p>Name of project cannot be used for derived products without permission</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Acknowlegment must be retained in all redistributions</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

### License Versioning

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Allows use of covered code under the terms of same version or any later version of the license.</p></td>
</tr>
</tbody>
</table>

Plexus Classworlds License
--------------------------

SPDX License ID  
[Plexus](https://spdx.org/licenses/Plexus.html)

Notes  
This license also includes a clause that states, "due credit should be
given" to the copyright holder, but given the non-obligatory nature of
"should", this is not considered a requirement.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>For binary distributions, this information must be provided in “the documentation and/or other materials provided with the distribution”</p></td>
</tr>
<tr class="odd">
<td><p>Name of project cannot be used for derived products without permission</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

Python License 2.0
------------------

SPDX License ID  
[Python-2.0](https://spdx.org/licenses/Python-2.0.html)

Notes  
This is a license “stack” comprised of various licenses that apply to
Python as it has developed over the years.

### Conditions

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>UB</th>
<th>MB</th>
<th>US</th>
<th>MS</th>
<th>Compliance Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Provide copy of license</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Provide copyright notice</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>Notice of modifications</p></td>
<td></td>
<td><p>X</p></td>
<td></td>
<td><p>X</p></td>
<td><p>Indicate the nature of the modifiations made in the work</p></td>
</tr>
</tbody>
</table>

### Termination Provisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Termination of license upon breach</p></td>
</tr>
</tbody>
</table>

TCL/TK License
--------------

SPDX License ID  
[TCL](https://spdx.org/licenses/TCL.html)

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Modified versions need not follow this license, provided that new license terms appear on first page of each applicable file</p></td>
</tr>
</tbody>
</table>

zlib License
------------

SPDX License ID  
[zlib](https://spdx.org/licenses/zlib.html)

### Other Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>This license also includes a request, but not a requirement for acknowledgment of use in your product documentation.</p></td>
</tr>
</tbody>
</table>
