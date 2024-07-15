**********************************
Package management with micromamba
**********************************

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
Here, we use the micromamba package manager.

Step 1: Installing micromamba
=============================

To install micromamba, you can use the following command inside your VSCode terminal (on Windows, issue this from a WSL session, cf. :ref:`vscode`):

.. code-block:: bash

    "${SHELL}" <(curl -L micro.mamba.pm/install.sh)

Afterwards, open a new terminal session.

Step 2: Installing a software stack
===================================

The central feature of micromamba is the ability to create isolated software environments.
This even means that multiple versions of the same software can be present on a system, in different environments.

We create a new environment that contains Datavzrd, a software for visualizing tables that we need in the next part of the course:

.. code-block:: bash

    micromamba create -n test -c conda-forge datavzrd

This command creates a new environment named ``test`` and installs the package ``datavzrd`` from the ``conda-forge`` channel.

Step 3: Activating the environment
==================================

To activate the environment, use the following command:

.. code-block:: bash

    micromamba activate test

Now you are inside the environment and can use any software installed within the environment via the terminal, e.g.:

.. code-block:: bash

    datavzrd --help

Step 4: Deactivating the environment
====================================

To deactivate the environment again, use the following command:

.. code-block:: bash

    micromamba deactivate

Step 5: Reproducible environments
=================================

The problem with a manual command like the one above is that it is not reproducible.
First, only the terminal history preserves what you did to create the environment.
Second, only the environment name is preserved, not the exact software versions.
The latter are just the latest available ones at the time of environment creation.
While this can be fine in certain cases, it is certainly not when you want to ensure reproducibility and document what you actually did to generate a certain result.

To solve this, we can create a file that contains the exact software versions, called an environment file.
We do that for the example from before.
Create a folder ``dataviz/micromamba`` that holds files related to this chapter, and in there create the file ``test-environment.yaml`` with the following content:

.. code-block:: yaml

    channels:
      - conda-forge
    dependencies:
      - datavzrd =2.41.0

.. dropdown:: Explanation

    The first section specifies the channel, the second section specifies the software tools or libraries to install including their versions.

Now, you can create the environment from this file:

.. code-block:: bash

    micromamba env create -f test-environment.yaml -n datavzrd

.. admonition:: Exercise

    The environment ``test`` from step 2 is no longer needed.
    Find out how using ``micromamba --help`` and remove it.