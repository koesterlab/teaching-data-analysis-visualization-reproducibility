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
    alt.data_transformers.enable("vegafusion")

The latter enables altair to perform some optimizations on the data before plotting.
This is always a good idea, since it improves the ability of the generated plots to deal with large datasets.


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
        pl.col("*").name.map(lambda name: name.lower().replace("_", " "))
    )

.. admonition:: Exercise

    1. What happens in each of the statements above?
    2. What is the reason for the ``with_columns`` and ``select`` statements (also look up the meaning of ``lower()`` and ``replace()`` in the `Python docs <https://docs.python.org/3/library/stdtypes.html#string-methods>`__? Try out how the dataframe looks like without them.

.. _altair_one_dimensional:

Step 3: A simple, one-dimensional chart
=======================================

Let us now create our first plot (in Altair called a chart):

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles per gallon")
    )

As can be seen, the point marks overlap to a large extend, somehow hiding the actual structure of the data.
A more appropriate mark for such a one-dimensional plot is ``mark_tick``:

.. code-block:: python

    alt.Chart(cars).mark_tick().encode(
        alt.X("miles per gallon")
    )

As can be seen, it becomes easier to distinguish the dense regions from sparser ones since individual marks don't occupy so much horizontal space.
Nevertheless, there are still overlapping marks.
Hence, we will return to this chart later (:ref:`altair_binning`), making it even more informative using more involved techniques.

.. _altair_scatter:

Step 4: A two-dimensional chart
===============================

Let us now create a two-dimensional chart, namely a classical so-called scatter plot, which can be used to show relationships between two variables:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles per gallon"),
        alt.Y("horsepower"),
    )

As can be seen, there is a pretty obvious relationship between horsepower and miles per gallon of a car.
We will again return to this later on, and try to make a more objective statement about this.

Step 5: Adding a third dimension using color
============================================

Let us now add a third dimension to the scatter plot above, by encoding the ``origin`` of the car as color:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles per gallon"),
        alt.Y("horsepower"),
        alt.Color("origin"),
    )

Since the origin column is a categorical variable (it lists countries), Altair automatically chooses an appropiate categorical color scale.
In contrast, using a quantitative column for the color leads to Altair choosing a continuous scale:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles per gallon"),
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
        alt.X("miles per gallon"),
        alt.Y("horsepower"),
        alt.Color("cylinders"),
    )

Altair correctly recognizes that cylinders are a quantitative variable.
However, it is also discrete, with just a few values in this case.
We can tell Altair that cylinders are "ordinal" instead, meaning that they are still categorical but ordered:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles per gallon"),
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

Let us create a histogram for the ``miles per gallon`` column:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles per gallon").bin(maxbins=30),
        alt.Y("count()"),
    )

.. admonition:: Exercise

    1. Compare this to the code in :ref:`altair_one_dimensional`. What is the difference, how does it affect the resulting plot?
    2. The ``bin`` method offers various additional parameters (hidden `here <https://altair-viz.github.io/user_guide/generated/core/altair.BinParams.html#altair.BinParams>`__ in the Altair documentation. Try to change the ``maxbins`` parameter to see how it affects the plot.

We can also color the histogram bars by the ``origin`` of the car:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles per gallon").bin(maxbins=30),
        alt.Y("count()"),
        alt.Color("origin"),
    )

.. admonition:: Exercise

    What is this way of coloring and stacking bars good for, where does it have problems?

Step 8: Layering and tooltips
=============================

Altair allows to layer multiple charts on top of each other.
Let us use this functionality to better visualize the difference in the distribution of ``miles per gallon`` per origin.

First, we represent the histogram via colors and use the y-axis for the origin:

.. code-block:: python

    alt.Chart(cars).mark_rect(tooltip=True).encode(
        alt.X("miles per gallon").bin(maxbins=30),
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
        alt.X("miles per gallon").bin(maxbins=30),
        alt.Y("origin"),
        alt.Color("count()"),
    ) + base.mark_tick(size=1, color="black", opacity=0.5).encode(
        alt.X("miles per gallon"),
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
        alt.X("miles per gallon").bin(maxbins=30),
        alt.Y("count()"),
    ).facet(row="origin")

As can be seen, this trades of the ability to see the actual numbers by the height of the bar by using a lot of additional vertial space.
The latter can be mitigated by two switches though.

First, we can limit the height per subplot:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles per gallon").bin(maxbins=30),
        alt.Y("count()"),
    ).properties(height=100).facet(row="origin")

here reducing the height to 100 instead of the default 300.

Second, the y-axes by default share the same scale.
This is good for comparability.
Depending on the aim of the visualization it can however waste space.
By using the ``resolve_scale`` method of the faceted chart, we can change this behavior:

