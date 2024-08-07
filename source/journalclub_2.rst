****************************************
Journal club 2: statistical significance
****************************************

Next, we will discuss the pitfalls of determining whether an observation should be considered significant or not.
For this purpose, we will read and discuss `"The fickle P value generates irreproducible results" by Halsey et al. <https://doi.org/10.1038/nmeth.3288>`_.

Now, let us use what we have learned before to explore the findings of this manuscript, relate this to the reality of your own research, and discuss alternatives.

.. admonition:: Exercise

    What conclusions can we draw from the article?

Step 1: Reproducing the article data
====================================

Create a notebook with a function that generates two samples of two normal distributions with a difference of 0.5 in their mean, just like the article suggests.

.. code-block:: python

    import polars as pl
    import altair as alt
    alt.data_transformers.enable("vegafusion")
    from scipy.stats import norm

    def random_samples():
        sample_0 = norm.rvs(size=10, loc=0)
        sample_1 = norm.rvs(size=10, loc=0.5)

        return pl.DataFrame({"value": sample_0, "group": "A"}).vstack(
            pl.DataFrame({"value": sample_1, "group": "B"})
        )

Initially we set the number of samples to 10 vs 10.

.. dropdown:: Explanation

    The first sample has a mean of 0, the second sample has a mean of 0.5.
    The two samples are represented as one :ref:`Polars <polars>` ``DataFrame`` with columns ``group`` (values ``A``, and ``B``) and ``value``.

.. admonition:: Exercise
    
    Assign this dataframe to the variable ``samples``.

Step 2: Visualizing the data
============================

Plot the two distributions as a point chart (use ``mark_point``) with :ref:`Altair <altair>`.
Show the mean of each group as a horizontal line (use ``mark_tick``) in a layer above the points (combine the two charts with ``+``).

Step 3: Calculating the effect size
===================================

We create a function that calculates the effect size between the two by calculating the mean and taking the difference.

.. code-block:: python

    def estimate_effect_size(samples):
        means = samples.group_by("group").mean()
        return (
            means.filter(pl.col("group") == "B").select(pl.col("value")) - 
            means.filter(pl.col("group") == "A").select(pl.col("value"))
        ).item()

.. _journalclub_bootstrap:

Step 4: Calculate a bootstrap sample
====================================

Bootstrapping is a way to estimate the uncertainty behind given data.
A precious property is that it does not require us to make statisticial assumptions about the underlying distribution of the data.
Hence, it can be used as a universal tool to estimate the uncertainty of effect sizes in a conservative way, without the risk to violate statistical assumptions.
Of course, such versatility comes at a cost: being conservative means that we might not detect an effect that is actually there.
In the scope of this course though (biomedicine), the only way to overcome the latter is to (a) increase sample sizes and (b) seek for advice from statisticians.
In contrast, trying to apply sophisticated statistical methods without thoroughly understanding them down to their requirements and assumptions is a dangerous path.

Bootstrapping means drawing **many** random samples **with replacement** from the original data.
For each of these samples, we calculate the effect size.
The distribution of these effect sizes gives us an idea of the uncertainty.

Let's do that now:

.. code-block:: python

    def get_bootstrap(samples):
        group_a = samples.filter(pl.col("group") == "A")
        group_b = samples.filter(pl.col("group") == "B")
        return group_a.sample(n=group_a.shape[0], with_replacement=True).vstack(
            group_b.sample(n=group_b.shape[0], with_replacement=True)
        )

    bootstraps = pl.DataFrame({"effect_size": [estimate_effect_size(get_bootstrap(samples)) for _ in range(10000)]})

.. dropdown:: Explanation

    We create a function that generates a bootstrap sample.
    The function first separates group ``A`` and group ``B`` in the data frame.
    Then, it takes a random sample of the same size as the original data from each group, with replacement.
    This is how bootstrapping is defined.

    Then, we apply this function 10000 times and calculate the effect size for each of the bootstrap samples.


Step 5: Visualizing the bootstrap distribution
==============================================

Plot the distribution of the effect sizes as a histogram with :ref:`Altair <altair>`.

.. admonition:: Exercise

    Repeatedly run the notebook with different sample sizes for Step 1.
    What can we learn from the distribution of the effect sizes?

.. dropdown:: Take-home message

    Depending on the size or the original samples the idea about the uncertainty can be more or less accurate.
    Therefore, it is **conservative** to consider the smallest effect instead of the most abundant as the truth.
    The best is always to show the entire distribution but (help the viewer to) interpret it conservatively.
