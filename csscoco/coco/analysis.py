

class TypeChecker:
    """
    Should check if there is an allow statement that does not relax any require statements
    """
    pass

#
# class ExpressionEvaluator(object):
#
#     def get_sequence_list(self, expr_list):
#         # if not expr_list:
#         #     return [seqs.Sequence([matching.NodeDescriptor.ANY])]
#         sequences = []
#         for markers_list in self._generate_possible_markers_lists(expr_list, []):
#             sequence = self._get_sequence(markers_list)
#             sequences.append(sequence)
#         return sequences
#
#     def _get_sequence(self, markers_list):
#         desc_list = []
#         for markers_expr in markers_list:
#             for marker in markers_expr.marker_list:
#                 desc = self.visit(marker)
#                 if type(desc) is seqs.SiblingSequence:
#                     for d in desc:
#                         desc_list.append(d)
#                 else:
#                     desc_list.append(desc)
#         if desc_list:
#             return seqs.SiblingSequence(desc_list)
#         return seqs.SiblingSequence.NONE
#
#     def _generate_possible_markers_lists(self, expr_list, result):
#         if len(expr_list) == 0:
#             yield result[:]
#         else:
#             first_expr = expr_list[0]
#             for marker_expr in first_expr.get_markers_expression():
#                 result.append(marker_expr)
#                 yield from self._generate_possible_markers_lists(expr_list[1:], result)
#                 del result[-1]
#
#     @vis.visitor(markers.RuleMarker)
#     def visit(self, node):
#         return descriptors.SimpleDescriptor(type_='ruleset')
#
#     @vis.visitor(markers.SelectorMarker)
#     def visit(self, node):
#         return descriptors.CompoundDescriptor([descriptors.SimpleDescriptor(type_='selector'),
#                                                descriptors.SimpleDescriptor(type_='simpleselector')])
#
#     @vis.visitor(markers.DeclarationMarker)
#     def visit(self, node):
#         return descriptors.SimpleDescriptor(type_='declaration')
#
#     @vis.visitor(markers.BlockMarker)
#     def visit(self, node):
#         return descriptors.CompoundDescriptor([descriptors.SimpleDescriptor(type_='block'),
#                                                descriptors.SimpleDescriptor(value='{'),
#                                                descriptors.SimpleDescriptor(value='}')])
#
#     @vis.visitor(markers.PropertyMarker)
#     def visit(self, node):
#         return descriptors.SimpleDescriptor(type_='property')
#
#     @vis.visitor(markers.ValueMarker)
#     def visit(self, node):
#         return descriptors.SimpleDescriptor(type_='value')
#
#     @vis.visitor(markers.EofMarker)
#     def visit(self, node):
#         return descriptors.SimpleDescriptor(type_='eof')
#
#     @vis.visitor(markers.CommentMarker)
#     def visit(self, node):
#         return descriptors.SimpleDescriptor(type_='comment')
#
#     @vis.visitor(markers.SymbolMarker)
#     def visit(self, node):
#         if node.value == '{':
#             return descriptors.CompoundDescriptor([descriptors.SimpleDescriptor(type_='block'),
#                                                    descriptors.SimpleDescriptor(value='{')])
#         if node.value == '}':
#             return descriptors.CompoundDescriptor([descriptors.SimpleDescriptor(type_='block'),
#                                                    descriptors.SimpleDescriptor(value='}')])
#
#         return descriptors.SimpleDescriptor(value=node.value)
#
#     @vis.visitor(markers.CsvCommaMarker)
#     def visit(self, node):
#         return descriptors.SimpleDescriptor(type_='operator', value=',')
#
#     @vis.visitor(markers.SelectorCommaMarker)
#     def visit(self, node):
#         return descriptors.SimpleDescriptor(type_='delim', value=',')
#
#     @vis.visitor(markers.WhitespaceMarker)
#     def visit(self, node):
#         return descriptors.CompoundDescriptor.WHITESPACE
#
#     @vis.visitor(markers.TabMarker)
#     def visit(self, node):
#         if node.is_repetitions_set():
#             ds = []
#             for i in range(0, node.repetitions):
#                 ds.append(descriptors.SimpleDescriptor(type_='tab', value='\t'))
#             return seqs.SiblingSequence(ds)
#         return descriptors.SimpleDescriptor(type_='tab')
#
#     @vis.visitor(markers.SpaceMarker)
#     def visit(self, node):
#         if node.is_repetitions_set():
#             ds = []
#             for i in range(0, node.repetitions):
#                 ds.append(descriptors.SimpleDescriptor(type_='space', value=' '))
#             return seqs.SiblingSequence(ds)
#         return descriptors.SimpleDescriptor(type_='space')
#
#     @vis.visitor(markers.NewlineMarker)
#     def visit(self, node):
#         if node.is_repetitions_set():
#             ds = []
#             for i in range(0, node.repetitions):
#                 ds.append(descriptors.SimpleDescriptor(type_='newline', value='\n'))
#             return seqs.SiblingSequence(ds)
#         return descriptors.SimpleDescriptor(type_='newline')
#
#
# class Evaluator():
#
#     @staticmethod
#     def evaluate(ast):
#         e = Evaluator()
#         return e.__eval(ast)
#
#     _context_stack = []
#
#     def _add_context_to_stack(self, c):
#         self._context_stack.append(c)
#
#     def _peek_context(self):
#         return self._context_stack[-1]
#
#     def _pop_context_from_stack(self):
#         self._context_stack = self._context_stack[:-1]
#
#     def __eval(self, tree):
#         return self.visit(tree)
#
#     @vis.visitor(ast.Sheet)
#     def visit(self, node):
#         return self.visit(node.contexts[0])
#
#     @vis.visitor(ast.WhitespaceContext)
#     def visit(self, node):
#         self._add_context_to_stack(node)
#         conventions = []
#         for stat in node.statements:
#             c = self.visit(stat)
#             conventions.append(c)
#         self._pop_context_from_stack()
#
#         return matching.ConventionsMap(conventions)
#
#     @vis.visitor(ast.CommentsContext)
#     def visit(self, node):
#         self._add_context_to_stack(node)
#         conventions = []
#         for stat in node.statements:
#             c = self.visit(stat)
#             conventions.append(c)
#         self._pop_context_from_stack()
#
#         return matching.ConventionsMap(conventions)
#
#     @vis.visitor(ast.ForbidRule)
#     def visit(self, node):
#         css_variation = self._get_cond(node)
#         option_list = self._get_list_of_ws_variations(node.markers_list)
#         requirement = matching.ForbidRequirement(option_list, self._peek_context().get_ignored_patterns())
#         return matching.ForbidConvention(css_variation, requirement)
#
#     @vis.visitor(ast.RequireRule)
#     def visit(self, node):
#         css_variation = self._get_cond(node)
#         option_list = self._get_list_of_ws_variations(node.markers_list)
#         requirement = matching.Requirement(option_list, self._peek_context().get_ignored_patterns())
#         return matching.RequireConvention(css_variation, requirement)
#
#     @vis.visitor(ast.AllowRule)
#     def visit(self, node):
#         css_variation = self._get_cond(node)
#         option_list = self._get_list_of_ws_variations(node.markers_list)
#         requirement = matching.Requirement(option_list, self._peek_context().get_ignored_patterns())
#         return matching.AllowConvention(css_variation, requirement)
#
#     def _get_cond(self, node):
#         css_expr_list = self._get_list_of_css_mark_expr(node.markers_list)
#         css_sequences = ExpressionEvaluator().get_sequence_list(css_expr_list)
#         if len(css_sequences) == 1 and css_sequences[0] is seqs.SiblingSequence.NONE:
#             css_sequences = [seqs.SiblingSequence([descriptors.NodeDescriptor.ANY])]
#         return seqs.SiblingsVariation(css_sequences, self._peek_context().get_target_patterns())
#
#     def _get_list_of_css_mark_expr(self, expr_list):
#         result = []
#         for expr in expr_list:
#             if self._contains_css_marker_expr(expr):
#                 result.append(expr)
#         return result
#
#     def _contains_css_marker_expr(self, expr):
#         for markers_expr in expr.get_markers_expression():
#             for marker in markers_expr:
#                 return self._peek_context().is_marker_in_condition(marker)
#
#     def _get_list_of_ws_variations(self, expr_list):
#         result = []
#         for markers_list in self._get_consecutive_ws_expr(expr_list):
#             sequences = ExpressionEvaluator().get_sequence_list(markers_list)
#             variation = seqs.SiblingsVariation.NONE
#             if sequences[0] is not seqs.SiblingSequence.NONE:
#                 variation = seqs.SiblingsVariation(sequences, self._peek_context().get_ignored_patterns())
#             result.append(variation)
#         return result
#
#     def _get_consecutive_ws_expr(self, expr_list):
#         buffer = []
#         for markers_expr in expr_list:
#             if self._contains_css_marker_expr(markers_expr):
#                 yield buffer
#                 buffer = []
#             else:
#                 buffer.append(markers_expr)
#         yield buffer
#
#     def _visit_options(self, ws_options):
#         res = []
#         for option in ws_options:
#             op = self.visit(option)
#             res.append(op)
#         return res
#
#     @vis.visitor(ast.MarkerSequenceVariation)
#     def visit(self, node):
#         if not node.marker_sequences:
#             return seqs.SiblingsVariation.NONE
#         res = []
#         for sequence in node.marker_sequences:
#             s = self.visit(sequence)
#             res.append(s)
#         return seqs.SiblingsVariation(res, [seqs.SiblingSequence([descriptors.SimpleDescriptor(type_='indent')])])
#
#     @vis.visitor(ast.MarkerSequence)
#     def visit(self, node):
#         res = []
#         for m in node.markers:
#             desc = self.visit(m)
#             res.append(desc)
#         return seqs.SiblingSequence(res)
#
