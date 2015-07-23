import os
from unittest import TestCase

import tests.helpers as helpers
import csscoco.lang.analysis.type_checker as checker
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

    def test_diff_eq_argument_types(self):

        coco_ast = self.get_coco_ast('Semantic { forbid id message \'Do not use ids\' }')
        css_tree = helpers.ParseHelper.parse_css_string('#a { z-index: 5; }')

        violation_log = violations.ViolationsFinder.find(coco_ast, css_tree)


        os.remove(self.filename)
