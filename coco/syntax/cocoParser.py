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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3#")
        buf.write("\u00dc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\7\2")
        buf.write("&\n\2\f\2\16\2)\13\2\3\3\3\3\3\3\7\3.\n\3\f\3\16\3\61")
        buf.write("\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5A\n\5\3\6\3\6\3\6\7\6F\n\6\f\6\16\6I\13\6")
        buf.write("\3\7\3\7\5\7M\n\7\3\7\3\7\5\7Q\n\7\3\b\3\b\5\bU\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nc\n")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nk\n\n\f\n\16\nn\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("{\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\7\13\u008c\n\13\f\13\16\13")
        buf.write("\u008f\13\13\3\f\3\f\3\f\3\f\3\f\5\f\u0096\n\f\3\f\3\f")
        buf.write("\5\f\u009a\n\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a2\n\f\3")
        buf.write("\f\3\f\5\f\u00a6\n\f\7\f\u00a8\n\f\f\f\16\f\u00ab\13\f")
        buf.write("\3\r\3\r\3\r\3\16\3\16\6\16\u00b2\n\16\r\16\16\16\u00b3")
        buf.write("\3\16\3\16\3\17\3\17\3\17\7\17\u00bb\n\17\f\17\16\17\u00be")
        buf.write("\13\17\3\20\3\20\3\20\5\20\u00c3\n\20\3\20\5\20\u00c6")
        buf.write("\n\20\3\21\3\21\3\21\3\21\7\21\u00cc\n\21\f\21\16\21\u00cf")
        buf.write("\13\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00d7\n\22\3")
        buf.write("\22\5\22\u00da\n\22\3\22\2\5\22\24\26\23\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"\2\5\3\2\33\35\6\2\4\4\b\b")
        buf.write("\20\22\24\24\3\2\26\27\u00ed\2\'\3\2\2\2\4*\3\2\2\2\6")
        buf.write("\64\3\2\2\2\b@\3\2\2\2\nB\3\2\2\2\fL\3\2\2\2\16R\3\2\2")
        buf.write("\2\20V\3\2\2\2\22b\3\2\2\2\24z\3\2\2\2\26\u0090\3\2\2")
        buf.write("\2\30\u00ac\3\2\2\2\32\u00af\3\2\2\2\34\u00b7\3\2\2\2")
        buf.write("\36\u00bf\3\2\2\2 \u00c7\3\2\2\2\"\u00d9\3\2\2\2$&\5\4")
        buf.write("\3\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\3\3\2")
        buf.write("\2\2)\'\3\2\2\2*+\7\36\2\2+/\7\5\2\2,.\5\6\4\2-,\3\2\2")
        buf.write("\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61")
        buf.write("/\3\2\2\2\62\63\7\7\2\2\63\5\3\2\2\2\64\65\5\b\5\2\65")
        buf.write("\7\3\2\2\2\66\67\7\t\2\2\678\5\n\6\289\5\30\r\29A\3\2")
        buf.write("\2\2:;\7\16\2\2;<\5\n\6\2<=\7\3\2\2=>\5\24\13\2>?\5\30")
        buf.write("\r\2?A\3\2\2\2@\66\3\2\2\2@:\3\2\2\2A\t\3\2\2\2BG\5\f")
        buf.write("\7\2CD\7\27\2\2DF\5\f\7\2EC\3\2\2\2FI\3\2\2\2GE\3\2\2")
        buf.write("\2GH\3\2\2\2H\13\3\2\2\2IG\3\2\2\2JK\7\36\2\2KM\7\6\2")
        buf.write("\2LJ\3\2\2\2LM\3\2\2\2MN\3\2\2\2NP\5\22\n\2OQ\5\20\t\2")
        buf.write("PO\3\2\2\2PQ\3\2\2\2Q\r\3\2\2\2RT\5\22\n\2SU\5\20\t\2")
        buf.write("TS\3\2\2\2TU\3\2\2\2U\17\3\2\2\2VW\7\5\2\2WX\5\24\13\2")
        buf.write("XY\7\7\2\2Y\21\3\2\2\2Z[\b\n\1\2[\\\7\34\2\2\\c\5\22\n")
        buf.write("\6]^\7\n\2\2^_\5\22\n\2_`\7\31\2\2`c\3\2\2\2ac\7\36\2")
        buf.write("\2bZ\3\2\2\2b]\3\2\2\2ba\3\2\2\2cl\3\2\2\2de\f\5\2\2e")
        buf.write("f\7\32\2\2fk\5\22\n\6gh\f\4\2\2hi\7\25\2\2ik\5\22\n\5")
        buf.write("jd\3\2\2\2jg\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2m\23")
        buf.write("\3\2\2\2nl\3\2\2\2op\b\13\1\2pq\t\2\2\2q{\5\24\13\frs")
        buf.write("\7\n\2\2st\5\24\13\2tu\7\31\2\2u{\3\2\2\2v{\5\26\f\2w")
        buf.write("{\5 \21\2x{\7 \2\2y{\7\37\2\2zo\3\2\2\2zr\3\2\2\2zv\3")
        buf.write("\2\2\2zw\3\2\2\2zx\3\2\2\2zy\3\2\2\2{\u008d\3\2\2\2|}")
        buf.write("\f\13\2\2}~\t\3\2\2~\u008c\5\24\13\f\177\u0080\f\n\2\2")
        buf.write("\u0080\u0081\t\4\2\2\u0081\u008c\5\24\13\13\u0082\u0083")
        buf.write("\f\7\2\2\u0083\u0084\7\32\2\2\u0084\u008c\5\24\13\b\u0085")
        buf.write("\u0086\f\6\2\2\u0086\u0087\7\25\2\2\u0087\u008c\5\24\13")
        buf.write("\7\u0088\u0089\f\t\2\2\u0089\u008a\7\13\2\2\u008a\u008c")
        buf.write("\5\22\n\2\u008b|\3\2\2\2\u008b\177\3\2\2\2\u008b\u0082")
        buf.write("\3\2\2\2\u008b\u0085\3\2\2\2\u008b\u0088\3\2\2\2\u008c")
        buf.write("\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\25\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\b\f")
        buf.write("\1\2\u0091\u0099\7\36\2\2\u0092\u0095\7\n\2\2\u0093\u0096")
        buf.write("\5\24\13\2\u0094\u0096\5\16\b\2\u0095\u0093\3\2\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\7\31\2")
        buf.write("\2\u0098\u009a\3\2\2\2\u0099\u0092\3\2\2\2\u0099\u009a")
        buf.write("\3\2\2\2\u009a\u00a9\3\2\2\2\u009b\u009c\f\4\2\2\u009c")
        buf.write("\u009d\7\r\2\2\u009d\u00a5\7\36\2\2\u009e\u00a1\7\n\2")
        buf.write("\2\u009f\u00a2\5\24\13\2\u00a0\u00a2\5\16\b\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a4\7\31\2\2\u00a4\u00a6\3\2\2\2\u00a5\u009e\3\2\2")
        buf.write("\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u009b")
        buf.write("\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\27\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac")
        buf.write("\u00ad\7\30\2\2\u00ad\u00ae\7 \2\2\u00ae\31\3\2\2\2\u00af")
        buf.write("\u00b1\7\5\2\2\u00b0\u00b2\5\b\5\2\u00b1\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\7\7\2\2\u00b6\33")
        buf.write("\3\2\2\2\u00b7\u00bc\7\36\2\2\u00b8\u00b9\7\r\2\2\u00b9")
        buf.write("\u00bb\5\34\17\2\u00ba\u00b8\3\2\2\2\u00bb\u00be\3\2\2")
        buf.write("\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\35\3")
        buf.write("\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c5\7\36\2\2\u00c0")
        buf.write("\u00c2\7\n\2\2\u00c1\u00c3\5\24\13\2\u00c2\u00c1\3\2\2")
        buf.write("\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6")
        buf.write("\7\31\2\2\u00c5\u00c0\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\37\3\2\2\2\u00c7\u00c8\7\17\2\2\u00c8\u00cd\5\"\22\2")
        buf.write("\u00c9\u00ca\7\f\2\2\u00ca\u00cc\5\"\22\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00d0\u00d1\7\23\2\2\u00d1!\3\2\2\2\u00d2\u00da\7\37")
        buf.write("\2\2\u00d3\u00da\7 \2\2\u00d4\u00d6\5\22\n\2\u00d5\u00d7")
        buf.write("\5\20\t\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00da\7\36\2\2\u00d9\u00d2\3\2\2")
        buf.write("\2\u00d9\u00d3\3\2\2\2\u00d9\u00d4\3\2\2\2\u00d9\u00d8")
        buf.write("\3\2\2\2\u00da#\3\2\2\2\33\'/@GLPTbjlz\u008b\u008d\u0095")
        buf.write("\u0099\u00a1\u00a5\u00a9\u00b3\u00bc\u00c2\u00c5\u00cd")
        buf.write("\u00d6\u00d9")
        return buf.getvalue()
		

class cocoParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__26=1
    T__25=2
    T__24=3
    T__23=4
    T__22=5
    T__21=6
    T__20=7
    T__19=8
    T__18=9
    T__17=10
    T__16=11
    T__15=12
    T__14=13
    T__13=14
    T__12=15
    T__11=16
    T__10=17
    T__9=18
    T__8=19
    T__7=20
    T__6=21
    T__5=22
    T__4=23
    T__3=24
    T__2=25
    T__1=26
    T__0=27
    Identifier=28
    Integer=29
    String=30
    Comment=31
    LineComment=32
    WS=33

    tokenNames = [ "<INVALID>", "'require'", "'!='", "'{'", "'='", "'}'", 
                   "'<='", "'forbid'", "'('", "'is'", "','", "'.'", "'find'", 
                   "'['", "'>='", "'=='", "'<'", "']'", "'>'", "'or'", "'match'", 
                   "'in'", "'message'", "')'", "'and'", "'+'", "'not'", 
                   "'-'", "Identifier", "Integer", "String", "Comment", 
                   "LineComment", "WS" ]

    RULE_stylesheet = 0
    RULE_context = 1
    RULE_declaration = 2
    RULE_convention = 3
    RULE_pattern = 4
    RULE_node = 5
    RULE_node_descriptor = 6
    RULE_constraint = 7
    RULE_type_expression = 8
    RULE_attr_expression = 9
    RULE_call_expression = 10
    RULE_message = 11
    RULE_convention_group = 12
    RULE_api_call = 13
    RULE_method_call = 14
    RULE_list_ = 15
    RULE_list_element = 16

    ruleNames =  [ "stylesheet", "context", "declaration", "convention", 
                   "pattern", "node", "node_descriptor", "constraint", "type_expression", 
                   "attr_expression", "call_expression", "message", "convention_group", 
                   "api_call", "method_call", "list_", "list_element" ]

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.Identifier:
                self.state = 34 
                self.context()
                self.state = 39
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
            self.state = 40
            localctx.name = self.match(self.Identifier)
            self.state = 41
            self.match(self.T__24)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__20 or _la==cocoParser.T__15:
                self.state = 42 
                self.declaration()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(self.T__22)
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
            self.state = 50 
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
            self.target = None # PatternContext
            self.msg = None # MessageContext
            self.requirement = None # Attr_expressionContext

        def pattern(self):
            return self.getTypedRuleContext(cocoParser.PatternContext,0)


        def attr_expression(self):
            return self.getTypedRuleContext(cocoParser.Attr_expressionContext,0)


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
            self.state = 62
            token = self._input.LA(1)
            if token in [self.T__20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(self.T__20)
                self.state = 53 
                localctx.target = self.pattern()
                self.state = 54 
                localctx.msg = self.message()

            elif token in [self.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(self.T__15)
                self.state = 57 
                localctx.target = self.pattern()
                self.state = 58
                self.match(self.T__26)
                self.state = 59 
                localctx.requirement = self.attr_expression(0)
                self.state = 60 
                localctx.msg = self.message()

            else:
                raise NoViableAltException(self)

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

        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.NodeContext)
            else:
                return self.getTypedRuleContext(cocoParser.NodeContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64 
            self.node()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__6:
                self.state = 65
                self.match(self.T__6)
                self.state = 66 
                self.node()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 74
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 72
                self.match(self.Identifier)
                self.state = 73
                self.match(self.T__23)


            self.state = 76 
            self.type_expression(0)
            self.state = 78
            _la = self._input.LA(1)
            if _la==cocoParser.T__24:
                self.state = 77 
                self.constraint()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Node_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constraint(self):
            return self.getTypedRuleContext(cocoParser.ConstraintContext,0)


        def type_expression(self):
            return self.getTypedRuleContext(cocoParser.Type_expressionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_node_descriptor

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitNode_descriptor(self)
            else:
                return visitor.visitChildren(self)




    def node_descriptor(self):

        localctx = cocoParser.Node_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_node_descriptor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self.type_expression(0)
            self.state = 82
            _la = self._input.LA(1)
            if _la==cocoParser.T__24:
                self.state = 81 
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
        self.enterRule(localctx, 14, self.RULE_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(self.T__24)
            self.state = 85 
            self.attr_expression(0)
            self.state = 86
            self.match(self.T__22)
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_type_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            token = self._input.LA(1)
            if token in [self.T__1]:
                self.state = 89
                localctx.operator = self.match(self.T__1)
                self.state = 90 
                localctx.operand = self.type_expression(4)

            elif token in [self.T__19]:
                self.state = 91
                self.match(self.T__19)
                self.state = 92 
                localctx.parenthesis = self.type_expression(0)
                self.state = 93
                self.match(self.T__4)

            elif token in [self.Identifier]:
                self.state = 95
                localctx.primary = self.match(self.Identifier)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 106
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 104
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 98
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 99
                        localctx.operator = self.match(self.T__3)
                        self.state = 100 
                        localctx.right = self.type_expression(4)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 101
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 102
                        localctx.operator = self.match(self.T__8)
                        self.state = 103 
                        localctx.right = self.type_expression(3)
                        pass

             
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            self.call = None # Call_expressionContext
            self.primary_list = None # List_Context
            self.primary_str = None # Token
            self.primary_int = None # Token
            self.right = None # Attr_expressionContext

        def call_expression(self):
            return self.getTypedRuleContext(cocoParser.Call_expressionContext,0)


        def attr_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Attr_expressionContext)
            else:
                return self.getTypedRuleContext(cocoParser.Attr_expressionContext,i)


        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def type_expression(self):
            return self.getTypedRuleContext(cocoParser.Type_expressionContext,0)


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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_attr_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            token = self._input.LA(1)
            if token in [self.T__2, self.T__1, self.T__0]:
                self.state = 110
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__2) | (1 << self.T__1) | (1 << self.T__0))) != 0)):
                    localctx.operator = self._errHandler.recoverInline(self)
                self.consume()
                self.state = 111 
                localctx.operand = self.attr_expression(10)

            elif token in [self.T__19]:
                self.state = 112
                self.match(self.T__19)
                self.state = 113 
                self.attr_expression(0)
                self.state = 114
                self.match(self.T__4)

            elif token in [self.Identifier]:
                self.state = 116 
                localctx.call = self.call_expression(0)

            elif token in [self.T__14]:
                self.state = 117 
                localctx.primary_list = self.list_()

            elif token in [self.String]:
                self.state = 118
                localctx.primary_str = self.match(self.String)

            elif token in [self.Integer]:
                self.state = 119
                localctx.primary_int = self.match(self.Integer)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 137
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 9):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 123
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__25) | (1 << self.T__21) | (1 << self.T__13) | (1 << self.T__12) | (1 << self.T__11) | (1 << self.T__9))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 124 
                        localctx.right = self.attr_expression(10)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 126
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==cocoParser.T__7 or _la==cocoParser.T__6):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 127 
                        localctx.right = self.attr_expression(9)
                        pass

                    elif la_ == 3:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 5):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 129
                        localctx.operator = self.match(self.T__3)
                        self.state = 130 
                        localctx.right = self.attr_expression(6)
                        pass

                    elif la_ == 4:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 132
                        localctx.operator = self.match(self.T__8)
                        self.state = 133 
                        localctx.right = self.attr_expression(5)
                        pass

                    elif la_ == 5:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 134
                        if not self.precpred(self._ctx, 7):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 135
                        localctx.operator = self.match(self.T__18)
                        self.state = 136 
                        localctx.right = self.type_expression(0)
                        pass

             
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Call_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.operand = None # Call_expressionContext
            self.call = None # Token
            self.argument = None # Attr_expressionContext
            self.argument2 = None # Node_descriptorContext

        def call_expression(self):
            return self.getTypedRuleContext(cocoParser.Call_expressionContext,0)


        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def node_descriptor(self):
            return self.getTypedRuleContext(cocoParser.Node_descriptorContext,0)


        def attr_expression(self):
            return self.getTypedRuleContext(cocoParser.Attr_expressionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_call_expression

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitCall_expression(self)
            else:
                return visitor.visitChildren(self)



    def call_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Call_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_call_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            localctx.call = self.match(self.Identifier)
            self.state = 151
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 144
                self.match(self.T__19)
                self.state = 147
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 145 
                    localctx.argument = self.attr_expression(0)
                    pass

                elif la_ == 2:
                    self.state = 146 
                    localctx.argument2 = self.node_descriptor()
                    pass


                self.state = 149
                self.match(self.T__4)


            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cocoParser.Call_expressionContext(self, _parentctx, _parentState)
                    localctx.operand = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_call_expression)
                    self.state = 153
                    if not self.precpred(self._ctx, 2):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 154
                    self.match(self.T__16)
                    self.state = 155
                    localctx.call = self.match(self.Identifier)
                    self.state = 163
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        self.state = 156
                        self.match(self.T__19)
                        self.state = 159
                        la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                        if la_ == 1:
                            self.state = 157 
                            localctx.argument = self.attr_expression(0)
                            pass

                        elif la_ == 2:
                            self.state = 158 
                            localctx.argument2 = self.node_descriptor()
                            pass


                        self.state = 161
                        self.match(self.T__4)

             
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(self.T__5)
            self.state = 171
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
        self.enterRule(localctx, 24, self.RULE_convention_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(self.T__24)
            self.state = 175 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174 
                self.convention()
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cocoParser.T__20 or _la==cocoParser.T__15):
                    break

            self.state = 179
            self.match(self.T__22)
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

        def api_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Api_callContext)
            else:
                return self.getTypedRuleContext(cocoParser.Api_callContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_api_call

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitApi_call(self)
            else:
                return visitor.visitChildren(self)




    def api_call(self):

        localctx = cocoParser.Api_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_api_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(self.Identifier)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 182
                    self.match(self.T__16)
                    self.state = 183 
                    self.api_call() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.method_name = None # Token

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
        self.enterRule(localctx, 28, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            localctx.method_name = self.match(self.Identifier)
            self.state = 195
            _la = self._input.LA(1)
            if _la==cocoParser.T__19:
                self.state = 190
                self.match(self.T__19)
                self.state = 192
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__19) | (1 << self.T__14) | (1 << self.T__2) | (1 << self.T__1) | (1 << self.T__0) | (1 << self.Identifier) | (1 << self.Integer) | (1 << self.String))) != 0):
                    self.state = 191 
                    self.attr_expression(0)


                self.state = 194
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
        self.enterRule(localctx, 30, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(self.T__14)
            self.state = 198 
            self.list_element()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__17:
                self.state = 199
                self.match(self.T__17)
                self.state = 200 
                self.list_element()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
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
            self.element_int = None # Token
            self.element_str = None # Token
            self.element_desc = None # Type_expressionContext
            self.element_id = None # Token

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def constraint(self):
            return self.getTypedRuleContext(cocoParser.ConstraintContext,0)


        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def type_expression(self):
            return self.getTypedRuleContext(cocoParser.Type_expressionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_list_element

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitList_element(self)
            else:
                return visitor.visitChildren(self)




    def list_element(self):

        localctx = cocoParser.List_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_element)
        self._la = 0 # Token type
        try:
            self.state = 215
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                localctx.element_int = self.match(self.Integer)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                localctx.element_str = self.match(self.String)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210 
                localctx.element_desc = self.type_expression(0)
                self.state = 212
                _la = self._input.LA(1)
                if _la==cocoParser.T__24:
                    self.state = 211 
                    self.constraint()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                localctx.element_id = self.match(self.Identifier)
                pass


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
        self._predicates[8] = self.type_expression_sempred
        self._predicates[9] = self.attr_expression_sempred
        self._predicates[10] = self.call_expression_sempred
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

    def call_expression_sempred(self, localctx:Call_expressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def type_expression_sempred(self, localctx:Type_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         



