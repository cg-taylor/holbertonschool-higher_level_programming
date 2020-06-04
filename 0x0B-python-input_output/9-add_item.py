#!/usr/bin/python3
"""My add_item module"""

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file


test = []
list_file = open("add_item.json", 'w')
