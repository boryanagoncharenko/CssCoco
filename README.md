# CssCoco

**Warning!** This is the product of a MSc Thesis hosted at the University of Amsterdam. It is work in progress.

**Css Coco** is a tool that lets you express a custom set of **CSS** **co**de **co**nventions and check your code for violations. It uses a domain-specific langauge that allows you express conventions that refer to whitespacing, indentation, syntax preference and code style.

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

1. Create a file with .coco extension. Alternatively, you can use of the [predefined coco files](../blob/master/samples).

2. Execute command csscoco. The command accepts two arguments: the path to the css file and the path to the coco file. For example:
`csscoco my_code.css conventions.coco`
