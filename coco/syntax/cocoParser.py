# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .cocoListener import cocoListener
    from .cocoVisitor import cocoVisitor
else:
    from cocoListener import cocoListener
    from cocoVisitor import cocoVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3 ")
        buf.write("\u009c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\7\2 \n\2\f\2\16\2#\13\2\3\3\3\3\3")
        buf.write("\3\7\3(\n\3\f\3\16\3+\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\5\78\n\7\3\7\3\7\5\7<\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tJ\n\t\3\t\3\t")
        buf.write("\3\t\7\tO\n\t\f\t\16\tR\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\na\n\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\no\n\n\f\n\16\nr\13\n")
        buf.write("\3\13\3\13\6\13v\n\13\r\13\16\13w\3\13\3\13\3\f\3\f\5")
        buf.write("\f~\n\f\3\f\3\f\3\f\7\f\u0083\n\f\f\f\16\f\u0086\13\f")
        buf.write("\3\r\3\r\3\r\5\r\u008b\n\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u0093\n\16\f\16\16\16\u0096\13\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\2\4\20\22\20\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\2\6\4\2\26\26\30\31\7\2\3\3\5\5\7\b\f\f\16\16\4")
        buf.write("\2\20\21\23\23\3\2\33\35\u00a4\2!\3\2\2\2\4$\3\2\2\2\6")
        buf.write(".\3\2\2\2\b\60\3\2\2\2\n\63\3\2\2\2\f\67\3\2\2\2\16=\3")
        buf.write("\2\2\2\20I\3\2\2\2\22`\3\2\2\2\24s\3\2\2\2\26}\3\2\2\2")
        buf.write("\30\u0087\3\2\2\2\32\u008e\3\2\2\2\34\u0099\3\2\2\2\36")
        buf.write(" \5\4\3\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2")
        buf.write("\2\"\3\3\2\2\2#!\3\2\2\2$%\7\33\2\2%)\7\6\2\2&(\5\6\4")
        buf.write("\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2\2")
        buf.write("+)\3\2\2\2,-\7\13\2\2-\5\3\2\2\2./\5\b\5\2/\7\3\2\2\2")
        buf.write("\60\61\7\17\2\2\61\62\5\n\6\2\62\t\3\2\2\2\63\64\5\f\7")
        buf.write("\2\64\13\3\2\2\2\65\66\7\33\2\2\668\7\n\2\2\67\65\3\2")
        buf.write("\2\2\678\3\2\2\289\3\2\2\29;\5\20\t\2:<\5\16\b\2;:\3\2")
        buf.write("\2\2;<\3\2\2\2<\r\3\2\2\2=>\7\6\2\2>?\5\22\n\2?@\7\13")
        buf.write("\2\2@\17\3\2\2\2AB\b\t\1\2BC\7\30\2\2CJ\5\20\t\5DE\7\22")
        buf.write("\2\2EF\5\20\t\2FG\7\24\2\2GJ\3\2\2\2HJ\7\33\2\2IA\3\2")
        buf.write("\2\2ID\3\2\2\2IH\3\2\2\2JP\3\2\2\2KL\f\4\2\2LM\7\r\2\2")
        buf.write("MO\5\20\t\5NK\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\21")
        buf.write("\3\2\2\2RP\3\2\2\2ST\b\n\1\2TU\t\2\2\2Ua\5\22\n\rVW\7")
        buf.write("\22\2\2WX\5\22\n\2XY\7\24\2\2Ya\3\2\2\2Za\5\f\7\2[a\5")
        buf.write("\26\f\2\\a\5\32\16\2]a\7\35\2\2^a\7\34\2\2_a\7\33\2\2")
        buf.write("`S\3\2\2\2`V\3\2\2\2`Z\3\2\2\2`[\3\2\2\2`\\\3\2\2\2`]")
        buf.write("\3\2\2\2`^\3\2\2\2`_\3\2\2\2ap\3\2\2\2bc\f\f\2\2cd\t\3")
        buf.write("\2\2do\5\22\n\ref\f\13\2\2fg\t\4\2\2go\5\22\n\fhi\f\n")
        buf.write("\2\2ij\7\25\2\2jo\5\22\n\13kl\f\t\2\2lm\7\r\2\2mo\5\22")
        buf.write("\n\nnb\3\2\2\2ne\3\2\2\2nh\3\2\2\2nk\3\2\2\2or\3\2\2\2")
        buf.write("pn\3\2\2\2pq\3\2\2\2q\23\3\2\2\2rp\3\2\2\2su\7\6\2\2t")
        buf.write("v\5\b\5\2ut\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2xy\3")
        buf.write("\2\2\2yz\7\13\2\2z\25\3\2\2\2{|\7\33\2\2|~\7\32\2\2}{")
        buf.write("\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0084\5\30\r\2\u0080")
        buf.write("\u0081\7\32\2\2\u0081\u0083\5\30\r\2\u0082\u0080\3\2\2")
        buf.write("\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085")
        buf.write("\3\2\2\2\u0085\27\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088")
        buf.write("\7\33\2\2\u0088\u008a\7\22\2\2\u0089\u008b\5\22\n\2\u008a")
        buf.write("\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008d\7\24\2\2\u008d\31\3\2\2\2\u008e\u008f\7\4")
        buf.write("\2\2\u008f\u0094\5\34\17\2\u0090\u0091\7\27\2\2\u0091")
        buf.write("\u0093\5\34\17\2\u0092\u0090\3\2\2\2\u0093\u0096\3\2\2")
        buf.write("\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\7\t\2\2\u0098")
        buf.write("\33\3\2\2\2\u0099\u009a\t\5\2\2\u009a\35\3\2\2\2\20!)")
        buf.write("\67;IP`npw}\u0084\u008a\u0094")
        return buf.getvalue()
		

class cocoParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__23=1
    T__22=2
    T__21=3
    T__20=4
    T__19=5
    T__18=6
    T__17=7
    T__16=8
    T__15=9
    T__14=10
    T__13=11
    T__12=12
    T__11=13
    T__10=14
    T__9=15
    T__8=16
    T__7=17
    T__6=18
    T__5=19
    T__4=20
    T__3=21
    T__2=22
    T__1=23
    T__0=24
    Identifier=25
    Integer=26
    String=27
    Comment=28
    LineComment=29
    WS=30

    tokenNames = [ "<INVALID>", "'!='", "'['", "'>='", "'{'", "'=='", "'<'", 
                   "']'", "'='", "'}'", "'>'", "'or'", "'<='", "'forbid'", 
                   "'match'", "'in'", "'('", "'is'", "')'", "'and'", "'+'", 
                   "','", "'not'", "'-'", "'.'", "Identifier", "Integer", 
                   "String", "Comment", "LineComment", "WS" ]

    RULE_stylesheet = 0
    RULE_context = 1
    RULE_declaration = 2
    RULE_convention = 3
    RULE_pattern = 4
    RULE_node = 5
    RULE_constraint = 6
    RULE_type_expression = 7
    RULE_attr_expression = 8
    RULE_convention_group = 9
    RULE_api_call = 10
    RULE_method_call = 11
    RULE_list_ = 12
    RULE_list_element = 13

    ruleNames =  [ "stylesheet", "context", "declaration", "convention", 
                   "pattern", "node", "constraint", "type_expression", "attr_expression", 
                   "convention_group", "api_call", "method_call", "list_", 
                   "list_element" ]

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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterStylesheet(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitStylesheet(self)

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
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.Identifier:
                self.state = 28 
                self.context()
                self.state = 33
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterContext(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitContext(self)

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
            self.state = 34
            localctx.name = self.match(self.Identifier)
            self.state = 35
            self.match(self.T__20)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__11:
                self.state = 36 
                self.declaration()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(self.T__15)
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitDeclaration(self)

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
            self.state = 44 
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


        def getRuleIndex(self):
            return cocoParser.RULE_convention

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterConvention(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitConvention(self)

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
            self.state = 46
            self.match(self.T__11)
            self.state = 47 
            self.pattern()
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitPattern(self)

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
            self.state = 49 
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitNode(self)
            else:
                return visitor.visitChildren(self)




    def node(self):

        localctx = cocoParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 51
                self.match(self.Identifier)
                self.state = 52
                self.match(self.T__16)


            self.state = 55 
            self.type_expression(0)
            self.state = 57
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 56 
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitConstraint(self)

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
            self.state = 59
            self.match(self.T__20)
            self.state = 60 
            self.attr_expression(0)
            self.state = 61
            self.match(self.T__15)
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

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def type_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Type_expressionContext)
            else:
                return self.getTypedRuleContext(cocoParser.Type_expressionContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_type_expression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterType_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitType_expression(self)

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
            self.state = 71
            token = self._input.LA(1)
            if token in [self.T__2]:
                self.state = 64
                self.match(self.T__2)
                self.state = 65 
                self.type_expression(3)

            elif token in [self.T__8]:
                self.state = 66
                self.match(self.T__8)
                self.state = 67 
                self.type_expression(0)
                self.state = 68
                self.match(self.T__6)

            elif token in [self.Identifier]:
                self.state = 70
                self.match(self.Identifier)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                    self.state = 73
                    if not self.precpred(self._ctx, 2):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 74
                    self.match(self.T__13)
                    self.state = 75 
                    self.type_expression(3) 
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            self.op = None # Token
            self.operand = None # Attr_expressionContext
            self.primary_rule = None # NodeContext
            self.primary = None # Token
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

        def node(self):
            return self.getTypedRuleContext(cocoParser.NodeContext,0)


        def list_(self):
            return self.getTypedRuleContext(cocoParser.List_Context,0)


        def getRuleIndex(self):
            return cocoParser.RULE_attr_expression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterAttr_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitAttr_expression(self)

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
            self.state = 94
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 82
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__4) | (1 << self.T__2) | (1 << self.T__1))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                self.consume()
                self.state = 83 
                localctx.operand = self.attr_expression(11)
                pass

            elif la_ == 2:
                self.state = 84
                self.match(self.T__8)
                self.state = 85 
                self.attr_expression(0)
                self.state = 86
                self.match(self.T__6)
                pass

            elif la_ == 3:
                self.state = 88 
                localctx.primary_rule = self.node()
                pass

            elif la_ == 4:
                self.state = 89 
                localctx.primary_rule = self.api_call()
                pass

            elif la_ == 5:
                self.state = 90 
                localctx.primary_rule = self.list_()
                pass

            elif la_ == 6:
                self.state = 91
                localctx.primary = self.match(self.String)
                pass

            elif la_ == 7:
                self.state = 92
                localctx.primary = self.match(self.Integer)
                pass

            elif la_ == 8:
                self.state = 93
                localctx.primary = self.match(self.Identifier)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 108
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 96
                        if not self.precpred(self._ctx, 10):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 97
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__23) | (1 << self.T__21) | (1 << self.T__19) | (1 << self.T__18) | (1 << self.T__14) | (1 << self.T__12))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 98 
                        localctx.right = self.attr_expression(11)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 99
                        if not self.precpred(self._ctx, 9):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 100
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__10) | (1 << self.T__9) | (1 << self.T__7))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 101 
                        localctx.right = self.attr_expression(10)
                        pass

                    elif la_ == 3:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 102
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 103
                        self.match(self.T__5)
                        self.state = 104 
                        localctx.right = self.attr_expression(9)
                        pass

                    elif la_ == 4:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 105
                        if not self.precpred(self._ctx, 7):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 106
                        self.match(self.T__13)
                        self.state = 107 
                        localctx.right = self.attr_expression(8)
                        pass

             
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterConvention_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitConvention_group(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitConvention_group(self)
            else:
                return visitor.visitChildren(self)




    def convention_group(self):

        localctx = cocoParser.Convention_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_convention_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(self.T__20)
            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114 
                self.convention()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cocoParser.T__11):
                    break

            self.state = 119
            self.match(self.T__15)
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterApi_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitApi_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitApi_call(self)
            else:
                return visitor.visitChildren(self)




    def api_call(self):

        localctx = cocoParser.Api_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_api_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 121
                self.match(self.Identifier)
                self.state = 122
                self.match(self.T__0)


            self.state = 125 
            self.method_call()
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 126
                    self.match(self.T__0)
                    self.state = 127 
                    self.method_call() 
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterMethod_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitMethod_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = cocoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(self.Identifier)
            self.state = 134
            self.match(self.T__8)
            self.state = 136
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__22) | (1 << self.T__8) | (1 << self.T__4) | (1 << self.T__2) | (1 << self.T__1) | (1 << self.Identifier) | (1 << self.Integer) | (1 << self.String))) != 0):
                self.state = 135 
                self.attr_expression(0)


            self.state = 138
            self.match(self.T__6)
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterList_(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitList_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitList_(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = cocoParser.List_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(self.T__22)
            self.state = 141 
            self.list_element()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__3:
                self.state = 142
                self.match(self.T__3)
                self.state = 143 
                self.list_element()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(self.T__17)
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

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterList_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitList_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitList_element(self)
            else:
                return visitor.visitChildren(self)




    def list_element(self):

        localctx = cocoParser.List_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
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
            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

    def type_expression_sempred(self, localctx:Type_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         



