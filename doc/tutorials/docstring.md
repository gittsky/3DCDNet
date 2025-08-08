<!--
Created: Fri Nov 24 2023 13:39:29 GMT+0100 (Mitteleuropäische Normalzeit)
Modified: Fri Nov 24 2023 13:49:05 GMT+0100 (Mitteleuropäische Normalzeit)
-->

# Docstrings and Python File Headers

This tutorial provides a guide on how to write clear file headers and docstrings for your Python project.

## Python File Header

VSCode allows you to easily create custom text snippets for generating file headers quickly. The purpose of a file header is to provide information about the content and purpose of the Python file, helping future developers identify the author, the date and the content of the code. This step-by-step tutorial is based on web articles[^1] [^2].

### Installation

1. Open VSCode and select `File` $\rightarrow$ `Preferences` $\rightarrow$ `Configure User Snippet`.
2. Search for `python.json` in the search box and select it.

![Installation: Step 2](imgs/installation_file_header_2.png)

3. Add the following code to the .json file:

```json
{
    "HEADER":{
        "prefix": "header_python",
        "body": [
        "#!/usr/bin/env python",
        "# -*-coding:utf-8 -*-", 
        "'''",
        "@File    :   $TM_FILENAME",
        "@Time    :   $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE:$CURRENT_SECOND",
        "@Author  :   Max Mustermann",
        "@Version :   $0",
        "@Contact :   max.mustermann@ipm.fraunhofer.de",
        "@License :   (C)Copyright $CURRENT_YEAR-$CURRENT_YEAR, Fraunhofer-Institut für Physikalische Messtechnik IPM, Max Mustermann",
        "@Desc    :   $1",
        "@Source  :   $2",
        
        "'''",
        "$3"
        ],
        "description": "Header of a python file."
    }
}
```

* Replace "Max Mustermann" with your name.
* The `@Desc` line should provide a brief description of the purpose of the Python file.
* The `@Source` line should indicate the reference used to implement the algorithm. If there are no sources, you can delete this line. If multiple sources were used, list them all on separate lines with numbering (`@Source0`,      `@Source1`,      `@Source2`, ...).

### Usage

1. To use the file header snippet, open a new Python file and start typing `header_python`. The snippet will appear.

![Usage: Step 1](imgs/usage_file_header_1.png)

2. Press Enter and the file header will be inserted into the file.

![Usage: Step 2](imgs/usage_file_header_2.png)

3. Tab through the fields to insert the version number, description, and source.

![Usage: Step 3](imgs/usage_file_header_3.png)

## Docstrings

