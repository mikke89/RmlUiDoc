# This source file is part of RmlUi, the HTML/CSS Interface Middleware
# 
# For the latest information, see http://github.com/mikke89/RmlUi
# 
# Copyright (c) 2021 The RmlUi Team, and contributors
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

import os
import re
import sys
import argparse

parser = argparse.ArgumentParser(description=\
'''Generate a list of elements and properties from the RmlUi Documentation
for use on the search page.

This script uses the element index and property index compiled html pages
to generate its output. Please run this script whenever one of those pages
are changed.

Before running this script, make sure the documentation site is compiled and 
located in the '_site' subdirectory of the RmlUiDoc root. The output is
saved to the file '_includes/elements_and_properties.index'.''')

parser.add_argument('dir',
                    help="RmlUi Documentation root directory.")

args = parser.parse_args()

dir = args.dir
element_index_path = os.path.join(dir, r'_site/pages/rml/element_index.html')
property_index_path = os.path.join(dir, r'_site/pages/rcss/property_index.html')

out_dir = os.path.join(dir, r'_includes')
out_path = os.path.join(out_dir, r'elements_and_properties.index')

if not os.path.isdir(dir):
	print("Error: Specified input directory '{}' does not exist.".format(dir))
	exit()
if not os.path.isdir(out_dir):
	print("Error: Output directory '{}' does not exist.".format(out_dir))
	exit()
if not os.path.isfile(element_index_path) or not os.path.isfile(property_index_path):
	print("Error: The compiled site files '{}' and '{}' could not be located.".format(element_index_path, property_index_path))
	exit()
for path in [element_index_path, property_index_path]:
	if not os.path.isfile(path):
		print("Error: The compiled site file '{}' could not be located.".format(path))
		exit()

output = r"// Generated from '_tools/generate_elements_and_properties_index.py'. Please do not edit manually."


# Parse property index
f = open(property_index_path, 'r', encoding="utf8")
content = f.read()
f.close()

matches = re.findall(r'''<a href="(\S+)"><code class="language-plaintext prop highlighter-rouge">([^<]+)</code>''', content)
num_properties = len(matches)

for match in matches:
	url = match[0] if match[0].startswith("/") else '/pages/rcss/' + match[0]
	property = match[1]

	output = output + r'''
{{
	"property": "{}",
	"element": "",
	"url": "{}",
	"title": "",
	"parent_title": "",
	"content": ""
}},'''.format(property, url)


# Parse element index
f = open(element_index_path, 'r', encoding="utf8")
content = f.read()
f.close()

matches = re.findall(r'''<a href="(\S+)"><code class="language-plaintext tag highlighter-rouge">&lt;([^<]+)&gt;</code>''', content)
num_elements = len(matches)

for match in matches:
	url = match[0] if match[0].startswith("/") else '/pages/rml/' + match[0]
	property = match[1]

	output = output + r'''
{{
	"property": "",
	"element": "{}",
	"url": "{}",
	"title": "",
	"parent_title": "",
	"content": ""
}},'''.format(property, url)

# Output file
output = output.strip(',') + '\n'

if num_properties == 0 or num_elements == 0:
	print("Error: Could not parse any properties or elements from the html sources. Regular expressions may need an update?")
	exit()

f = open(out_path, 'w', encoding="utf8")
f.write(output)
f.close()

print(r"Succesfully generated index with {} properties and {} elements to file '{}'.".format(num_properties, num_elements, out_path))
