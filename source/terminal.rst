************
The terminal
************

The terminal is a powerful tool that allows you to interact with your computer via text commands.
It can be used to automate tasks, invoke software, and perform various other operations.
For this course, we just use the terminal to invoke other software.

To open the terminal in VSCode, click on the "Terminal" menu and select "New Terminal".

Filesystem operations
=====================

Within the terminal, you can first of all conduct operations that are equivalent to what you can do with a file manager.
You can list the files and folders in the current directory by typing:

.. code-block:: bash

    ls

Most commands of the terminal have additional options, which can be view via adding the ``--help`` option.

.. code-block:: bash

    ls --help

displays all the options just the simple ``ls`` command supports, nicely illustrating the power of the terminal.
With the ``mkdir`` command (for "make directory"), you can create a new directory.

.. code-block:: bash

    mkdir new_directory

With the ``cd`` command (for "change directory"), you can navigate to other directories.

.. code-block:: bash

    cd new_directory

navigates to the directory ``new_directory``.

.. admonition:: Exercise

    1. Navigate to ``new_directory``.
    2. List the contents of the directory. It should be empty.
    3. Navigate back to the parent directory (``cd`` accepts the special parameter ``..`` for this purpose).

The command ``rm`` can be used to remove files and directories.
Attention, it does so permanently, without moving them into a trash bin!
By default ``rm`` refuses to remove directories.
To remove a directory, you have to add the option ``-r`` (for "recursive"), which tells ``rm`` to remove all files and subdirectories.

.. code-block:: bash

    rm -r new_directory

removes the directory ``new_directory``.
Do this now.