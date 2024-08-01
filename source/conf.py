# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from sphinxawesome_theme.postprocess import Icons


project = 'Course: Data Analysis and Visualization'
copyright = '2024, Prof. Dr. rer. nat. Johannes Köster'
author = 'Prof. Dr. rer. nat. Johannes Köster'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_design']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']

html_permalinks_icon = Icons.permalinks_icon

pygments_style = "sphinx"

html_compact_lists = True