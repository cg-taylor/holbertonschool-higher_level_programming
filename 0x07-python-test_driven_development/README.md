0x07. Python - Test-driven development

Up until now, we have been learning to code through procedure-driven development. This project introduces test-driven development primarily through doctests, but there is one mandatory unittest task at the end of the project.

## Background Context
Starting from today:
- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
- The intranet checks for Python projects won't be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- We strongly encourage you to work together on test cases, so that you don't miss any edge case. But not in the implementation of them!
- Don't trust the user, always thing about all possible edge cases!

## Learning Objectives
- Why Python programming is awesome
- What's an interactive test
- Why tests are important
- How to write docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements
**General**
- Allowed editors: vi, vim, emacs
- All your files should end with a new line

**Python Scripts**
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- The first line of all your files should be `#!/usr/bin/python3` exactly
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

**Python Test Cases**
- All your test files should be inside a folder `test`
- All your tests files should be text files (extension `.txt`)
- All your tests should be executed using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Akk your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- We strongly encourage you to work together on test cases so that you don't miss any edge cases

## Files
0-add_integer.py:
	Adds two numbers (handles integers and floats)

2-matrix_divided.py:
	Divides all elements of a matrix by a non-zero divisor

3-say_my_name.py:
	Prints a sentence with a first and last name

4-print_square.py:
	Prints a square of size `size` using the `#` character

5-text_indentation.py:
	Print a block of text with two new lines after each `.`, `?`, and `:`

**tests/**:
	Contains all doctest and unittest files

The following files are doctest files for the corresponding Python script above:
	- 0-add_integer.txt
	- 2-matrix_divided.txt
	- 3-say_my_name.txt
	- 4-print_square.txt
	- 5-text_indentation.txt


6-max_integer_test.py:
	Unittests for the max_integer function, which locates the largest integer in a list of integers
