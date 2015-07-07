# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .cocoVisitor import cocoVisitor
else:
    from cocoVisitor import cocoVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3!")
        buf.write("\u00a4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\7\2\"\n\2\f\2\16\2%\13\2")
        buf.write("\3\3\3\3\3\3\7\3*\n\3\f\3\16\3-\13\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\5\7;\n\7\3\7\3\7\5\7?\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("M\n\t\3\t\3\t\3\t\3\t\3\t\3\t\7\tU\n\t\f\t\16\tX\13\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nf")
        buf.write("\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7")
        buf.write("\nt\n\n\f\n\16\nw\13\n\3\13\3\13\3\13\3\f\3\f\6\f~\n\f")
        buf.write("\r\f\16\f\177\3\f\3\f\3\r\3\r\5\r\u0086\n\r\3\r\3\r\3")
        buf.write("\r\7\r\u008b\n\r\f\r\16\r\u008e\13\r\3\16\3\16\3\16\5")
        buf.write("\16\u0093\n\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17\u009b")
        buf.write("\n\17\f\17\16\17\u009e\13\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\2\4\20\22\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2")
        buf.write("\6\3\2\31\33\6\2\3\3\7\7\16\20\22\22\4\2\n\n\24\25\3\2")
        buf.write("\34\36\u00ab\2#\3\2\2\2\4&\3\2\2\2\6\60\3\2\2\2\b\62\3")
        buf.write("\2\2\2\n\66\3\2\2\2\f:\3\2\2\2\16@\3\2\2\2\20L\3\2\2\2")
        buf.write("\22e\3\2\2\2\24x\3\2\2\2\26{\3\2\2\2\30\u0085\3\2\2\2")
        buf.write("\32\u008f\3\2\2\2\34\u0096\3\2\2\2\36\u00a1\3\2\2\2 \"")
        buf.write("\5\4\3\2! \3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\3\3")
        buf.write("\2\2\2%#\3\2\2\2&\'\7\34\2\2\'+\7\4\2\2(*\5\6\4\2)(\3")
        buf.write("\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2")
        buf.write("\2./\7\6\2\2/\5\3\2\2\2\60\61\5\b\5\2\61\7\3\2\2\2\62")
        buf.write("\63\7\b\2\2\63\64\5\n\6\2\64\65\5\24\13\2\65\t\3\2\2\2")
        buf.write("\66\67\5\f\7\2\67\13\3\2\2\289\7\34\2\29;\7\5\2\2:8\3")
        buf.write("\2\2\2:;\3\2\2\2;<\3\2\2\2<>\5\20\t\2=?\5\16\b\2>=\3\2")
        buf.write("\2\2>?\3\2\2\2?\r\3\2\2\2@A\7\4\2\2AB\5\22\n\2BC\7\6\2")
        buf.write("\2C\17\3\2\2\2DE\b\t\1\2EF\7\32\2\2FM\5\20\t\6GH\7\t\2")
        buf.write("\2HI\5\20\t\2IJ\7\27\2\2JM\3\2\2\2KM\7\34\2\2LD\3\2\2")
        buf.write("\2LG\3\2\2\2LK\3\2\2\2MV\3\2\2\2NO\f\5\2\2OP\7\30\2\2")
        buf.write("PU\5\20\t\6QR\f\4\2\2RS\7\23\2\2SU\5\20\t\5TN\3\2\2\2")
        buf.write("TQ\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\21\3\2\2\2X")
        buf.write("V\3\2\2\2YZ\b\n\1\2Z[\t\2\2\2[f\5\22\n\f\\]\7\t\2\2]^")
        buf.write("\5\22\n\2^_\7\27\2\2_f\3\2\2\2`f\5\30\r\2af\5\34\17\2")
        buf.write("bf\7\36\2\2cf\7\35\2\2df\7\34\2\2eY\3\2\2\2e\\\3\2\2\2")
        buf.write("e`\3\2\2\2ea\3\2\2\2eb\3\2\2\2ec\3\2\2\2ed\3\2\2\2fu\3")
        buf.write("\2\2\2gh\f\13\2\2hi\t\3\2\2it\5\22\n\fjk\f\n\2\2kl\t\4")
        buf.write("\2\2lt\5\22\n\13mn\f\t\2\2no\7\30\2\2ot\5\22\n\npq\f\b")
        buf.write("\2\2qr\7\23\2\2rt\5\22\n\tsg\3\2\2\2sj\3\2\2\2sm\3\2\2")
        buf.write("\2sp\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2v\23\3\2\2\2")
        buf.write("wu\3\2\2\2xy\7\26\2\2yz\7\36\2\2z\25\3\2\2\2{}\7\4\2\2")
        buf.write("|~\5\b\5\2}|\3\2\2\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\7\6\2\2\u0082")
        buf.write("\27\3\2\2\2\u0083\u0084\7\34\2\2\u0084\u0086\7\f\2\2\u0085")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0087\u008c\5\32\16\2\u0088\u0089\7\f\2\2\u0089\u008b")
        buf.write("\5\32\16\2\u008a\u0088\3\2\2\2\u008b\u008e\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\31\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008f\u0090\7\34\2\2\u0090\u0092\7\t\2")
        buf.write("\2\u0091\u0093\5\22\n\2\u0092\u0091\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\7\27\2\2\u0095")
        buf.write("\33\3\2\2\2\u0096\u0097\7\r\2\2\u0097\u009c\5\36\20\2")
        buf.write("\u0098\u0099\7\13\2\2\u0099\u009b\5\36\20\2\u009a\u0098")
        buf.write("\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009f\u00a0\7\21\2\2\u00a0\35\3\2\2\2\u00a1\u00a2\t\5")
        buf.write("\2\2\u00a2\37\3\2\2\2\21#+:>LTVesu\177\u0085\u008c\u0092")
        buf.write("\u009c")
        return buf.getvalue()
		

class cocoParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__24=1
    T__23=2
    T__22=3
    T__21=4
    T__20=5
    T__19=6
    T__18=7
    T__17=8
    T__16=9
    T__15=10
    T__14=11
    T__13=12
    T__12=13
    T__11=14
    T__10=15
    T__9=16
    T__8=17
    T__7=18
    T__6=19
    T__5=20
    T__4=21
    T__3=22
    T__2=23
    T__1=24
    T__0=25
    Identifier=26
    Integer=27
    String=28
    Comment=29
    LineComment=30
    WS=31

    tokenNames = [ "<INVALID>", "'!='", "'{'", "'='", "'}'", "'<='", "'forbid'", 
                   "'('", "'is'", "','", "'.'", "'['", "'>='", "'=='", "'<'", 
                   "']'", "'>'", "'or'", "'match'", "'in'", "'message'", 
                   "')'", "'and'", "'+'", "'not'", "'-'", "Identifier", 
                   "Integer", "String", "Comment", "LineComment", "WS" ]

    RULE_stylesheet = 0
    RULE_context = 1
    RULE_declaration = 2
    RULE_convention = 3
    RULE_pattern = 4
    RULE_node = 5
    RULE_constraint = 6
    RULE_type_expression = 7
    RULE_attr_expression = 8
    RULE_message = 9
    RULE_convention_group = 10
    RULE_api_call = 11
    RULE_method_call = 12
    RULE_list_ = 13
    RULE_list_element = 14

    ruleNames =  [ "stylesheet", "context", "declaration", "convention", 
                   "pattern", "node", "constraint", "type_expression", "attr_expression", 
                   "message", "convention_group", "api_call", "method_call", 
                   "list_", "list_element" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StylesheetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def context(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.ContextContext)
            else:
                return self.getTypedRuleContext(cocoParser.ContextContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_stylesheet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitStylesheet(self)
            else:
                return visitor.visitChildren(self)




    def stylesheet(self):

        localctx = cocoParser.StylesheetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stylesheet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.Identifier:
                self.state = 30 
                self.context()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(cocoParser.DeclarationContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_context

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitContext(self)
            else:
                return visitor.visitChildren(self)




    def context(self):

        localctx = cocoParser.ContextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_context)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            localctx.name = self.match(self.Identifier)
            self.state = 37
            self.match(self.T__23)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__19:
                self.state = 38 
                self.declaration()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(self.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def convention(self):
            return self.getTypedRuleContext(cocoParser.ConventionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = cocoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self.convention()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConventionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(cocoParser.PatternContext,0)


        def message(self):
            return self.getTypedRuleContext(cocoParser.MessageContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_convention

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitConvention(self)
            else:
                return visitor.visitChildren(self)




    def convention(self):

        localctx = cocoParser.ConventionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_convention)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(self.T__19)
            self.state = 49 
            self.pattern()
            self.state = 50 
            self.message()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node(self):
            return self.getTypedRuleContext(cocoParser.NodeContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_pattern

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = cocoParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self.node()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def constraint(self):
            return self.getTypedRuleContext(cocoParser.ConstraintContext,0)


        def type_expression(self):
            return self.getTypedRuleContext(cocoParser.Type_expressionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_node

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitNode(self)
            else:
                return visitor.visitChildren(self)




    def node(self):

        localctx = cocoParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 54
                self.match(self.Identifier)
                self.state = 55
                self.match(self.T__22)


            self.state = 58 
            self.type_expression(0)
            self.state = 60
            _la = self._input.LA(1)
            if _la==cocoParser.T__23:
                self.state = 59 
                self.constraint()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_expression(self):
            return self.getTypedRuleContext(cocoParser.Attr_expressionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_constraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitConstraint(self)
            else:
                return visitor.visitChildren(self)




    def constraint(self):

        localctx = cocoParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(self.T__23)
            self.state = 63 
            self.attr_expression(0)
            self.state = 64
            self.match(self.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Type_expressionContext
            self.operator = None # Token
            self.operand = None # Type_expressionContext
            self.parenthesis = None # Type_expressionContext
            self.primary = None # Token
            self.right = None # Type_expressionContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def type_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Type_expressionContext)
            else:
                return self.getTypedRuleContext(cocoParser.Type_expressionContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_type_expression

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitType_expression(self)
            else:
                return visitor.visitChildren(self)



    def type_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Type_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_type_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            token = self._input.LA(1)
            if token in [self.T__1]:
                self.state = 67
                localctx.operator = self.match(self.T__1)
                self.state = 68 
                localctx.operand = self.type_expression(4)

            elif token in [self.T__18]:
                self.state = 69
                self.match(self.T__18)
                self.state = 70 
                localctx.parenthesis = self.type_expression(0)
                self.state = 71
                self.match(self.T__4)

            elif token in [self.Identifier]:
                self.state = 73
                localctx.primary = self.match(self.Identifier)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 76
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 77
                        localctx.operator = self.match(self.T__3)
                        self.state = 78 
                        localctx.right = self.type_expression(4)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 79
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 80
                        localctx.operator = self.match(self.T__8)
                        self.state = 81 
                        localctx.right = self.type_expression(3)
                        pass

             
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attr_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Attr_expressionContext
            self.operator = None # Token
            self.operand = None # Attr_expressionContext
            self.primary_call = None # Api_callContext
            self.primary_lit = None # List_Context
            self.primary_str = None # Token
            self.primary_int = None # Token
            self.primary_id = None # Token
            self.right = None # Attr_expressionContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def api_call(self):
            return self.getTypedRuleContext(cocoParser.Api_callContext,0)


        def attr_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Attr_expressionContext)
            else:
                return self.getTypedRuleContext(cocoParser.Attr_expressionContext,i)


        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def list_(self):
            return self.getTypedRuleContext(cocoParser.List_Context,0)


        def getRuleIndex(self):
            return cocoParser.RULE_attr_expression

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitAttr_expression(self)
            else:
                return visitor.visitChildren(self)



    def attr_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Attr_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_attr_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 88
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__2) | (1 << self.T__1) | (1 << self.T__0))) != 0)):
                    localctx.operator = self._errHandler.recoverInline(self)
                self.consume()
                self.state = 89 
                localctx.operand = self.attr_expression(10)
                pass

            elif la_ == 2:
                self.state = 90
                self.match(self.T__18)
                self.state = 91 
                self.attr_expression(0)
                self.state = 92
                self.match(self.T__4)
                pass

            elif la_ == 3:
                self.state = 94 
                localctx.primary_call = self.api_call()
                pass

            elif la_ == 4:
                self.state = 95 
                localctx.primary_lit = self.list_()
                pass

            elif la_ == 5:
                self.state = 96
                localctx.primary_str = self.match(self.String)
                pass

            elif la_ == 6:
                self.state = 97
                localctx.primary_int = self.match(self.Integer)
                pass

            elif la_ == 7:
                self.state = 98
                localctx.primary_id = self.match(self.Identifier)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 101
                        if not self.precpred(self._ctx, 9):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 102
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__24) | (1 << self.T__20) | (1 << self.T__13) | (1 << self.T__12) | (1 << self.T__11) | (1 << self.T__9))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 103 
                        localctx.right = self.attr_expression(10)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 105
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__17) | (1 << self.T__7) | (1 << self.T__6))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 106 
                        localctx.right = self.attr_expression(9)
                        pass

                    elif la_ == 3:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 7):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 108
                        localctx.operator = self.match(self.T__3)
                        self.state = 109 
                        localctx.right = self.attr_expression(8)
                        pass

                    elif la_ == 4:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 110
                        if not self.precpred(self._ctx, 6):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 111
                        localctx.operator = self.match(self.T__8)
                        self.state = 112 
                        localctx.right = self.attr_expression(7)
                        pass

             
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MessageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def String(self):
            return self.getToken(cocoParser.String, 0)

        def getRuleIndex(self):
            return cocoParser.RULE_message

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitMessage(self)
            else:
                return visitor.visitChildren(self)




    def message(self):

        localctx = cocoParser.MessageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(self.T__5)
            self.state = 119
            self.match(self.String)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Convention_groupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def convention(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.ConventionContext)
            else:
                return self.getTypedRuleContext(cocoParser.ConventionContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_convention_group

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitConvention_group(self)
            else:
                return visitor.visitChildren(self)




    def convention_group(self):

        localctx = cocoParser.Convention_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_convention_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(self.T__23)
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122 
                self.convention()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cocoParser.T__19):
                    break

            self.state = 127
            self.match(self.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Api_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def method_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Method_callContext)
            else:
                return self.getTypedRuleContext(cocoParser.Method_callContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_api_call

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitApi_call(self)
            else:
                return visitor.visitChildren(self)




    def api_call(self):

        localctx = cocoParser.Api_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_api_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 129
                self.match(self.Identifier)
                self.state = 130
                self.match(self.T__15)


            self.state = 133 
            self.method_call()
            self.state = 138
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 134
                    self.match(self.T__15)
                    self.state = 135 
                    self.method_call() 
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def attr_expression(self):
            return self.getTypedRuleContext(cocoParser.Attr_expressionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = cocoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(self.Identifier)
            self.state = 142
            self.match(self.T__18)
            self.state = 144
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__18) | (1 << self.T__14) | (1 << self.T__2) | (1 << self.T__1) | (1 << self.T__0) | (1 << self.Identifier) | (1 << self.Integer) | (1 << self.String))) != 0):
                self.state = 143 
                self.attr_expression(0)


            self.state = 146
            self.match(self.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.List_elementContext)
            else:
                return self.getTypedRuleContext(cocoParser.List_elementContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_list_

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitList_(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = cocoParser.List_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(self.T__14)
            self.state = 149 
            self.list_element()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__16:
                self.state = 150
                self.match(self.T__16)
                self.state = 151 
                self.list_element()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(self.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def getRuleIndex(self):
            return cocoParser.RULE_list_element

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitList_element(self)
            else:
                return visitor.visitChildren(self)




    def list_element(self):

        localctx = cocoParser.List_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.Identifier) | (1 << self.Integer) | (1 << self.String))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.type_expression_sempred
        self._predicates[8] = self.attr_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def attr_expression_sempred(self, localctx:Attr_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

    def type_expression_sempred(self, localctx:Type_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         



