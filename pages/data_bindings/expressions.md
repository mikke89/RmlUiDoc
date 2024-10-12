---
layout: page
title: Data variables and expressions
parent: data_bindings
next: model
---

{% raw %}

### Data variables

Data variables are wrappers around the user's raw data. There are three primary types.

1. `Scalar`. A single value which can be read from and usually written to (but not necessarily).
2. `Array`. A container which can be indexed into. The underlying type can be any data variable type.
3. `Struct`. A collection of named members. Members can be any data variable type.

In the data model, each variable has an associated *data address*. The address follows the normal C++ syntax, use `.x` to access a member, and `[i]` to index into an array. In addition, `.size` can be used on arrays to get their size.

The following examples are valid data addresses.
```
title
invader.health
invaders[1].name
invaders.size
a.very[5].long.data[99].address
```

Arithmetic types (eg. `int`, `float`), enums, as well as `Rml::String` are supported without the need to register them. Enums are treated as its underlying type, and can also be registered manually. Other types need to be registered first. It is also possible to bind a variable using getter and setter functions, then the data variable acts as a scalar type. See details for registering types in the data model documentation.


### Data expressions

Data expressions are small expressions which can take one or several data variables, modify them through common operations, and return the result. Several data views and controllers can use them for more flexibility in how the data should be displayed.

The syntax resembles C++, and should be familiar for most programmers. The following table lists the allowed operators, and their precedence. Operators with the same precedence are evaluated left-to-right.

| Precedence| Operator        | Description                       |
| --------- | ----------------| --------------------------------- |
|   1       |  !              | Logical NOT.                      |
|   2       |  \* /           | Multiplication and division.      |
|   3       |  +              | Addition or string concatenation. |
|   3       |  -              | Subtraction.                      |
|   4       | == != < <= > => | Relational comparisons.           |
|   5       | && \|\|         | Logical AND, OR.                  |
|   5       | \|              | Transform.                        |
|   5       | a?b:c           | Ternary conditional.              |

Parenthesis `( )` always take precedence over operators. The addition operator will do string concatenation if either of its arguments is a string, otherwise it uses numeric addition.

The following types can be used in the expressions.

1. Data address, pointing to a scalar data variable.
2. Literal.
    - Numeric. Eg. `42` or `-3.2`. Integers or fractional.
    - String. Eg. `'Play!'`. Always written using single quotes.
3. Keyword. `true` or `false`.

Operators read their arguments either as a `bool`, a `double`, or a `String`. Conversions are done implicitly when needed using the type conversion facilities in RmlUi.

#### Transform functions

A *transform function* takes any number of input arguments and produces a new value. The function can be called using the function call convention.
```
transform_name([data_expression], [data_expression], ...)
```
Alternatively, the pipe operator `|` can equivalently be used which uses the value on the left-hand-side of the operator as the first argument to the transform function.
```
[data_expression] | transform_name([data_expression], ...)
```
If the transform function takes a single argument the parenthesis can be omited.
```
[data_expression] | transform_name
```

There are several built-in transform functions.

| Transform name | Arguments                                                | Return type  | Description                           |
| -------------  | -------------------------------------------------------- | ------------ | ------------------------------------- |
|   to_upper     |  `value`                                                 | String       | Transform string to upper case.       |
|   to_lower     |  `value`                                                 | String       | Transform string to lower case.       |
|   round        |  `value`                                                 | Numeric      | Round a value to its nearest integer. |
|   format       |  `value`, `precision`, `remove_trailing_zeros` = `false` | String       | Format a numeric value.<br/>`precision` determines the number of fractional digits written.<br/>`remove_trailing_zeros` removes any trailing zeros and possibly the decimal character from the number. |

Additionally, users can [provide their own transform functions](model.html#registering-transforms) as detailed in the data model documentation.

The pipe operator `|` allows transform functions to easily be chained as in the following example.
```
i * 3.14159 | round | my_pow(4) | transform(2)
```
In other situations the function call syntax or a combination may be more convenient.
```
make_lines('It takes', num_trolls*3 + ' goats', 'to outsmart', num_trolls | number_suffix('troll','trolls'))
```


#### Assignment expressions

Data views never assign values to data variables, they only read from them. On the other hand, data controllers can assign values to data variables. For this purpose, there is also support for *assignment expressions*.

For now, assignment expressions can only be used in the [`data-event` controller](views_and_controllers.html#data-event). Syntax and details are located in the documentation for this controller.


#### Expression examples


| Example                                                                 | Possible result       |
| ---------------------------------------------------------------------   | --------------------- |
| `rating < 80`                                                           | `1`                   |
| `radius + 'm'`                                                          | `8.7m`                |
| `(radius | format(2)) + 'm'`                                            | `8.70m`               |
| `radius < 10.5 ? 'small' : 'large'`                                     | `small`               |
| `'hot' + 'dog' | to_upper`                                              | `HOTDOG`              |
| `'x: ' + ev.mouse_x + '<br/>y: ' + ev.mouse_y`                          | `x: 128<br/>y: 958`   |
| `true || false ? (true && 3==1+2 ? 'Absolutely!' : 'well..') : 'no'`    | `Absolutely!`         |


{% endraw %}
