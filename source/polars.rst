.. _polars:

*******************************************************
Reading, writing, and manipulating tabular data: polars
*******************************************************

Polars is a programming library for reading, writing, and manipulating tabular data.
It is a fast and efficient library that is written in Rust and has so-called Python bindings which offer the ability to use it from within Python code.
For this and the following chapter, we first create a micromamba environment that contains the necessary software tools.
Create the file ``dataviz/envs/pystats.yaml`` with the following content:

.. code-block:: yaml

    channels:
      - conda-forge
    dependencies:
      - python =3.11
      - polars =1.1
      - altair =5.3
      - altair_saver =0.5
      - vegafusion =1.6
      - vegafusion-python-embed =1.6
      - vl-convert-python =1.5
      - ipykernel =6.29
      - scipy =1.14

.. admonition:: Exercise

    Now create a new micromamba environment named ``pystats`` from this file.

THe following steps are inspired by the official `getting started <https://docs.pola.rs/user-guide/getting-started>`__ guide of Polars.

Step 1: Setup the notebook
==========================

First, create a new file ``polars.ipynb`` under ``dataviz/chapters/polars`` and open it in VSCode.
In the opened notebook, select the pystats environment as the kernel with the button on the top right.

Step 2: Creating a dataframe from scratch
=========================================

We can create a dataframe from scratch by using the ``pl.DataFrame`` constructor.
In the first cell of the notebook, we import relevant modules:

.. code-block:: python

    import polars as pl
    from datetime import datetime

.. dropdown:: Explanation

    The first line imports the Polars library and provides it as a shorthand alias ``pl``.
    The second line imports the datetime module from the Python standard library.
    This module allows us to define dates.

Then, we create a second cell with the following content:

.. code-block:: 

    df = pl.DataFrame(
        {
            "integer": [1, 2, 3],
            "date": [
                datetime(2025, 1, 1),
                datetime(2025, 1, 2),
                datetime(2025, 1, 3),
            ],
            "float": [4.0, 5.0, 6.0],
            "string": ["a", "b", "c"],
        }
    )

..dropdown:: Explanation

    The dictionary passed to the ``pl.DataFrame`` constructor contains the column names as keys and lists of values as values.


Step 3: Inspecting the dataframe
================================

By simply ending the cell with the variable name, the dataframe is shown below the cell.

Step 4: Reading and writing data frames
=======================================

Polars supports reading and writing data frames from and to various file formats.
Let us write the dataframe ``df`` to a CSV file:

.. code-block:: python

    df.write_csv("data.csv")

And subsequently read it back:

.. code-block:: python

    df2 = pl.read_csv("data.csv")

Step 5: Comparing data frames
=============================

We can compare two data frames by using the ``equals`` method:

.. code-block:: python

    df.equals(df2)

Step 6: Expressions
===================

Polars offers four central ways to manipulate data frames:

* ``select``
* ``filter``
* ``with_columns``
* ``groupby``

All of these take one or more expressions as arguments.