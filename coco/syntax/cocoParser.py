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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3(")
        buf.write("\u010b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\7\2(\n\2\f\2\16\2+\13\2\3\3\3\3\3\3\7\3\60\n\3\f")
        buf.write("\3\16\3\63\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5J\n")
        buf.write("\5\3\6\3\6\3\6\7\6O\n\6\f\6\16\6R\13\6\3\7\3\7\5\7V\n")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b_\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\ti\n\t\3\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\tq\n\t\f\t\16\tt\13\t\3\n\3\n\3\n\7\ny\n\n\f\n\16\n|")
        buf.write("\13\n\3\13\3\13\3\13\3\13\3\13\5\13\u0083\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0092")
        buf.write("\n\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u009a\n\f\f\f\16\f\u009d")
        buf.write("\13\f\3\r\3\r\3\r\3\r\5\r\u00a3\n\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00a9\n\r\3\r\3\r\3\r\3\r\5\r\u00af\n\r\3\r\3\r\3\r")
        buf.write("\5\r\u00b4\n\r\5\r\u00b6\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00bf\n\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\7\16\u00c7\n\16\f\16\16\16\u00ca\13\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00d1\n\17\3\17\3\17\5\17\u00d5\n\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00dd\n\17\3\17\3")
        buf.write("\17\5\17\u00e1\n\17\7\17\u00e3\n\17\f\17\16\17\u00e6\13")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f0")
        buf.write("\n\20\3\21\3\21\6\21\u00f4\n\21\r\21\16\21\u00f5\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\7\22\u00fe\n\22\f\22\16\22\u0101")
        buf.write("\13\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u0109\n\23\3")
        buf.write("\23\2\6\20\26\32\34\24\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$\2\5\4\2\23\23\35\35\6\2\5\5\t\t\26\30\32\32")
        buf.write("\5\2\3\3\24\24\34\35\u0124\2)\3\2\2\2\4,\3\2\2\2\6\66")
        buf.write("\3\2\2\2\bI\3\2\2\2\nK\3\2\2\2\fU\3\2\2\2\16Y\3\2\2\2")
        buf.write("\20h\3\2\2\2\22u\3\2\2\2\24}\3\2\2\2\26\u0091\3\2\2\2")
        buf.write("\30\u00b5\3\2\2\2\32\u00be\3\2\2\2\34\u00cb\3\2\2\2\36")
        buf.write("\u00ef\3\2\2\2 \u00f1\3\2\2\2\"\u00f9\3\2\2\2$\u0108\3")
        buf.write("\2\2\2&(\5\4\3\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2")
        buf.write("\2\2*\3\3\2\2\2+)\3\2\2\2,-\7#\2\2-\61\7\6\2\2.\60\5\6")
        buf.write("\4\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2")
        buf.write("\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\b\2\2\65\5\3\2\2")
        buf.write("\2\66\67\5\b\5\2\67\7\3\2\2\289\7\n\2\29:\5\n\6\2:;\7")
        buf.write("\36\2\2;<\7%\2\2<J\3\2\2\2=>\7\4\2\2>?\5\26\f\2?@\7\36")
        buf.write("\2\2@A\7%\2\2AJ\3\2\2\2BC\7\21\2\2CD\5\n\6\2DE\7\4\2\2")
        buf.write("EF\5\26\f\2FG\7\36\2\2GH\7%\2\2HJ\3\2\2\2I8\3\2\2\2I=")
        buf.write("\3\2\2\2IB\3\2\2\2J\t\3\2\2\2KP\5\f\7\2LM\t\2\2\2MO\5")
        buf.write("\f\7\2NL\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\13\3\2")
        buf.write("\2\2RP\3\2\2\2ST\7#\2\2TV\7\7\2\2US\3\2\2\2UV\3\2\2\2")
        buf.write("VW\3\2\2\2WX\5\16\b\2X\r\3\2\2\2Y^\5\20\t\2Z[\7\6\2\2")
        buf.write("[\\\5\26\f\2\\]\7\b\2\2]_\3\2\2\2^Z\3\2\2\2^_\3\2\2\2")
        buf.write("_\17\3\2\2\2`a\b\t\1\2ab\7!\2\2bi\5\20\t\6cd\7\13\2\2")
        buf.write("de\5\20\t\2ef\7\37\2\2fi\3\2\2\2gi\7#\2\2h`\3\2\2\2hc")
        buf.write("\3\2\2\2hg\3\2\2\2ir\3\2\2\2jk\f\5\2\2kl\7 \2\2lq\5\20")
        buf.write("\t\6mn\f\4\2\2no\7\33\2\2oq\5\20\t\5pj\3\2\2\2pm\3\2\2")
        buf.write("\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\21\3\2\2\2tr\3\2\2\2")
        buf.write("uz\5\24\13\2vw\7\33\2\2wy\5\24\13\2xv\3\2\2\2y|\3\2\2")
        buf.write("\2zx\3\2\2\2z{\3\2\2\2{\23\3\2\2\2|z\3\2\2\2}\u0082\7")
        buf.write("#\2\2~\177\7\6\2\2\177\u0080\5\36\20\2\u0080\u0081\7\b")
        buf.write("\2\2\u0081\u0083\3\2\2\2\u0082~\3\2\2\2\u0082\u0083\3")
        buf.write("\2\2\2\u0083\25\3\2\2\2\u0084\u0085\b\f\1\2\u0085\u0086")
        buf.write("\7!\2\2\u0086\u0092\5\26\f\7\u0087\u0088\7\13\2\2\u0088")
        buf.write("\u0089\5\26\f\2\u0089\u008a\7\37\2\2\u008a\u0092\3\2\2")
        buf.write("\2\u008b\u008c\5\32\16\2\u008c\u008d\7\r\2\2\u008d\u008e")
        buf.write("\7#\2\2\u008e\u0092\3\2\2\2\u008f\u0092\5\30\r\2\u0090")
        buf.write("\u0092\5\32\16\2\u0091\u0084\3\2\2\2\u0091\u0087\3\2\2")
        buf.write("\2\u0091\u008b\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0090")
        buf.write("\3\2\2\2\u0092\u009b\3\2\2\2\u0093\u0094\f\6\2\2\u0094")
        buf.write("\u0095\7 \2\2\u0095\u009a\5\26\f\7\u0096\u0097\f\5\2\2")
        buf.write("\u0097\u0098\7\33\2\2\u0098\u009a\5\26\f\6\u0099\u0093")
        buf.write("\3\2\2\2\u0099\u0096\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\27\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u009f\5\22\n\2\u009f\u00a2\7\22\2")
        buf.write("\2\u00a0\u00a3\7#\2\2\u00a1\u00a3\5\16\b\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00b6\3\2\2\2\u00a4")
        buf.write("\u00a5\5\22\n\2\u00a5\u00a8\7\20\2\2\u00a6\u00a9\7#\2")
        buf.write("\2\u00a7\u00a9\5\16\b\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a9\u00b6\3\2\2\2\u00aa\u00ab\5\22\n\2\u00ab")
        buf.write("\u00ae\7\f\2\2\u00ac\u00af\7#\2\2\u00ad\u00af\5\16\b\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b0\3")
        buf.write("\2\2\2\u00b0\u00b3\7 \2\2\u00b1\u00b4\7#\2\2\u00b2\u00b4")
        buf.write("\5\16\b\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u009e\3\2\2\2\u00b5\u00a4\3\2\2\2")
        buf.write("\u00b5\u00aa\3\2\2\2\u00b6\31\3\2\2\2\u00b7\u00b8\b\16")
        buf.write("\1\2\u00b8\u00b9\7\"\2\2\u00b9\u00bf\5\32\16\t\u00ba\u00bf")
        buf.write("\5\34\17\2\u00bb\u00bf\7$\2\2\u00bc\u00bf\7%\2\2\u00bd")
        buf.write("\u00bf\5\"\22\2\u00be\u00b7\3\2\2\2\u00be\u00ba\3\2\2")
        buf.write("\2\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c8\3\2\2\2\u00c0\u00c1\f\b\2\2\u00c1")
        buf.write("\u00c2\t\3\2\2\u00c2\u00c7\5\32\16\t\u00c3\u00c4\f\7\2")
        buf.write("\2\u00c4\u00c5\t\4\2\2\u00c5\u00c7\5\32\16\b\u00c6\u00c0")
        buf.write("\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\33\3\2\2\2\u00ca")
        buf.write("\u00c8\3\2\2\2\u00cb\u00cc\b\17\1\2\u00cc\u00d4\7#\2\2")
        buf.write("\u00cd\u00d0\7\13\2\2\u00ce\u00d1\5\32\16\2\u00cf\u00d1")
        buf.write("\5\16\b\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d3\7\37\2\2\u00d3\u00d5\3\2\2")
        buf.write("\2\u00d4\u00cd\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00e4")
        buf.write("\3\2\2\2\u00d6\u00d7\f\4\2\2\u00d7\u00d8\7\17\2\2\u00d8")
        buf.write("\u00e0\7#\2\2\u00d9\u00dc\7\13\2\2\u00da\u00dd\5\32\16")
        buf.write("\2\u00db\u00dd\5\16\b\2\u00dc\u00da\3\2\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\7\37\2\2\u00df")
        buf.write("\u00e1\3\2\2\2\u00e0\u00d9\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e3\3\2\2\2\u00e2\u00d6\3\2\2\2\u00e3\u00e6\3")
        buf.write("\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\35")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00f0\7$\2\2\u00e8")
        buf.write("\u00e9\7$\2\2\u00e9\u00ea\7\16\2\2\u00ea\u00f0\7$\2\2")
        buf.write("\u00eb\u00ec\7\16\2\2\u00ec\u00f0\7$\2\2\u00ed\u00ee\7")
        buf.write("$\2\2\u00ee\u00f0\7\16\2\2\u00ef\u00e7\3\2\2\2\u00ef\u00e8")
        buf.write("\3\2\2\2\u00ef\u00eb\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0")
        buf.write("\37\3\2\2\2\u00f1\u00f3\7\6\2\2\u00f2\u00f4\5\b\5\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\7")
        buf.write("\b\2\2\u00f8!\3\2\2\2\u00f9\u00fa\7\25\2\2\u00fa\u00ff")
        buf.write("\5$\23\2\u00fb\u00fc\7\16\2\2\u00fc\u00fe\5$\23\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3")
        buf.write("\2\2\2\u0102\u0103\7\31\2\2\u0103#\3\2\2\2\u0104\u0109")
        buf.write("\7$\2\2\u0105\u0109\7%\2\2\u0106\u0109\5\16\b\2\u0107")
        buf.write("\u0109\7#\2\2\u0108\u0104\3\2\2\2\u0108\u0105\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109%\3\2\2")
        buf.write("\2!)\61IPU^hprz\u0082\u0091\u0099\u009b\u00a2\u00a8\u00ae")
        buf.write("\u00b3\u00b5\u00be\u00c6\u00c8\u00d0\u00d4\u00dc\u00e0")
        buf.write("\u00e4\u00ef\u00f5\u00ff\u0108")
        return buf.getvalue()
		

class cocoParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__31=1
    T__30=2
    T__29=3
    T__28=4
    T__27=5
    T__26=6
    T__25=7
    T__24=8
    T__23=9
    T__22=10
    T__21=11
    T__20=12
    T__19=13
    T__18=14
    T__17=15
    T__16=16
    T__15=17
    T__14=18
    T__13=19
    T__12=20
    T__11=21
    T__10=22
    T__9=23
    T__8=24
    T__7=25
    T__6=26
    T__5=27
    T__4=28
    T__3=29
    T__2=30
    T__1=31
    T__0=32
    Identifier=33
    Integer=34
    String=35
    Comment=36
    LineComment=37
    WS=38

    tokenNames = [ "<INVALID>", "'not match'", "'require'", "'!='", "'{'", 
                   "'='", "'}'", "'<='", "'forbid'", "'('", "'between'", 
                   "'is'", "','", "'.'", "'after'", "'find'", "'before'", 
                   "'next-to'", "'not in'", "'['", "'>='", "'=='", "'<'", 
                   "']'", "'>'", "'or'", "'match'", "'in'", "'message'", 
                   "')'", "'and'", "'not'", "'-'", "Identifier", "Integer", 
                   "String", "Comment", "LineComment", "WS" ]

    RULE_stylesheet = 0
    RULE_context = 1
    RULE_declaration = 2
    RULE_convention = 3
    RULE_pattern = 4
    RULE_node_declaration = 5
    RULE_semantic_node = 6
    RULE_type_expression = 7
    RULE_whitespace_variation = 8
    RULE_whitespace_node = 9
    RULE_logic_expr = 10
    RULE_type_expr = 11
    RULE_calls_expr = 12
    RULE_call_expression = 13
    RULE_repeater = 14
    RULE_convention_group = 15
    RULE_list_ = 16
    RULE_list_element = 17

    ruleNames =  [ "stylesheet", "context", "declaration", "convention", 
                   "pattern", "node_declaration", "semantic_node", "type_expression", 
                   "whitespace_variation", "whitespace_node", "logic_expr", 
                   "type_expr", "calls_expr", "call_expression", "repeater", 
                   "convention_group", "list_", "list_element" ]

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
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.Identifier:
                self.state = 36 
                self.context()
                self.state = 41
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
            self.state = 42
            localctx.name = self.match(self.Identifier)
            self.state = 43
            self.match(self.T__28)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__30) | (1 << self.T__24) | (1 << self.T__17))) != 0):
                self.state = 44 
                self.declaration()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(self.T__26)
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
            self.state = 52 
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
            self.message = None # Token
            self.requirement = None # Logic_exprContext

        def pattern(self):
            return self.getTypedRuleContext(cocoParser.PatternContext,0)


        def String(self):
            return self.getToken(cocoParser.String, 0)

        def logic_expr(self):
            return self.getTypedRuleContext(cocoParser.Logic_exprContext,0)


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
            self.state = 71
            token = self._input.LA(1)
            if token in [self.T__24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(self.T__24)
                self.state = 55 
                localctx.target = self.pattern()
                self.state = 56
                self.match(self.T__4)
                self.state = 57
                localctx.message = self.match(self.String)

            elif token in [self.T__30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(self.T__30)
                self.state = 60 
                localctx.requirement = self.logic_expr(0)
                self.state = 61
                self.match(self.T__4)
                self.state = 62
                localctx.message = self.match(self.String)

            elif token in [self.T__17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(self.T__17)
                self.state = 65 
                localctx.target = self.pattern()
                self.state = 66
                self.match(self.T__30)
                self.state = 67 
                localctx.requirement = self.logic_expr(0)
                self.state = 68
                self.match(self.T__4)
                self.state = 69
                localctx.message = self.match(self.String)

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
            self.relation = None # Token

        def node_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Node_declarationContext)
            else:
                return self.getTypedRuleContext(cocoParser.Node_declarationContext,i)


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
            self.state = 73 
            self.node_declaration()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__15 or _la==cocoParser.T__5:
                self.state = 74
                localctx.relation = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==cocoParser.T__15 or _la==cocoParser.T__5):
                    localctx.relation = self._errHandler.recoverInline(self)
                self.consume()
                self.state = 75 
                self.node_declaration()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Node_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variable = None # Token
            self.node = None # Semantic_nodeContext

        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def getRuleIndex(self):
            return cocoParser.RULE_node_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitNode_declaration(self)
            else:
                return visitor.visitChildren(self)




    def node_declaration(self):

        localctx = cocoParser.Node_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_node_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 81
                localctx.variable = self.match(self.Identifier)
                self.state = 82
                self.match(self.T__27)


            self.state = 85 
            localctx.node = self.semantic_node()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Semantic_nodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node_type = None # Type_expressionContext
            self.constraint = None # Logic_exprContext

        def logic_expr(self):
            return self.getTypedRuleContext(cocoParser.Logic_exprContext,0)


        def type_expression(self):
            return self.getTypedRuleContext(cocoParser.Type_expressionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_semantic_node

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitSemantic_node(self)
            else:
                return visitor.visitChildren(self)




    def semantic_node(self):

        localctx = cocoParser.Semantic_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_semantic_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87 
            localctx.node_type = self.type_expression(0)
            self.state = 92
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 88
                self.match(self.T__28)
                self.state = 89 
                localctx.constraint = self.logic_expr(0)
                self.state = 90
                self.match(self.T__26)


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
            self.state = 102
            token = self._input.LA(1)
            if token in [self.T__1]:
                self.state = 95
                localctx.operator = self.match(self.T__1)
                self.state = 96 
                localctx.operand = self.type_expression(4)

            elif token in [self.T__23]:
                self.state = 97
                self.match(self.T__23)
                self.state = 98 
                localctx.parenthesis = self.type_expression(0)
                self.state = 99
                self.match(self.T__3)

            elif token in [self.Identifier]:
                self.state = 101
                localctx.primary = self.match(self.Identifier)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 110
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 105
                        localctx.operator = self.match(self.T__2)
                        self.state = 106 
                        localctx.right = self.type_expression(4)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 108
                        localctx.operator = self.match(self.T__7)
                        self.state = 109 
                        localctx.right = self.type_expression(3)
                        pass

             
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Whitespace_variationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whitespace_node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Whitespace_nodeContext)
            else:
                return self.getTypedRuleContext(cocoParser.Whitespace_nodeContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_whitespace_variation

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitWhitespace_variation(self)
            else:
                return visitor.visitChildren(self)




    def whitespace_variation(self):

        localctx = cocoParser.Whitespace_variationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whitespace_variation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115 
            self.whitespace_node()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__7:
                self.state = 116
                self.match(self.T__7)
                self.state = 117 
                self.whitespace_node()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Whitespace_nodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node_type = None # Token
            self.quantifier = None # RepeaterContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def repeater(self):
            return self.getTypedRuleContext(cocoParser.RepeaterContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_whitespace_node

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitWhitespace_node(self)
            else:
                return visitor.visitChildren(self)




    def whitespace_node(self):

        localctx = cocoParser.Whitespace_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whitespace_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            localctx.node_type = self.match(self.Identifier)
            self.state = 128
            _la = self._input.LA(1)
            if _la==cocoParser.T__28:
                self.state = 124
                self.match(self.T__28)
                self.state = 125 
                localctx.quantifier = self.repeater()
                self.state = 126
                self.match(self.T__26)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Logic_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Logic_exprContext
            self.operator = None # Token
            self.operand = None # Logic_exprContext
            self.parenthesis = None # Logic_exprContext
            self.node_type = None # Token
            self.primary_type = None # Type_exprContext
            self.primary_call = None # Calls_exprContext
            self.right = None # Logic_exprContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def calls_expr(self):
            return self.getTypedRuleContext(cocoParser.Calls_exprContext,0)


        def type_expr(self):
            return self.getTypedRuleContext(cocoParser.Type_exprContext,0)


        def logic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Logic_exprContext)
            else:
                return self.getTypedRuleContext(cocoParser.Logic_exprContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_logic_expr

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitLogic_expr(self)
            else:
                return visitor.visitChildren(self)



    def logic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Logic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 131
                localctx.operator = self.match(self.T__1)
                self.state = 132 
                localctx.operand = self.logic_expr(5)
                pass

            elif la_ == 2:
                self.state = 133
                self.match(self.T__23)
                self.state = 134 
                localctx.parenthesis = self.logic_expr(0)
                self.state = 135
                self.match(self.T__3)
                pass

            elif la_ == 3:
                self.state = 137 
                localctx.operand = self.calls_expr(0)
                self.state = 138
                localctx.operator = self.match(self.T__21)
                self.state = 139
                localctx.node_type = self.match(self.Identifier)
                pass

            elif la_ == 4:
                self.state = 141 
                localctx.primary_type = self.type_expr()
                pass

            elif la_ == 5:
                self.state = 142 
                localctx.primary_call = self.calls_expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 151
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Logic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 145
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 146
                        localctx.operator = self.match(self.T__2)
                        self.state = 147 
                        localctx.right = self.logic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Logic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 148
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 149
                        localctx.operator = self.match(self.T__7)
                        self.state = 150 
                        localctx.right = self.logic_expr(4)
                        pass

             
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Type_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variation = None # Whitespace_variationContext
            self.operator = None # Token
            self.variable = None # Token
            self.operand = None # Semantic_nodeContext
            self.second_variable = None # Token
            self.second_operand = None # Semantic_nodeContext

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(cocoParser.Identifier)
            else:
                return self.getToken(cocoParser.Identifier, i)

        def semantic_node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Semantic_nodeContext)
            else:
                return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,i)


        def whitespace_variation(self):
            return self.getTypedRuleContext(cocoParser.Whitespace_variationContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_type_expr

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitType_expr(self)
            else:
                return visitor.visitChildren(self)




    def type_expr(self):

        localctx = cocoParser.Type_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_expr)
        try:
            self.state = 179
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156 
                localctx.variation = self.whitespace_variation()
                self.state = 157
                localctx.operator = self.match(self.T__16)
                self.state = 160
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 158
                    localctx.variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 159 
                    localctx.operand = self.semantic_node()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162 
                localctx.variation = self.whitespace_variation()
                self.state = 163
                localctx.operator = self.match(self.T__18)
                self.state = 166
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 164
                    localctx.variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 165 
                    localctx.operand = self.semantic_node()
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168 
                localctx.variation = self.whitespace_variation()
                self.state = 169
                localctx.operator = self.match(self.T__22)
                self.state = 172
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 170
                    localctx.variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 171 
                    localctx.operand = self.semantic_node()
                    pass


                self.state = 174
                self.match(self.T__2)
                self.state = 177
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 175
                    localctx.second_variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 176 
                    localctx.second_operand = self.semantic_node()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Calls_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Calls_exprContext
            self.operator = None # Token
            self.operand = None # Calls_exprContext
            self.primary_call = None # Call_expressionContext
            self.primary_int = None # Token
            self.primary_str = None # Token
            self.primary_list = None # List_Context
            self.right = None # Calls_exprContext

        def call_expression(self):
            return self.getTypedRuleContext(cocoParser.Call_expressionContext,0)


        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def calls_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Calls_exprContext)
            else:
                return self.getTypedRuleContext(cocoParser.Calls_exprContext,i)


        def list_(self):
            return self.getTypedRuleContext(cocoParser.List_Context,0)


        def getRuleIndex(self):
            return cocoParser.RULE_calls_expr

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitCalls_expr(self)
            else:
                return visitor.visitChildren(self)



    def calls_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Calls_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_calls_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            token = self._input.LA(1)
            if token in [self.T__0]:
                self.state = 182
                localctx.operator = self.match(self.T__0)
                self.state = 183 
                localctx.operand = self.calls_expr(7)

            elif token in [self.Identifier]:
                self.state = 184 
                localctx.primary_call = self.call_expression(0)

            elif token in [self.Integer]:
                self.state = 185
                localctx.primary_int = self.match(self.Integer)

            elif token in [self.String]:
                self.state = 186
                localctx.primary_str = self.match(self.String)

            elif token in [self.T__13]:
                self.state = 187 
                localctx.primary_list = self.list_()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 196
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Calls_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_calls_expr)
                        self.state = 190
                        if not self.precpred(self._ctx, 6):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 191
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__29) | (1 << self.T__25) | (1 << self.T__12) | (1 << self.T__11) | (1 << self.T__10) | (1 << self.T__8))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 192 
                        localctx.right = self.calls_expr(7)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Calls_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_calls_expr)
                        self.state = 193
                        if not self.precpred(self._ctx, 5):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 194
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__31) | (1 << self.T__14) | (1 << self.T__6) | (1 << self.T__5))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 195 
                        localctx.right = self.calls_expr(6)
                        pass

             
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.argument = None # Calls_exprContext
            self.abstract = None # Semantic_nodeContext

        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


        def call_expression(self):
            return self.getTypedRuleContext(cocoParser.Call_expressionContext,0)


        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def calls_expr(self):
            return self.getTypedRuleContext(cocoParser.Calls_exprContext,0)


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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_call_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            localctx.call = self.match(self.Identifier)
            self.state = 210
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 203
                self.match(self.T__23)
                self.state = 206
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 204 
                    localctx.argument = self.calls_expr(0)
                    pass

                elif la_ == 2:
                    self.state = 205 
                    localctx.abstract = self.semantic_node()
                    pass


                self.state = 208
                self.match(self.T__3)


            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cocoParser.Call_expressionContext(self, _parentctx, _parentState)
                    localctx.operand = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_call_expression)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    self.match(self.T__19)
                    self.state = 214
                    localctx.call = self.match(self.Identifier)
                    self.state = 222
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        self.state = 215
                        self.match(self.T__23)
                        self.state = 218
                        la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                        if la_ == 1:
                            self.state = 216 
                            localctx.argument = self.calls_expr(0)
                            pass

                        elif la_ == 2:
                            self.state = 217 
                            localctx.abstract = self.semantic_node()
                            pass


                        self.state = 220
                        self.match(self.T__3)

             
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class RepeaterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.exact = None # Token
            self.lower = None # Token
            self.upper = None # Token

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(cocoParser.Integer)
            else:
                return self.getToken(cocoParser.Integer, i)

        def getRuleIndex(self):
            return cocoParser.RULE_repeater

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitRepeater(self)
            else:
                return visitor.visitChildren(self)




    def repeater(self):

        localctx = cocoParser.RepeaterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_repeater)
        try:
            self.state = 237
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                localctx.exact = self.match(self.Integer)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                localctx.lower = self.match(self.Integer)
                self.state = 231
                self.match(self.T__20)
                self.state = 232
                localctx.upper = self.match(self.Integer)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.match(self.T__20)
                self.state = 234
                localctx.upper = self.match(self.Integer)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                localctx.lower = self.match(self.Integer)
                self.state = 236
                self.match(self.T__20)
                pass


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
        self.enterRule(localctx, 30, self.RULE_convention_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(self.T__28)
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 240 
                self.convention()
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__30) | (1 << self.T__24) | (1 << self.T__17))) != 0)):
                    break

            self.state = 245
            self.match(self.T__26)
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
        self.enterRule(localctx, 32, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(self.T__13)
            self.state = 248 
            self.list_element()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__20:
                self.state = 249
                self.match(self.T__20)
                self.state = 250 
                self.list_element()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
            self.match(self.T__9)
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
            self.element_desc = None # Semantic_nodeContext
            self.element_id = None # Token

        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


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
        self.enterRule(localctx, 34, self.RULE_list_element)
        try:
            self.state = 262
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                localctx.element_int = self.match(self.Integer)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                localctx.element_str = self.match(self.String)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260 
                localctx.element_desc = self.semantic_node()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
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
        self._predicates[7] = self.type_expression_sempred
        self._predicates[10] = self.logic_expr_sempred
        self._predicates[12] = self.calls_expr_sempred
        self._predicates[13] = self.call_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def calls_expr_sempred(self, localctx:Calls_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

    def call_expression_sempred(self, localctx:Call_expressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def type_expression_sempred(self, localctx:Type_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def logic_expr_sempred(self, localctx:Logic_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         



