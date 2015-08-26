##CssCoco Syntax Overview

The language constructs that define conventions try to resemble the way conventions are expressed in natural language. There is a construct that describes directly what is disallowed. For example, the convention *Do not use import statements* is expressed in the following way:

```
￼￼￼forbid import  
message ’Do not use import statements.’  
```

￼The keyword `forbid` is followed by a description of the node that is disallowed. In the current convention, we only need to state its type — import. Each convention requires a message clause. The string after the message keyword will be displayed to the user when a violation is found.

Conventions are often expressed as a pattern that, if found, needs to meet given constraints. In CssCoco syntax such conventions are defined using the `find ... require ...` construct. For example, the convention *All class names should be lowercase* is described as follows:

```
find c=class  
require c.name match lowercase  
message ’All class names should be lowercase’  
```

The `find` clause in the above rule specifies the pattern that needs to be found and the require clause states the constraint that should be applied to the discovered nodes. Note that to refer to a matched node in the `require` clause, the node should be assigned an identifier (`c` in the above example).
Conventions can put more constraints on a node description in the pattern. For example, the convention *Use a leading zero for decimal values* requires finding all nodes of type number that have a numeric value in the interval [-1, 1]. Such constraints are put in curly brackets immediately after the type of the node.

```
find n=number{num-value < 1 and num-value > -1}  
require n.string match ’^0.*’  
message ’Use a leading zero for decimal values’  
```

Conventions can describe patterns that consist of more than one node. For example, the rule *Use single quotes in charsets* can be expressed in the following way:

```
find s=string in charset  
require s.has-single-quotes  
message ’Use single quotes in charsets’  
```

The pattern contains the description of two nodes: a node that is of type string and a node of type charset. The `in` keyword in the pattern description indicates that the string node is nested in the charset node. In this way, the pattern will match only the strings that appear in a charset.

In CssCoco, conventions are grouped in contexts that specify what nodes should be ignored when searching for patterns. For example, often when rules refer to newlines they completely disregard indentation. The convention *Every declaration must be on a new line* requires a newline to be present immediately before the declaration. However, when declarations are indented their immediate previous sibling is an indentation node. To handle such cases, the language uses contexts that explicitly describe the ignored nodes.

```
Whitespace  
ignore indent  
{  
find d=declaration  
require newline before d  
message ’Put every declaration on a new line’  
}  
```

Contexts have a user-defined name and an optional `ignore` clause. The `ignore` keyword is followed by a description of the nodes that need to disregarded.
