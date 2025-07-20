****************************
Package management with pixi
****************************

A data analysis does not solely comprise of your configuration (for e.g. datavzrd) or programming code, but also of all the software packages needed to execute it.
Outside of data analysis or programming, people will know the usual ways of installing software via software stores/centers,  system wide package managers, or by installing manually downloaded packages.
Deploying a software stack for a data analysis this way is not recommended.

1. It is not reproducible, as the software versions are not fixed.
2. It is not portable, as the software stack might not be compatible with other systems.
3. It is, as a manual process, not scalable.
4. It is not isolated, as the software would be installed system wide, being affected by future installations or updates.

To solve these issues, we use package managers.
A package manager is a tool that automates the process of installing, updating, configuring, and removing software packages.
In science, one of the most popular package management systems is the Conda ecosystem.
There are various frontends for Conda.
Here, we use the pixi package manager.

Step 1: Installing pixi
=============================

To install pixi, you can use the following command inside your VSCode terminal (on Windows, issue this from a WSL session, cf. :ref:`vscode`):

.. code-block:: bash

    curl -fsSL https://pixi.sh/install.sh | sh

Afterwards, open a new terminal session.

Step 2: Installing a software stack
===================================

For us, the central feature of pixi is the ability to create isolated software environments.
This even means that multiple versions of the same software can be present on a system, in different environments.
With pixi, these environments are usually tied to a working directory.
This way, each analysis can have its own environment.

Inside of your `working directory dataviz <git>`_, create a new subfolder name ``datavzrd``.
We will use this folder for the chapter about `Datavzrd <datavzrd>`_.
Now, change to this folder via the `terminal <terminal>`_, and create a new environment that contains Datavzrd, a software for visualizing tables that we need in the next part of the course:

.. code-block:: bash

    pixi init .
    pixi add datavzrd

This command creates a new environment and installs the package ``datavzrd`` from the ``conda-forge`` channel.

Exercise
--------

1. Have a look at the contents of the file ``pixi.toml`` and try to understand the meaning of the different entries using the `pixi documtentation <https://prefix.dev>`__.
2. How to pixi ensure reproduciblity of the environment and compatibility of the package versions with your analysis?


Step 3: Activating the environment
==================================

To activate the environment, use the following command:

.. code-block:: bash

    pixi shell

Now you are inside the environment and can use any software installed within the environment via the terminal, e.g.:

.. code-block:: bash

    datavzrd --help

Step 4: Deactivating the environment
====================================

To deactivate the environment again, hit Ctrl+D or type ``exit`` in the same terminal.
