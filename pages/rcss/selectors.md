---
layout: page
title: Selectors
parent: rcss
next: cascade
---

Selectors are used to select elements to apply specific rules to. The following selectors are supported in RCSS:

Selector            | Matches
---                 | ---
`*`{:.cls}          | Any element.
`E`{:.cls}          | Any element of type E (i.e., an element declared in an RML document as `<E>`{:.tag}).
`.foo`{:.cls}       | Any element that has been declared with class `foo`{:.cls}.
`#foo`{:.cls}       | Any element that has been declared with an ID of `foo`{:.value}.
`:foo`{:.cls}       | Any element that has the pseudo-class `foo`{:.cls} currently active, or matches a structural selector below.
`[foo]`{:.cls}      | Any element with a `foo`{:.attr} attribute, regardless of value.
`[foo=bar]`{:.cls}  | Any element with a `foo`{:.attr} attribute equal to `bar`{:.value}.
`[foo~=bar]`{:.cls} | Any element with a `foo`{:.attr} attribute with a space-separated list of values, one of which is equal to `bar`{:.value}.
`[foo|=bar]`{:.cls} | Any element with a `foo`{:.attr} attribute equal to `bar`{:.value} or which begins with `bar-`{:.value} including the hyphen.
`[foo^=bar]`{:.cls} | Any element with a `foo`{:.attr} attribute which begins with `bar`{:.value}.
`[foo$=bar]`{:.cls} | Any element with a `foo`{:.attr} attribute which ends with `bar`{:.value}.
`[foo*=bar]`{:.cls} | Any element with a `foo`{:.attr} attribute which contains `bar`{:.value}.
`E F`{:.cls}        | Any element of type F that is a descendant of an E element.
`E > F`{:.cls}      | Any element of type F that is a direct descendant of an E element.
`E + F`{:.cls}      | Any element of type F that is immediately preceded by an E element.
`E ~ F`{:.cls}      | Any element of type F that is preceded by an E element.

Details and combinations of the listed selectors are described below.


