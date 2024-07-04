# 0x00. Python - Variable Annotations

## Description

This project focuses on learning and applying type annotations in Python. Type annotations help in specifying function signatures and variable types, improving code readability, and enabling static type checking with tools like mypy.

## Learning Objectives

By the end of this project, you should be able to:

- Understand type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Comprehend duck typing and its application.
- Validate your Python code with mypy.

## Resources

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Requirements

- All files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files must end with a new line.
- First line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder.
- Code should follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- Modules, classes, and functions should have documentation.
- Documentation should be a real sentence explaining the purpose.

## Tasks

### 0. Basic annotations - add

Write a type-annotated function `add` that takes two floats `a` and `b` and returns their sum as a float.

### 1. Basic annotations - concat

Write a type-annotated function `concat` that takes two strings `str1` and `str2` and returns a concatenated string.

### 2. Basic annotations - floor

Write a type-annotated function `floor` that takes a float `n` and returns the floor of the float.

### 3. Basic annotations - to string

Write a type-annotated function `to_str` that takes a float `n` and returns its string representation.

### 4. Define variables

Define and annotate the following variables:

- `a`: an integer with a value of 1.
- `pi`: a float with a value of 3.14.
- `i_understand_annotations`: a boolean with a value of True.
- `school`: a string with a value of “Holberton”.

### 5. Complex types - list of floats

Write a type-annotated function `sum_list` that takes a list of floats `input_list` and returns their sum as a float.

### 6. Complex types - mixed list

Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats `mxd_lst` and returns their sum as a float.

### 7. Complex types - string and int/float to tuple

Write a type-annotated function `to_kv` that takes a string `k` and an int or float `v`, returning a tuple. The tuple's first element is `k` and the second element is the square of `v`.

### 8. Complex types - functions

Write a type-annotated function `make_multiplier` that takes a float `multiplier` and returns a function that multiplies a float by `multiplier`.

### 9. Let's duck type an iterable object

Annotate the function `element_length` with appropriate types.

### 10. Duck typing - first element of a sequence

Augment the function `safe_first_element` with the correct duck-typed annotations.

### 11. More involved type annotations

Add type annotations to the function `safely_get_value` based on the given parameters and return values.

### 12. Type Checking

Use mypy to validate and apply necessary changes to the given code.

## Usage

To check your type annotations with mypy:

```sh
mypy your_script.py
