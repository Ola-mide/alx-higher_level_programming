#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then save them to a file
"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if not os.path.exists("add_item.json"):
    save_to_json_file([], "add_item.json")

json_rep = load_from_json_file("add_item.json")
if len(sys.argv) > 1:
    for item in sys.argv[1:]:
        json_rep.append(item)
    save_to_json_file(json_rep, "add_item.json")
