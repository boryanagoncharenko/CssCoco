from csscoco.lang.ast.ast import *


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
        dim = Node(NodeTypeDescriptor('dimension'))
        id = Node(NodeTypeDescriptor('ident'), identifier='i')
        relations = NodeRelations()
        relations.register_relation(dim, IsParentOf(id))
        pattern = PatternDescriptor(dim, [dim, id], relations)

        requirement = EqualExpr(PropertyExpr(VariableExpr('i'), PropertyExpr('value')), StringExpr('em'))

        return FindRequireConvention(pattern, msg, requirement)


    @staticmethod
    def conv2():
        msg = 'Avoid using z-index property'
        name_expr = EqualExpr(PropertyExpr(VariableExpr('current'), StringExpr('name')), StringExpr('z-index'))
        and_ = Node(NodeTypeDescriptor('property'), name_expr)
        pattern = PatternDescriptor(and_, [and_], NodeRelations())

        return ForbidConvention(pattern, msg)


    @staticmethod
    def conv3():
        msg = 'Do not use !important'
        node = Node(NodeTypeDescriptor('important'))
        pattern = PatternDescriptor(node, [node], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv4():
        msg = 'Do not use ids'
        node = Node(NodeTypeDescriptor('id'))
        pattern = PatternDescriptor(node, [node], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv5():
        msg = 'Id and class names should be lowercase'
        node = Node(NodeTypeDescriptor.build_expr(lambda n: 'class' in n.search_labels or 'id' in n.search_labels),
                               identifier='n')
        pattern = PatternDescriptor(node, [node], NodeRelations())
        requirement = MatchExpr(PropertyExpr(VariableExpr('n'), 'name'), StringExpr('^[a-z\-]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv6():
        msg = 'Properties should be lowercase; vendor-specific properties are exception'
        attr = NotExpr(PropertyExpr(VariableExpr('current'), 'is-vendor-specific'))
        node = Node(NodeTypeDescriptor.build_type('property'),
                               constraint=attr,
                               identifier='p')
        pattern = PatternDescriptor(node, [node], NodeRelations())
        requirement = MatchExpr(PropertyExpr(VariableExpr('p'), 'name'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv7():
        msg = 'All values except the contents of strings should be lowercase'
        value_part_node = Node(NodeTypeDescriptor.build_expr(lambda n: 'string' not in n.search_labels),
                                          identifier='n')
        value_node = Node(NodeTypeDescriptor.build_type('value'))
        relations = NodeRelations()
        relations.register_relation(value_node, IsAncestorOf(value_part_node))
        pattern = PatternDescriptor(value_node, [value_node, value_part_node], relations)
        requirement = MatchExpr(PropertyExpr(VariableExpr('n'), 'string'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv8():
        msg = 'Attribute selectors and their values should be lowercase'
        attr_selector = Node(NodeTypeDescriptor.build_type('attribute-selector'))
        any_selector = Node(NodeTypeDescriptor.build_any(), identifier='a')
        relations = NodeRelations()
        relations.register_relation(attr_selector, IsParentOf(any_selector))
        pattern = PatternDescriptor(attr_selector, [attr_selector, any_selector], relations)
        requirement = MatchExpr(PropertyExpr(VariableExpr('a'), 'string'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv9():
        msg = 'Html tags should be lowercase'
        node = Node(NodeTypeDescriptor.build_type('tag'), identifier='t')
        pattern = PatternDescriptor(node, [node], NodeRelations())
        requirement = MatchExpr(PropertyExpr(VariableExpr('t'), 'name'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv10():
        msg = 'Put a ; at the end of declarations'
        node = Node(NodeTypeDescriptor.build_type('declaration'), identifier='d')
        pattern = PatternDescriptor(node, [node], NodeRelations())
        requirement = EqualExpr(PropertyExpr(
            PropertyExpr(VariableExpr('d'), MethodExpr('child', -1)), 'string'), StringExpr(';'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv11():
        msg = 'Do not put quotes in url declarations'
        url = Node(NodeTypeDescriptor.build_type('uri'))
        string = Node(NodeTypeDescriptor.build_type('string'))
        relations = NodeRelations()
        relations.register_relation(url, IsParentOf(string))
        pattern = PatternDescriptor(url, [url, string], relations)

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv12():
        msg = 'Use short hex values'
        is_long = PropertyExpr(VariableExpr(''), 'is-long')
        match_short = MatchExpr(PropertyExpr(VariableExpr(''), 'string'),
                                StringExpr('(?P<gr1>[0-9a-f])(?P=gr1)(?P<gr2>[0-9a-f])(?P=gr2)(?P<gr3>[0-9a-f])(?P=gr3)'))
        attr = AndExpr(is_long, match_short)
        hex_value = Node(NodeTypeDescriptor.build_type('hex'), constraint=attr)
        pattern = PatternDescriptor(hex_value, [hex_value], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv13():
        msg = 'Use the shorthand margin property instead'
        attr = ContainsAllExpr(VariableExpr(''), ListExpr([
            Node(NodeTypeDescriptor.build_type('property'), EqualExpr(PropertyExpr(VariableExpr(''), 'name'), StringExpr('margin-right'))),
            Node(NodeTypeDescriptor.build_type('property'), EqualExpr(PropertyExpr(VariableExpr(''), 'name'), StringExpr('margin-left'))),
            Node(NodeTypeDescriptor.build_type('property'), EqualExpr(PropertyExpr(VariableExpr(''), 'name'), StringExpr('margin-top'))),
            Node(NodeTypeDescriptor.build_type('property'), EqualExpr(PropertyExpr(VariableExpr(''), 'name'), StringExpr('margin-bottom'))),
        ]))
        rule = Node(NodeTypeDescriptor.build_type('ruleset'), constraint=attr)

        pattern = PatternDescriptor(rule, [rule], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv14():
        msg = 'Do not use units after 0 values'
        dim = Node(NodeTypeDescriptor('dimension'))
        value_zero = EqualExpr(PropertyExpr(VariableExpr(''), 'value'), IntegerExpr(0))
        num = Node(NodeTypeDescriptor('number'), constraint=value_zero)
        relations = NodeRelations()
        relations.register_relation(dim, IsParentOf(num))
        pattern = PatternDescriptor(dim, [dim, num], relations)

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv15():
        msg = 'Use a leading zero for decimal values'
        value_btw = AndExpr(GreaterThanExpr(PropertyExpr(VariableExpr(''), 'value'), IntegerExpr(-1)),
                            LessThanExpr(PropertyExpr(VariableExpr(''), 'value'), IntegerExpr(1)))
        node = Node(NodeTypeDescriptor.build_type('number'), constraint=value_btw, identifier='n')
        pattern = PatternDescriptor(node, [node], NodeRelations())
        requirement = MatchExpr(PropertyExpr(VariableExpr('n'), 'string'), StringExpr('^0.*'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv16():
        msg = 'Use single quotes in attribute selectors'
        node = Node(NodeTypeDescriptor.build_type('attribute-value'), identifier='v')
        pattern = PatternDescriptor(node, [node], NodeRelations())
        requirement = AndExpr(IsExpr(VariableExpr('v'), NodeTypeExpr('string')),
                              PropertyExpr(VariableExpr('v'), 'has-single-quotes'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv17():
        msg = 'Use single quotes in charsets'
        charset = Node(NodeTypeDescriptor('charset'))
        string = Node(NodeTypeDescriptor('string'), identifier='s')
        relations = NodeRelations()
        relations.register_relation(charset, IsParentOf(string))
        pattern = PatternDescriptor(charset, [charset, string], relations)
        requirement = PropertyExpr(VariableExpr('s'), StringExpr('has-double-quotes'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv18():
        msg = 'Use single quotes in values'
        value = Node(NodeTypeDescriptor('value'))
        string = Node(NodeTypeDescriptor('string'), identifier='s')
        relations = NodeRelations()
        relations.register_relation(value, IsParentOf(string))
        pattern = PatternDescriptor(value, [value, string], relations)
        requirement = PropertyExpr(VariableExpr('s'), StringExpr('has-single-quotes'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv19():
        msg = 'Do not specify the encoding of style sheets as these assume UTF-8.'
        charset = Node(NodeTypeDescriptor('charset'))
        pattern = PatternDescriptor(charset, [charset], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv20():
        msg = 'Omit the protocol http(s) in url'
        url = Node(NodeTypeDescriptor('uri'))
        raw = Node(NodeTypeDescriptor('raw'), identifier='r')
        relations = NodeRelations()
        relations.register_relation(url, IsParentOf(raw))
        pattern = PatternDescriptor(url, [url, raw], relations)
        requirement = NotExpr(MatchExpr(PropertyExpr(VariableExpr('r'), StringExpr('string')), StringExpr('(?i)https?:.*')))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv21():
        # TODO: Currently the pattern matcher accepts sequences, but not variations
        # the convention is forbid tag (class or id), and it is cool to be like that, however, that is a variation
        # and not a sequence
        msg = 'Do not overqualify classes and ids with html tags'
        seq = SequencePattern([Node(NodeTypeDescriptor.build_type('tag')),
                                   Node(NodeTypeDescriptor.build_expr(lambda n: 'id' in n.search_labels
                                                                             or 'class' in n.search_labels))
                                   ])

        return ForbidConvention(seq, msg)

    @staticmethod
    def conv22():
        msg = 'Put one or two blank lines between rules'

        seq = SequencePattern([Node(NodeTypeDescriptor.build_type('ruleset'), identifier='r1'),
                                   Node(NodeTypeDescriptor.build_type('ruleset'), identifier='r2')])
        requirement = BetweenExpr(VariableExpr('r1'),
                                  WhitespaceVariation([SequencePattern([
                                      WhitespaceNode(NodeTypeDescriptor.build_type('newline'), Repeater(2, 3))])]),
                                  VariableExpr('r2'))
        return FindRequireConvention(seq, msg, requirement)

    @staticmethod
    def conv23():
        msg = 'Put one space between the colon and the value of a declaration.'

        seq = SequencePattern([Node(NodeTypeDescriptor.build_type('colon'), identifier='i1'),
                                   Node(NodeTypeDescriptor.build_type('value'), identifier='i2')])
        requirement = BetweenExpr(VariableExpr('i1'),
                                  WhitespaceVariation([SequencePattern([
                                      Node(NodeTypeDescriptor.build_type('space'))])]),
                                  VariableExpr('i2'))
        return FindRequireConvention(seq, msg, requirement)

    @staticmethod
    def conv24():
        msg = 'Put one space between the last selector and the block.'

        seq = SequencePattern([Node(NodeTypeDescriptor.build_type('selector'), identifier='i1'),
                                   Node(NodeTypeDescriptor.build_type('block'), identifier='i2')])
        requirement = BetweenExpr(VariableExpr('i1'),
                                  WhitespaceVariation([SequencePattern([
                                      Node(NodeTypeDescriptor.build_type('space'))])]),
                                  VariableExpr('i2'))
        return FindRequireConvention(seq, msg, requirement)

    @staticmethod
    def conv25():
        msg = 'One selector per line.'

        seq = SequencePattern([Node(NodeTypeDescriptor.build_type('delim'), identifier='d1'),
                                   Node(NodeTypeDescriptor.build_type('simpleselector'), identifier='d2')])
        requirement = BetweenExpr(VariableExpr('d1'),
                                  WhitespaceVariation([SequencePattern([
                                    Node(NodeTypeDescriptor.build_type('newline'))])]),
                                  VariableExpr('d2')
                                  )
        return FindRequireConvention(seq, msg, requirement)

    @staticmethod
    def conv26():
        msg = 'No trailing spaces.'

        seq = SequencePattern([Node(NodeTypeDescriptor.build_type('space')),
                                   Node(NodeTypeDescriptor.build_expr(lambda n: 'newline' in n.search_labels
                                                                             or 'eof' in n.search_labels))])

        return ForbidConvention(seq, msg)

    @staticmethod
    def conv27():
        msg = 'Use 4 spaces for indentation, no tabs.'

        indent = Node(NodeTypeDescriptor.build_type('indent'), identifier='i')
        pattern = PatternDescriptor(indent, [indent], NodeRelations())
        requirement = EqualExpr(PropertyExpr(VariableExpr('i'), StringExpr('string')), StringExpr('    '))
        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv27():
        msg = 'Do not use @import'

        at_import = Node(NodeTypeDescriptor.build_type('import'))
        pattern = PatternDescriptor(at_import, [at_import], NodeRelations())
        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv28():
        msg = "Warning if a rule contains width and border, border-left, " \
              "border-right, padding, padding-left, or padding-right"

        width = Node(NodeTypeDescriptor.build_type('property'),
                                EqualExpr(PropertyExpr(VariableExpr('anything'), StringExpr('name')), StringExpr('width')))
        border = Node(NodeTypeDescriptor.build_type('property'),
                                 InExpr(PropertyExpr(VariableExpr('anything'), StringExpr('name')),
                                        ListExpr([StringExpr('border'),
                                                  StringExpr('border-left'),
                                                  StringExpr('border-right'),
                                                  StringExpr('padding'),
                                                  StringExpr('padding-left'),
                                                  StringExpr('padding-right'),
                                                  ])))
        rule = Node(NodeTypeDescriptor.build_type('ruleset'),
                               constraint=AndExpr(ContainsExpr(VariableExpr(''), width),
                                                 ContainsExpr(VariableExpr(''), border)))

        pattern = PatternDescriptor(rule, [rule], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv29():
        msg = "Warning if a rule contains height and border, border-top, " \
              "border-bottom, padding, padding-top, or padding-bottom"

        width = Node(NodeTypeDescriptor.build_type('property'),
                                EqualExpr(PropertyExpr(VariableExpr('anything'), StringExpr('name')), StringExpr('height')))
        border = Node(NodeTypeDescriptor.build_type('property'),
                                 InExpr(PropertyExpr(VariableExpr('anything'), StringExpr('name')),
                                        ListExpr([StringExpr('border'),
                                                  StringExpr('border-top'),
                                                  StringExpr('border-bottom'),
                                                  StringExpr('padding'),
                                                  StringExpr('padding-top'),
                                                  StringExpr('padding-bottom'),
                                                  ])))
        rule = Node(NodeTypeDescriptor.build_type('ruleset'),
                               constraint=AndExpr(ContainsExpr(VariableExpr(''), width),
                                                 ContainsExpr(VariableExpr(''), border)))

        pattern = PatternDescriptor(rule, [rule], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv30():
        msg = 'A rule that has display: inline-block should not use float'

        float_ = Node(NodeTypeDescriptor.build_type('property'),
                                 EqualExpr(PropertyExpr(VariableExpr('anything'), 'name'), StringExpr('float')))
        decl = Node(NodeTypeDescriptor.build_type('declaration'),
                               AndExpr(EqualExpr(PropertyExpr(PropertyExpr(VariableExpr('anything'), StringExpr('property')), StringExpr('name')), StringExpr('display')),
                                       EqualExpr(PropertyExpr(PropertyExpr(VariableExpr('anything'), StringExpr('value')), StringExpr('string')), StringExpr('inline-block'))))

        rule = Node(NodeTypeDescriptor.build_type('ruleset'),
                               constraint=AndExpr(ContainsExpr(VariableExpr(''), float_),
                                                 ContainsExpr(VariableExpr(''), decl)))

        pattern = PatternDescriptor(rule, [rule], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv31():
        msg = 'A rule that has display: block should not use vertical-align'

        float_ = Node(NodeTypeDescriptor.build_type('property'),
                                 EqualExpr(PropertyExpr(VariableExpr('anything'), 'name'), StringExpr('vertical-align')))
        decl = Node(NodeTypeDescriptor.build_type('declaration'),
                               AndExpr(EqualExpr(PropertyExpr(PropertyExpr(VariableExpr('anything'), StringExpr('property')), StringExpr('name')), StringExpr('display')),
                                       EqualExpr(PropertyExpr(PropertyExpr(VariableExpr('anything'), StringExpr('value')), StringExpr('string')), StringExpr('block'))))

        rule = Node(NodeTypeDescriptor.build_type('ruleset'),
                               constraint=AndExpr(ContainsExpr(VariableExpr(''), float_),
                                                 ContainsExpr(VariableExpr(''), decl)))

        pattern = PatternDescriptor(rule, [rule], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv32():
        msg = 'Warning if a property is included in a rule twice and contains the same value.'

        decl1 = Node(NodeTypeDescriptor.build_type('declaration'), identifier='d1')
        decl2 = Node(NodeTypeDescriptor.build_type('declaration'), identifier='d2')

        rule = Node(NodeTypeDescriptor.build_type('ruleset'))
        rs = NodeRelations()
        rs.register_relation(rule, IsAncestorOf(decl1))
        rs.register_relation(rule, IsAncestorOf(decl2))
        pattern = PatternDescriptor(rule, [rule, decl1, decl2], rs)

        req = AndExpr(EqualExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('name')),
                                 PropertyExpr(PropertyExpr(VariableExpr('d2'), StringExpr('property')), StringExpr('name'))),
                      EqualExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('value')), StringExpr('string')),
                                 PropertyExpr(PropertyExpr(VariableExpr('d2'), StringExpr('value')), StringExpr('string'))))

        return FindForbidConvention(pattern, msg, req)

    @staticmethod
    def conv33():
        # TODO: this rule is significantly slower than the other rules
        msg = 'A property is included twice and is separated by at least one other property.'

        decl1 = Node(NodeTypeDescriptor.build_type('declaration'), identifier='d1')
        decl2 = Node(NodeTypeDescriptor.build_type('declaration'), identifier='d2')
        decl3 = Node(NodeTypeDescriptor.build_type('declaration'), identifier='d3')

        rule = Node(NodeTypeDescriptor.build_type('ruleset'))
        rs = NodeRelations()
        rs.register_relation(rule, IsAncestorOf(decl1))
        rs.register_relation(rule, IsAncestorOf(decl2))
        rs.register_relation(rule, IsAncestorOf(decl3))
        pattern = PatternDescriptor(rule, [rule, decl1, decl2, decl3], rs)

        req = AndExpr(EqualExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('name')),
                                 PropertyExpr(PropertyExpr(VariableExpr('d3'), StringExpr('property')), StringExpr('name'))),
                      AndExpr(NotEqualExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('value')), StringExpr('string')),
                                            PropertyExpr(PropertyExpr(VariableExpr('d3'), StringExpr('value')), StringExpr('string'))),
                              NotEqualExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('name')),
                                            PropertyExpr(PropertyExpr(VariableExpr('d2'), StringExpr('property')), StringExpr('name')))
                              )
                      )

        return FindForbidConvention(pattern, msg, req)

    @staticmethod
    def conv34():
        msg = 'Forbid empty rules.'

        decl = Node(NodeTypeDescriptor.build_type('declaration'))
        rule = Node(NodeTypeDescriptor.build_type('ruleset'),
                               constraint=NotExpr(ContainsExpr(VariableExpr(''), decl)))
                               # attr_expr=EqualsExpr(CountExpr(VariableExpr(''), decl), DecimalExpr(0)))
        pattern = PatternDescriptor(rule, [rule], NodeRelations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv35():
        msg = 'Warning if found a vendor-prefixed property without a standard property after it.'

        decl1 = Node(NodeTypeDescriptor.build_type('declaration'), identifier='d1',
                                constraint=PropertyExpr(PropertyExpr(VariableExpr(''), StringExpr('property')), StringExpr('is-vendor-specific')))
        pattern = PatternDescriptor(decl1, [decl1], NodeRelations())
        req = AndExpr(IsExpr(NextSiblingExpr(VariableExpr('d1')), NodeTypeExpr('declaration')),
                      OrExpr(AndExpr(PropertyExpr(NextSiblingExpr(VariableExpr('d1')), StringExpr('is-vendor-specific')),
                                     EqualExpr(PropertyExpr(PropertyExpr(NextSiblingExpr(VariableExpr('d1')), StringExpr('property')), StringExpr('standard')),
                                                PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('standard')))),
                             AndExpr(NotExpr(PropertyExpr(NextSiblingExpr(VariableExpr('d1')), StringExpr('is-vendor-specific'))),
                                     EqualExpr(PropertyExpr(PropertyExpr(VariableExpr('d1'), StringExpr('property')), StringExpr('standard')),
                                                PropertyExpr(PropertyExpr(NextSiblingExpr(VariableExpr('d1')), StringExpr('property')), StringExpr('name')))
                                   )
                             )
                      )
        return FindRequireConvention(pattern, msg, req)


    @staticmethod
    def conv36():
        msg = 'Require fallback color. A color property with a rgba(), hsl(), or hsla() color ' \
              'without a preceding color property that has an older color format.'

        decl1 = Node(NodeTypeDescriptor.build_type('declaration'), identifier='d1',
                                constraint=EqualExpr(PropertyExpr(PropertyExpr(VariableExpr(''), StringExpr('property')), StringExpr('name')),
                                                     StringExpr('color')))
        func = Node(NodeTypeDescriptor.build_type('function'),
                               constraint=InExpr(PropertyExpr(VariableExpr(''), StringExpr('name')),
                                                ListExpr([StringExpr('rgb'),
                                                          StringExpr('rgba'),
                                                          StringExpr('hsl'),
                                                          StringExpr('hsla')])
                                                )
                               )
        relations = NodeRelations()
        relations.register_relation(decl1, IsAncestorOf(func))
        pattern = PatternDescriptor(decl1, [decl1, func], relations)

        req = AndExpr(AndExpr(IsExpr(PreviousSiblingExpr(VariableExpr('d1')), NodeTypeExpr('declaration')),
                              EqualExpr(PropertyExpr(PropertyExpr(PreviousSiblingExpr(VariableExpr('d1')), StringExpr('property')), StringExpr('name')),
                                         StringExpr('color'))),
                      ContainsExpr(PreviousSiblingExpr(VariableExpr('d1')), Node(NodeTypeDescriptor.build_expr(
                          lambda n: 'hex' in n.search_labels or 'color-name' in n.search_labels
                      )))
        )
        # ToGo.or_(ToGo.type_(''))
        return FindRequireConvention(pattern, msg, req)

