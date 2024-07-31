.. _altair:

********************
Plotting with Altair
********************

The plotting library `Altair <https://altair-viz.github.io>`__ offers a high-level, declarative way to visualize data.
It directly integrates with Polars, and allows to visualize any given dataframe with only few lines of code.
Beside classical file formats like ``PDF`` and ``SVG``, Altair allows to output plots as `HTML <https://de.wikipedia.org/wiki/Hypertext_Markup_Language>`__, such that they become interactively explorable.
Altair is a Python frontend for Vega-Lite, which we have used before when learning :ref:`Datavzrd <datavzrd>`.

Analogously to Vega-Lite, the central idea of Altair is to define plots by specifying the mark(s) and the encodings to use for the visualization of a given (Polars) dataframe.

This chapter is heavily inspired by the official `Altair tutorial <https://altair-viz.github.io/altair-tutorial/README.html>`__.

Step 1: Setup the notebook
==========================

First, create a new file ``notebook.ipynb`` under ``dataviz/chapters/altair`` and open it in VSCode.
In the opened notebook, select the :ref:`pystats environment <polars>` as the kernel with the button on the top right.

In the first cell of the new notebook, let us import some modules we need for this chapter:

.. code-block:: python

    import altair as alt
    import polars as pl
    from vega_datasets import data


Step 2: Obtain test data
========================

The ``vega_datasets`` package offers some widely used test datasets.
In this chapter, we will use the ``cars`` dataset, but modify it a bit to become more convenient to use:

.. code-block:: python

    cars = pl.from_pandas(
        data.cars()
    ).with_columns(
        pl.col("Year").dt.year()
    ).select(
        pl.col("*").name.to_lowercase()
    )

.. admonition:: Exercise

    1. What happens in each of the statements above?
    2. What is the reason for the ``with_columns`` and ``select`` statements?

Step 3: A simple, one-dimensional chart
=======================================

Let us now create our first plot (in Altair called a chart):

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles_per_gallon")
    )

As can be seen, the point marks overlap to a large extend, somehow hiding the actual structure of the data.
A more appropriate mark for such a one-dimensional plot is ``mark_tick``:

.. code-block:: python

    alt.Chart(cars).mark_tick().encode(
        alt.X("miles_per_gallon")
    )

As can be seen, it becomes easier to distinguish the dense regions from sparser ones since individual marks don't occupy so much horizontal space.
Nevertheless, there are still overlapping marks.
Hence, we will return to this chart later, making it even more informative using more involved techniques.

Step 4: A two-dimensional chart
===============================

Let us now create a two-dimensional chart, namely a classical so-called scatter plot, which can be used to show relationships between two variables:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles_per_gallon"),
        alt.Y("horsepower"),
    )

As can be seen, there is a pretty obvious relationship between horsepower and miles per gallon of a car.
We will again return to this later on, and try to make a more objective statement about this.

Step 5: Adding a third dimension using color
============================================

Let us now add a third dimension to the scatter plot above, by encoding the ``origin`` of the car as color:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles_per_gallon"),
        alt.Y("horsepower"),
        alt.Color("origin"),
    )

Since the origin column is a categorical variable (it lists countries), Altair automatically chooses an appropiate categorical color scale.
In contrast, using a quantitative column for the color leads to Altair choosing a continuous scale:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles_per_gallon"),
        alt.Y("horsepower"),
        alt.Color("acceleration"),
    )

.. admonition:: Exercise

    1. What is the difference between a categorical and a continuous color scale?
    2. Seems like there is another relationship, between horsepower and acceleration. What can you do to make it more visible?

Step 6: Explicitly define the data type
=======================================

So far, we have left the decision about the data type (quantitative, categorical) to Altair.
Consider the following example:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles_per_gallon"),
        alt.Y("horsepower"),
        alt.Color("cylinders"),
    )

Altair correctly recognizes that cylinders are a quantitative variable.
However, it is also discrete, with just a few values in this case.
We can tell Altair that cylinders are "ordinal" instead, meaning that they are actually categorical but ordered:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles_per_gallon"),
        alt.Y("horsepower"),
        alt.Color("cylinders").type("ordinal"),
    )

.. admonition:: Exercise

    What happens to the visualization, why does that improve the chart?