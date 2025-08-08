<!--
Created: Wed Feb 28 2024 15:06:46 GMT+0100 (Mitteleuropäische Normalzeit)
Modified: Thu Feb 29 2024 16:58:05 GMT+0100 (Mitteleuropäische Normalzeit)
-->

# Automatic docstring documentation with Sphinx

This tutorial will explain how the [sphinx-package](https://www.sphinx-doc.org/en/master/tutorial/index.html) can be utilised to produce documentation from docstring of the source code.
This process can be performed by the CI-Runner automatically and moved to the Gitlab pages.[^1] [^2]

## Build documentation locally

01. Make sure, you are in a python enviroment, which contains all python packages used in the source code. Furthermore, add an empty `__init__.py` file in each subdirectory of the `src`-folder.
02. Install sphinx and all necessary packages:

```shell
pip install --upgrade pip
pip install -U sphinx furo sphinx-rtd-theme sphinx-copybutton numpydoc matplotlib
```

03. Create a `docs` folder in the project directory and navigate into it:

```shell
mkdir docs
cd docs
```

04. Generate the minimal sphinx documentation structure by entering following in the terminal [^8]:

```shell
sphinx-quickstart
```

05. Series of questions are presented. They need to be answered which will result in following output:

```shell
Welcome to the Sphinx 5.0.2 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name: Python-Template
> Author name(s): Max Mustermann
> Project release []: 0.1

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: en

Creating file /.../python/docs/source/conf.py.
Creating file /.../python/docs/source/index.rst.
Creating file /.../python/docs/Makefile.
Creating file /.../python/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /.../python/docs/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

06. Modify the generated `docs/source/conf.py` file to autodetect the docstrings of the source files in the `src` folder:

```python
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
```

07. Next all python modules and their docstrings need to be linked by sphinx. Enter following to let sphinx crawl through the source folder `src` and save the docstring collection as `.rst`-files to the `docs/source/`:

```shell
cd ..
sphinx-apidoc -o docs/source  src 
```

08. Add `modules` to the `docs/source/index.rst` generated by the `sphinx-quickstart`:

```reST
.. Python-Template documentation master file, created by
   sphinx-quickstart on Wed Feb 28 13:31:15 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Python-Template's documentation!
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

09. Following command will build the documentation based on the `.rst`-files in the `docs/source/` path as `html` and store it in `docs/build`:

```shell
sphinx-build -b html docs/source docs/build
```

10. Inspecting the website enter these commands and open the website [http://0.0.0.0:60078/](http://0.0.0.0:60078/):

```shell
cd docs/build
python -m http.server 60078
```

## Build documentation with the CI-Runner and push it to Gitlab-pages

01. Add the `documentation` stage to the CI-Runner by modify the `.gitlab-ci.yml`:

```yml
# Build a Docker image with CI/CD and push to the GitLab registry.
# Docker-in-Docker documentation: https://docs.gitlab.com/ee/ci/docker/using_docker_build.html

# clones all submodules, otherwise they are not present for the build context.
variables:
  GIT_SUBMODULE_STRATEGY: recursive

stages:
  - build
  - documentation

default:
  interruptible: true

# Rules for when the docker file should be built, they have to be referenced whan they should be applied.
# ------------------------------------------------------------------------------------------------
.every_merge_request:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_PIPELINE_SOURCE == "web"'

.main_and_dev_commits:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "push" && ($CI_COMMIT_BRANCH == "dev" || $CI_COMMIT_BRANCH == "main")'
    - if: '$CI_PIPELINE_SOURCE == "schedule"'
    - if: '$CI_PIPELINE_SOURCE == "web"'
# ------------------------------------------------------------------------------------------------

# Build the docker image
# ------------------------------------------------------------------------------------------------
docker-build:
  # Use the official docker image.
  image: docker:latest
  stage: build
  services:
    - docker:dind
  before_script:
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
  variables:
    DOCKER_HOST: "tcp://docker:2376"
    DOCKER_TLS_CERTDIR: "/certs"
  timeout: 12h
  rules:
  - !reference [.every_merge_request, rules]
  - !reference [.main_and_dev_commits, rules]

  # on which runner the docker should be built
  tags:
    - container-builder-linux

  # Default branch leaves tag empty (= latest tag)
  # All other branches are tagged with the escaped branch name (commit ref slug)
  script:
    - docker pull "$CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG" || true
    - docker build --rm --pull --cache-from "$CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG" -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG" -f docker/Dockerfile .
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG"
# ------------------------------------------------------------------------------------------------

# Generate the sphinx documentation
# ------------------------------------------------------------------------------------------------
pages:
  stage: documentation
  # Use the build docker image to have all package dependencies
  image: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG
  # Install sphinx and its dependencies
  before_script:
    - pip install --upgrade pip
    - pip install -U sphinx furo sphinx-rtd-theme sphinx-copybutton numpydoc matplotlib
  script:
  # Sphinx crawles through the source code and collects the docstrings
    - sphinx-apidoc -o docs/source src
  # Sphinx builds the documentation as html and saves it to the Gitlab-Pages, where it can be inspected
    - sphinx-build -b html docs/source public
  artifacts:
    expose_as: "docs-generated"
    paths:
    - public
  rules:
    - !reference [.every_merge_request, rules]
    - !reference [.main_and_dev_commits, rules]
  # on which runner the docker should be built
  tags:
    - container-builder-linux
# ------------------------------------------------------------------------------------------------
```

02. Add an empty `__init__.py` file in each subdirectory of the `src` folder and install the python package `sphinx`.

```shell
pip install --upgrade pip
pip install -U sphinx
```

03. Create a `docs` folder in the project directory and navigate into it:

```shell
mkdir docs
cd docs
```

04. Generate the minimal sphinx documentation structure by entering following in the terminal [^8]:

```shell
sphinx-quickstart
```

05. Series of questions are presented. They need to be answered which will result in following output:

```shell
Welcome to the Sphinx 5.0.2 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name: Python-Template
> Author name(s): Max Mustermann
> Project release []: 0.1

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: en

Creating file /.../python/docs/source/conf.py.
Creating file /.../python/docs/source/index.rst.
Creating file /.../python/docs/Makefile.
Creating file /.../python/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /.../python/docs/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

06. Modify the generated `docs/source/conf.py` file to autodetect the docstrings of the source files in the `src` folder:

```python
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
```

07. Commit and push these changes and every time something is pushed/merged to the `dev` or `main` branch, the CI-runner will generate a documentation based on the docstrings within the python code in the `src` folder.
08. Inspect the documentation in the sidebar menu under `Deploy` $\rightarrow$ `Pages` $\rightarrow$ `Access pages`, where a link is provided.

[^1]: https://www.sphinx-doc.org/en/master/usage/quickstart.html, 28.02.2024
[^2]: https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs, 28.02.2024
[^3]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration, 28.02.2024
[^4]: https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/, 28.02.2024
[^5]: https://github.com/romanvm/sphinx_tutorial/blob/master/docs/conf.py, 28.02.2024
[^6]: https://stackoverflow.com/questions/53668052/sphinx-cannot-find-my-python-files-says-no-module-named
[^7]: https://gitlab.com/pages/sphinx
[^8]: https://www.sphinx-doc.org/en/master/usage/quickstart.html, 28.02.2024
