import os
from unittest import TestCase

import tests.helpers as helpers
import csscoco.lang.analysis.violations as violations


class TypeCheckerTests(TestCase):

    filename = 'test.coco'

    def setupFile(self, content):
        fo = open(self.filename, 'w')
        fo.write(content)
        fo.close()
        return fo

    def get_coco_ast(self, data):
        file = self.setupFile(data)
        return helpers.ParseHelper.parse_coco_string(file.name)

    def test_em_instead_of_pt_px_cm_valid(self):
        """
        Use em instead of pt, px, cm
        """
        coco_ast = self.get_coco_ast("Semantic { forbid unit{string in ['px', 'pt', 'cm']} message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a { margin: 5px; padding: 10cm; margin: 0pt; padding: 15em;}')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_forbid_z_index(self):
        """
        Avoid using z-index property
        """
        coco_ast = self.get_coco_ast("Semantic { forbid property{name=='z-index'} message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a { z-index: 100; } .class { z-index: 200; }')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_forbid_important(self):
        """
        Do not use !important
        """
        coco_ast = self.get_coco_ast("Semantic { forbid important message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a { z-index: 100; margin: 5px !important;}'
                                                        '.class { padding: 10px !important; color: red; }')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_forbid_ids(self):
        """
        Avoid using ids
        """
        coco_ast = self.get_coco_ast("Semantic { forbid id message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a {} .class#id {} h1 #id {} h1 h2 {} .class {}')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_lowercase_ids_and_classes(self):
        """
        All id and class names should be lowercase
        """
        coco_ast = self.get_coco_ast("Semantic { find p=(id or class) require p.name match lowercase message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a {} .class#id {} h1 #ID {} H1#id {} .clAss {}')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_lowercase_properties(self):
        """
        Properties should be lowercase (vendor-specific properties are exception)
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find p=property{is-vendor-specific == false} "
                                     "require p.name match lowercase "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{ z-index: 1; COLOR: 2; Margin: 5px;'
                                                        ' -o-color: red; -O-COLOR: pink; }')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_lowercase_values(self):
        """
        All values except the contents of strings should be lowercase
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find value=(not string) in value "
                                     "require value.string match lowercase "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{ border: 5px solid red;'
                                                        'font-family: Consolas, Monaco, "Andale Mono", monospace; }')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_lowercase_tags(self):
        """
        Html tags should be lowercase
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find t=tag "
                                     "require t.name match lowercase "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{ } P{} PRE.class{}')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_semicolon_after_declarations(self):
        """
        Put a ; at the end of declarations
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find d=declaration "
                                     "require d.child(-1).string == ';' "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{ b:red; m:pink } P{ a:blue } ')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_no_strings_in_uri(self):
        """
        Do not put quotes in url declarations
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid string in uri "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{ a: uri(\'test\'); b: url("another") } ')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_use_short_hex(self):
        """
        Use short hex values
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid hex{is-long and string match shorten} "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{ color: #112233; color: #E6E6E6 } ')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_use_short_margin(self):
        """
        Use the shorthand margin property instead
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid ruleset{contains-all([ "
                                     "property{name=='margin-right'},"
                                     "property{name=='margin-left'},"
                                     "property{name=='margin-top'},"
                                     "property{name=='margin-bottom'}"
                                     "])} message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{margin-left:0;margin-top:0;margin-bottom:0;margin-right:0}'
                                                        'b{margin-top:0;margin-bottom:0;margin-right:0}')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_unitless_zero(self):
        """
        Do not use units after 0 values
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid number{num-value == 0} in (dimension or percentage) message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a { margin: 0; padding: 0px; offset: 0cm; top: 0%; }')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_use_leading_zero(self):
        """
        Use a leading zero for decimal values
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find n=number{num-value < 1 and num-value > -1} "
                                     "require n.string match '^0.*' "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a { left: .6em; right: -.6em; top: 0.6em; }')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_use_single_quotes_in_attribute_selectors(self):
        """
        Use single quotes in attribute selectors
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find v=attribute-value "
                                     "require v is string and v.has-single-quotes "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('[attr=test] {} [attr=\'test\'] {} [attr="test"] {}')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_use_single_quotes_in_charsets(self):
        """
        Use single quotes in charsets
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find s=string in charset "
                                     "require s.has-single-quotes "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('@charset \'UFT-8\'; @charset "UFT-8";')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_use_single_quotes_in_values(self):
        """
        Use single quotes in values
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find s=string in value "
                                     "require s.has-single-quotes "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a { font: "Arial" "Black"; color: \'red\'; }')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_use_single_quotes_in_string(self):
        """
        Use single quotes in values
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find s=string "
                                     "require s.has-single-quotes "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a[b="test"] { font: "Black"; color: \'red\'; }')
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_forbid_charset(self):
        """
        Do not specify the encoding of style sheets as these assume UTF-8
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid charset "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("@charset 'uft-8'")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_omit_protocol(self):
        """
        Omit the protocol http(s) in url
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "find u=uri "
                                     "require u.string not match '(?i)https?:.*' "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("a { image: url('https://test'); "
                                                        "image: url(http://test) "
                                                        "image: url(\"http://test\") }")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_no_overqualified_tags(self):
        """
        Do not over-qualify classes and ids with html tags
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid tag next-to (class or id) "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("h1.class {} h2#id {} h1 h2 {} ")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_no_import(self):
        """
        Do not use @import
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid import "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("@import url;")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_width_and_border(self):
        """
        Warning if a rule contains width and border, border-left, border-right, padding, padding-left, or padding-right
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid ruleset{contains(property{name=='width'}) "
                                     "and contains(property{name in ['border',"
                                     "'border-left',"
                                     "'border-right',"
                                     "'padding',"
                                     "'padding-left',"
                                     "'padding-right']}) }"
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("a {width: 5px; border: 10px}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_width_and_padding(self):
        """
        Warning if a rule contains width and border, border-left, border-right, padding, padding-left, or padding-right
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid ruleset{contains(property{name=='width'}) "
                                     "and contains(property{name in ['border',"
                                     "'border-left',"
                                     "'border-right',"
                                     "'padding',"
                                     "'padding-left',"
                                     "'padding-right']}) }"
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("a {width: 5px; padding: 10px}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_height_and_border(self):
        """
        Warning if a rule contains height and border, border-top, border-bottom, padding, padding-top, or padding-bottom
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid ruleset{contains(property{name=='height'}) "
                                     "and contains(property{name in ['border',"
                                     "'border-top',"
                                     "'border-bottom',"
                                     "'padding',"
                                     "'padding-top',"
                                     "'padding-bottom']}) }"
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("a {height: 5px; border: 10px}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_height_and_padding(self):
        """
        Warning if a rule contains height and border, border-top, border-bottom, padding, padding-top, or padding-bottom
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid ruleset{contains(property{name=='height'}) "
                                     "and contains(property{name in ['border',"
                                     "'border-top',"
                                     "'border-bottom',"
                                     "'padding',"
                                     "'padding-top',"
                                     "'padding-bottom']}) }"
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("a {height: 5px; padding: 10px}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_display_inline_block_and_float(self):
        """
        A rule that has display: inline-block should not use float
        """
        cos = "Semantic { " \
              "forbid ruleset{contains(declaration{property.name=='display' and value.string=='inline-block'}) " \
              "and contains(property{name=='float'})} message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { display: inline-block; float: 4;}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_display_block_and_vertical_align(self):
        """
        A rule that has display: block should not use vertical-align
        """
        cos = "Semantic { " \
              "forbid ruleset{contains(declaration{property.name=='display' and value.string=='block'}) " \
              "and contains(property{name=='vertical-align'})} message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { display: block; vertical-align: 4;}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_exact_duplicates(self):
        """
        Warning if a property is included in a rule twice and contains the same value.
        """
        cos = "Semantic { " \
              "find (d1=declaration, d2=declaration) in ruleset "\
              "forbid d1.property.name == d2.property.name and "\
              "d1.value.string == d2.value.string message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { color: red; margin: 0; color: red; }")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_crossed_duplicates(self):
        """
        A property is included twice and is separated by at least one other property.
        """
        cos = "Semantic { " \
              "find (d1=declaration, d2=declaration, d3=declaration) in ruleset "\
              "forbid d1.property.name == d3.property.name and "\
              "d2.property.name != d1.property.name and "\
              "d1.value.string != d3.value.string message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { color: red; margin: 0; color: blue; }")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_empty_rules(self):
        """
        Forbid empty rules.
        """
        cos = "Semantic { " \
              "forbid ruleset{count(declaration) == 0} "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { } b {}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_no_standard_property(self):
        """
        Do not use a vendor-prefixed property without a standard property after it.
        """
        cos = "Semantic ignore space, newline{ " \
              "find d=declaration{property.is-vendor-specific} " \
              "require d.next-sibling is declaration and " \
              "((d.next-sibling.is-vendor-specific and d.next-sibling.property.standard == d.property.standard) or " \
              "(not d.next-sibling.is-vendor-specific and d.next-sibling.property.standard == d.property.standard)) "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { -webkit-hyphens: none; -moz-hyphens: "
                                                        "none; -ms-hyphens: none; }")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_color_fallback_property(self):
        """
        No fallback color for properties with a rgba(), hsl(), or hsla() color
        """
        cos = "Semantic ignore space, newline{ " \
              "find (rgba or hsl or hsla) in d=declaration{property.name == 'color'} " \
              "require d.previous-sibling is declaration and " \
              "d.previous-sibling.property.name == 'color' and " \
              "(d.previous-sibling.contains(hex) or d.previous-sibling.contains(colorname)) "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { color: rgba(1,2,3,0); } "
                                                        "b {color: red; color:rgba(1,2,3,0); }")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_space_btw_colon_value(self):
        """
        Put one space between the colon and the value of a declaration
        """
        cos = "Whitespace { " \
              "find c=colon next-to v=value " \
              "require space between c and v "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { color: red; } "
                                                        "b {color:   red; color:red; }")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_blank_lines_btw_rules_valid(self):
        """
        Put one or two blank lines between rules
        """
        cos = "Whitespace { " \
              "find r1=ruleset next-to r2=ruleset " \
              "require newline{2,3} between r1 and r2 "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { }\n\nb{}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 0

    def test_blank_lines_btw_rules(self):
        """
        Put one or two blank lines between rules
        """
        cos = "Whitespace { " \
              "find r1=ruleset next-to r2=ruleset " \
              "require newline{2,3} between r1 and r2 "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { }\nb{}\n\n\n\nc{}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_blank_lines_btw_rules_ignore_comments(self):
        """
        Put one or two blank lines between rules
        """
        cos = "Whitespace { " \
              "find r1=ruleset next-to r2=ruleset " \
              "require newline{2} between r1 and r2 "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a { }\n\n/*comment*/\nb{}\n\nc{}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 0

    def test_space_btw_selector_and_block_valid(self):
        """
        Put one space between the last selector and the block
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find s=selector next-to b=block " \
              "require space between s and b "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a, b {} c {}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 0

    def test_space_btw_selector_and_block(self):
        """
        Put one space between the last selector and the block
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find s=selector next-to b=block " \
              "require space between s and b "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a, b{} c  {} d\n{}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_newline_btw_selectors(self):
        """
        One selector per line
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find s1=delim next-to s2=simpleselector " \
              "require newline between s1 and s2 "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a, b{} c,\nd  {}")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_trailing_spaces(self):
        """
        No trailing spaces
        """
        cos = "Whitespace ignore newline comment newline { " \
              "forbid (space or indent) next-to (newline or eof) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a {}  \n  b{}  \n")
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_indentation(self):
        """
        Use 4 spaces for indentation, no tabs
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find i=indent " \
              "require i.string match '^ {4}$' " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("\n    a {}\n  b{}\n c{}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_declaration_on_newline(self):
        """
        Put every declaration on a new line
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find d=declaration " \
              "require newline before d " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ color:red; color:red\ncolor:red;}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_closing_brace_newline(self):
        """
        Place closing brace on a new line
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find b=block " \
              "require newline before b.child(-1) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ color:red;\n} a{ color:red;\n\n} a{ color:red; }")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_newline_around_block_braces_valid(self):
        """
        Put newline after "{" and before "}"
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find b=block{count(declaration) != 1} " \
              "require newline after b.child(0) and newline before b.child(-1) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{\ncolor:red;\ncolor:red;\n}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert not violation_log.number_of_violations()

    def test_newline_around_block_braces_spaces(self):
        """
        Put newline after "{" and before "}"
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find b=block{count(declaration) != 1} " \
              "require newline after b.child(0) and newline before b.child(-1) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{\ncolor:red;\ncolor:red; }b{ color:red;\ncolor:red;\n}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_newline_around_block_braces_newlines(self):
        """
        Put newline after "{" and before "}"
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find b=block{count(declaration) != 1} " \
              "require newline after b.child(0) and newline before b.child(-1) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{\ncolor:red;\ncolor:red;\n\n}b{\n\n\ncolor:red;\ncolor:red;\n}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_newline_around_block_braces_no_matches(self):
        """
        Put newline after "{" and before "}"
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find b=block{count(declaration) != 1} " \
              "require newline after b.child(0) and newline before b.child(-1) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ color:red; }b{\n\n\ncolor:red;\n\n\n}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert not violation_log.number_of_violations()

    def test_space_around_oneliner_braces_valid(self):
        """
        You can put spaces in one line declarations
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find b=block{count(declaration) == 1} " \
              "require (newline after b.child(0) and newline before b.child(-1)) or "\
              "(space after b.child(0) and space before b.child(-1)) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ color:red; }")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert not violation_log.number_of_violations()

    def test_space_around_oneliner_braces(self):
        """
        You can put spaces in one line declarations
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find b=block{count(declaration) == 1} " \
              "require (newline after b.child(0) and newline before b.child(-1)) or "\
              "(space after b.child(0) and space before b.child(-1)) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{\ncolor:red; } a{ color:red;   }")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_space_after_commas_valid(self):
        """
        Multiple csv values should be separated by either space of newline
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find c=comma " \
              "require space or newline after c "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ color: rgb(1, 2,\n3); }")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert not violation_log.number_of_violations()

    def test_space_after_commas(self):
        """
        Multiple csv values should be separated by either space of newline
        """
        cos = "Whitespace ignore newline comment newline { " \
              "find c=comma " \
              "require space or newline after c "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ color: rgb(1,  2,\n\n3); }")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_comments_on_new_line(self):
        """
        Place comments on a new line
        """
        cos = "Whitespace ignore indent{ " \
              "find c=comment " \
              "require newline{1,} before c and newline{1,} after c "\
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{\n/*comment*/\n}\n b /*commend*/\n{}\n/*comment*/ c {}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_no_js_prefixed_classes(self):
        """
        Do not make js- prefixed classes. They are used exclusively from JS files. Use the is- prefix instead.
        """
        cos = "Whitespace ignore indent{ " \
              "forbid class{name match '.*js-.*'} " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string(".js-class{} .is-class{} .class{}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_use_hex_for_colors(self):
        """
        Use hex for colors
        """
        cos = "Semantic ignore indent, space, newline,  { " \
              "forbid colorname " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ color: red; color: #FFFFFF }")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    # def test_use_rgba_with_opacity(self):
    #     """
    #     Use rgba only when opacity is needed
    #     """
    #     cos = "Semantic ignore indent, space, newline,  { " \
    #           "forbid rgba{opacity == 1} " \
    #           "message '' }"
    #     coco_ast = self.get_coco_ast(cos)
    #     css_tree = helpers.ParseHelper.parse_css_string("a{ color: rgba(1, 1, 2, 0.9); color: rgba(1, 1, 2, 1) }")
    #     css_tree.pretty_print()
    #     _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
    #     assert violation_log.number_of_violations() == 1

    def test_use_px_for_font_size(self):
        """
        Use px for font-size
        """
        cos = "Semantic ignore indent, space, newline,  { " \
              "find d=declaration{property.name=='font-size'} " \
              "require d.value.contains(dimension{unit=='px'}) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ font-size: 10px; font-size: 10em; }")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_unitless_line_height(self):
        """
        Line height should also be unit-less, unless necessary to be defined as a specific pixel value.
        """
        cos = "Semantic ignore indent, space, newline,  { " \
              "find d=declaration{property.name=='line-height'} " \
              "require not d.contains(dimension) or d.contains(dimension{unit=='px'}) " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("a{ line-height: 10px; line-height: 10em; line-height: 10; }")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_single_id_selector(self):
        """
        If you must use an id selector make sure that you have no more than one in your rule declaration.
        """
        cos = "Semantic ignore indent, space, newline,  { " \
              "find id in s=simpleselector " \
              "forbid s.count(selectorpart) > 1 " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css_tree = helpers.ParseHelper.parse_css_string("h1#a { } #b {} #a, #b{}")
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_not_oneliner_space_btw_rules_valid(self):
        """
        Add one blank line between rulesets
        """
        cos = "Whitespace ignore indent  { " \
              "find r1=ruleset next-to r2=ruleset " \
              "where not r1.is-single-line or not r2.is-single-line " \
              "require newline{2} between r1 and r2 " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """a {
                }

                b {}

                c {
                }"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert not violation_log.number_of_violations()

    def test_not_oneliner_space_btw_rules(self):
        """
        Add one blank line between rulesets
        """
        cos = "Whitespace ignore indent  { " \
              "find r1=ruleset next-to r2=ruleset " \
              "where not r1.is-single-line or not r2.is-single-line " \
              "require newline{2} between r1 and r2 " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """a {
                }
                c {
                }


                d {
                }"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_oneliner_space_btw_rules_valid(self):
        """
        Single-line rules may appear on adjacent lines
        """
        cos = "Whitespace ignore indent  { " \
              "find r1=ruleset next-to r2=ruleset " \
              "where r1.is-single-line and r2.is-single-line " \
              "require newline{1, 2} between r1 and r2 " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """a { }
                c {  }

                d {}"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert not violation_log.number_of_violations()

    def test_oneliner_space_btw_rules(self):
        """
        Single-line rules may appear on adjacent lines
        """
        cos = "Whitespace ignore indent  { " \
              "find r1=ruleset next-to r2=ruleset " \
              "where r1.is-single-line and r2.is-single-line " \
              "require newline{1, 2} between r1 and r2 " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """a { } c {  }


                d {}"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_disallow_adjoining_classes(self):
        """
        Disallow adjoining classes
        """
        cos = "Whitespace ignore indent  { " \
              "forbid class next-to class " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """.a.b {} .a .b{} h1.a{}"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_disallow_star_hack(self):
        """
        Disallow star hack
        """
        cos = "Whitespace ignore indent  { " \
              "find p=property " \
              "forbid p.name match '^\*.*'" \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """* {*color: red; color: red;}"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_disallow_font_face(self):
        """
        There are more than five font-faces in the stylesheet
        """
        cos = "Whitespace ignore indent  { " \
              "find s=stylesheet " \
              "forbid s.count(fontface) > 5" \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """@font-face{} @font-face{} @font-face{} @font-face{} @font-face{} @font-face{}"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_disallow_attr_selectors(self):
        """
        Disallow selectors that look like regular expressions
        """
        cos = "Whitespace ignore indent  { " \
              "find a=attrselector " \
              "forbid a.string in ['*=', '|=', '^=', '~=', '$=']" \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """[prop*='test'] {} [another='test']{}"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_disallow_universal_selector(self):
        """
        Disallow the universal selector
        """
        cos = "Whitespace ignore indent { " \
              "forbid universal " \
              "message '' }"
        coco_ast = self.get_coco_ast(cos)
        css = """* {}"""
        css_tree = helpers.ParseHelper.parse_css_string(css)
        css_tree.pretty_print()
        _, violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

