# 0x0C. Python - Almost a circle

## Background Context
The AirBnB project is a significant part of the Higher Level curriculum. This project helps students prepare for it by integrating everything that they have learned about Python up to this point in one larger project.

## Learning Objectives
- What is unit testing and how to implement it in a large project
- How to serialize and deserialize a class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Requirements
- Allowed editors: vi, vim, emacs
- All of your files should end with a new line

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- The first line of all your files should be `#!/usr/bin/python3` exactly
- A README.md at the root of the project directory is mandatory
- Your code should use the `PEP8` style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should be documented: `python3 -c 'print(__import("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import("my_module").my_function.__doc__)'` and `python3 -c 'print(__import("my_module").MyClass.my_function.__doc__)'`

### Python Unit Tests
- All your test fles should be inside a folder `tests`
- You have to use the unitttest module
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start with `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base.py`, unit tests must be in `tests/test_models/test_base.py`
- All your tests should be executed using `python3 -m unittest discover tests`
- You can also test file by file using `python3 -m unittest <filename>`
- We strongly encourage you to work together on test cases so that you don't miss any edge cases

### Tasks and Files
 0. If it's not tested it doesn't work
    - File: `tests/`
    - All files, classes, and methods must be unit tested and PEP8 validated

 1. Base class
    - File: `models/base.py`
    - Define the parent class called `Base` to manage the `id` attribute
         - private class attribute: `__nb_objects`
	 - class constructor parameter: `id=None`

    - File: `models/__init__.py`
    - empty

 2. First Rectangle
    - File: `models/rectangle.py`
    - Define class `Rectangle`, which extends `Base`
         - private instance attributes: `__width`, `__height`, `__x`, `__y`
	 - public getters/setters for each attribute
	 - class constructor parameters: `width, height, x=0, y=0, id=None`

 3. Validate attributes
    - File: Update `models/rectangle.py`
    - Validate all setter methods and instantiation (`id` excluded)
        - raise TypeError if an attribute is not an integer
	- raise ValueError if `width` or `height` are <= 0
	- raise ValueError if `x` or `y` are less than 0

 4. Area first
    - File: Update `models/rectangle.py`
    - public method: `def area(self)`
        - return the area of the Rectangle instance

 5. Display #0
    - File: Update `models/rectangle.py`
    - public method: `def display(self)`
        - print the Rectangle instance to stdout using `#`

 6. __str__
    - File: Update `models/rectangle.py`
    - override the `__str__` method to return a different string
        - `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

 7. Display #1
    - File: Update `models/rectangle.py`
    - Update the `display` method
        - print the Rectangle beginning at offset (<x>,<y>) in stdout

 8. Update #0
    - File: Update `models/rectangle.py`
    - public method: `def update(self, *args)
        - update all attributes using no-keyword arguments
	- order of arguments: id, width, height, x, y

 9. Update #1
    - File: Update `models/rectangle.py`
    - Update `update` method --> `def update(self, *args, **kwargs)`
        - same purpose as Task #8
        - skip **kwargs if *args exists and is not empty
	- each key represents an attribute in the instance

10. And now, the Square!
    - File: models/square.py
    - Define class Square, which extends Rectangle
        - class constructor: `def __init__(self, size, x=0, y=0, id=None)
	    - call the super class, do not create new attributes for Square
	- override `__str__` method
	    - print `[Square] (<id>) <x>/<y> - <size>

11. Square size
    - File: Update `models/square.py`
    - Add getter and setter for `size`
        - Set `width` and then `height`
	- Same value validation as Rectangle

12. Square update
    - File: Update `models/square.py`
    - Add `def update(self, *args, **kwargs)`
        - Update/assign attributes
	- `*args` order of attributes: id, size, x, y
	- try `*args` before `**kwargs`

13. Rectangle instance to dictionary representation
    - File: Update `models/rectangle.py`
    - Add `def to_dictionary(self)`
        - Return dictionary representation of a Rectangle
	- Must contain: id, width, height, x, y

14. Square instance to dictionary representation
    - File: Update `models/square.py`
    - Add `def to_dictionary(self)`
        - Return dictionary representation of a Rectangle
	- Must contain: id, size, x, y

15. Dictionary to JSON string
    - File: Update `models/base.py`
    - Add static method: `def to_json_string(list_dictionaries)`
        - Return JSON string representation of `list_dictionaries`
	- if `list_dictionaries` is `None` or empty, return `"[]"`
        - `list_dictionaries` is a list of dictionaries

16. JSON string to file
    - File: Update `models/base.py`
    - Add class method: `def save_to_file(cls, list_objs)`
        - Write JSON str representation of `list_objs` to a file
	- `list_objs` is a list of instances that inherit from `Base`
	    - if None, save an empty list
	- saved file name: `<Class name>.json`
	- use static method: `to_json_string`
	- overwrite if preexisting

17. JSON string to dictionary
    - File: Update `models/base.py`
    - Add static method: `from_json_string(json_string)`
        - Return list represented by a JSON-string
	- `json_string` - string representing a list of dictionaries
	    - if None or empty, return an empty list

18. Dictionary to instance
    - File: Update `models/base.py`
    - Add class method: `def create(cls, **dictionary)`
        - Return an instance with all attributes set
	- Create a dummy instance, then call `update` to apply real values
	- Must use the `update` method
	- `**dictionary` must be used as the `**kwargs` arg of `update`
	- You are not allowed to use `eval`

19. File to instances
    - File: Update `models/base.py`
    - Add class method: `def load_from_file(cls):
        - Return a list of instances from a file
	- `cls` is the filename; must be <Class name>.json
	- If the file doesn't exist, return an empty list
	- Must use the methods `from_json_string` and `create`
	- Type of instances returned depends on the class using the method

### Author
Cynthia Taylor
June 9, 2020
Holberton School