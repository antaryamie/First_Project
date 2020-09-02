'''bash
https://support.atlassian.com/bitbucket-cloud/docs/types-of-version-control/

https://www.geeksforgeeks.org/version-control-systems/
'''

### Types of version control
When you work on a development team, you may be touching similar parts of the code throughout a project. As a result, changes made in one part of the source can be incompatible with those made by another developer working at the same time.

Version control helps solve these kinds of problems and provides:

A complete history of every file, which enables you to go back to previous versions to analyze the source of bugs and fix problems in older versions.

The ability to work on independent streams of changes, which allows you to merge that work back together and verify that your changes conflict.

The ability to trace each change with a message describing the purpose and intent of the change and connect it to project management and bug tracking software.

There are two types of version control: centralized and distributed.

## Centralized version control
With centralized version control systems, you have a single “central” copy of your project on a server and commit your changes to this central copy. You pull the files that you need, but you never have a full copy of your project locally. Some of the most common version control systems are centralized, including Subversion (SVN) and Perforce.

## Distributed version control
With distributed version control systems (DVCS), you don't rely on a central server to store all the versions of a project’s files. Instead, you clone a copy of a repository locally so that you have the full history of the project. Two common distributed version control systems are Git and Mercurial.

While you don't have to have a central repository for your files, you may want one "central" place to keep your code so that you can share and collaborate on your project with others. That's where Bitbucket comes in. Keep a copy of your code in a repository on Bitbucket so that you and your teammates can use Git or Mercurial locally and to push and pull code.

### Git Fork
A fork is a rough copy of a repository. Forking a repository allows you to freely test and debug with changes without affecting the original project. One of the excessive use of forking is to propose changes for bug fixing. To resolve an issue for a bug that you found, you can:

Fork the repository.
Make the fix.
Forward a pull request to the project owner.
Forking is not a Git function; it is a feature of Git service like GitHub.

When to Use Git Fork

Generally, forking a repository allows us to experiment on the project without affecting the original project. Following are the reasons for forking the repository:

Propose changes to someone else's project.
Use an existing project as a starting point.