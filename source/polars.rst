.. _polars:

*******************************************************
Reading, writing, and manipulating tabular data: polars
*******************************************************

This part of the course is inspired by the `Polars Getting Started Guide <https://docs.pola.rs/user-guide/getting-started>`__.

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
    from datetime import date

.. dropdown:: Explanation

    The first line imports the Polars library and provides it as a shorthand alias ``pl``.
    The second line imports the datetime module from the Python standard library.
    This module allows us to define dates.

Then, we create a second cell with the following content:

.. code-block:: python

    df = pl.DataFrame(
        {
            "a": [1, 2, 3],
            "b": [
                date(2025, 1, 1),
                date(2025, 1, 2),
                date(2025, 1, 3),
            ],
            "c": [4.0, 5.0, 6.0],
            "d": ["a", "b", "c"],
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

* ``select``: select and manipulate columns, replacing the existing ones
* ``with_columns``: select and manipulate columns, adding new ones
* ``filter``: filter rows based on conditions
* ``groupby``: group rows based on conditions

All of these take one or more expressions as arguments.
Thereby, the semantic of the expressions depends on the context.

Step 7: Selecting data
======================

Let us select something in the example dataframe ``df``:

.. code-block:: python

    df.select(
        pl.col("a") * 2,
        pl.col("b").year(),
        pl.col("d").map(lambda s: s + "x"),
    )

Expressions in the ``select`` or ``with_columns`` context produce so-called ``Series``, which represent columns of the dataframe.
Both operations can contain multiple expressions, which may yield either single (scalar) values or series that have the same length as the dataframe has rows.
In the mixed case, the scalar values are broadcasted (i.e. repeated) to the number of rows.

Step 8: Filtering data
======================

Expressions in the ``filter`` context have to produce a boolean series that has the same length as the dataframe has rows.
The rows for which the series is ``True`` are kept, while the others are removed.

Step 9: Grouping data
=====================


