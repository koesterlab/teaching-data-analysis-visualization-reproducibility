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
3. Read the text below while trying out all of the examples by literally typing them yourself in the notebook, each of them in a separate cell. Use :ref:`comments` to connect examples and exercises to the text.

.. _comments:

Comments
--------

Crucial for the readability, and thereby longterm sustainability, of code, are comments in natural language.
They can be used to outline thoughts or decisions behind the code, or explain complex technical necessities that aren't immediately obvious.
In Python, comments are written by prepending a line with a hash sign:

.. code-block:: python

    # this is a comment

.. _data_types:

Primitive data types, classes and objects
-----------------------------------------

Python supports various basic, so-called primitive, data types, namely

* integer: ``some_value = 5``
* decimal numbers (also called floats): ``some_value = 5.0``
* logical values (true/false, also called booleans): ``some_value = True``
* text (so-called strings): ``some_value = "this is my text"``

Each of these data types is implemented as a so-called class.
Classes are blueprints for objects, which are instances of a class.
In the scope of this course, we won't define our own classes, but we will use both the primitive types/classes named above as well as some classes defined in other libraries (e.g. Polars and Altair).

Operators over primitive data types
-----------------------------------

Python supports various operators that can be used on primitive data types.
The most important ones are:

* arithmetic operators: ``+``, ``-``, ``*`` (multiplication), ``/`` (division), ``%`` (modulo, returning the rest of a division)
* comparison operators: ``==`` (equal), ``!=`` (not equal), ``<`` (less than), ``>`` (greater than), ``<=`` (less than or equal), ``>=`` (greater than or equal)
* logical operators: ``and``, ``or``, ``not``
* assignment operators: ``=`` (assign a value to a variable), ``+=`` (add a value to a variable), ``-=`` (subtract a value from a variable), ``*=`` (multiply a variable by a value), ``/=`` (divide a variable by a value)

.. admonition:: Exercise

    Not all of these operators are available for all primitive data types.
    Try to guess and explain which ones are available for which data type.
    Below, verify your guesses in the notebook.

All of these operators can also be defined for arbitrary classes.
One has to check which of them are available in the documentation of the respective class.

Formatting
----------

The readability of source code is crucial for its maintainability and transparency for others.
Python already enforces a certain standardized structure by requiring indentation for blocks of code (see :ref:`control_flow`).
In addition, one should adhere to the official Python style guide, called `PEP8 <https://peps.python.org/pep-0008>`__.
To a large extend, PEP8 can be enforced automatically by IDEs like Visual Studio Code.
When setting up the development environment, we have already installed the `black <https://black.readthedocs.io>`__ code formatter, which can be used to automatically format Python code according to PEP8.
In a notebook, you can apply black's formatting by hitting Ctrl+Shift+P, typing format, and selecting format notebook.


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


.. _control_flow:

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

Above, we observe a central element of Python, which is the indentation.
Unlike in many other programming languages where indentation is solely used for improving the readability of code, indentation in Python literally has a meaning.
It is used to define and separate blocks of code that belong together, e.g. the body of a function, a loop, or a conditional statement.
While technically not enforced, it is best-practice to use four spaces for indentation.

Modify the for-loop from above:

.. code-block:: python
    
        for i in range(5):
            print(f"this is the {i}-th iteration")
        print("hello")

.. admonition:: Exercise

    Think about it: what happens upon execution of the loop? When is the ``hello`` printed?
    What happens if you shift the last print statement to the same indentation level as the first?

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

Functions always return something.
If nothing is specified (like above), they return the special value ``None`` (which means exactly that, none).
Alternatively, one can specify any return value, taken from whatever the function computes.

Consider the following example:

.. code-block:: python

    def twice(value):
        return value * 2

.. admonition:: Exercise

    Instead of directly returning the computation result, store it in a variable first and return the variable.
    Is the result the same when using both versions of the function?

There is an alternative way to write functions in Python, so-called lambda expressions.
Their single purpose is to define functions on the fly (e.g. when you have to pass a function as a parameter to another function).
They are meant only for single line statements, i.e. should have very little code in them.
An example lambda function could be

.. code-block:: python

    lambda x: x * 2

.. admonition:: Exercise

    1. What would above function return?
    2. Although not common, it is possible to assign a lambda expression to a variable.
       Then, it behaves exactly like the analogous normal function. Try this out here.

Methods
=======

Any data type, both the primitive ones and others defined by the user or certain libraries, can have so-called methods.
Methods are functions that are called on a so-called `object`, which is a realisation of a data type.

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

Tuples
======

Tuples represent an immutable collection of items:

.. code-block:: python

    some_tuple = (1, 2, 3)

They can be accessed by index:

.. code-block:: python

    print(some_tuple[0])

Lists
=====

Lists represent a mutable collection of items:

.. code-block:: python

    some_list = [1, 2, 3]

They can be accessed by index like tuples.
In addition, they can be modified by replacing, appending, removing, or inserting items:

.. code-block:: python

    some_list[0] = 42
    some_list.append(4)
    some_list.remove(2)
    some_list.insert(1, 23)

As can be seen, the latter three operations are conducted by invoking :ref:`methods <data_types>` of the list object.

Dictionaries
============

Dictionaries (in Python implemented via a built-in class called ``dict``) represent a collection of key-value pairs:

.. code-block:: python

    some_dict = {"name": "Alice", "age": 42}

They can be accessed by key:

.. code-block:: python

    print(some_dict["name"])

They can be modified by updating, adding, or removing key-value pairs:

.. code-block:: python

    some_dict["name"] = "Bob"
    some_dict["city"] = "New York"
    del some_dict["age"]

.. _iterables:

Iterables
=========

Objects in Python can be iterable, which means that their items can be accessed one after the other, e.g. in a for-loop.
Lists, tuples, and dictionaries are iterable, similar to the ``range`` object that we use :ref:`above <control_flow>`.

.. admonition:: Exercises

    1. Write a program that prints the tuple, list, and dictionary defined above by iterating over them in for-loops.
    2. Python offers a wide range of built-in helper functions for working with iterables, e.g. ``enumerate``, ``zip``, ``sorted``, ``reversed``.
       The ``itertools`` module of the Python standard library offers further functions, e.g. ``chain`` for concatenating the items of multiple iterables.
       Look up all of those examples in the documentation and try them out in the notebook.

Instantiating classes
=====================

Above, for tuples, lists, and dictionaries, we have seen that Python allows to instantiate classes by specifying their literal content with a special syntax.
This only works for certain built-in types like those shown above.
In general, classes are instantiated by calling the class name followed by parentheses, which enclose arguments needed to create the object, just like calling functions.
This is called a constructor.
This also works for lists, tuples, and dictionaries, since they are classes as well.
For example, we can convert the tuple to a list by using this mechanism:

.. code-block:: python

    converted_tuple = list(some_tuple)

It depends on the class which arguments a constructor accepts.
The list and tuple constructors accept and :ref:`iterable <iterables>` as argument.
The dictionary constructor (called ``dict``) accepts a dictionary or an iterable of tuples that are interpreted as key-value pairs.

.. admonition:: Exercises

    1. Try to convert the list back to a tuple.
    2. The ``dict`` class has a method ``items`` which returns an iterable of tuples representing the key-value pairs.
       Use this method to convert the dictionary to a list of tuples.
       Convert that list back into a dictionary using the ``dict`` constructor.

Exercises
=========

1. Write a program that prints the numbers from 1 to 10.
2. Write a program that declares a variable that holds a random number between 10 and 20.
3. Extend that program to print whether the number is even or odd.