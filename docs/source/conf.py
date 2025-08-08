# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Imports --------------------------------------------------------------
from datetime import date
import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Get the directory path of the conf.py
curpath = os.path.dirname(__file__)
# Absolute path to the src folder
path_to_src = os.path.join(os.path.abspath(os.path.join(curpath, "..", "..")))
# Add it the sys paths
sys.path.insert(0, path_to_src)

# -- Project information -----------------------------------------------------

project = "Python-Template"
# Inspired from: https://github.com/scikit-image/scikit-image/blob/main/doc/source/conf.py
copyright = f"2024-{date.today().year}, Max Mustermann"
author = "Max Mustermann"

# The full version, including alpha/beta/rc tags
release = "0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # extensions for autodetection of docstrings
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    # extension to link sphinx documentation --> allows to inlcude the documentation of python or other packages like numpy, torch etc..
    "sphinx.ext.intersphinx",
    # extension to detect also numpy docstrings (sphinx-own)
    "sphinx.ext.napoleon",
    # extension to detect also numpy docstrings (used by numpy itself)
    # "numpydoc", # https://stackoverflow.com/questions/12206334/sphinx-autosummary-toctree-contains-reference-to-nonexisting-document-warnings
    # extension to build a full HTTP link to the code on Github or such like --> not preferred
    # "sphinx.ext.linkcode",
    # extension to add links to highlighted source code
    "sphinx.ext.viewcode",
    # extension to add mathjax support
    "sphinx.ext.mathjax",
    # extension to add todo's
    "sphinx.ext.todo",
    # extension to be able to copy code blocks
    "sphinx_copybutton",
    # extension which makes it possible to plot in the documentation based on a python script
    # "matplotlib.sphinxext.plot_directive",
]

# Display todos by setting to True
todo_include_todos = True

# The encoding of source files.
source_encoding = "utf-8-sig"

# The master toctree document.
master_doc = "index"
# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Autodetection configuration ---------------------------------------------------

# Include Python objects as they appear in source files
# Default: alphabetically ('alphabetical')
autodoc_member_order = "bysource"
# Default flags used by autodoc directives
autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}
# Generate autodoc stubs with summaries from code
autosummary_generate = True

# How data-typing is done in the documentation
autodoc_typehints = "both"  # Data-type is in signature and also on the description
# autodoc_typehints = "description" # Data-type is only in the description
# Makes short typehints
# autodoc_typehints_format = "short"

# -- Napoleaon configuration -------------------------------------------------

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# Standard design
# html_theme = "alabaster"
# Classy design
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, maps document names to template names.
# Sidebars configuration
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "searchbox.html",
    ]
}

# If false, links to the reST sources are added to the pages.
html_show_sourcelink = True

# -- Options for linking different documentations ------------------------------
# Example configuration for intersphinx
# Refers to the Python, Numpy and Pytorch standard library.
intersphinx_mapping = {
    "python": (
        "https://docs.python.org/3",
        None,
    ),  # Python, add Python version number to the default address to corretcly reference the Python standard library
    "numpy": ("https://numpy.org/doc/stable/", None),  # Numpy
    "torch": ("https://pytorch.org/docs/stable/", None),  # Pytorch
}


# -- Options for filtering and converting docstring before building the documentations --------------


# This will convert all np to numpy, so that it can be linked in the documentation
def autodoc_convert_aliases(app, what, name, obj, options, lines):
    # print(what, name, obj, options)
    for i in range(len(lines)):
        lines[i] = lines[i].replace("np.", "numpy.")
        # Needs to be added for other packages
        # lines[i] = lines[i].replace("List[", "~typing.List[") # Not needed since the type are used


# This will filter the module docstring and parse only the @Desc
def autodoc_process_module(app, what, name, obj, options, lines):
    # Check if it is a module docstring and the lines are not empty
    if what == "module" and bool(lines):
        # Drop all lines except the lines with "@Desc" in front of the line
        # Cut everything except the actual description.
        lines[:] = list(  # [:] means inplace modification, which is needed
            map(
                lambda line: line.split(" : ")[-1].strip(),
                filter(lambda x: "@Desc" in x, lines),
            )
        )


# Parse the docu with the setup function
def setup(app):
    app.connect("autodoc-process-docstring", autodoc_convert_aliases)
    app.connect("autodoc-process-docstring", autodoc_process_module)
