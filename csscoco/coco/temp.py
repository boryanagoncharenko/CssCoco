from csscoco.coco.ast.ast import *


class ToGo(object):

    @staticmethod
    def get_lint_set():
        sem_conventions = [
            # ToGo.conv3(),
            # ToGo.conv4(),
            # ToGo.conv27(),
            # ToGo.conv28(),
            # ToGo.conv29(),
            # ToGo.conv30(),
            # ToGo.conv31(),
            # ToGo.conv32(),
            # ToGo.conv33(),
            # ToGo.conv34(),
            # ToGo.conv35(),
            ToGo.conv36(),
            ]

        sem_context = SemanticContext(sem_conventions, [])

        return ConventionSet([
            sem_context
        ])

    @staticmethod
    def get_google_set():
        sem_conventions = [
            # ToGo.conv1(),
            # ToGo.conv2(),
            # ToGo.conv3(),
            # ToGo.conv4(),
            # ToGo.conv5(),
            # ToGo.conv6(),
            # ToGo.conv7(),
            # ToGo.conv8(),
            # ToGo.conv9(),
            # ToGo.conv10(),
            # ToGo.conv11(),
            # ToGo.conv12(),
            # ToGo.conv13(),
            # ToGo.conv14(),
            # ToGo.conv15(),
            ToGo.conv16(),
            # ToGo.conv17(),
            # ToGo.conv18(),
            # ToGo.conv19(),
            # ToGo.conv20(),
            # ToGo.conv21(),
            ]

        sem_context = SemanticContext(sem_conventions, [])

        white_conventions = [
            # ToGo.conv22(),
            # ToGo.conv23(),
            # ToGo.conv24(),
            # ToGo.conv25(),
        ]

        white_context = WhitespaceContext(white_conventions, [])

        indent_conventions = [
            # ToGo.conv26(),
            # ToGo.conv27(),
        ]

        indent_context = IndentContext(indent_conventions, [])

        return ConventionSet([
            sem_context,
            white_context,
            indent_context,
        ])

    @staticmethod
    def conv1():
        msg = 'Use em instead of pt, px, cm'
        dim = NodeExprWrapper(NodeDescriptor('dimension'))
        id = NodeExprWrapper(NodeDescriptor('ident'), identifier='i')
        relations = Relations()
        relations.register_relation(dim, IsParentOfRelation(id))
        pattern = PatternExpr(dim, [dim, id], relations)

        requirement = EqualsExpr(PropertyExpr(VariableExpr('i'), PropertyExpr('value')), StringExpr('em'))

        return FindRequireConvention(pattern, msg, requirement)


    @staticmethod
    def conv2():
        msg = 'Avoid using z-index property'
        name_expr = EqualsExpr(PropertyExpr(VariableExpr('current'), StringExpr('name')), StringExpr('z-index'))
        and_ = NodeExprWrapper(NodeDescriptor('property'), name_expr)
        pattern = PatternExpr(and_, [and_], Relations())

        return ForbidConvention(pattern, msg)


    @staticmethod
    def conv3():
        msg = 'Do not use !important'
        node = NodeExprWrapper(NodeDescriptor('important'))
        pattern = PatternExpr(node, [node], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv4():
        msg = 'Do not use ids'
        node = NodeExprWrapper(NodeDescriptor('id'))
        pattern = PatternExpr(node, [node], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv5():
        msg = 'Id and class names should be lowercase'
        node = NodeExprWrapper(NodeDescriptor.build_expr(lambda n: 'class' in n.search_labels or 'id' in n.search_labels),
                               identifier='n')
        pattern = PatternExpr(node, [node], Relations())
        requirement = MatchExpr(PropertyExpr(VariableExpr('n'), 'name'), StringExpr('^[a-z\-]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv6():
        msg = 'Properties should be lowercase; vendor-specific properties are exception'
        attr = NotExpr(PropertyExpr(VariableExpr('current'), 'is-vendor-specific'))
        node = NodeExprWrapper(NodeDescriptor.build_type('property'),
                               attr_expr=attr,
                               identifier='p')
        pattern = PatternExpr(node, [node], Relations())
        requirement = MatchExpr(PropertyExpr(VariableExpr('p'), 'name'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv7():
        msg = 'All values except the contents of strings should be lowercase'
        value_part_node = NodeExprWrapper(NodeDescriptor.build_expr(lambda n: 'string' not in n.search_labels),
                                          identifier='n')
        value_node = NodeExprWrapper(NodeDescriptor.build_type('value'))
        relations = Relations()
        relations.register_relation(value_node, IsAncestorOfRelation(value_part_node))
        pattern = PatternExpr(value_node, [value_node, value_part_node], relations)
        requirement = MatchExpr(PropertyExpr(VariableExpr('n'), 'string'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv8():
        msg = 'Attribute selectors and their values should be lowercase'
        attr_selector = NodeExprWrapper(NodeDescriptor.build_type('attribute-selector'))
        any_selector = NodeExprWrapper(NodeDescriptor.build_any(), identifier='a')
        relations = Relations()
        relations.register_relation(attr_selector, IsParentOfRelation(any_selector))
        pattern = PatternExpr(attr_selector, [attr_selector, any_selector], relations)
        requirement = MatchExpr(PropertyExpr(VariableExpr('a'), 'string'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv9():
        msg = 'Html tags should be lowercase'
        node = NodeExprWrapper(NodeDescriptor.build_type('tag'), identifier='t')
        pattern = PatternExpr(node, [node], Relations())
        requirement = MatchExpr(PropertyExpr(VariableExpr('t'), 'name'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv10():
        msg = 'Put a ; at the end of declarations'
        node = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d')
        pattern = PatternExpr(node, [node], Relations())
        requirement = EqualsExpr(PropertyExpr(
            PropertyExpr(VariableExpr('d'), MethodExpr('child', -1)), 'string'), StringExpr(';'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv11():
        msg = 'Do not put quotes in url declarations'
        url = NodeExprWrapper(NodeDescriptor.build_type('uri'))
        string = NodeExprWrapper(NodeDescriptor.build_type('string'))
        relations = Relations()
        relations.register_relation(url, IsParentOfRelation(string))
        pattern = PatternExpr(url, [url, string], relations)

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv12():
        msg = 'Use short hex values'
        is_long = PropertyExpr(VariableExpr(''), 'is-long')
        match_short = MatchExpr(PropertyExpr(VariableExpr(''), 'string'),
                                StringExpr('(?P<gr1>[0-9a-f])(?P=gr1)(?P<gr2>[0-9a-f])(?P=gr2)(?P<gr3>[0-9a-f])(?P=gr3)'))
        attr = AndExpr(is_long, match_short)
        hex_value = NodeExprWrapper(NodeDescriptor.build_type('hex'), attr_expr=attr)
        pattern = PatternExpr(hex_value, [hex_value], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv13():
        msg = 'Use the shorthand margin property instead'
        attr = ContainsAllExpr(VariableExpr(''), ListExpr([
            NodeExprWrapper(NodeDescriptor.build_type('property'), EqualsExpr(PropertyExpr(VariableExpr(''), 'name'), StringExpr('margin-right'))),
            NodeExprWrapper(NodeDescriptor.build_type('property'), EqualsExpr(PropertyExpr(VariableExpr(''), 'name'), StringExpr('margin-left'))),
            NodeExprWrapper(NodeDescriptor.build_type('property'), EqualsExpr(PropertyExpr(VariableExpr(''), 'name'), StringExpr('margin-top'))),
            NodeExprWrapper(NodeDescriptor.build_type('property'), EqualsExpr(PropertyExpr(VariableExpr(''), 'name'), StringExpr('margin-bottom'))),
        ]))
        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'), attr_expr=attr)

        pattern = PatternExpr(rule, [rule], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv14():
        msg = 'Do not use units after 0 values'
        dim = NodeExprWrapper(NodeDescriptor('dimension'))
        value_zero = EqualsExpr(PropertyExpr(VariableExpr(''), 'value'), DecimalExpr(0))
        num = NodeExprWrapper(NodeDescriptor('number'), attr_expr=value_zero)
        relations = Relations()
        relations.register_relation(dim, IsParentOfRelation(num))
        pattern = PatternExpr(dim, [dim, num], relations)

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv15():
        msg = 'Use a leading zero for decimal values'
        value_btw = AndExpr(GreaterThanExpr(PropertyExpr(VariableExpr(''), 'value'), DecimalExpr(-1)),
                            LessThanExpr(PropertyExpr(VariableExpr(''), 'value'), DecimalExpr(1)))
        node = NodeExprWrapper(NodeDescriptor.build_type('number'), attr_expr=value_btw, identifier='n')
        pattern = PatternExpr(node, [node], Relations())
        requirement = MatchExpr(PropertyExpr(VariableExpr('n'), 'string'), StringExpr('^0.*'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv16():
        msg = 'Use single quotes in attribute selectors'
        node = NodeExprWrapper(NodeDescriptor.build_type('attribute-value'), identifier='v')
        pattern = PatternExpr(node, [node], Relations())
        requirement = AndExpr(IsExpr(VariableExpr('v'), NodeTypeExpr('string')),
                              PropertyExpr(VariableExpr('v'), 'has-single-quotes'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv17():
        msg = 'Use single quotes in charsets'
        charset = NodeExprWrapper(NodeDescriptor('charset'))
        string = NodeExprWrapper(NodeDescriptor('string'), identifier='s')
        relations = Relations()
        relations.register_relation(charset, IsParentOfRelation(string))
        pattern = PatternExpr(charset, [charset, string], relations)
        requirement = PropertyExpr(VariableExpr('s'), StringExpr('has-double-quotes'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv18():
        msg = 'Use single quotes in values'
        value = NodeExprWrapper(NodeDescriptor('value'))
        string = NodeExprWrapper(NodeDescriptor('string'), identifier='s')
        relations = Relations()
        relations.register_relation(value, IsParentOfRelation(string))
        pattern = PatternExpr(value, [value, string], relations)
        requirement = PropertyExpr(VariableExpr('s'), StringExpr('has-single-quotes'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv19():
        msg = 'Do not specify the encoding of style sheets as these assume UTF-8.'
        charset = NodeExprWrapper(NodeDescriptor('charset'))
        pattern = PatternExpr(charset, [charset], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv20():
        msg = 'Omit the protocol http(s) in url'
        url = NodeExprWrapper(NodeDescriptor('uri'))
        raw = NodeExprWrapper(NodeDescriptor('raw'), identifier='r')
        relations = Relations()
        relations.register_relation(url, IsParentOfRelation(raw))
        pattern = PatternExpr(url, [url, raw], relations)
        requirement = NotExpr(MatchExpr(PropertyExpr(VariableExpr('r'), StringExpr('string')), StringExpr('(?i)https?:.*')))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv21():
        # TODO: Currently the pattern matcher accepts sequences, but not variations
        # the convention is forbid tag (class or id), and it is cool to be like that, however, that is a variation
        # and not a sequence
        msg = 'Do not overqualify classes and ids with html tags'
        seq = SequencePatternExpr([NodeExprWrapper(NodeDescriptor.build_type('tag')),
                                   NodeExprWrapper(NodeDescriptor.build_expr(lambda n: 'id' in n.search_labels
                                                                             or 'class' in n.search_labels))
                                   ])

        return ForbidConvention(seq, msg)

    @staticmethod
    def conv22():
        msg = 'Put one or two blank lines between rules'

        seq = SequencePatternExpr([NodeExprWrapper(NodeDescriptor.build_type('ruleset'), identifier='r1'),
                                   NodeExprWrapper(NodeDescriptor.build_type('ruleset'), identifier='r2')])
        requirement = BetweenExpr(VariableExpr('r1'),
                                  WhitespaceVariation([SequencePatternExpr([
                                      NodeSequenceExprWrapper(NodeDescriptor.build_type('newline'), Repeater(2, 3))])]),
                                  VariableExpr('r2'))
        return FindRequireConvention(seq, msg, requirement)

    @staticmethod
    def conv23():
        msg = 'Put one space between the colon and the value of a declaration.'

        seq = SequencePatternExpr([NodeExprWrapper(NodeDescriptor.build_type('colon'), identifier='i1'),
                                   NodeExprWrapper(NodeDescriptor.build_type('value'), identifier='i2')])
        requirement = BetweenExpr(VariableExpr('i1'),
                                  WhitespaceVariation([SequencePatternExpr([
                                      NodeExprWrapper(NodeDescriptor.build_type('space'))])]),
                                  VariableExpr('i2'))
        return FindRequireConvention(seq, msg, requirement)

    @staticmethod
    def conv24():
        msg = 'Put one space between the last selector and the block.'

        seq = SequencePatternExpr([NodeExprWrapper(NodeDescriptor.build_type('selector'), identifier='i1'),
                                   NodeExprWrapper(NodeDescriptor.build_type('block'), identifier='i2')])
        requirement = BetweenExpr(VariableExpr('i1'),
                                  WhitespaceVariation([SequencePatternExpr([
                                      NodeExprWrapper(NodeDescriptor.build_type('space'))])]),
                                  VariableExpr('i2'))
        return FindRequireConvention(seq, msg, requirement)

    @staticmethod
    def conv25():
        msg = 'One selector per line.'

        seq = SequencePatternExpr([NodeExprWrapper(NodeDescriptor.build_type('delim'), identifier='d1'),
                                   NodeExprWrapper(NodeDescriptor.build_type('simpleselector'), identifier='d2')])
        requirement = BetweenExpr(VariableExpr('d1'),
                                  WhitespaceVariation([SequencePatternExpr([
                                    NodeExprWrapper(NodeDescriptor.build_type('newline'))])]),
                                  VariableExpr('d2')
                                  )
        return FindRequireConvention(seq, msg, requirement)

    @staticmethod
    def conv26():
        msg = 'No trailing spaces.'

        seq = SequencePatternExpr([NodeExprWrapper(NodeDescriptor.build_type('space')),
                                   NodeExprWrapper(NodeDescriptor.build_expr(lambda n: 'newline' in n.search_labels
                                                                             or 'eof' in n.search_labels))])

        return ForbidConvention(seq, msg)

    @staticmethod
    def conv27():
        msg = 'Use 4 spaces for indentation, no tabs.'

        indent = NodeExprWrapper(NodeDescriptor.build_type('indent'), identifier='i')
        pattern = PatternExpr(indent, [indent], Relations())
        requirement = EqualsExpr(PropertyExpr(VariableExpr('i'), StringExpr('string')), StringExpr('    '))
        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv27():
        msg = 'Do not use @import'

        at_import = NodeExprWrapper(NodeDescriptor.build_type('import'))
        pattern = PatternExpr(at_import, [at_import], Relations())
        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv28():
        msg = "Warning if a rule contains width and border, border-left, " \
              "border-right, padding, padding-left, or padding-right"

        width = NodeExprWrapper(NodeDescriptor.build_type('property'),
                                EqualsExpr(PropertyExpr(VariableExpr('anything'), StringExpr('name')), StringExpr('width')))
        border = NodeExprWrapper(NodeDescriptor.build_type('property'),
                                 InExpr(PropertyExpr(VariableExpr('anything'), StringExpr('name')),
                                        ListExpr([StringExpr('border'),
                                                  StringExpr('border-left'),
                                                  StringExpr('border-right'),
                                                  StringExpr('padding'),
                                                  StringExpr('padding-left'),
                                                  StringExpr('padding-right'),
                                                  ])))
        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'),
                               attr_expr=AndExpr(ContainsExpr(VariableExpr(''), width),
                                                 ContainsExpr(VariableExpr(''), border)))

        pattern = PatternExpr(rule, [rule], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv29():
        msg = "Warning if a rule contains height and border, border-top, " \
              "border-bottom, padding, padding-top, or padding-bottom"

        width = NodeExprWrapper(NodeDescriptor.build_type('property'),
                                EqualsExpr(PropertyExpr(VariableExpr('anything'), StringExpr('name')), StringExpr('height')))
        border = NodeExprWrapper(NodeDescriptor.build_type('property'),
                                 InExpr(PropertyExpr(VariableExpr('anything'), StringExpr('name')),
                                        ListExpr([StringExpr('border'),
                                                  StringExpr('border-top'),
                                                  StringExpr('border-bottom'),
                                                  StringExpr('padding'),
                                                  StringExpr('padding-top'),
                                                  StringExpr('padding-bottom'),
                                                  ])))
        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'),
                               attr_expr=AndExpr(ContainsExpr(VariableExpr(''), width),
                                                 ContainsExpr(VariableExpr(''), border)))

        pattern = PatternExpr(rule, [rule], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv30():
        msg = 'A rule that has display: inline-block should not use float'

        float_ = NodeExprWrapper(NodeDescriptor.build_type('property'),
                                 EqualsExpr(PropertyExpr(VariableExpr('anything'), 'name'), StringExpr('float')))
        decl = NodeExprWrapper(NodeDescriptor.build_type('declaration'),
                               AndExpr(EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('anything'), StringExpr('property')), StringExpr('name')), StringExpr('display')),
                                       EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('anything'), StringExpr('value')), StringExpr('string')), StringExpr('inline-block'))))

        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'),
                               attr_expr=AndExpr(ContainsExpr(VariableExpr(''), float_),
                                                 ContainsExpr(VariableExpr(''), decl)))

        pattern = PatternExpr(rule, [rule], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv31():
        msg = 'A rule that has display: block should not use vertical-align'

        float_ = NodeExprWrapper(NodeDescriptor.build_type('property'),
                                 EqualsExpr(PropertyExpr(VariableExpr('anything'), 'name'), StringExpr('vertical-align')))
        decl = NodeExprWrapper(NodeDescriptor.build_type('declaration'),
                               AndExpr(EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('anything'), StringExpr('property')), StringExpr('name')), StringExpr('display')),
                                       EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('anything'), StringExpr('value')), StringExpr('string')), StringExpr('block'))))

        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'),
                               attr_expr=AndExpr(ContainsExpr(VariableExpr(''), float_),
                                                 ContainsExpr(VariableExpr(''), decl)))

        pattern = PatternExpr(rule, [rule], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv32():
        msg = 'Warning if a property is included in a rule twice and contains the same value.'

        decl1 = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d1')
        decl2 = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d2')

        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'))
        rs = Relations()
        rs.register_relation(rule, IsAncestorOfRelation(decl1))
        rs.register_relation(rule, IsAncestorOfRelation(decl2))
        pattern = PatternExpr(rule, [rule, decl1, decl2], rs)

        req = AndExpr(EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('name')),
                                 PropertyExpr(PropertyExpr(VariableExpr('d2'), StringExpr('property')), StringExpr('name'))),
                      EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('value')), StringExpr('string')),
                                 PropertyExpr(PropertyExpr(VariableExpr('d2'), StringExpr('value')), StringExpr('string'))))

        return FindForbidConvention(pattern, msg, req)

    @staticmethod
    def conv33():
        # TODO: this rule is significantly slower than the other rules
        msg = 'A property is included twice and is separated by at least one other property.'

        decl1 = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d1')
        decl2 = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d2')
        decl3 = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d3')

        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'))
        rs = Relations()
        rs.register_relation(rule, IsAncestorOfRelation(decl1))
        rs.register_relation(rule, IsAncestorOfRelation(decl2))
        rs.register_relation(rule, IsAncestorOfRelation(decl3))
        pattern = PatternExpr(rule, [rule, decl1, decl2, decl3], rs)

        req = AndExpr(EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('name')),
                                 PropertyExpr(PropertyExpr(VariableExpr('d3'), StringExpr('property')), StringExpr('name'))),
                      AndExpr(NotEqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('value')), StringExpr('string')),
                                            PropertyExpr(PropertyExpr(VariableExpr('d3'), StringExpr('value')), StringExpr('string'))),
                              NotEqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('name')),
                                            PropertyExpr(PropertyExpr(VariableExpr('d2'), StringExpr('property')), StringExpr('name')))
                              )
                      )

        return FindForbidConvention(pattern, msg, req)

    @staticmethod
    def conv34():
        msg = 'Forbid empty rules.'

        decl = NodeExprWrapper(NodeDescriptor.build_type('declaration'))
        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'),
                               attr_expr=NotExpr(ContainsExpr(VariableExpr(''), decl)))
                               # attr_expr=EqualsExpr(CountExpr(VariableExpr(''), decl), DecimalExpr(0)))
        pattern = PatternExpr(rule, [rule], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv35():
        msg = 'Warning if found a vendor-prefixed property without a standard property after it.'

        decl1 = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d1',
                                attr_expr=PropertyExpr(PropertyExpr(VariableExpr(''), StringExpr('property')), StringExpr('is-vendor-specific')))
        pattern = PatternExpr(decl1, [decl1], Relations())
        req = AndExpr(IsExpr(NextSiblingExpr(VariableExpr('d1')), NodeTypeExpr('declaration')),
                      OrExpr(AndExpr(PropertyExpr(NextSiblingExpr(VariableExpr('d1')), StringExpr('is-vendor-specific')),
                                     EqualsExpr(PropertyExpr(PropertyExpr(NextSiblingExpr(VariableExpr('d1')), StringExpr('property')), StringExpr('standard')),
                                                PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('standard')))),
                             AndExpr(NotExpr(PropertyExpr(NextSiblingExpr(VariableExpr('d1')), StringExpr('is-vendor-specific'))),
                                     EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('standard')),
                                                PropertyExpr(PropertyExpr(NextSiblingExpr(VariableExpr('d1')), StringExpr('property')), StringExpr('name')))
                                   )
                             )
                      )
        return FindRequireConvention(pattern, msg, req)


    @staticmethod
    def conv36():
        msg = 'Require fallback color. A color property with a rgba(), hsl(), or hsla() color ' \
              'without a preceding color property that has an older color format.'

        decl1 = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d1',
                                attr_expr=EqualsExpr(PropertyExpr(PropertyExpr(VariableExpr(''), StringExpr('property')), StringExpr('name')),
                                                     StringExpr('color')))
        func = NodeExprWrapper(NodeDescriptor.build_type('function'),
                               attr_expr=InExpr(PropertyExpr(VariableExpr(''), StringExpr('name')),
                                                ListExpr([StringExpr('rgb'),
                                                          StringExpr('rgba'),
                                                          StringExpr('hsl'),
                                                          StringExpr('hsla')])
                                                )
                               )
        relations = Relations()
        relations.register_relation(decl1, IsAncestorOfRelation(func))
        pattern = PatternExpr(decl1, [decl1, func], relations)

        req = AndExpr(AndExpr(IsExpr(PreviousSiblingExpr(VariableExpr('d1')), NodeTypeExpr('declaration')),
                              EqualsExpr(PropertyExpr(PropertyExpr(PreviousSiblingExpr(VariableExpr('d1')), StringExpr('property')), StringExpr('name')),
                                         StringExpr('color'))),
                      ContainsExpr(PreviousSiblingExpr(VariableExpr('d1')), NodeExprWrapper(NodeDescriptor.build_expr(
                          lambda n: 'hex' in n.search_labels or 'color-name' in n.search_labels
                      )))
        )
        # ToGo.or_(ToGo.type_(''))
        return FindRequireConvention(pattern, msg, req)

