# This source file is part of RmlUi, the HTML/CSS Interface Middleware
#
# For the latest information, see http://github.com/mikke89/RmlUi
#
# Copyright (c) 2008-2010 CodePoint Ltd, Shift Technology Ltd
# Copyright (c) 2019 The RmlUi Team, and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# This script was used to extract data from rmlui_lua_documentation.json and convert
# it to a readable markdown format in api_reference.md. The markdown file was later manually altered wherever
# required however.

import json

with open("rmlui_lua_documentation.json") as json_file:
    docs = json.load(json_file)
    docs = json.loads(json.dumps(docs, sort_keys=True))

final = """---
layout: page
title: Lua API Reference
status: improve
---

All instantiable classes define a `new()` function which returns an object of that particular class. 

With the exception of this `new()` function, all members listed will be member functions.

| Contents |
| -------- |
{contents}

---

"""

contents_table = ""
content_format = "| [{name}](#{name}) |\n"
for global_table_name in docs:
    contents_table += content_format.format(name=global_table_name)
final = final.format(contents=contents_table)

addition = ""

for global_table_name in docs:
    addition = '''
## <a href='#{table_name}' name='{table_name}'>{table_name}</a>

Inherits: `{inherited}`{{: .lua-type }}

{description}

### Properties

{properties_header}
{properties}

### Functions

{functions_header}
{functions}

### Metafunctions

{metafunctions_header}
{metafunctions}

### Property Descriptions

{property_descriptions}

### Function Descriptions

{function_descriptions}

---
'''
    global_table = docs[global_table_name]

    if global_table["inherits"] == "":
        global_table["inherits"] = "nil"

    # Make functions summary table
    function_doc_format = "| [{function_name}](#{class_name}-{function_name}){{: .lua-function }}{arguments} | {return_value} |\n"
    properties_doc_format = "| [{name}](#{class_name}-{name}){{: .lua-function }} | `{type}`{{: .lua-type }} |\n"

    functions_table = ""
    properties_table = ""

    metatable_overrides_table_format = "| {name} |\n"
    metatable_overrides_table = ""
    
    for function_name in global_table["functions"]:
        if global_table["functions"][function_name]["type"] == "py_only":
            continue

        # Find properties from the list of functions
        if function_name[0].islower():
            type_name = ""
            if len(global_table["functions"][function_name]["returns"]) == 0:
                type_name = "nil"
            else:
                for type_string in global_table["functions"][function_name]["returns"]:
                    type_name += type_string.replace("push", "") + ", "
                type_name += "]"
                type_name = type_name.replace(", ]", "")

            properties_table += properties_doc_format.format(
                type=str(type_name),
                class_name=global_table_name,
                name=function_name
            )
            continue

        # Check if it is a metatable function
        if function_name.find("__") != -1:
            metatable_overrides_table += metatable_overrides_table_format.format(
                name=function_name[function_name.find("__"):]
            )
            continue

        # Form arguments
        arguments = global_table["functions"][function_name]["py_arguments"]
        argument_types = [] 
        for argument in global_table["functions"][function_name]["arguments"]:
            argument_types.append(str(argument["type"]))
        arguments = '('+', '.join(["`" + name+'`{: .lua-type } '+arg for name,arg in zip(argument_types, arguments[1:-1].split(", "))]) + ')'
        global_table["functions"][function_name]["arguments"] = arguments
        
        # Conjoin return values
        return_values = ""
        for return_value in global_table["functions"][function_name]["returns"]:
            type_name = str(return_value).replace("push", "")
            return_values += "`" + type_name + "`{: .lua-type }<br>"
        if return_values == "":
            return_values = "`nil`" + "{: .lua-type }"

        if function_name.find("new") != -1:
            function_name = "new"
            return_values = "`" + global_table_name + "`{: .lua-type}"
        
        # Push functions table row
        functions_table += function_doc_format.format(
            class_name=global_table_name,
            return_value=return_values,
            function_name=function_name,
            arguments=arguments
        )

    # Create function and property descriptions
    property_descriptions = ""
    property_descriptions_format = "#### {type} <a href='#{class_name}-{name}' name='{class_name}-{name}'>{name}</a>{{: .lua-function }}\n\n{description}\n\n"
    function_descriptions = ""
    function_descriptions_format = "#### {return_types} <a href='#{class_name}-{name}' name='{class_name}-{name}'>{name}</a>{{: .lua-function }}{arguments}\n\n{description}\n\n"

    for function_name in global_table["functions"]:
        if global_table["functions"][function_name]["type"] == "py_only":
            continue

        # All properties start with a lowercase letter
        if function_name[0].islower():
            property_name = function_name
            type_name = ""
            if len(global_table["functions"][function_name]["returns"]) == 0:
                type_name = "`nil`{: .lua-type }"
            else:
                raw_type_names = "["
                for return_type in global_table["functions"][function_name]["returns"]:
                    raw_type_names += ", `" + str(return_type) + "`{: .lua-type }"
                raw_type_names = raw_type_names.replace("[,", "")
                type_name = raw_type_names.replace("push", "")
            property_descriptions += property_descriptions_format.format(
                type=type_name,
                class_name=global_table_name,
                name=property_name,
                description=global_table["functions"][function_name]["py_description"]
            )
            continue
        
        if function_name.find("__") != -1:
            continue

        type_name = ""
        if len(global_table["functions"][function_name]["returns"]) == 0:
            type_name = "`nil`{: .lua-type}"
        else:
            raw_type_names = "["
            for return_type in global_table["functions"][function_name]["returns"]:
                raw_type_names += ", `" + str(return_type) + "`{: .lua-type }"
            raw_type_names = raw_type_names.replace("[,", "")
            type_name = raw_type_names.replace("push", "")
        name = function_name.replace(global_table_name, "")
        function_descriptions += function_descriptions_format.format(
            return_types=type_name,
            name=name,
            class_name=global_table_name,
            description=global_table["functions"][function_name]["py_description"],
            arguments=global_table["functions"][function_name]["arguments"]
        )

    global_table["functions"] = functions_table
    global_table["properties"] = properties_table
    global_table["metafunctions"] = metatable_overrides_table
    global_table["property_descriptions"] = property_descriptions
    global_table["function_descriptions"] = function_descriptions
    global_table["properties_header"] = "| Name | Type |\n| ------------ | ---- |"
    if properties_table == "":
        global_table["properties_header"] = ""
    global_table["functions_header"] = "| Name | Return Type |\n| ------------ | ---- |"
    if functions_table == "":
        global_table["functions_header"] = ""
    global_table["metafunctions_header"] = "| Metafunctions |\n| ------------- |"
    if metatable_overrides_table == "":
        global_table["metafunctions_header"] = ""

    final += addition.format(
        table_name=global_table_name,
        inherited=global_table["inherits"],
        description=global_table["py_description"],
        properties_header=global_table["properties_header"],
        properties=global_table["properties"],
        functions_header=global_table["functions_header"],
        functions=global_table["functions"],
        metafunctions_header=global_table["metafunctions_header"],
        metafunctions=global_table["metafunctions"],
        property_descriptions=global_table["property_descriptions"],
        function_descriptions=global_table["function_descriptions"]
    )

with open("api_reference.md", mode="w") as final_file:
    final_file.write(final)
