# 0x0A. Python - Inheritance

## Learning Objectives
- Why Python programming is awesome
- What is a superclass, base class, or parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when, and how to use the `isinstance`, `issubclass`, `type`, and `super`built-in functions


## Requirements
- Allowed editors: vi, vim, emacs
- All your files should end wth a new line
- All modules, classes, and functions should have documentation

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- The first line of all your filess should be `#!/usr/bin/python3` exactly
- A `README.md` file at the root of your project directory is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- All your test files should be inside a folder called `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed using this command: `python3 -m doctest ./tests/*`
- We encourage you to work together on test cases so that you don't miss any edge cases


## Files
0-lookup.py:
	Return the list of available attributes and methods of an object

1-my_list.py:
tests/1-my_list.txt:
	Print a list of integers in ascending order

2-is_same_class.py:
	Return True if the object is exactly an instance of the specified class, otherwise False

3-is_kind_of_class.py:
	Return True if the object is an instance of, or of a class that inherited from, the specified class; otherwise False

4-inherits_from.py:
	Return True if the object is an instance of a class that inherited, directly or indirectly, from the specified class

5-base_geometry.py:
	Define an empty class BaseGeometry

6-base_geometry.py:
	Define a method in the BaseGeometry class called `area`

7-base_geometry.py:
tests/7-base_geometry.txt:
	Define a method in BaseGeometry called `integer_validator` that checks if a variable is an integer

8-rectangle.py:
	Define a class Rectangle that inherits from BaseGeometry and has two values to inialize

9-rectangle.py:
	Implement the area() method, modify print() and str() methods to print/return a specific descriptor string

10-square.py:
	Define a class Square that inherits from Rectangle, override __init__ and implement area()

11-square.py:
	Moduify print() and str() to print/return the square descriptor string "[Square] <width>/<height>"


### Author
Cynthia Taylor
June 2, 2020