A docstring is a string literal that appears as the first statement in a module, function, class, or method definition. It becomes the `__doc__` special attribute of that object. Docstrings should summarize the functionality and define the arguments, exceptions, etc. associated with the Python object. For more information, please refer to the following websites: [Source 1](https://peps.python.org/pep-0257/), [Source 2](https://peps.python.org/pep-0287/), [Source 3](http://daouzli.com/blog/docstring.html). 
The preferred docstring format is the **`Numpydoc`** format style. You can find a detailed description of this format on this [website](https://developer.lsst.io/python/numpydoc.html), which may answer any further questions you have.

### Methods and functions

There is a VSCode extensions called [`autoDocstring`](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) that makes generating docstrings for functions and methods easier. To install it, follow these steps:

#### Installation

1. Go to the `Extensions: Marketplace` in VSCode, search for `autoDocstring`, and install the extension.

![Installation: autoDocstring](imgs/installation_autoDocstring.png)

2. Enable the correct docstring format by following these steps:
    * Press `Ctrl + Shift + P` to open the Visual Studio Code Command Palette.
    * Search for `Preferences: Open User Settings` and press `Enter`.
    * In the search bar for extensions, search for `autoDocstring` and hit `Enter`.
    * Adjust the values as shown in the following image:

![Settings for docstring](imgs/setting_docstring_format.png)

#### Usage

1. Write the entire function first.
2. Make sure the [data typing](https://docs.python.org/3/library/typing.html) is correctly specified in the function signature.
   * **Important:** Do not format the function using Black before writing the docstring, as `autoDocstring` is not compatible with Black-formatted function signatures.
   * The function should look like this:

![Usage autoDocstring: Step 1](imgs/usage_autodocstring.png)

1. Place the cursor below the function signature, type `"""`, and press `Enter` to trigger the docstring popup window.

![Usage autoDocstring: Step 2](imgs/trigger_docstring.png)

4. The docstring template will appear, as shown in the example below.

```python
def foobar(foo: int, bar: None | int | NDArray[np.int16] = None, baz: None | Callable[[int, int], int] = lambda x,y: x+y) -> list[int]:
    """_summary_

    _extended_summary_

    Parameters
    ----------
    foo : int
        _description_
    y : x
        _description_
    bar : None | int | NDArray[np.int16], optional
        _description_, by default None
    baz : None | Callable[[int, int], int], optional
        _description_, by default lambdax

    Returns
    -------
    list[int]
        _description_

    Raises
    ------
    InvalidFooValue
        _description_
    """
    # Check for invalid foo values
    if foo == -1:
        raise InvalidFooValue()

    # Do some processing
    out = [-1]
    if bar is None:
        out = foo * [foo]
    else:
        if isinstance(bar, int):
            out = [baz(foo, bar) if baz is not None else foo * bar]
        else:
            out = bar.flat[0] * [foo]
            
    return out
```

5. Complete the placeholders by following these rules:
   * `_summary_` : summarize the function with one sentence.
   * `_extended_summary_` : if more content is needed to clarify the `_summary_` , add it to this section, but keep it under 3 sentences.
   * `Returns` : Add the name of the returned object. If only a value is returned, add a name, describing the returned value. This will assure a nicer formatting.
   * `Yields` : `Yields` is used identically to `Returns` , but for generators.
   * `See Also` : Use the `See Also` section to link to related APIs that the user may not be aware of, or may not easily discover from other parts of the docstring. 
   * `Notes` : `Notes` is an optional section that provides additional conceptual information about the API.
   * `Reference` : `References` cited in the `Notes` section are listed here.
   * `Examples` : `Examples` is an optional section for usage examples written in the doctest format. These examples do not replace unit tests, but are intended to be tested to ensure documentation and code are consistent. While optional, this section is useful for users and developers alike.
   * **For Numpy Users:**
       * if possible, add the dimensionality of the numpy array when occuring in parameters or returns. This will help future readers and users.

6. The completed docstring should look like this:

```python
def foobar(foo: int, bar: None | int | NDArray[np.int16] = None, baz: None | Callable[[int, int], int] = lambda x,y: x+y) -> list[int]:
    """Processes the input parameters and showcases docstrings and typing.

    The processing is based on the possible data types of the input parameters. Different arithmetic operations are performed depending on them.

    Parameters
    ----------
    foo : int
        Containing an integer value.
    bar : None | int | NDArray[np.int16] (N, 3), optional
        Containing None, an integer, or a numpy array with shape (N, 3), by default None.
    baz : None | Callable[[int, int], int], optional
        If not None, it is a function, by default lambda x,y: x+y.

    Returns
    -------
    out : list[int]
        Processed data.

    Raises
    ------
    InvalidFooValue
        Raised if foo has an invalid value.

    See Also
    --------
    foobar2()
    
    Notes
    -----
    **Source:** This docstring style is based on this tutorial [1]_.
    **Notes for future coder:** This section is optional but supports conceptual documentation.
    
    References
    ----------
      [1] [Tutorial Docstrings](https://developer.lsst.io/python/numpydoc.html#py-docstring-short-summary)
      
    Examples
    --------
    A simple example for the usage of the function:

    >>> foobar(2)
    [ 2, 2 ]  
    """
    # Check for invalid foo values
    if foo == -1:
        raise InvalidFooValue()

    # Do some processing
    out = [-1]
    if bar is None:
        out = foo * [foo]
    else:
        if isinstance(bar, int):
            out = [baz(foo, bar) if baz is not None else foo * bar]
        else:
            out = bar.flat[0] * [foo]
            
    return out
```

### Classes

Numpydocstrings for classes are not included by the `autoDocstring` extension. Therefore, it is necessary to define them similiarly to the [Python file header](#python-file-header).

#### Installation

To create the template, follow these steps:

1. Open the `python.json` as described in the [Python file header section](#python-file-header).
2. Insert the following snippet template:

```json
"CLASS_DOCSTRING": {
    "prefix": "docstring_class",
    "body": [
        "\"\"\"${1:_summary_}.\n\n",
        "${2:_extended_summary_}.\n\n",
        "Attributes",
        "----------",
        "${3:_attribute_} : ${4:_type_}",
        "\t${5:_description_}.\n",
        "Methods",
        "-------",
        "${6:_method_signature_}(${7:_params_} : ${8:_datatype_}) -> ${9:_return_datatype_}",
        "\t${10:_description_}.\n",
        "\"\"\"",
        "$0",
    ],
    "description": "Numpy-Docstring for classes."
}
```

#### Usage

1. Write the class, its methods and attributes first.
2. Make sure the [data typing](https://docs.python.org/3/library/typing.html) is correctly specified in the method signatures. Use the `autoDocstring` extension and the tutorial from [`Methods and functions` section](#methods-and-functions). Follow these guidlines for the different types of class methods based on the Sphinx documentation [^3] [^4]:
   * Do not include the `self` parameter in the `Parameters` .
   * Regular class methods have the same docstring as regular functions.  
   * [`Properties`](https://realpython.com/python-property/) with both a getter and setter should be documented in their getter method. Only if the setter method contains notable behavior, it should be mentioned in the setter-docstring.
   * Special members (Any methods or attributes, that starts and ends with double underscore, e.g. `def __special__(self)` ) with docstrings are not included by default, but can be set to.
   * Private members (Any methods or attributes, that starts with an underscore, e.g. `def _private(self)` ) with docstrings are not included by default, but can set to.
3. Place the cursor below the class signature, type `docstring_class`, and press `Enter` to trigger the template snippet.
4. Complete the placeholders following these rules:
   * `_summary_` : Describe the class in one sentence. 
   * `_extended_summary_` : If more information is needed to describe the class, add it here. 
   * `_attribute_` : List all of the class's attributes here and add their datatypes and descriptions. Exclude private attributes.
   * `_method_signature_` : List all of the class's methods here and add their parameters + datatypes, datatype of the returned values and a brief description. Exclude private methods.

[^1]: https://shantoroy.com/tutorial/add-header-to-python-file-vscode.md/ by Shanto Roy, 14.11.2023
[^2]: https://code.visualstudio.com/docs/editor/userdefinedsnippets by VSCode, 14.11.2023
[^3]: https://developer.lsst.io/python/numpydoc.html#py-docstring-class-structure by lsst package, 23.11.2023
[^4]: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html by napolean package, 23.11.2023
