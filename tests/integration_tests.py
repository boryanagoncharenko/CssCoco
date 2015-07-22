import os
from unittest import TestCase

import tests.helpers as helpers
import csscoco.lang.analysis.type_checker as checker
import csscoco.lang.analysis.violations as violations


class TypeCheckerTests(TestCase):

    def setupFile(self, content):
        fo = open("foo.coco", "w")
        fo.write(content)
        fo.close()
        return fo

    def test_diff_eq_argument_types(self):

        file = self.setupFile('Semantic { forbid id message \'Do not use ids\' }')
        coco_ast = helpers.ParseHelper.parse_coco_string(file.name)
        css_tree = helpers.ParseHelper.parse_css_string('#a { z-index: 5; }')

        errors = checker.TypeChecker.check(coco_ast)
        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)

        os.remove(file.name)
