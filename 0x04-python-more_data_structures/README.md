# 0x04. Python - More Data Structures: Set, Dictionary

## Learning Objectives
- What are sets and how to use them
- What are the most common methods of sets and how to use them
- When to use sets vs. lists
- How to iterate through a set
- What are dictionaries and how to use them
- When to use dictionaries vs. lists or sets
- What is a key in a dictionary
- How to iterate through a dictionary\
- What is a lambda function
- What are the map and reduce functions

## Requirements
- Allowed editors: vi, vim, emacs
- ALl your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a newline
- The first line of all your files should be `#!/usr/bin/python3` exactly
- Your code should use the `PEP8` style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks
0. Squared simple
    File: 0-square_matrix_simple.py
    Compute the square value of all integers of a matrix
        - the matrix is a list of lists
	- initial matrix should not be modified

1. Search and replace
    File: 1-search_replace.py
    Replace all occurrences of an element by another
        - original list should not be modified

2. Unique addition
    File: 2-uniq_add.py
    Add all unique integers in a list

3. Present in both
    File: 3-common_elements.py
    Return the set of common elements in two sets

4. Only differents
    File: 4-only_diff_elements.py
    Return the set of all unique elements in two sets

5. Number of keys
    File: 5-number_keys.py
    Return the number of keys in a dictionary

6. Print sorted dictionary
    File: 6-print_sorted_dictionary
    Print a dictionary by ordered keys
        - sort alphabetically
	- only sort the first level
	- dictionary values can be of any type

7. Update dictionary
    File: 7-update_dictionary.py
    Replace or add a key/value in a dictionary
        - replace if the key exists, create it if it does not

8. Simple delete by key
    File: 8-simple_delete.py
    Delete a key in a dictionary
        - do nothing if the key does not exist

9. Multiply by 2
    File: 9-multiply_by_2.py
    Return a dictionary with all values multiplied by 2
        - original dictionary should not be modified

10. Best score
    File: 10-best_score.py
    Return a key with the biggest integer value
        - if no score is found, return `None`
	- assume all scores are different and are integers

11. Multiply by using map
    File: 11-multiply_list_map.py
    Return a list with all values multiplied by a number using `map`
        - initial list should not be modified
	- file should be 3 lines max

12. Roman to Integer
    File: 12-roman_to_int.py
    Convert a Roman numeral to an integer
        - if the Roman number is not a string or is `None`, return 0
	- assume the number is between 1 and 3999

13. Weighted average! (advanced)
    File: 100-weighted_average.py
    Return the weighted average of a list of scores
        - return 0 if the list is empty
	- data is passed as a list of tuples `(<score>, <weight>)`

14. Squared by using map (advanced)
    File: 101-square_matrix_map.py
    Compute the square value of all integers in a matrix using `map`
        - initial matrix should not be modified
	- file should be 3 lines max
	- must use `map`, cannot use `for` or `while`

15. Delete by value (advanced)
    File: 102-complex_delete.py
    Delete keys with a specific value in a dictionary
        - do nothing if the key does not exist
	- delete all keys with the specified value

### Author
Cynthia Taylor
June 11, 2020