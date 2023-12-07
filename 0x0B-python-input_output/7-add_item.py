#!/usr/bin/python3
"""
Script to save Argment in .json file and load it as llist object
"""
import sys
import json

save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
with open(filename, "a+", encoding="utf-8") as f:
    """This step is to create the file if it doesn't exist
    and if it exist it does not dlt the data (a+) mode = append and read
    """
    pass

try:
    ls = load_from(filename)
except ValueError:
    ls = []
args = [sys.argv[i] for i in range(1, len(sys.argv))]
ls += args
save_to(ls, filename)
