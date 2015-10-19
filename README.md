# CssCoco


This is the product of a MSc Thesis hosted at the University of Amsterdam. Please keep in mind that this is work in progress. Your comments/suggestions/criticism will be highly appreciated :)
___


We often use CSS code conventions that put constrains on whitespacing, indentation, choice of id and class names, usage of single quotes over double quotes, usage of !important or units after 0 values, etc. Typically, we express these conventions in natural language. Some examples are the CSS style guides of [Google](https://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml), [GitHub](http://primercss.io/guidelines/#css), [Wordpress](https://make.wordpress.org/core/handbook/best-practices/coding-standards/css/), [Mozilla](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Writing_efficient_CSS). 

The problem is that we have to check whether our code complies to a given set of code conventions manually. Even though there are some great tools available that can assist us in the process, most of them specialize in a specific type of conventions, e.g. they focus on whitespacing or naming conventions, but not both. It gets even worse! Most of the tools offer a predefined set of conventions that we can enable or disable and they do not allow us to alter conventions or create our custom conventions.

This is where **CssCoco** comes to the rescue! It lets developers define a custom set of **CSS** **co**de **co**nventions and discovers violations automatically. **CssCoco** uses a domain-specific language to express code conventions that refer to whitespacing, indentation, syntax preference and code anti-patterns. It is designed to offer greater flexibility and cover a wide range of conventions. The tool comes with popular code convention sets that are ready for use.

## Installation

The tool requires Python 3.4 and nodejs. There is a python3 package available at pypi, so you can install it using pip. Please note that currently only a python3 package is available.

### OS X

1. Install CSS coco:

    `pip3 install csscoco`

2. Install node:

    `brew install node`

### Linux

1. Install CSS coco:

    `pip3 install csscoco`

2. Install nodejs:

    `sudo apt-get install nodejs`

The tool uses the `node` command. In some cases you might need to create a symbolic link for the node command to work: 

`sudo ln -s /usr/bin/nodejs /usr/bin/node`

## Configuration and Use

1. Create a file with .coco extension. Alternatively, you can use one of the [predefined coco files](https://github.com/boryanagoncharenko/CssCoco/tree/master/samples).

2. Execute command csscoco. The command accepts two arguments: the path to the css file and the path to the coco file. For example:
`csscoco my_code.css conventions.coco`
