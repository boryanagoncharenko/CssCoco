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