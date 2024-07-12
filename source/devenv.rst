***************************
The development environment
***************************

There are numerous options for how to perform data analysis.
A central question is which environment to use.
This entails

1. the operating system (OS),
2. the development environment.

The operating system is crucial for ensuring reproducibility of results.
Proprietary operating systems, such as Microsoft Windows or macOS, entail the risk of not being runnable on newer hardware after a while.
Hence, one would have to update the OS, which can cause the analysis to break.
Therefore, it is recommended to use open-source operating systems, such as Linux distributions, which are free to use and distribute.
Luckily, linux is directly available from windows via the Windows Subsystem for Linux (WSL).

Choosing a suitable development environment can dramatically increase the productivity while performing data analysis.
There are numerous options available.
In this course, we will use Visual Studio Code (VSCode), which is one of the most popular options and offers numerous useful extensions for our tasks.

If you are on Windows, follow `these <https://code.visualstudio.com/docs/remote/wsl>`_ instructions to install VSCode in combination with WSL.
Otherwise, just install `VSCode <https://code.visualstudio.com>`_.

After installing VSCode, open it and install the following extensions:

* Python
* Jupyter
* Rainbow csv
* indent-rainbow

The VSCode windows contains three main areas:

.. image:: https://code.visualstudio.com/assets/home/home-screenshot-mac-2x-v2.png
   :alt: VSCode window
   :align: center

1. The sidebar on the left contains the file explorer, which allows you to navigate through your files.
2. The main area in the right center is where you edit files or notebooks.
3. The area at the bottom right shows a so-called terminal, which allows you to run commands directly from within VSCode.
   It might be hidden initially, but can be opened by clicking on the "Terminal" menu and selecting "New Terminal".