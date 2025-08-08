<!--
Created: Wed Feb 21 2024 09:53:14 GMT+0100 (Mitteleuropäische Normalzeit)
Modified: Thu Feb 22 2024 17:41:26 GMT+0100 (Mitteleuropäische Normalzeit)
-->

# Collection of useful VSCode Extensions and their settings

This tutorial provides information about usefule VSCode Extesnions and their setting.

## Spell Checker

> We recommend the VSCode extension [ `Code Spell Checker` ](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).
> As it will check also the code for spelling errors, we need to limit its correction behavior to comments only.

## Tutorial 

1. Go to the `Extensions: Marketplace` in VSCode, search for `Code Spell Checker` by `Street Side Software`, and install the extension.

2. Enable the correct docstring format by following these steps:
    - Press `Ctrl + Shift + P` to open the Visual Studio Code Command Palette.
    - Search for `Preferences: Open User Settings` and press `Enter`.
    - Open the user settings JSON file by clicking on the icon `Open Settings (JSON)` in the right top corner.
    - Add the following configuration to the JSON-file:

```json
"cSpell.languageSettings": [
    {
        "languageId": "python",
        "includeRegExpList": [
            "/#.*/",
            "/('''|\"\"\")[^\\1]+?\\1/g"
        ]
    },
    {
        "languageId": "javascript",
        "includeRegExpList": [
            "CStyleComment"
        ]
    }
]
```

3. The spellchecker should be now active for `.py` files and mark errors only in the comment sections.