.. code-block:: python

    alt.Chart(cars).mark_bar().encode(
        alt.X("miles per gallon").bin(maxbins=30),
        alt.Y("count()"),
    ).properties(height=100).facet(row="origin").resolve_scale(y="independent")

.. admonition:: Exercise

    With independent scales on the y-axis, what should be kept in mind when publishing such a plot?

Step 10: Two-dimensional binning
================================

Histograms can also be generated across two dimensions.
This marks an alternative to the scatter plot.
It has the advantage to better show the differences in very dense regions.
Let us create a two-dimensional histogram for the ``miles per gallon`` and ``horsepower`` columns:

.. code-block:: python

    alt.Chart(cars).mark_rect().encode(
        alt.X("miles per gallon").bin(maxbins=30),
        alt.Y("horsepower").bin(maxbins=30),
        alt.Color("count()"),
    )

Alternatives to such a two-dimensional heatmap are kde (kernel density estimation) plots.
However, these are more complex to create while adding little to no additional value.
In contrast, heatmaps are easy to understand and directly interpretable, without any hidden effects.

Again, it can be beneficial to superimpose the actual data:

.. code-block:: python

    base = alt.Chart(cars)

    base.mark_rect(tooltip=True).encode(
        alt.X("miles per gallon").bin(maxbins=30).title("miles per gallon"),
        alt.Y("horsepower").bin(maxbins=30),
        alt.Color("count()"),
    ) + base.mark_circle(size=2, opacity=0.5, color="black").encode(
        alt.X("miles per gallon"),
        alt.Y("horsepower"),
    )

.. admonition:: Exercise

    1. Explain the individual statements in the code above.
    2. An alternative to displaying count information via the color is to use two dimensions instead.
       This can improve the interpretability because it becomes easier to distinguish different values.
       Change the encoding from ``mark_rect`` to ``mark_point`` and add a channel ``alt.Size`` that also encodes the count.
       What is better, what is worse? Are the individual data points still necessary in this case?

Step 11: Other aggregation methods
==================================

Let us have a look at the relationship between the miles per gallon and the year of production.
Altair offers the ability to on the fly calculate e.g. the mean over a column/field (many other aggregation functions are `available <https://altair-viz.github.io/user_guide/encodings/index.html#aggregation-functions>`__).
Let us start with displaying the mean miles per gallon per year as a simple line chart:

.. code-block:: python

    alt.Chart(cars).mark_line().encode(
        alt.X("year", type="ordinal"),
        alt.Y("mean(miles per gallon)"),
    )

.. admonition:: Exercise

    Here, it is important to explicitly inform Altair about the type of the year column.
    It is not continuous, but ordinal instead.
    What happens if you remove the type annotation?

Let us now stratify the chart per origin:

.. code-block:: python

    alt.Chart(cars).mark_line().encode(
        alt.X("year", type="ordinal"),
        alt.Y("mean(miles per gallon)"),
        alt.Color("origin"),
    )

.. admonition:: Bootstrapping

    Let's take a step back and think about the message of this plot.
    It postulates that the mean miles per gallon of cars has increased over the years, in all three countries.
    However, we only have a sample of the real set of cars per country in this dataset.
    Hence, the true mean might be actually different.
    What could be done?
    Instead of having a single sample, we could instead obtain many samples.
    This would allow us to estimate the uncertainty of the mean miles per gallon per year, and the estimate would be more accurate the more samples we would take.
    Imagine this dataset would not be cars but some kind of measurement.
    Hence, it might be infeasible to obtain more samples.
    Another option is to have profound statistical knowledge about the theoretical distribution of the data the sample was generated from (and the appropriate training).
    Then, one can create a statistical model that allows to reason about the uncertainty given the observed sample.
    However, this is not the case here.
    If the sample that we have consists of sufficiently many independent measurements, we can instead use `bootstrapping <https://en.wikipedia.org/wiki/Bootstrapping_(statistics)>`__ to estimate the uncertainty of the mean.
    Bootstrapping applies a trick: it draws many samples with replacement from the original sample.
    Values that are abundant in the original sample with more often occur in the bootstrapped samples than rare values.
    If one then calculates the summary statistic or any other measure (in this case the mean) on each bootstrapped sample and plots those values, one obtains an approximation of the distribution of the summary statistic as if it would have been created by really creating many sufficiently new samples.

Altair supports the calculation of the 95% confidence interval for the mean via bootstrapping via the ``ci0`` and ``ci1`` aggregation functions:

