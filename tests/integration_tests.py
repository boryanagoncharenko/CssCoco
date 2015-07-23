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
        coco_ast = self.get_coco_ast("Semantic { forbid ident{string in ['px', 'pt', 'cm']} message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a { margin: 5px; padding: 10cm; margin: 0pt; padding: 15em;}')
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_forbid_z_index(self):
        """
        Avoid using z-index property
        """
        coco_ast = self.get_coco_ast("Semantic { forbid property{name=='z-index'} message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a { z-index: 100; } .class { z-index: 200; }')
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_forbid_important(self):
        """
        Do not use !important
        """
        coco_ast = self.get_coco_ast("Semantic { forbid important message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a { z-index: 100; margin: 5px !important;}'
                                                        '.class { padding: 10px !important; color: red; }')
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_forbid_ids(self):
        """
        Avoid using ids
        """
        coco_ast = self.get_coco_ast("Semantic { forbid id message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a {} .class#id {} h1 #id {} h1 h2 {} .class {}')
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_lowercase_ids_and_classes(self):
        """
        All id and class names should be lowercase
        """
        coco_ast = self.get_coco_ast("Semantic { find p=(id or class) require p.name match lowercase message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('#a {} .class#id {} h1 #ID {} H1#id {} .clAss {}')
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_no_strings_in_uri(self):
        """
        Do not put quotes in url declarations
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid string in uri "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{ a: uri(\'test\'); b: url("another") } ')
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_use_short_hex(self):
        """
        Use short hex values
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid hex{is-long and string match shorten} "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a{ color: #112233; color: #E6E6E6 } ')
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_unitless_zero(self):
        """
        Do not use units after 0 values
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid number{num-value == 0} in (dimension or percentage) message '' }")
        css_tree = helpers.ParseHelper.parse_css_string('a { margin: 0; padding: 0px; offset: 0cm; top: 0%; }')
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_forbid_charset(self):
        """
        Do not specify the encoding of style sheets as these assume UTF-8
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid charset "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("@charset 'uft-8'")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_no_overqualified_tags(self):
        """
        Do not over-qualify classes and ids with html tags
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid tag next-to (class or id) "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("h1.class {} h2#id {} h1 h2 {} ")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_no_import(self):
        """
        Do not use @import
        """
        coco_ast = self.get_coco_ast("Semantic { "
                                     "forbid import "
                                     "message '' }")
        css_tree = helpers.ParseHelper.parse_css_string("@import url;")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
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
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_display_inline_block_and_float(self):
        """
        A rule that has display: inline-block should not use float
        """
        css = "Semantic { " \
              "forbid ruleset{contains(declaration{property.name=='display' and value.string=='inline-block'}) " \
              "and contains(property{name=='float'})} message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { display: inline-block; float: 4;}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_display_block_and_vertical_align(self):
        """
        A rule that has display: block should not use vertical-align
        """
        css = "Semantic { " \
              "forbid ruleset{contains(declaration{property.name=='display' and value.string=='block'}) " \
              "and contains(property{name=='vertical-align'})} message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { display: block; vertical-align: 4;}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_exact_duplicates(self):
        """
        Warning if a property is included in a rule twice and contains the same value.
        """
        css = "Semantic { " \
              "find (d1=declaration, d2=declaration) in ruleset "\
              "forbid d1.property.name == d2.property.name and "\
              "d1.value.string == d2.value.string message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { color: red; margin: 0; color: red; }")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_crossed_duplicates(self):
        """
        A property is included twice and is separated by at least one other property.
        """
        css = "Semantic { " \
              "find (d1=declaration, d2=declaration, d3=declaration) in ruleset "\
              "forbid d1.property.name == d3.property.name and "\
              "d2.property.name != d1.property.name and "\
              "d1.value.string != d3.value.string message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { color: red; margin: 0; color: blue; }")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_empty_rules(self):
        """
        Forbid empty rules.
        """
        css = "Semantic { " \
              "forbid ruleset{count(declaration) == 0} "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { } b {}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_no_standard_property(self):
        """
        Warning if found a vendor-prefixed property without a standard property after it.
        """
        css = "Semantic ignore space, newline{ " \
              "find d=declaration{property.is-vendor-specific} " \
              "require d.next-sibling is declaration and " \
              "((d.next-sibling.is-vendor-specific and d.next-sibling.property.standard == d.property.standard) or " \
              "(not d.next-sibling.is-vendor-specific and d.next-sibling.property.standard == d.property.standard)) "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { -webkit-hyphens: none; -moz-hyphens: "
                                                        "none; -ms-hyphens: none; }")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_color_fallback_property(self):
        """
        No fallback color for properties with a rgba(), hsl(), or hsla() color
        """
        css = "Semantic ignore space, newline{ " \
              "find (rgba or hsl or hsla) in d=declaration{property.name == 'color'} " \
              "require d.previous-sibling is declaration and " \
              "d.previous-sibling.property.name == 'color' and " \
              "(d.previous-sibling.contains(hex) or d.previous-sibling.contains(ident)) "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { color: rgba(1,2,3,0); } "
                                                        "b {color: red; color:rgba(1,2,3,0); }")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_space_btw_colon_value(self):
        """
        Put one space between the colon and the value of a declaration
        """
        css = "Whitespace { " \
              "find c=colon next-to v=value " \
              "require space between c and v "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { color: red; } "
                                                        "b {color:   red; color:red; }")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_blank_lines_btw_rules_valid(self):
        """
        Put one or two blank lines between rules
        """
        css = "Whitespace { " \
              "find r1=ruleset next-to r2=ruleset " \
              "require newline{2,3} between r1 and r2 "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { }\n\nb{}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 0

    def test_blank_lines_btw_rules(self):
        """
        Put one or two blank lines between rules
        """
        css = "Whitespace { " \
              "find r1=ruleset next-to r2=ruleset " \
              "require newline{2,3} between r1 and r2 "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { }\nb{}\n\n\n\nc{}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_blank_lines_btw_rules_ignore_comments(self):
        """
        Put one or two blank lines between rules
        """
        css = "Whitespace ignore newline comment newline { " \
              "find r1=ruleset next-to r2=ruleset " \
              "require newline{2} between r1 and r2 "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a { }\n\n/*comment*/\nb{}\n\nc{}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 0

    def test_space_btw_selector_and_block_valid(self):
        """
        Put one space between the last selector and the block
        """
        css = "Whitespace ignore newline comment newline { " \
              "find s=selector next-to b=block " \
              "require space between s and b "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a, b {} c {}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 0

    def test_space_btw_selector_and_block(self):
        """
        Put one space between the last selector and the block
        """
        css = "Whitespace ignore newline comment newline { " \
              "find s=selector next-to b=block " \
              "require space between s and b "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a, b{} c  {} d\n{}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 3

    def test_newline_btw_selectors(self):
        """
        One selector per line
        """
        css = "Whitespace ignore newline comment newline { " \
              "find s1=delim next-to s2=simpleselector " \
              "require newline between s1 and s2 "\
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a, b{} c,\nd  {}")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 1

    def test_no_trailing_spaces(self):
        """
        No trailing spaces
        """
        css = "Whitespace ignore newline comment newline { " \
              "forbid (space or indent) next-to (newline or eof) " \
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a {}  \n  b{}  \n")
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_indentation(self):
        """
        Use 4 spaces for indentation, no tabs
        """
        css = "Whitespace ignore newline comment newline { " \
              "find i=indent " \
              "require i.string match '^ {4}$' " \
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("\n    a {}\n  b{}\n c{}")
        css_tree.pretty_print()
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

    def test_declaration_on_newline(self):
        """
        Put every declaration on a new line
        """
        css = "Whitespace ignore newline comment newline { " \
              "find d=declaration " \
              "require newline before d " \
              "message '' }"
        coco_ast = self.get_coco_ast(css)
        css_tree = helpers.ParseHelper.parse_css_string("a{ color:red; color:red\ncolor:red;}")
        css_tree.pretty_print()
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)
        assert violation_log.number_of_violations() == 2

