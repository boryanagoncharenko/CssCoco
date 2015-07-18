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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3)")
        buf.write("\u011c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\7\2*\n\2\f\2\16\2-\13\2\3\3\3\3\3\3\7\3")
        buf.write("\62\n\3\f\3\16\3\65\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4J\n")
        buf.write("\4\3\5\3\5\3\5\7\5O\n\5\f\5\16\5R\13\5\3\5\3\5\3\5\7\5")
        buf.write("W\n\5\f\5\16\5Z\13\5\5\5\\\n\5\3\6\3\6\3\6\3\6\6\6b\n")
        buf.write("\6\r\6\16\6c\3\6\3\6\3\7\3\7\5\7j\n\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\5\bs\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\t}\n\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0085\n\t\f\t\16")
        buf.write("\t\u0088\13\t\3\n\3\n\3\n\7\n\u008d\n\n\f\n\16\n\u0090")
        buf.write("\13\n\3\13\3\13\3\13\3\13\3\13\5\13\u0097\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a2\n\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\7\f\u00aa\n\f\f\f\16\f\u00ad\13\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b7\n\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00bd\n\r\3\r\3\r\3\r\5\r\u00c2\n\r\5\r\u00c4\n\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u00cb\n\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\7\16\u00d3\n\16\f\16\16\16\u00d6\13")
        buf.write("\16\3\17\3\17\3\17\3\17\5\17\u00dc\n\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00e3\n\20\3\20\3\20\5\20\u00e7\n\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\5\20\u00ef\n\20\3\20\3\20")
        buf.write("\5\20\u00f3\n\20\7\20\u00f5\n\20\f\20\16\20\u00f8\13\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0102\n")
        buf.write("\21\3\22\3\22\6\22\u0106\n\22\r\22\16\22\u0107\3\22\3")
        buf.write("\22\3\23\3\23\3\23\3\23\7\23\u0110\n\23\f\23\16\23\u0113")
        buf.write("\13\23\3\23\3\23\3\24\3\24\3\24\5\24\u011a\n\24\3\24\2")
        buf.write("\6\20\26\32\36\25\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&\2\7\4\2\4\4\n\n\4\2\23\23\35\35\4\2\20\20\22")
        buf.write("\22\6\2\5\5\t\t\26\30\32\32\5\2\3\3\24\24\34\35\u0135")
        buf.write("\2+\3\2\2\2\4.\3\2\2\2\6I\3\2\2\2\b[\3\2\2\2\n]\3\2\2")
        buf.write("\2\fi\3\2\2\2\16m\3\2\2\2\20|\3\2\2\2\22\u0089\3\2\2\2")
        buf.write("\24\u0091\3\2\2\2\26\u00a1\3\2\2\2\30\u00c3\3\2\2\2\32")
        buf.write("\u00ca\3\2\2\2\34\u00db\3\2\2\2\36\u00dd\3\2\2\2 \u0101")
        buf.write("\3\2\2\2\"\u0103\3\2\2\2$\u010b\3\2\2\2&\u0119\3\2\2\2")
        buf.write("(*\5\4\3\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\3")
        buf.write("\3\2\2\2-+\3\2\2\2./\7$\2\2/\63\7\6\2\2\60\62\5\6\4\2")
        buf.write("\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2")
        buf.write("\2\64\66\3\2\2\2\65\63\3\2\2\2\66\67\7\b\2\2\67\5\3\2")
        buf.write("\2\289\7\n\2\29:\5\b\5\2:;\7\36\2\2;<\7&\2\2<J\3\2\2\2")
        buf.write("=>\7\4\2\2>?\5\26\f\2?@\7\36\2\2@A\7&\2\2AJ\3\2\2\2BC")
        buf.write("\7\21\2\2CD\5\b\5\2DE\t\2\2\2EF\5\26\f\2FG\7\36\2\2GH")
        buf.write("\7&\2\2HJ\3\2\2\2I8\3\2\2\2I=\3\2\2\2IB\3\2\2\2J\7\3\2")
        buf.write("\2\2KP\5\f\7\2LM\t\3\2\2MO\5\f\7\2NL\3\2\2\2OR\3\2\2\2")
        buf.write("PN\3\2\2\2PQ\3\2\2\2Q\\\3\2\2\2RP\3\2\2\2SX\5\n\6\2TU")
        buf.write("\7\35\2\2UW\5\f\7\2VT\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3")
        buf.write("\2\2\2Y\\\3\2\2\2ZX\3\2\2\2[K\3\2\2\2[S\3\2\2\2\\\t\3")
        buf.write("\2\2\2]^\7\13\2\2^a\5\f\7\2_`\7\16\2\2`b\5\f\7\2a_\3\2")
        buf.write("\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2de\3\2\2\2ef\7\37\2")
        buf.write("\2f\13\3\2\2\2gh\7$\2\2hj\7\7\2\2ig\3\2\2\2ij\3\2\2\2")
        buf.write("jk\3\2\2\2kl\5\16\b\2l\r\3\2\2\2mr\5\20\t\2no\7\6\2\2")
        buf.write("op\5\26\f\2pq\7\b\2\2qs\3\2\2\2rn\3\2\2\2rs\3\2\2\2s\17")
        buf.write("\3\2\2\2tu\b\t\1\2uv\7!\2\2v}\5\20\t\6wx\7\13\2\2xy\5")
        buf.write("\20\t\2yz\7\37\2\2z}\3\2\2\2{}\7$\2\2|t\3\2\2\2|w\3\2")
        buf.write("\2\2|{\3\2\2\2}\u0086\3\2\2\2~\177\f\5\2\2\177\u0080\7")
        buf.write(" \2\2\u0080\u0085\5\20\t\6\u0081\u0082\f\4\2\2\u0082\u0083")
        buf.write("\7\33\2\2\u0083\u0085\5\20\t\5\u0084~\3\2\2\2\u0084\u0081")
        buf.write("\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\21\3\2\2\2\u0088\u0086\3\2\2\2\u0089")
        buf.write("\u008e\5\24\13\2\u008a\u008b\7\33\2\2\u008b\u008d\5\24")
        buf.write("\13\2\u008c\u008a\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\23\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0096\7$\2\2\u0092\u0093\7\6\2\2\u0093")
        buf.write("\u0094\5 \21\2\u0094\u0095\7\b\2\2\u0095\u0097\3\2\2\2")
        buf.write("\u0096\u0092\3\2\2\2\u0096\u0097\3\2\2\2\u0097\25\3\2")
        buf.write("\2\2\u0098\u0099\b\f\1\2\u0099\u009a\7!\2\2\u009a\u00a2")
        buf.write("\5\26\f\7\u009b\u009c\7\13\2\2\u009c\u009d\5\26\f\2\u009d")
        buf.write("\u009e\7\37\2\2\u009e\u00a2\3\2\2\2\u009f\u00a2\5\30\r")
        buf.write("\2\u00a0\u00a2\5\32\16\2\u00a1\u0098\3\2\2\2\u00a1\u009b")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2")
        buf.write("\u00ab\3\2\2\2\u00a3\u00a4\f\6\2\2\u00a4\u00a5\7 \2\2")
        buf.write("\u00a5\u00aa\5\26\f\7\u00a6\u00a7\f\5\2\2\u00a7\u00a8")
        buf.write("\7\33\2\2\u00a8\u00aa\5\26\f\6\u00a9\u00a3\3\2\2\2\u00a9")
        buf.write("\u00a6\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ac\3\2\2\2\u00ac\27\3\2\2\2\u00ad\u00ab\3\2")
        buf.write("\2\2\u00ae\u00af\5\32\16\2\u00af\u00b0\7\r\2\2\u00b0\u00b1")
        buf.write("\7$\2\2\u00b1\u00c4\3\2\2\2\u00b2\u00b3\5\22\n\2\u00b3")
        buf.write("\u00b6\t\4\2\2\u00b4\u00b7\7$\2\2\u00b5\u00b7\5\16\b\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00c4\3")
        buf.write("\2\2\2\u00b8\u00b9\5\22\n\2\u00b9\u00bc\7\f\2\2\u00ba")
        buf.write("\u00bd\7$\2\2\u00bb\u00bd\5\16\b\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c1\7")
        buf.write(" \2\2\u00bf\u00c2\7$\2\2\u00c0\u00c2\5\16\b\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00ae\3\2\2\2\u00c3\u00b2\3\2\2\2\u00c3\u00b8\3\2\2\2")
        buf.write("\u00c4\31\3\2\2\2\u00c5\u00c6\b\16\1\2\u00c6\u00c7\7\"")
        buf.write("\2\2\u00c7\u00cb\5\32\16\7\u00c8\u00cb\5\36\20\2\u00c9")
        buf.write("\u00cb\5\34\17\2\u00ca\u00c5\3\2\2\2\u00ca\u00c8\3\2\2")
        buf.write("\2\u00ca\u00c9\3\2\2\2\u00cb\u00d4\3\2\2\2\u00cc\u00cd")
        buf.write("\f\6\2\2\u00cd\u00ce\t\5\2\2\u00ce\u00d3\5\32\16\7\u00cf")
        buf.write("\u00d0\f\5\2\2\u00d0\u00d1\t\6\2\2\u00d1\u00d3\5\32\16")
        buf.write("\6\u00d2\u00cc\3\2\2\2\u00d2\u00cf\3\2\2\2\u00d3\u00d6")
        buf.write("\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\33\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00dc\7#\2\2\u00d8")
        buf.write("\u00dc\7%\2\2\u00d9\u00dc\7&\2\2\u00da\u00dc\5$\23\2\u00db")
        buf.write("\u00d7\3\2\2\2\u00db\u00d8\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00da\3\2\2\2\u00dc\35\3\2\2\2\u00dd\u00de\b\20")
        buf.write("\1\2\u00de\u00e6\7$\2\2\u00df\u00e2\7\13\2\2\u00e0\u00e3")
        buf.write("\5\34\17\2\u00e1\u00e3\5\16\b\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7\37\2")
        buf.write("\2\u00e5\u00e7\3\2\2\2\u00e6\u00df\3\2\2\2\u00e6\u00e7")
        buf.write("\3\2\2\2\u00e7\u00f6\3\2\2\2\u00e8\u00e9\f\4\2\2\u00e9")
        buf.write("\u00ea\7\17\2\2\u00ea\u00f2\7$\2\2\u00eb\u00ee\7\13\2")
        buf.write("\2\u00ec\u00ef\5\34\17\2\u00ed\u00ef\5\16\b\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f1\7\37\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00eb\3\2\2")
        buf.write("\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00e8")
        buf.write("\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\37\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9")
        buf.write("\u0102\7%\2\2\u00fa\u00fb\7%\2\2\u00fb\u00fc\7\16\2\2")
        buf.write("\u00fc\u0102\7%\2\2\u00fd\u00fe\7\16\2\2\u00fe\u0102\7")
        buf.write("%\2\2\u00ff\u0100\7%\2\2\u0100\u0102\7\16\2\2\u0101\u00f9")
        buf.write("\3\2\2\2\u0101\u00fa\3\2\2\2\u0101\u00fd\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0102!\3\2\2\2\u0103\u0105\7\6\2\2\u0104")
        buf.write("\u0106\5\6\4\2\u0105\u0104\3\2\2\2\u0106\u0107\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\3")
        buf.write("\2\2\2\u0109\u010a\7\b\2\2\u010a#\3\2\2\2\u010b\u010c")
        buf.write("\7\25\2\2\u010c\u0111\5&\24\2\u010d\u010e\7\16\2\2\u010e")
        buf.write("\u0110\5&\24\2\u010f\u010d\3\2\2\2\u0110\u0113\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114\3")
        buf.write("\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\7\31\2\2\u0115")
        buf.write("%\3\2\2\2\u0116\u011a\7%\2\2\u0117\u011a\7&\2\2\u0118")
        buf.write("\u011a\5\16\b\2\u0119\u0116\3\2\2\2\u0119\u0117\3\2\2")
        buf.write("\2\u0119\u0118\3\2\2\2\u011a\'\3\2\2\2$+\63IPX[cir|\u0084")
        buf.write("\u0086\u008e\u0096\u00a1\u00a9\u00ab\u00b6\u00bc\u00c1")
        buf.write("\u00c3\u00ca\u00d2\u00d4\u00db\u00e2\u00e6\u00ee\u00f2")
        buf.write("\u00f6\u0101\u0107\u0111\u0119")
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
    Boolean=33
    Identifier=34
    Integer=35
    String=36
    Comment=37
    LineComment=38
    WS=39

    tokenNames = [ "<INVALID>", "'not match'", "'require'", "'!='", "'{'", 
                   "'='", "'}'", "'<='", "'forbid'", "'('", "'between'", 
                   "'is'", "','", "'.'", "'after'", "'find'", "'before'", 
                   "'next-to'", "'not in'", "'['", "'>='", "'=='", "'<'", 
                   "']'", "'>'", "'or'", "'match'", "'in'", "'message'", 
                   "')'", "'and'", "'not'", "'-'", "Boolean", "Identifier", 
                   "Integer", "String", "Comment", "LineComment", "WS" ]

    RULE_stylesheet = 0
    RULE_context = 1
    RULE_convention = 2
    RULE_pattern = 3
    RULE_fork_pattern = 4
    RULE_node_declaration = 5
    RULE_semantic_node = 6
    RULE_node_type = 7
    RULE_whitespace_variation = 8
    RULE_whitespace_node = 9
    RULE_logic_expr = 10
    RULE_type_expr = 11
    RULE_arithmetic_expr = 12
    RULE_element = 13
    RULE_call_expr = 14
    RULE_repeater = 15
    RULE_convention_group = 16
    RULE_list_ = 17
    RULE_list_element = 18

    ruleNames =  [ "stylesheet", "context", "convention", "pattern", "fork_pattern", 
                   "node_declaration", "semantic_node", "node_type", "whitespace_variation", 
                   "whitespace_node", "logic_expr", "type_expr", "arithmetic_expr", 
                   "element", "call_expr", "repeater", "convention_group", 
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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.Identifier:
                self.state = 38 
                self.context()
                self.state = 43
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

        def convention(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.ConventionContext)
            else:
                return self.getTypedRuleContext(cocoParser.ConventionContext,i)


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
            self.state = 44
            localctx.name = self.match(self.Identifier)
            self.state = 45
            self.match(self.T__28)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__30) | (1 << self.T__24) | (1 << self.T__17))) != 0):
                self.state = 46 
                self.convention()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(self.T__26)
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
            self.action = None # Token
            self.target = None # PatternContext
            self.message = None # Token
            self.requirement = None # Logic_exprContext
            self.find = None # Token

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
        self.enterRule(localctx, 4, self.RULE_convention)
        self._la = 0 # Token type
        try:
            self.state = 71
            token = self._input.LA(1)
            if token in [self.T__24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                localctx.action = self.match(self.T__24)
                self.state = 55 
                localctx.target = self.pattern()
                self.state = 56
                self.match(self.T__4)
                self.state = 57
                localctx.message = self.match(self.String)

            elif token in [self.T__30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                localctx.action = self.match(self.T__30)
                self.state = 60 
                localctx.requirement = self.logic_expr(0)
                self.state = 61
                self.match(self.T__4)
                self.state = 62
                localctx.message = self.match(self.String)

            elif token in [self.T__17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                localctx.find = self.match(self.T__17)
                self.state = 65 
                localctx.target = self.pattern()
                self.state = 66
                localctx.action = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==cocoParser.T__30 or _la==cocoParser.T__24):
                    localctx.action = self._errHandler.recoverInline(self)
                self.consume()
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
            self.simple = None # Node_declarationContext
            self.relation = None # Token
            self.fork = None # Fork_patternContext

        def node_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Node_declarationContext)
            else:
                return self.getTypedRuleContext(cocoParser.Node_declarationContext,i)


        def fork_pattern(self):
            return self.getTypedRuleContext(cocoParser.Fork_patternContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_pattern

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = cocoParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.state = 89
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73 
                localctx.simple = self.node_declaration()
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

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81 
                localctx.fork = self.fork_pattern()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cocoParser.T__5:
                    self.state = 82
                    localctx.relation = self.match(self.T__5)
                    self.state = 83 
                    self.node_declaration()
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fork_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Node_declarationContext)
            else:
                return self.getTypedRuleContext(cocoParser.Node_declarationContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_fork_pattern

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitFork_pattern(self)
            else:
                return visitor.visitChildren(self)




    def fork_pattern(self):

        localctx = cocoParser.Fork_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fork_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(self.T__23)
            self.state = 92 
            self.node_declaration()
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.match(self.T__20)
                self.state = 94 
                self.node_declaration()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cocoParser.T__20):
                    break

            self.state = 99
            self.match(self.T__3)
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
            self.state = 103
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 101
                localctx.variable = self.match(self.Identifier)
                self.state = 102
                self.match(self.T__27)


            self.state = 105 
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
            self.type_ = None # Node_typeContext
            self.constraint = None # Logic_exprContext

        def node_type(self):
            return self.getTypedRuleContext(cocoParser.Node_typeContext,0)


        def logic_expr(self):
            return self.getTypedRuleContext(cocoParser.Logic_exprContext,0)


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
            self.state = 107 
            localctx.type_ = self.node_type(0)
            self.state = 112
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 108
                self.match(self.T__28)
                self.state = 109 
                localctx.constraint = self.logic_expr(0)
                self.state = 110
                self.match(self.T__26)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Node_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Node_typeContext
            self.operator = None # Token
            self.operand = None # Node_typeContext
            self.parenthesis = None # Node_typeContext
            self.primary = None # Token
            self.right = None # Node_typeContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def node_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Node_typeContext)
            else:
                return self.getTypedRuleContext(cocoParser.Node_typeContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_node_type

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitNode_type(self)
            else:
                return visitor.visitChildren(self)



    def node_type(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Node_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_node_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            token = self._input.LA(1)
            if token in [self.T__1]:
                self.state = 115
                localctx.operator = self.match(self.T__1)
                self.state = 116 
                localctx.operand = self.node_type(4)

            elif token in [self.T__23]:
                self.state = 117
                self.match(self.T__23)
                self.state = 118 
                localctx.parenthesis = self.node_type(0)
                self.state = 119
                self.match(self.T__3)

            elif token in [self.Identifier]:
                self.state = 121
                localctx.primary = self.match(self.Identifier)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 130
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Node_typeContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_node_type)
                        self.state = 124
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 125
                        localctx.operator = self.match(self.T__2)
                        self.state = 126 
                        localctx.right = self.node_type(4)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Node_typeContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_node_type)
                        self.state = 127
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 128
                        localctx.operator = self.match(self.T__7)
                        self.state = 129 
                        localctx.right = self.node_type(3)
                        pass

             
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
            self.state = 135 
            self.whitespace_node()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__7:
                self.state = 136
                self.match(self.T__7)
                self.state = 137 
                self.whitespace_node()
                self.state = 142
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
            self.type_ = None # Token
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
            self.state = 143
            localctx.type_ = self.match(self.Identifier)
            self.state = 148
            _la = self._input.LA(1)
            if _la==cocoParser.T__28:
                self.state = 144
                self.match(self.T__28)
                self.state = 145 
                localctx.quantifier = self.repeater()
                self.state = 146
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
            self.type_ = None # Type_exprContext
            self.call = None # Arithmetic_exprContext
            self.right = None # Logic_exprContext

        def arithmetic_expr(self):
            return self.getTypedRuleContext(cocoParser.Arithmetic_exprContext,0)


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
            self.state = 159
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 151
                localctx.operator = self.match(self.T__1)
                self.state = 152 
                localctx.operand = self.logic_expr(5)
                pass

            elif la_ == 2:
                self.state = 153
                self.match(self.T__23)
                self.state = 154 
                localctx.parenthesis = self.logic_expr(0)
                self.state = 155
                self.match(self.T__3)
                pass

            elif la_ == 3:
                self.state = 157 
                localctx.type_ = self.type_expr()
                pass

            elif la_ == 4:
                self.state = 158 
                localctx.call = self.arithmetic_expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 167
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Logic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 162
                        localctx.operator = self.match(self.T__2)
                        self.state = 163 
                        localctx.right = self.logic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Logic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 165
                        localctx.operator = self.match(self.T__7)
                        self.state = 166 
                        localctx.right = self.logic_expr(4)
                        pass

             
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.operand = None # Arithmetic_exprContext
            self.operator = None # Token
            self.type_ = None # Token
            self.variation = None # Whitespace_variationContext
            self.variable = None # Token
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


        def arithmetic_expr(self):
            return self.getTypedRuleContext(cocoParser.Arithmetic_exprContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 193
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172 
                localctx.operand = self.arithmetic_expr(0)
                self.state = 173
                localctx.operator = self.match(self.T__21)
                self.state = 174
                localctx.type_ = self.match(self.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176 
                localctx.variation = self.whitespace_variation()
                self.state = 177
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==cocoParser.T__18 or _la==cocoParser.T__16):
                    localctx.operator = self._errHandler.recoverInline(self)
                self.consume()
                self.state = 180
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 178
                    localctx.variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 179 
                    localctx.operand = self.semantic_node()
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182 
                localctx.variation = self.whitespace_variation()
                self.state = 183
                localctx.operator = self.match(self.T__22)
                self.state = 186
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 184
                    localctx.variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 185 
                    localctx.operand = self.semantic_node()
                    pass


                self.state = 188
                self.match(self.T__2)
                self.state = 191
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 189
                    localctx.second_variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 190 
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

    class Arithmetic_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Arithmetic_exprContext
            self.operator = None # Token
            self.operand = None # Arithmetic_exprContext
            self.call = None # Call_exprContext
            self.primary = None # ElementContext
            self.right = None # Arithmetic_exprContext

        def element(self):
            return self.getTypedRuleContext(cocoParser.ElementContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(cocoParser.Call_exprContext,0)


        def arithmetic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(cocoParser.Arithmetic_exprContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_arithmetic_expr

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitArithmetic_expr(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Arithmetic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_arithmetic_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            token = self._input.LA(1)
            if token in [self.T__0]:
                self.state = 196
                localctx.operator = self.match(self.T__0)
                self.state = 197 
                localctx.operand = self.arithmetic_expr(5)

            elif token in [self.Identifier]:
                self.state = 198 
                localctx.call = self.call_expr(0)

            elif token in [self.T__13, self.Boolean, self.Integer, self.String]:
                self.state = 199 
                localctx.primary = self.element()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Arithmetic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 203
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__29) | (1 << self.T__25) | (1 << self.T__12) | (1 << self.T__11) | (1 << self.T__10) | (1 << self.T__8))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 204 
                        localctx.right = self.arithmetic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Arithmetic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 206
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__31) | (1 << self.T__14) | (1 << self.T__6) | (1 << self.T__5))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 207 
                        localctx.right = self.arithmetic_expr(4)
                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.primary_bool = None # Token
            self.primary_int = None # Token
            self.primary_str = None # Token
            self.primary_list = None # List_Context

        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def Boolean(self):
            return self.getToken(cocoParser.Boolean, 0)

        def list_(self):
            return self.getTypedRuleContext(cocoParser.List_Context,0)


        def getRuleIndex(self):
            return cocoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = cocoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_element)
        try:
            self.state = 217
            token = self._input.LA(1)
            if token in [self.Boolean]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                localctx.primary_bool = self.match(self.Boolean)

            elif token in [self.Integer]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                localctx.primary_int = self.match(self.Integer)

            elif token in [self.String]:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                localctx.primary_str = self.match(self.String)

            elif token in [self.T__13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 216 
                localctx.primary_list = self.list_()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.operand = None # Call_exprContext
            self.call = None # Token
            self.argument = None # ElementContext
            self.abstract = None # Semantic_nodeContext

        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def element(self):
            return self.getTypedRuleContext(cocoParser.ElementContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(cocoParser.Call_exprContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitCall_expr(self)
            else:
                return visitor.visitChildren(self)



    def call_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Call_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_call_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            localctx.call = self.match(self.Identifier)
            self.state = 228
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 221
                self.match(self.T__23)
                self.state = 224
                token = self._input.LA(1)
                if token in [self.T__13, self.Boolean, self.Integer, self.String]:
                    self.state = 222 
                    localctx.argument = self.element()

                elif token in [self.T__23, self.T__1, self.Identifier]:
                    self.state = 223 
                    localctx.abstract = self.semantic_node()

                else:
                    raise NoViableAltException(self)

                self.state = 226
                self.match(self.T__3)


            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cocoParser.Call_exprContext(self, _parentctx, _parentState)
                    localctx.operand = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_call_expr)
                    self.state = 230
                    if not self.precpred(self._ctx, 2):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 231
                    self.match(self.T__19)
                    self.state = 232
                    localctx.call = self.match(self.Identifier)
                    self.state = 240
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        self.state = 233
                        self.match(self.T__23)
                        self.state = 236
                        token = self._input.LA(1)
                        if token in [self.T__13, self.Boolean, self.Integer, self.String]:
                            self.state = 234 
                            localctx.argument = self.element()

                        elif token in [self.T__23, self.T__1, self.Identifier]:
                            self.state = 235 
                            localctx.abstract = self.semantic_node()

                        else:
                            raise NoViableAltException(self)

                        self.state = 238
                        self.match(self.T__3)

             
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_repeater)
        try:
            self.state = 255
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                localctx.exact = self.match(self.Integer)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                localctx.lower = self.match(self.Integer)
                self.state = 249
                self.match(self.T__20)
                self.state = 250
                localctx.upper = self.match(self.Integer)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.match(self.T__20)
                self.state = 252
                localctx.upper = self.match(self.Integer)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                localctx.lower = self.match(self.Integer)
                self.state = 254
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
        self.enterRule(localctx, 32, self.RULE_convention_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(self.T__28)
            self.state = 259 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 258 
                self.convention()
                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__30) | (1 << self.T__24) | (1 << self.T__17))) != 0)):
                    break

            self.state = 263
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
        self.enterRule(localctx, 34, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(self.T__13)
            self.state = 266 
            self.list_element()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__20:
                self.state = 267
                self.match(self.T__20)
                self.state = 268 
                self.list_element()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 274
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

        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


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
        self.enterRule(localctx, 36, self.RULE_list_element)
        try:
            self.state = 279
            token = self._input.LA(1)
            if token in [self.Integer]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                localctx.element_int = self.match(self.Integer)

            elif token in [self.String]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                localctx.element_str = self.match(self.String)

            elif token in [self.T__23, self.T__1, self.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 278 
                localctx.element_desc = self.semantic_node()

            else:
                raise NoViableAltException(self)

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
        self._predicates[7] = self.node_type_sempred
        self._predicates[10] = self.logic_expr_sempred
        self._predicates[12] = self.arithmetic_expr_sempred
        self._predicates[14] = self.call_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def node_type_sempred(self, localctx:Node_typeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def arithmetic_expr_sempred(self, localctx:Arithmetic_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

    def call_expr_sempred(self, localctx:Call_exprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def logic_expr_sempred(self, localctx:Logic_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         