.. code-block:: python

    base = alt.Chart(cars)

    base.mark_area(opacity=0.4).encode(
        alt.X("year", type="ordinal"),
        alt.Y("ci0(miles per gallon)"),
        alt.Y2("ci1(miles per gallon)"),
        alt.Color("origin"),
    ) + base.mark_line(point=True).encode(
        alt.X("year", type="ordinal"),
        alt.Y("mean(miles per gallon)").title("miles per gallon (mean, CI)"),
        alt.Color("origin"),
    )

.. admonition:: Exercise

    1. Explain the individual statements in the code above. In particular, what is the purpose of ``point=True`` and why is it important here?
    2. What is the difference between the ``ci0`` and ``ci1`` aggregation functions?
    3. Why do we have to set a title for the y-axis?
    5. Since the mean and the confidence interval are just summary statistics of the actual data, it is always a good idea to also include the actual data points in the plot.
       Add a layer that shows the actual data points as ``mark_circle`` to the plot above.
    4. Altair supports interactivity in plots. This can be configured in great detail, which is however out of scope for this tutorial. Basic interactivity can however be generated for any plot by calling the method ``interactive()`` on the chart object. Try it out here.

Step 12: Correlation analysis
=============================

The scatter plot we created before revealed a releationship between horsepower and miles per gallon.
We can quantify the strength of this relationship by calculating the correlation coefficient.
The most important question to ask when striving to calculate a correlation is whether the relationship (let's say between two variables :math:`x` and :math:`y`) is expected to be linear (i.e. :math:`y = a \cdot x + b` with :math:`a` and :math:`b` being constant) or not.

.. admonition:: Exercise

    Revisit the plot of :ref:`altair_scatter`, is this a linear relationship?
    If the relationship is expected to be linear, the Pearson correlation coefficient is the most appropriate measure.
    Otherwise spearman correlation should be used, which instead measures to what extend an increase in :math:`x` leads :math:`y` to increase (correlation) or decrease (anticorrelation).
    Make your choice and store the desired measure in the variable ``correlation_method`` (either ``pearson`` or ``spearman``) in your notebook.

Let us now calculate the correlation coefficient between horsepower and miles per gallon with the chosen method using :ref:`Polars <polars>`.

.. code-block:: python

    correlation_coeff = cars.select(
        pl.corr("miles per gallon", "horsepower", method=correlation_method).alias(
            "correlation"
        )
    )

    alt.Chart(
        cars,
        title=alt.Title(
            "Relationship between horsepower and miles per gallon",
            subtitle=f"spearman correlation: {correlation_coeff.item():.2f}",
        ),
    ).mark_point().encode(
        alt.X("miles per gallon"),
        alt.Y("horsepower"),
    )

.. admonition:: Exercise

    We display the correlation coefficient in the title of the plot, using string formatting.
    Check the `Python docs <https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting>`__ to understand what we are doing here and what effect it has on the displayed correlation coefficient.

However, the data considered here is still a sample of the true set of cars offered in the considered time frame.
Hence, similar to above, we can use the bootstrap strategy to obtain **an approximation** of the posterior distribution of the correlation.
The more data points we have, the better this approximation will be.
It is not a perfect approach, but better than just showing a single correlation coefficient.

We first create the bootstrapped data via 

.. code-block:: python

    def bootstrap(df):
        return df.sample(cars.shape[0], with_replacement=True)

    correlation_dist = pl.concat(
        [
            bootstrap(cars).select(pl.corr("miles per gallon", "horsepower", method=correlation_method).alias(
                "correlation"
            ))
            for _ in range(10000)
        ]
    )


.. admonition:: Exercise

    As always, try to explain the statements above.
    Display the contents of the dataframe correlation_dist.
    What does it contain, why is that helpful in this case?

Next, let us use this dataframe in combination with the scatter plot from before to show both the data points and the empirical probability distribution of the correlation coefficient.

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles per gallon"),
        alt.Y("horsepower"),
    ) & alt.Chart(correlation_dist).mark_bar().encode(
        alt.X("correlation")
        .bin(maxbins=30)
        alt.Y("count()")
    )

In principle, this already shows what we want (we will interpret it later).
However, the visuals are not yet optimal.
Let us tune the result a bit:

.. code-block:: python

    alt.Chart(cars).mark_point().encode(
        alt.X("miles per gallon"),
        alt.Y("horsepower"),
    ) & alt.Chart(correlation_dist).mark_bar().encode(
        alt.X("correlation")
        .bin(maxbins=30)
        .title("correlation (bootstrapped)")
        .axis(labelAngle=-90),
        alt.Y("count()").axis(None),
    ).properties(
        height=50
    )

.. admonition:: Exercise

    What did we change? Why is that a good idea?