#### Pseudo selectors
{:#pseudo-selectors}

The following table lists the built-in pseudo class selectors, in addition to the negation selector and all of the tree-structural selectors from CSS3.

**Pseudo-class**                               |
`:hover`{:.cls pseudo-def}                     | Matches an element that is currently under the mouse cursor.
`:active`{:.cls pseudo-def}                    | Matches an element that has been clicked on, only until the button is released.
`:focus`{:.cls pseudo-def}                     | Matches an element that has input focus. Unlike CSS, this pseudo-class propagates backwards through its parents, making it closer in functionality to [focus-within](https://www.w3.org/TR/selectors-4/#the-focus-within-pseudo).
`:focus-visible`{:.cls pseudo-def}             | Matches an element that has input focus, and whose focus should be visibly indicated. This can be particularly useful to style the focused element when using keyboard or spatial navigation.
`:checked`{:.cls pseudo-def}                   | Matches a checked checkbox and radio button. Matches a [select element]({{"pages/cpp_manual/element_packages/form.html#drop-down-select-box"|relative_url}}) when it is open, as well as the selected option in its drop-down list.
**Logical**                                    |
`:not(s1, s2, …)`{:.cls pseudo-def}            | Matches an element that does not match any of its selectors s1, s2, ….
**Tree-structural**                            |
`:nth-child(an + b)`{:.cls pseudo-def}         | Matches an element that has an + b - 1 siblings before it.
`:nth-last-child(an + b)`{:.cls pseudo-def}    | Similar to nth-child, but counts backwards.
`:nth-of-type(an + b)`{:.cls pseudo-def}       | Similar to nth-child, but only counts sibling elements of the same type.
`:nth-last-of-type(an + b)`{:.cls pseudo-def}  | Similar to nth-of-type, but counts backwards.
`:first-child`{:.cls pseudo-def}               | Matches an element that is the first child of its parent.
`:last-child`{:.cls pseudo-def}                | Matches an element that is the last child of its parent.
`:first-of-type`{:.cls pseudo-def}             | Matches an element that is the first child of its type.
`:last-of-type`{:.cls pseudo-def}              | Matches an element that is the last child of its type.
`:only-child`{:.cls pseudo-def}                | Matches an element that has no sibling elements.
`:only-of-type`{:.cls pseudo-def}              | Matches an element that has no sibling elements of its type.
`:empty`{:.cls pseudo-def}                     | Matches an element that has no child nodes.

See the [CSS selectors specifications](https://www.w3.org/TR/selectors-4/) for more thorough documentation and examples on the use of selectors. Please note that pseudo-elements such as `::first-letter`{:.cls} and `::before`{:.cls} are not yet supported in RCSS.


#### Compound selectors

A *compound selector* is made up of an optional element type followed by zero or more class selectors, ID selectors, attribute selectors, and pseudo selectors. If an element type is not given, any element type will be matched. So, for example, the selector:

```css
div#level_list:hover
```

will match any element of type `div`{:.tag} with an ID of `level_list`{:.value} that is currently being hovered by the cursor.


#### Complex selectors

A *complex selector* is made up of potentially multiple compound selectors, each separated by a combinator.

```css
div.content p {}
div.content > p {}
div.content + p {}
div.content ~ p {}
```
For an element to be matched by a selector with multiple compound selectors, it itself must match the last compound selector. And then, each of the preceding compound selectors must match elements in the RML hierarchy according to the rule of their connecting combinator.

##### Descendant combinator

The descendent combinator (whitespace) must have descendants in the RML hierarchy that match the preceding compound selector. So, for example, the selector

```css
div#level_list input.select option:nth-child(even)
```

will only match if *all* of the following are satisfied:
- An element of type `option`{:.tag} that is an even-numbered child of its parent,
- which has an ancestor of an `input`{:.tag} element of class `select`{:.cls},
- which itself has an ancestor that is a `div`{:.tag} element with the ID `level_list`{:.value}.

##### Child combinator

The child combinator `>` can be used as in CSS to select a child of another element.
```css
p.green_theme > button { image-color: #0f0; }
```
Here, any `button`{:.tag} elements which have a parent `p.green_theme`{:.value} will have their image color set to green.

In the following example it is combined with the universal selector `*`{:.value}.
```css
div.red_theme > * > p { color: #f00; }
```
Here, `p`{:.tag} grandchildren of `div.red_theme`{:.value} will have their color set to red.

##### Sibling combinators

The next-sibling combinator `+` can be used to style elements that immediately follow each other, sharing a common parent.
```css
p + img { margin-top: 0; }
```
Similarly, the subsequent-sibling combinator `~` can be used to select an element that comes after another element, sharing a common parent.
```css
p.content ~ p { font-size: 0.9em; }
```


#### Selector list

Multiple selectors can be appended with commas, which is equivalent to an OR statement. For example, the following:

```css
div#level_list,
div#weapon_list,
.color_list
```

will match a `div`{:.tag} element with ID `level_list`{:.value}, or ID `weapon_list`{:.value}, or any element that has a class of `color_list`{:.value}.


#### Negation selector `:not()`{:.cls}

The negation selector `:not()`{:.cls} can be used to filter some types, for example all input elements that are not checked.
```css
input:not(:checked)
```
It can also take multiple complex selectors. The following will match all `div`{:.tag}s that are not children of `p`{:.tag} and not the second child of their parent.
```css
div:not(:nth-child(2),p > *)
```
The specificity of this selector is determined by the sub-selector that has the largest specificity, as in CSS.


#### Numbered selectors `:nth-`{:.cls}

For a much fuller description of the `:nth-`{:.cls} style selectors, please refer to the [respective sections](https://www.w3.org/TR/selectors-4/#the-nth-child-pseudo) of the CSS selectors specification. `even`{:.cls} and `odd`{:.cls} are supported in RCSS.


#### Performance considerations

In brief, each element is matched against each [complex selector](#complex-selectors). This process begins by matching the right-most compound selector and then subsequently each selector left of that while traversing the element's tree. To speed-up this process, all style rules with IDs, classes, and tags are indexed for fast retrieval. This way a lot of selectors can be eliminated immediately. However, if the right-most compound selector does not contain any of these three types of selectors (ID, class, tag) then they will have to be tested against every element.

Based on this, here are some general guidelines to ensure good performance:

- Try to keep the number of style rules low.
- The right-most selector should contain either an ID, class, or tag (in preferred order - the more unique the better).
- Pseudo, structural, and attribute selectors are not indexed and can be slow. Preferably combine them with ID, class, or tag.
- Prefer the child `>` and next-sibling `+` combinators over the descendant (whitespace) and subsequent-sibling `~` combinators.
