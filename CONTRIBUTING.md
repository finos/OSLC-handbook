
Thanks for your interest in the Open Source License Handbook!  We welcome input and contributions to this work.  Please review the information below related to ways and how to contribute.

Before you begin, please familiarize yourself with the [DOCUMENTATION.md] and other related information.  Check for [https://github.com/jlovejoy/OSLC-handbook/issues](open issues) or start a discussion around a new feature idea or a bug.

# Ways to contribute

## Improve documentation
We've tried to explain the purpose, structure, and limitations of this handbook as clearly as possible. But if you think improvements can be made or additional information would be helpful, then do let us know.

## Revise an existing license
Maybe you spot a typo or a better way to word something or make an entry's wording more consistent with like entries.  

## Add a new license
If there is license that is not included here, but you'd like to add the license compliance information to this handbook, great! Please create a new YAML file, following the structure as described in DOCUMENTATION, as shown in existing license YAML files, and as used in the example file.  Please only add open source licenses, that is, licenses that meet the Open Source Definition or the 4 freedoms as defined by the Free Software Foundation. 

## Create a script for a new output type
add some stuff here... 

# How to contribute

First off, clone the repository locally

    clone https://github.com/jlovejoy/OSLC-handbook.git

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
