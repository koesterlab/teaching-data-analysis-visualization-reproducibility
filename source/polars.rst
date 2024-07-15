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

Step 1: Setup the notebooks
===========================

First, create a new file ``polars.ipynb`` under ``notebooks/`` and open it in VSCode.
In the opened notebook, select the pystats environment as the kernel with the button on the top right.