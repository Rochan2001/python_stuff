#!/usr/bin/env python3

"""Search for a regex pattern in all txt files in a directory."""
from pathlib import Path
import os
import re
p = Path.cwd()/Path('Automate_stuff_with_python')
txt_files = list(p.glob('*.txt'))
# Write regex to match
search_regex = re.compile(r'NOUN')   # Matches all words ending in !

# Open each txt file in turn and if regex triggers print matches to console
for doc in txt_files:
    opened_file = open('{}'.format(doc))
    contents = opened_file.read()
    string = ''.join(contents)
    found = search_regex.findall(string)
    found_str = ' '.join(found)
    print(found_str)
