from coco.ast.ast import *


class ToGo(object):
    
    @staticmethod
    def get_set():
        sem_conventions = [
            ToGo.conv1(),
            ToGo.conv2(),
            ToGo.conv3(),
            ToGo.conv4(),
            ToGo.conv5(),
            ToGo.conv6(),
            ToGo.conv7(),
            ToGo.conv8(),
            ToGo.conv9(),
            ToGo.conv10(),
            ToGo.conv11(),
            ToGo.conv12(),
            ToGo.conv13(),
            ToGo.conv14(),
            ToGo.conv15(),
            ToGo.conv16(),
            ToGo.conv17(),
            ToGo.conv18(),
            ToGo.conv19(),
            ToGo.conv20(),
            ToGo.conv21(),
            ]

        sem_context = SemanticContext(sem_conventions, [])

        white_conventions = [
            # ToGo.conv22(),
            ToGo.conv23(),
        ]

        white_context = WhitespaceContext(white_conventions, [])

        return ConventionSet([
            # sem_context,
            white_context
        ])

    @staticmethod
    def conv1():
        msg = 'Use em instead of pt, px, cm'
        dim = NodeExprWrapper(NodeDescriptor('dimension'))
        id = NodeExprWrapper(NodeDescriptor('ident'), identifier='i')
        relations = Relations()
        relations.register_relation(dim, IsParentOfRelation(id))
        pattern = PatternExpr(dim, [dim, id], relations)

        requirement = EqualsExpr(ApiCallExpr(VariableExpr('i'), 'value'), StringExpr('em'))

        return FindRequireConvention(pattern, msg, requirement)


    @staticmethod
    def conv2():
        msg = 'Avoid using z-index property'
        name_expr = EqualsExpr(ApiCallExpr(VariableExpr('current'), 'name'), StringExpr('z-index'))
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
        requirement = MatchExpr(ApiCallExpr(VariableExpr('n'), 'name'), StringExpr('^[a-z\-]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv6():
        msg = 'Properties should be lowercase; vendor-specific properties are exception'
        attr = NotExpr(ApiCallExpr(VariableExpr('current'), 'is-vendor-specific'))
        node = NodeExprWrapper(NodeDescriptor.build_type('property'),
                               attr_expr=attr,
                               identifier='p')
        pattern = PatternExpr(node, [node], Relations())
        requirement = MatchExpr(ApiCallExpr(VariableExpr('p'), 'name'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv7():
        msg = 'Everything except the contents of strings should be lowercase'
        value_part_node = NodeExprWrapper(NodeDescriptor.build_expr(lambda n: 'string' not in n.search_labels),
                                          identifier='n')
        value_node = NodeExprWrapper(NodeDescriptor.build_type('value'))
        relations = Relations()
        relations.register_relation(value_node, IsAncestorOfRelation(value_part_node))
        pattern = PatternExpr(value_node, [value_node, value_part_node], relations)
        requirement = MatchExpr(ApiCallExpr(VariableExpr('n'), 'string'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv8():
        msg = 'Attribute selectors and their values should be lowercase'
        attr_selector = NodeExprWrapper(NodeDescriptor.build_type('attribute-selector'))
        any_selector = NodeExprWrapper(NodeDescriptor.build_any(), identifier='a')
        relations = Relations()
        relations.register_relation(attr_selector, IsParentOfRelation(any_selector))
        pattern = PatternExpr(attr_selector, [attr_selector, any_selector], relations)
        requirement = MatchExpr(ApiCallExpr(VariableExpr('a'), 'string'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv9():
        msg = 'Html tags should be lowercase'
        node = NodeExprWrapper(NodeDescriptor.build_type('tag'), identifier='t')
        pattern = PatternExpr(node, [node], Relations())
        requirement = MatchExpr(ApiCallExpr(VariableExpr('t'), 'name'), StringExpr('^[^A-Z]+$'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv10():
        msg = 'Put a ; at the end of declarations'
        node = NodeExprWrapper(NodeDescriptor.build_type('declaration'), identifier='d')
        pattern = PatternExpr(node, [node], Relations())
        requirement = EqualsExpr(ApiCallExpr(
            ApiCallExprWithArg(VariableExpr('d'), 'child', -1), 'string'), StringExpr(';'))

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
        is_long = ApiCallExpr(VariableExpr(''), 'is-long')
        match_short = MatchExpr(ApiCallExpr(VariableExpr(''), 'string'),
                                StringExpr('(?P<gr1>[0-9a-f])(?P=gr1)(?P<gr2>[0-9a-f])(?P=gr2)(?P<gr3>[0-9a-f])(?P=gr3)'))
        attr = AndExpr(is_long, match_short)
        hex_value = NodeExprWrapper(NodeDescriptor.build_type('hex'), attr_expr=attr)
        pattern = PatternExpr(hex_value, [hex_value], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv13():
        msg = 'Use the shorthand margin property instead'
        attr = ContainsAllExpr(VariableExpr(''), ListExpr([
            NodeExprWrapper(NodeDescriptor.build_type('property'), EqualsExpr(ApiCallExpr(VariableExpr(''), 'name'), StringExpr('margin-right'))),
            NodeExprWrapper(NodeDescriptor.build_type('property'), EqualsExpr(ApiCallExpr(VariableExpr(''), 'name'), StringExpr('margin-left'))),
            NodeExprWrapper(NodeDescriptor.build_type('property'), EqualsExpr(ApiCallExpr(VariableExpr(''), 'name'), StringExpr('margin-top'))),
            NodeExprWrapper(NodeDescriptor.build_type('property'), EqualsExpr(ApiCallExpr(VariableExpr(''), 'name'), StringExpr('margin-bottom'))),
        ]))
        rule = NodeExprWrapper(NodeDescriptor.build_type('ruleset'), attr_expr=attr)

        pattern = PatternExpr(rule, [rule], Relations())

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv14():
        msg = 'Do not use units after 0 values'
        dim = NodeExprWrapper(NodeDescriptor('dimension'))
        value_zero = EqualsExpr(ApiCallExpr(VariableExpr(''), 'value'), DecimalExpr(0))
        num = NodeExprWrapper(NodeDescriptor('number'), attr_expr=value_zero)
        relations = Relations()
        relations.register_relation(dim, IsParentOfRelation(num))
        pattern = PatternExpr(dim, [dim, num], relations)

        return ForbidConvention(pattern, msg)

    @staticmethod
    def conv15():
        msg = 'Use a leading zero for decimal values'
        value_btw = AndExpr(GreaterThanExpr(ApiCallExpr(VariableExpr(''), 'value'), DecimalExpr(-1)),
                            LessThanExpr(ApiCallExpr(VariableExpr(''), 'value'), DecimalExpr(1)))
        node = NodeExprWrapper(NodeDescriptor.build_type('number'), attr_expr=value_btw, identifier='n')
        pattern = PatternExpr(node, [node], Relations())
        requirement = MatchExpr(ApiCallExpr(VariableExpr('n'), 'string'), StringExpr('^0.*'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv16():
        msg = 'Use single quotes in attribute selectors'
        node = NodeExprWrapper(NodeDescriptor.build_type('attribute-value'), identifier='v')
        pattern = PatternExpr(node, [node], Relations())
        requirement = AndExpr(IsExpr(VariableExpr('v'), NodeTypeExpr('string')),
                              ApiCallExpr(VariableExpr('v'), 'has-single-quotes'))

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv17():
        msg = 'Use single quotes in charsets'
        charset = NodeExprWrapper(NodeDescriptor('charset'))
        string = NodeExprWrapper(NodeDescriptor('string'), identifier='s')
        relations = Relations()
        relations.register_relation(charset, IsParentOfRelation(string))
        pattern = PatternExpr(charset, [charset, string], relations)
        requirement = ApiCallExpr(VariableExpr('s'), 'has-double-quotes')

        return FindRequireConvention(pattern, msg, requirement)

    @staticmethod
    def conv18():
        msg = 'Use single quotes in values'
        value = NodeExprWrapper(NodeDescriptor('value'))
        string = NodeExprWrapper(NodeDescriptor('string'), identifier='s')
        relations = Relations()
        relations.register_relation(value, IsParentOfRelation(string))
        pattern = PatternExpr(value, [value, string], relations)
        requirement = ApiCallExpr(VariableExpr('s'), 'has-single-quotes')

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
        requirement = NotExpr(MatchExpr(ApiCallExpr(VariableExpr('r'), 'string'), StringExpr('(?i)https?:.*')))

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