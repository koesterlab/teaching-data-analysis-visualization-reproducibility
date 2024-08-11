************************
Version control with Git
************************

Data analysis is usually an iterative process, that is moreover sometimes not straightforward and might require to try out multiple alternatives.
Sometimes, you might have to go back to a previous version of your analysis in order to undo a change that turned out to be suboptimal.
Sometimes, you will have to figure out why exactly you performed a certain change in your code.

Version control systems (VCS) are tools that help you to manage these challenges.
They allow you to keep track of changes in your code, to go back to previous versions, and to collaborate with others on the same codebase.

One of the most popular VCS is Git, which is directly integrated with VSCode.
We will now learn how to set up a new Git repository and how to use it to manage changes in our codebase.

Step 1: Setting up a new Git repository for this course
=======================================================

We will in the following assume that the rest of the course is conducted in subfolders of the folder ``dataviz`` on some machine.
If you run this course via Gitpod, we simply assume that the working directory in the gitpod is this folder ``dataviz``.

1. If you are **not working in Gitpod**, open VSCode in a new and empty folder for this course (named ``dataviz``).
2. Click on the "Source Control" icon in the sidebar on the left and select "Initialize Repository".

Now, you have set up a new Git repository in that folder.
Any changes you make to this folder will occur in the source control view in the VSCode sidebar.

Step 2: Making changes to your codebase
=======================================

1. Create a new file and name it ``README.txt``.
2. Write some text into the file, briefly mentioning that this repository contains your exercises for the data analysis and visualization course.

You will see that the file appears in the source control view in the sidebar.

Step 3: Committing changes
==========================

While Git sees that you have added a file (and likewise would see that you have changed any existing file), it does not yet track these changes.
To do so, you have to commit them.

1. Click on the ``+`` icon next to the file in the source control view.
2. Write a commit message in the text field at the top of the source control view. This message should always comprehensively (but short) describe what you changed and ideally why.
3. Click on the commit button to commit the changes.

Now, the changes are in the local history of your git repository.
This allows you to go back to this version at any time.

Step 4: Pushing changes to a remote repository
==============================================

Usually, it is a good idea to make a git repository independent of your local machine, so that you can access it from anywhere, collaborate with others, and also have a backup.
For this, you can use a remote repository, which is a git repository that is hosted on a server.

1. Go to `GitHub <https://github.com>`_ and create a new account if you do not have one yet.
2. Sign in to this account from VSCode by clicking the ``Accounts`` icon in the bottom left and selecting ``Sign in to GitHub``.
3. In the source control view, click publish to GitHub.
   A dialog occurs that asks you whether it shall be a private or public repository.
   Choose private.

For the rest of the course, we will use this repository to store our exercises and solutions.
Please keep in mind to regularly check out the source control view in VSCode to commit your changes and to push them to the remote repository.
