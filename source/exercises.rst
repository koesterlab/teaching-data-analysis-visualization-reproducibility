.. _further_exercises:

*****************
Further exercises
*****************

In order to pracice what we have learned, you can now on your own explore a public dataset (or your own data).

For the public dataset, do the following:

Create a new subfolder ``chapters/further_exercises``, and use pixi to install 

* ``altair``
* ``polars``
* ``pyarrow``
* ``altair_saver``
* ``vegafusion``
* ``vegafusion-python-embed``
* ``ipykernel``
* ``ucimlrepo``

The latter will allow us to download public biomedical example datasets from UC Irvine.
Then, in the following, you find example code showing how to download the `heart disease dataset <https://archive.ics.uci.edu/dataset/45/heart+disease>`__ using the ``ucimlrepo`` package and load it into a single polars dataframe.
Try to understand the code with what you have learned so far (if in doubt, try to find the documentation of the respective functions and methods in the polars and ucimlrepo documentation).

.. code-block:: python

    import polars as pl
    from ucimlrepo import fetch_ucirepo

    heart_disease = fetch_ucirepo(id=45) # the heart disease dataset has the id 45 in the ucimlrepo package
    data = pl.from_pandas(heart_disease.data.features).with_row_index().join(
        pl.from_pandas(heart_disease.data.targets).with_row_index(),
        on="index"
    )
    print(heart_disease.variables) # print info about the contained variables
    # The variable `num` is the target variable, indicating no heart disease (0) or heart disease of increasing severity (1, 2, 3, 4).

Next, start analyzing the resulting polars dataframe using Polars and Altair.
Try to find as many insights as possible, e.g., by plotting the distributions of the features, looking for correlations, etc.
