.. _altair:

********************
Plotting with Altair
********************

The plotting library `Altair <https://altair-viz.github.io>`__ offers a high-level, declarative way to visualize data.
It directly integrates with Polars, and allows to visualize any given dataframe with only few lines of code.
Beside classical file formats like ``PDF`` and ``SVG``, Altair allows to output plots as `HTML <https://de.wikipedia.org/wiki/Hypertext_Markup_Language>`__, such that they become interactively explorable.
Altair is a Python frontend for Vega-Lite, which we have used before when learning :ref:`Datavzrd <datavzrd>`.

Analogously to Vega-Lite, the central idea of Altair is to define plots by specifying the mark(s) and the encodings to use for the visualization of a given (Polars) dataframe.
Each encoding has a *scale*, i.e. the mapping of data values to visual properties.
The scale maps data values in a certain *domain* to visual properties in a certain *range*.
In addition, each encoding has a type (quantitative, ordinal, nominal, temporal) that determines how the data values are interpreted.

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

.. _altair_one_dimensional:

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
Hence, we will return to this chart later (:ref:`altair_binning`), making it even more informative using more involved techniques.

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
We can tell Altair that cylinders are "ordinal" instead, meaning that they are still categorical but ordered:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles_per_gallon"),
        alt.Y("horsepower"),
        alt.Color("cylinders").type("ordinal"),
    )

.. admonition:: Exercise

    What happens to the visualization, why does that improve the chart?

.. _altair_binning:

Step 7: Binning
===============

In the first chart (:ref:`altair_one_dimensional`) we have seen that overlapping marks can make it hard to accurately interpret the density of data points at certain regions of a distribution.
One way to mitigate this issue is to bin the data, i.e., to group data points into bins and then visualize the number of data points in each bin.
This is also known as a histogram.

Let us create a histogram for the ``miles_per_gallon`` column:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles_per_gallon").bin(maxbins=30),
        alt.Y("count()"),
    )

.. admonition:: Exercise

    1. Compare this to the code in :ref:`altair_one_dimensional`. What is the difference, how does it affect the resulting plot?
    2. The ``bin`` method offers various additional parameters (hidden `here <https://altair-viz.github.io/user_guide/generated/core/altair.BinParams.html#altair.BinParams>`__ in the Altair documentation. Try to change the ``maxbins`` parameter to see how it affects the plot.

We can also color the histogram bars by the ``origin`` of the car:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles_per_gallon").bin(maxbins=30),
        alt.Y("count()"),
        alt.Color("origin"),
    )

.. admonition:: Exercise

    What is this way of coloring and stacking bars good for, where does it have problems?

Step 8: Layering and tooltips
=============================

Altair allows to layer multiple charts on top of each other.
Let us use this functionality to better visualize the difference in the distribution of ``miles_per_gallon`` per origin.

First, we represent the histogram via colors and use the y-axis for the origin:

.. code-block:: python

    alt.Chart(cars).mark_rect(tooltip=True).encode(
        alt.X("miles_per_gallon").bin(maxbins=30),
        alt.Y("origin"),
        alt.Color("count()"),
    )

.. admonition:: Exercise

    Explain the individual statements and their effect in the code above.

Next, we superimpose a tick chart that shows the underlying individual datapoints.
Altair allows us to combine charts via operators, like ``+`` for layering/superimposing.
Further, it is possible to specialize charts, i.e. create a base chart and then use it in different ways to define the layers.

.. code-block:: python

    base = alt.Chart(cars)

    base.mark_rect(tooltip=True).encode(
        alt.X("miles_per_gallon").bin(maxbins=30),
        alt.Y("origin"),
        alt.Color("count()"),
    ) + base.mark_tick(size=1, color="black", opacity=0.5).encode(
        alt.X("miles_per_gallon"),
        alt.Y("origin"),
    )

.. admonition:: Exercise

    1. Explain each statement in the code above.
    2. Altair names axes automatically.
       For layers, names are concatenated by commas.
       Here, this is misleading since essentially the two labels for the x axis are the same.
       Overwrite the axis label by using the ``title`` method on the x axis object of the first or the second chart (``.title("miles per gallon")``).
    3. In addition to layering, Altair supports vertical and horizontal concatenation of charts, implemented via the operators ``|`` and ``&``. Try them out here.

Step 9: Faceting
================

The downside of the color based histogram representation above is that the actual numbers are just visible by hovering over the colored rectangles while the color scale only allows a rough eyeballing of the actual counts.
If the actual counts per bin are particularly important, we can instead return to the bar-styled histogram from before, but use the Altair's faceting functionality to create a separate histogram for each origin:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles_per_gallon").bin(maxbins=30),
        alt.Y("count()"),
    ).facet(row="origin")

As can be seen, this trades of the ability to see the actual numbers by the height of the bar by using a lot of additional vertial space.
The latter can be mitigated by two switches though.

First, we can limit the height per subplot:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles_per_gallon").bin(maxbins=30),
        alt.Y("count()"),
    ).properties(height=100).facet(row="origin")

here reducing the height to 100 instead of the default 300.

Second, the y-axes by default share the same scale.
This is good for comparability.
Depending on the aim of the visualization it can however waste space.
By using the ``resolve_scale`` method of the faceted chart, we can change this behavior:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles_per_gallon").bin(maxbins=30),
        alt.Y("count()"),
    ).properties(height=100).facet(row="origin").resolve_scale(y="independent")

.. admonition:: Exercise

    With independent scales on the y-axis, what should be kept in mind when publishing such a plot?

