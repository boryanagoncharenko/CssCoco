from coco.ast.ast import *


class ToGo(object):
    
    @staticmethod
    def get_set():
        conventions = []
        
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())

        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())

        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())

        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())
        conventions.append(ToGo.conv1())
        conventions.append(ToGo.conv2())
        conventions.append(ToGo.conv3())
        conventions.append(ToGo.conv4())

        context = SemanticContext(conventions, [])
        return ConventionSet([context])

    @staticmethod
    def conv1():
        msg = 'Use em instead of pt, px, cm'
        dim = NodeExprWrapper(NodeDescriptor('dimension'))
        id = NodeExprWrapper(NodeDescriptor('ident'), identifier='i')
        relations = Relations()
        relations.register_relation(dim, IsParentOfRelation(id))
        pattern = PatternExpr(dim, [dim, id], relations)

        requirement = EqualsExpr(ApiCallExpr('i', 'value'), StringExpr('em'))

        return FindRequireConvention(pattern, msg, requirement)


    @staticmethod
    def conv2():
        msg = 'Avoid using z-index property'
        name_expr = EqualsExpr(ApiCallExpr('current', 'name'), StringExpr('z-index'))
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
        node = NodeExprWrapper(NodeDescriptor('shash'))
        pattern = PatternExpr(node, [node], Relations())

        return ForbidConvention(pattern, msg)

    # is_stylesheet = IsExpr(ImplicitVariableExpr.DEFAULT, NodeTypeExpr(type_string='stylesheet'))
    # is_rule = IsExpr(ImplicitVariableExpr.DEFAULT, NodeTypeExpr(type_string='ruleset'))
    # is_declaration = IsExpr(ImplicitVariableExpr.DEFAULT, NodeTypeExpr(type_string='declaration'))
    # is_next_rule = cocoIsExpr(cocoImplicitVariableExpr.DEFAULT, cocoNodeTypeExpr(type_string='ruleset'))
    # is_tag = cocoIsExpr(cocoImplicitVariableExpr.DEFAULT, cocoNodeTypeExpr(type_string='ident'))
    # is_child = cocoIsExpr(cocoImplicitVariableExpr.DEFAULT,
    #                           cocoNodeTypeExpr(type_string='combinator', value_string='>'))
    # contains_tag = cocoContainsExpr(cocoImplicitVariableExpr.DEFAULT, is_tag)
    
    # stylesheet = NodeExprWrapper(NodeDescriptor('stylesheet'), is_stylesheet)
    # rule = NodeExprWrapper(is_rule)
    # declaration1 = NodeExprWrapper(is_declaration, identifier='a')
    # declaration2 = NodeExprWrapper(is_declaration, identifier='b')
    # declaration3 = NodeExprWrapper(is_declaration, identifier='c')
    #
    # is_newline = IsExpr(ImplicitVariableExpr.DEFAULT, NodeTypeExpr(type_string='newline'))
    # is_space = IsExpr(ImplicitVariableExpr.DEFAULT, NodeTypeExpr(type_string='space'))
    # requirement = cocoBetweenExpr(cocoVariableExpr('r1'),
    #                                   cocoWhitespaceVariation([
    #                                       cocoSequencePatternExpr([cocoNodeSequenceExprWrapper(is_newline, cocoRepeater(2, 3))]),
    #                                       # cocoSequencePatternExpr([cocoNodeSequenceExprWrapper(is_space, cocoRepeater(lower=1, upper=10))])
    #                                       ]),
    #                                   cocoVariableExpr('r2')
    #                                   )
    
    # requirement = cocoBeforeExpr(cocoVariableExpr('d1'), cocoWhitespaceVariation([
    #     cocoSequencePatternExpr([cocoNodeExprWrapper(is_newline)])
    # ]))
    
    # relations = Relations()
    # relations.register_relation(stylesheet, IsAncestorOfRelation(rule))
    # relations.register_relation(rule, IsAncestorOfRelation(declaration1))
    # relations.register_relation(rule, IsAncestorOfRelation(declaration2))
    # relations.register_relation(rule, IsAncestorOfRelation(declaration3))
    # pattern = PatternExpr(stylesheet, [stylesheet, rule, declaration1, declaration2, declaration3], relations)
    #
    # convention = ForbidConvention(pattern, "Forbid pattern found")