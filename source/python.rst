***********************************************
A short introduction to programming with Python
***********************************************

The central idea behind programming is to write instructions that tell a computer what to do.
These instructions are written in a programming language, which provides a vocabulary and a grammar to work with.
Python is one such language.

Python is a high-level, interpreted programming language.
It is widely used in scientific computing, data analysis, and machine learning.
Python is known for its readability and ease of use.
It is a versatile language that can be used for a wide range of applications.
It is particularly popular in data science.

Python is an open-source language, which means that it is free to use and distribute. It has a large and active community of developers who contribute to its development and maintenance.
Python is supported by a wide range of libraries and frameworks that make it easy to work with data.

Central concepts
================

Python is programmed by creating text files that contain Python code.
Alternatively, it can be programmed within so-called (Jupyter) notebooks, which allow for a more interactive way of programming.
For simplicity, we will use the latter.
First, create a new notebook in your IDE (assuming you use Visual Studio Code or Gitpod):

1. Create a file named python.ipynb in the left panel.
2. Open the file and select the Python interpreter in the top right.
3. Read the text below while trying out all of the examples by literally typing them yourself in the notebook.

Primitive data types
--------------------

Python supports various basic, so-called primitive, data types, namely

* integer: ``some_value = 5``
* decimal numbers (also called floats): ``some_value = 5.0``
* logical values (true/false, also called booleans): ``some_value = True``
* text (so-called strings): ``some_value = "this is my text"``

Operators over primitive data types
-----------------------------------

Python supports various operators that can be used on primitive data types.
The most important ones are:

* arithmetic operators: ``+``, ``-``, ``*`` (multiplication), ``/`` (division), ``%`` (modulo, returning the rest of a division)
* comparison operators: ``==`` (equal), ``!=`` (not equal), ``<`` (less than), ``>`` (greater than), ``<=`` (less than or equal), ``>=`` (greater than or equal)
* logical operators: ``and``, ``or``, ``not``
* assignment operators: ``=`` (assign a value to a variable), ``+=`` (add a value to a variable), ``-=`` (subtract a value from a variable), ``*=`` (multiply a variable by a value), ``/=`` (divide a variable by a value)

Programming Python with Jupyter notebooks
=========================================

Open VSCode, and create a new Jupyter notebook by creating a file in the left panel ending on ``.ipynb``.


Variables
=========

Variables are used to store data in a program.
They can be declared by specifying name and value, written as an "equation":

.. code-block:: python

    some_value = 42

Investigating variables in a notebook
-------------------------------------

When putting the name of a variable at the end of a notebook cell, it will be automatically printed below the cell.

Printing information
====================

It is often useful to output information while a program is executed.
Python supports this via the built-in ``print`` :ref:`function <functions>`.

.. code-block:: python

    print("Hello, world!")

Formatting strings
==================

Strings can be formatted by prepending an "f" to the string and using curly braces to insert values of variables:

.. code-block:: python

    name = "Alice"
    age = 42
    print(f"Hello, my name is {name} and I am {age} years old.")

Control structures
==================

It is possible to encode decisions and repetitions in a program.
This is done via control structures.
The most important ones are if/else:

.. code-block:: python

    if some_value > 10:
        print("The value is greater than 10.")
    else:
        print("The value is less than or equal to 10.")

and for-loops:

.. code-block:: python
    
        for i in range(5):
            print(f"this is the {i}-th iteration")

.. _functions:

Functions
=========

Functions are used to encapsulate code that can then be executed multiple times.
They are defined with the ``def`` keyword, followed by the function name and the arguments in parentheses:

.. code-block:: python

    def greet(name):
        print(f"Hello, {name}!")

They are called by their name followed by parentheses (containing possible arguments/parameters):

.. code-block:: python

    greet("Alice")
    greet("Bob")

Imports
=======

Python has a large standard library, that is composed of so-called modules.
It is also possible to import modules from external packages.
This is done via the ``import`` keyword:

.. code-block:: python

    import math

    print(math.sqrt(16))

Documentation of the standard library can be found at https://docs.python.org/3/library/index.html
External packages can be found at https://pypi.org/, including links to their package specific documentation.

Exercises
=========

1. Write a program that prints the numbers from 1 to 10.
2. Write a program that declares a variable that holds a random number between 10 and 20.
3. Extend that program to print whether the number is even or odd.
4. Use the `requests <https://requests.readthedocs.io>`_ package to download the file https://raw.githubusercontent.com/koesterlab/data-analysis-and-visualization/main/data/kaggle_healthcare_dataset.csv.