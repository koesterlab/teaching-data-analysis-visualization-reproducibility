.. _polars:

*******************************************************
Reading, writing, and manipulating tabular data: polars
*******************************************************

This part of the course is inspired by the `Polars Getting Started Guide <https://docs.pola.rs/user-guide/getting-started>`__.

Polars is a programming library for reading, writing, and manipulating tabular data.
It is a fast and efficient library that is written in Rust and has so-called Python bindings which offer the ability to use it from within Python code.
For this and the following chapter, we first create a micromamba environment that contains the necessary software tools.
Create the file ``envs/pystats.yaml`` with the following content:

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
      - vega_datasets =0.9
      - ipykernel =6.29
      - scipy =1.14

.. admonition:: Exercise

    Now create a new micromamba environment named ``pystats`` from this file.

THe following steps are inspired by the official `getting started <https://docs.pola.rs/user-guide/getting-started>`__ guide of Polars.

Step 1: Setup the notebook
==========================

First, create a new file ``notebook.ipynb`` under ``chapters/polars`` and open it in VSCode.
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
                date(2019, 1, 1),
                date(2021, 1, 2),
                date(2023, 1, 3),
            ],
            "c": [4.0, 5.0, 6.0],
            "d": ["a", "b", "c"],
        }
    )

.. dropdown:: Explanation

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
        pl.col("d").map_elements(lambda s: s + "x", return_dtype=str),
    )

.. dropdown:: Explanation

    The first expression multiplies the values in column ``a`` by 2.
    The second expression appends an ``x`` to each value in column ``d``.
    Returned is the modified dataframe with just the two columns.

Expressions in the ``select`` or ``with_columns`` context produce so-called ``Series``, which represent columns of the dataframe.
Both operations can contain multiple expressions, which may yield either single (scalar) values or series that have the same length as the dataframe has rows.
In the mixed case, the scalar values are broadcasted (i.e. repeated) to the number of rows.

.. admonition:: Exercise

    The ``sum`` method of expressions computes the sum of all values in a column, which is obviously a single value.
    Extend above selection by an additional expression that computes the sum of column ``c``.
    See how the value is broadcasted to all rows because the other expressions are row-wise.

Select can also be used to remove columns from the dataframe:

.. code-block:: python

    df.select(pl.col("*").exclude("c", "d"))

.. admonition:: Exercise

    What is the meaning of the individual elements of this statement?

While ``select`` limits the returned dataframe to the queried columns, ``with_columns`` adds new columns or replaces exising ones:

.. code-block:: python

    df.with_columns(
        (pl.col("a") * 2).alias("a_times_two"),
        pl.col("d").map_elements(lambda s: s + "x", return_dtype=str).alias("d_with_x"),
    )

.. dropdown:: Explanation

    The ``alias`` method that expressions offer allows to assign a reasonable name to the resulting columns.
    If we would omit the ``alias`` invocations, the expressions would modify their columns.

Step 8: Filtering data
======================

Expressions in the ``filter`` context have to produce a boolean series that has the same length as the dataframe has rows.
The rows for which the series is ``True`` are kept, while the others are removed.

Let us filter the dataframe ``df`` to keep only the rows where the value in column ``c`` is at least 5.0:

.. code-block:: python

    df.filter(pl.col("c") >= 5.0)

Step 9: Accessing individual items
==================================

The ``item`` method of dataframes returns an individual value, in particular if the dataframe has only one row and column.
In combination with ``select`` and ``filter`` this allows to access individual items in the dataframe.
Let us select the value in the ``a`` column where the ``d`` column contains the value ``b``:

.. code-block:: python

    df.filter(pl.col("d") == "b").select(pl.col("a")).item()

.. admonition:: Exercise

    The ``is_between`` method of expressions allows to filter for values that fall in a specific range.
    Look up its usage in the Polars `API docs <https://docs.pola.rs/api/python/stable/reference/index.html>`__.
    Use it to filter for the row where the column ``b`` is between the beginning of 2020 (``date(2020, 1, 1)``) and the beginning of 2022 (``date(2022, 1, 1)``).
    This should be a single row.
    Obtain the value of the column ``c`` from that row.

Step 10: Grouping data
======================

Let us first append some additional data to our dataframe:

.. code-block:: python

    extended_df = df.vstack(
        pl.DataFrame(
            {
                "a": [5, 1, 2],
                "b": [
                    date(2021, 1, 1),
                    date(2019, 1, 2),
                    date(2023, 1, 3),
                ],
                "c": [None, 1.1, 2.0],
                "d": ["a", "a", "c"],
            }
        )
    )

.. admonition:: Exercise

    1. What is the meaning and implication of the ``None`` in the ``c`` column?
    2. Display the resulting dataframe in the variable ``extended_df`` in your notebook.

Grouping of data can be useful to e.g. calculate summary statistics per group.
Let us group ``extended_df`` by the values in column ``d`` and calculate the mean of column ``a`` per group:

.. code-block:: python

    extended_df.group_by("d").agg(
        pl.col("c").mean()
    )

.. admonition:: Exercise

    1. What happens with the the ``None`` value in column ``c``?
    2. Now, group by the year. For this purpose, first add a new column (using ``with_columns``) that holds the year of each row, derived from column ``b``.
       For this purpose, polars offers a special subset of expressions that perform operations on date or time objects, accessible by the attribute `dt`, see `the docs <https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.year.html>`__.
       Assign a reasonable name for this column.
       Then, group by the year, and calculate the minimum value of column ``a`` per group (use the expression method ``min()`` for this).
