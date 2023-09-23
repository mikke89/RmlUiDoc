# This source file is part of RmlUi, the HTML/CSS Interface Middleware
# 
# For the latest information, see http://github.com/mikke89/RmlUi
# 
# Copyright (c) The RmlUi Team, and contributors
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
import os
import argparse

parser = argparse.ArgumentParser(description=\
'''List properties found both in markdown documentation, as well as the 
property index. List them such that we can cross-check that all of them
are listed in the property index and in the documentation.''')

parser.add_argument('root', default = '..', nargs='?',
                    help="Root directory of RmlUi documentation repository, default=%(default)s")
args = parser.parse_args()

root = args.root

def extract_words_from_md_files(main_directory, additional_files, pattern):
    word_counts = {}
    main_files = [os.path.join(main_directory, file) for file in os.listdir(main_directory) if file.endswith('.md')]
    for file in main_files + additional_files:
        with open(file, 'r', encoding='utf-8') as md_file:
            content = md_file.read()
            matches = re.findall(pattern, content, re.MULTILINE)
            for match in matches:
                word = match.strip()
                word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

file_path_index = os.path.join(root, 'pages/rcss/property_index.md')
directory_md = os.path.join(root, 'pages/rcss/')
additional_files_md = [os.path.join(root, file) for file in [
    'pages/cpp_manual/element_packages/progress_bar.md',
    'pages/style_guide.md',
    ]]

with open(file_path_index, 'r') as file:
    input_string = file.read()

pattern_index_link = r'\[([^\]]+)\]:'
matches_index_link = re.findall(pattern_index_link, input_string)
word_list_index_link = [match.strip() for match in matches_index_link]

pattern_md = r'^`([^`]+)`{:\.prop}\s*$'
word_counts_md = extract_words_from_md_files(directory_md, additional_files_md, pattern_md)

combined_property_list = sorted(set(word_list_index_link + list(word_counts_md.keys())))

pattern_index_usage = r'{:\.prop}\]\[(' + '|'.join(re.escape(word) for word in combined_property_list) + r')\]'
matches_index_usage = re.findall(pattern_index_usage, input_string)

word_counts_index_usage = {word: 0 for word in combined_property_list}
for match in matches_index_usage:
    word_counts_index_usage[match] += 1

print("{:<25} {:<20} {:<20} {:<20}".format("Property", "Index link", "Index usage count", "Markdown files count"))
print("-" * 90)

for word in combined_property_list:
    is_index_link = word in word_list_index_link
    count_in_index = word_counts_index_usage.get(word, 0)
    count_in_md_files = word_counts_md.get(word, 0)
    
    print("{:<25} {:<20} {:<20} {:<20}".format(word, is_index_link, count_in_index, count_in_md_files))
