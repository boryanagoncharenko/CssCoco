# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from csscoco.coco.syntax import cocoVisitor
else:
    from cocoVisitor import cocoVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3(")
        buf.write("\u0126\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\7\2,\n\2\f\2\16\2/\13\2\3\3\3")
        buf.write("\3\3\3\7\3\64\n\3\f\3\16\3\67\13\3\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5N\n\5\3\6\3\6\3\6\7\6S\n\6\f\6\16\6V\13")
        buf.write("\6\3\6\3\6\3\6\7\6[\n\6\f\6\16\6^\13\6\5\6`\n\6\3\7\3")
        buf.write("\7\3\7\3\7\6\7f\n\7\r\7\16\7g\3\7\3\7\3\b\3\b\5\bn\n\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tw\n\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u0081\n\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\7\n\u0089\n\n\f\n\16\n\u008c\13\n\3\13\3\13\3\13\7\13")
        buf.write("\u0091\n\13\f\13\16\13\u0094\13\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u009b\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00aa\n\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r")
        buf.write("\u00b2\n\r\f\r\16\r\u00b5\13\r\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00bb\n\16\3\16\3\16\3\16\3\16\5\16\u00c1\n\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u00c7\n\16\3\16\3\16\3\16\5\16\u00cc")
        buf.write("\n\16\5\16\u00ce\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00d5")
        buf.write("\n\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00dd\n\17\f")
        buf.write("\17\16\17\u00e0\13\17\3\20\3\20\3\20\5\20\u00e5\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u00ec\n\21\3\21\3\21\5\21")
        buf.write("\u00f0\n\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00f8\n")
        buf.write("\21\3\21\3\21\5\21\u00fc\n\21\7\21\u00fe\n\21\f\21\16")
        buf.write("\21\u0101\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u010b\n\22\3\23\3\23\6\23\u010f\n\23\r\23\16\23")
        buf.write("\u0110\3\23\3\23\3\24\3\24\3\24\3\24\7\24\u0119\n\24\f")
        buf.write("\24\16\24\u011c\13\24\3\24\3\24\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u0124\n\25\3\25\2\6\22\30\34 \26\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(\2\6\4\2\4\4\n\n\4\2\23\23")
        buf.write("\35\35\6\2\5\5\t\t\26\30\32\32\5\2\3\3\24\24\34\35\u0140")
        buf.write("\2-\3\2\2\2\4\60\3\2\2\2\6:\3\2\2\2\bM\3\2\2\2\n_\3\2")
        buf.write("\2\2\fa\3\2\2\2\16m\3\2\2\2\20q\3\2\2\2\22\u0080\3\2\2")
        buf.write("\2\24\u008d\3\2\2\2\26\u0095\3\2\2\2\30\u00a9\3\2\2\2")
        buf.write("\32\u00cd\3\2\2\2\34\u00d4\3\2\2\2\36\u00e4\3\2\2\2 \u00e6")
        buf.write("\3\2\2\2\"\u010a\3\2\2\2$\u010c\3\2\2\2&\u0114\3\2\2\2")
        buf.write("(\u0123\3\2\2\2*,\5\4\3\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2")
        buf.write("\2-.\3\2\2\2.\3\3\2\2\2/-\3\2\2\2\60\61\7#\2\2\61\65\7")
        buf.write("\6\2\2\62\64\5\6\4\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63")
        buf.write("\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\7\b")
        buf.write("\2\29\5\3\2\2\2:;\5\b\5\2;\7\3\2\2\2<=\7\n\2\2=>\5\n\6")
        buf.write("\2>?\7\36\2\2?@\7%\2\2@N\3\2\2\2AB\7\4\2\2BC\5\30\r\2")
        buf.write("CD\7\36\2\2DE\7%\2\2EN\3\2\2\2FG\7\21\2\2GH\5\n\6\2HI")
        buf.write("\t\2\2\2IJ\5\30\r\2JK\7\36\2\2KL\7%\2\2LN\3\2\2\2M<\3")
        buf.write("\2\2\2MA\3\2\2\2MF\3\2\2\2N\t\3\2\2\2OT\5\16\b\2PQ\t\3")
        buf.write("\2\2QS\5\16\b\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2")
        buf.write("\2U`\3\2\2\2VT\3\2\2\2W\\\5\f\7\2XY\7\35\2\2Y[\5\16\b")
        buf.write("\2ZX\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]`\3\2\2\2")
        buf.write("^\\\3\2\2\2_O\3\2\2\2_W\3\2\2\2`\13\3\2\2\2ab\7\13\2\2")
        buf.write("be\5\16\b\2cd\7\16\2\2df\5\16\b\2ec\3\2\2\2fg\3\2\2\2")
        buf.write("ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7\37\2\2j\r\3\2\2\2k")
        buf.write("l\7#\2\2ln\7\7\2\2mk\3\2\2\2mn\3\2\2\2no\3\2\2\2op\5\20")
        buf.write("\t\2p\17\3\2\2\2qv\5\22\n\2rs\7\6\2\2st\5\30\r\2tu\7\b")
        buf.write("\2\2uw\3\2\2\2vr\3\2\2\2vw\3\2\2\2w\21\3\2\2\2xy\b\n\1")
        buf.write("\2yz\7!\2\2z\u0081\5\22\n\6{|\7\13\2\2|}\5\22\n\2}~\7")
        buf.write("\37\2\2~\u0081\3\2\2\2\177\u0081\7#\2\2\u0080x\3\2\2\2")
        buf.write("\u0080{\3\2\2\2\u0080\177\3\2\2\2\u0081\u008a\3\2\2\2")
        buf.write("\u0082\u0083\f\5\2\2\u0083\u0084\7 \2\2\u0084\u0089\5")
        buf.write("\22\n\6\u0085\u0086\f\4\2\2\u0086\u0087\7\33\2\2\u0087")
        buf.write("\u0089\5\22\n\5\u0088\u0082\3\2\2\2\u0088\u0085\3\2\2")
        buf.write("\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\23\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u0092")
        buf.write("\5\26\f\2\u008e\u008f\7\33\2\2\u008f\u0091\5\26\f\2\u0090")
        buf.write("\u008e\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\25\3\2\2\2\u0094\u0092\3\2")
        buf.write("\2\2\u0095\u009a\7#\2\2\u0096\u0097\7\6\2\2\u0097\u0098")
        buf.write("\5\"\22\2\u0098\u0099\7\b\2\2\u0099\u009b\3\2\2\2\u009a")
        buf.write("\u0096\3\2\2\2\u009a\u009b\3\2\2\2\u009b\27\3\2\2\2\u009c")
        buf.write("\u009d\b\r\1\2\u009d\u009e\7!\2\2\u009e\u00aa\5\30\r\7")
        buf.write("\u009f\u00a0\7\13\2\2\u00a0\u00a1\5\30\r\2\u00a1\u00a2")
        buf.write("\7\37\2\2\u00a2\u00aa\3\2\2\2\u00a3\u00a4\5\34\17\2\u00a4")
        buf.write("\u00a5\7\r\2\2\u00a5\u00a6\7#\2\2\u00a6\u00aa\3\2\2\2")
        buf.write("\u00a7\u00aa\5\32\16\2\u00a8\u00aa\5\34\17\2\u00a9\u009c")
        buf.write("\3\2\2\2\u00a9\u009f\3\2\2\2\u00a9\u00a3\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00b3\3\2\2\2")
        buf.write("\u00ab\u00ac\f\6\2\2\u00ac\u00ad\7 \2\2\u00ad\u00b2\5")
        buf.write("\30\r\7\u00ae\u00af\f\5\2\2\u00af\u00b0\7\33\2\2\u00b0")
        buf.write("\u00b2\5\30\r\6\u00b1\u00ab\3\2\2\2\u00b1\u00ae\3\2\2")
        buf.write("\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\31\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7")
        buf.write("\5\24\13\2\u00b7\u00ba\7\22\2\2\u00b8\u00bb\7#\2\2\u00b9")
        buf.write("\u00bb\5\20\t\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2")
        buf.write("\2\u00bb\u00ce\3\2\2\2\u00bc\u00bd\5\24\13\2\u00bd\u00c0")
        buf.write("\7\20\2\2\u00be\u00c1\7#\2\2\u00bf\u00c1\5\20\t\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00ce\3\2\2\2")
        buf.write("\u00c2\u00c3\5\24\13\2\u00c3\u00c6\7\f\2\2\u00c4\u00c7")
        buf.write("\7#\2\2\u00c5\u00c7\5\20\t\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cb\7 \2\2")
        buf.write("\u00c9\u00cc\7#\2\2\u00ca\u00cc\5\20\t\2\u00cb\u00c9\3")
        buf.write("\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00b6")
        buf.write("\3\2\2\2\u00cd\u00bc\3\2\2\2\u00cd\u00c2\3\2\2\2\u00ce")
        buf.write("\33\3\2\2\2\u00cf\u00d0\b\17\1\2\u00d0\u00d1\7\"\2\2\u00d1")
        buf.write("\u00d5\5\34\17\7\u00d2\u00d5\5 \21\2\u00d3\u00d5\5\36")
        buf.write("\20\2\u00d4\u00cf\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5\u00de\3\2\2\2\u00d6\u00d7\f\6\2\2\u00d7")
        buf.write("\u00d8\t\4\2\2\u00d8\u00dd\5\34\17\7\u00d9\u00da\f\5\2")
        buf.write("\2\u00da\u00db\t\5\2\2\u00db\u00dd\5\34\17\6\u00dc\u00d6")
        buf.write("\3\2\2\2\u00dc\u00d9\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\35\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e1\u00e5\7$\2\2\u00e2\u00e5\7%\2\2\u00e3")
        buf.write("\u00e5\5&\24\2\u00e4\u00e1\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e4\u00e3\3\2\2\2\u00e5\37\3\2\2\2\u00e6\u00e7\b\21")
        buf.write("\1\2\u00e7\u00ef\7#\2\2\u00e8\u00eb\7\13\2\2\u00e9\u00ec")
        buf.write("\5\36\20\2\u00ea\u00ec\5\20\t\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\7\37\2")
        buf.write("\2\u00ee\u00f0\3\2\2\2\u00ef\u00e8\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0\u00ff\3\2\2\2\u00f1\u00f2\f\4\2\2\u00f2")
        buf.write("\u00f3\7\17\2\2\u00f3\u00fb\7#\2\2\u00f4\u00f7\7\13\2")
        buf.write("\2\u00f5\u00f8\5\36\20\2\u00f6\u00f8\5\20\t\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00fa\7\37\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f4\3\2\2")
        buf.write("\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00f1")
        buf.write("\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100!\3\2\2\2\u0101\u00ff\3\2\2\2\u0102")
        buf.write("\u010b\7$\2\2\u0103\u0104\7$\2\2\u0104\u0105\7\16\2\2")
        buf.write("\u0105\u010b\7$\2\2\u0106\u0107\7\16\2\2\u0107\u010b\7")
        buf.write("$\2\2\u0108\u0109\7$\2\2\u0109\u010b\7\16\2\2\u010a\u0102")
        buf.write("\3\2\2\2\u010a\u0103\3\2\2\2\u010a\u0106\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010b#\3\2\2\2\u010c\u010e\7\6\2\2\u010d")
        buf.write("\u010f\5\b\5\2\u010e\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3")
        buf.write("\2\2\2\u0112\u0113\7\b\2\2\u0113%\3\2\2\2\u0114\u0115")
        buf.write("\7\25\2\2\u0115\u011a\5(\25\2\u0116\u0117\7\16\2\2\u0117")
        buf.write("\u0119\5(\25\2\u0118\u0116\3\2\2\2\u0119\u011c\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\3")
        buf.write("\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e\7\31\2\2\u011e")
        buf.write("\'\3\2\2\2\u011f\u0124\7$\2\2\u0120\u0124\7%\2\2\u0121")
        buf.write("\u0124\5\20\t\2\u0122\u0124\7#\2\2\u0123\u011f\3\2\2\2")
        buf.write("\u0123\u0120\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122\3")
        buf.write("\2\2\2\u0124)\3\2\2\2%-\65MT\\_gmv\u0080\u0088\u008a\u0092")
        buf.write("\u009a\u00a9\u00b1\u00b3\u00ba\u00c0\u00c6\u00cb\u00cd")
        buf.write("\u00d4\u00dc\u00de\u00e4\u00eb\u00ef\u00f7\u00fb\u00ff")
        buf.write("\u010a\u0110\u011a\u0123")
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
    RULE_fork_pattern = 5
    RULE_node_declaration = 6
    RULE_semantic_node = 7
    RULE_type_expression = 8
    RULE_whitespace_variation = 9
    RULE_whitespace_node = 10
    RULE_logic_expr = 11
    RULE_type_expr = 12
    RULE_calls_expr = 13
    RULE_element = 14
    RULE_call_expression = 15
    RULE_repeater = 16
    RULE_convention_group = 17
    RULE_list_ = 18
    RULE_list_element = 19

    ruleNames =  [ "stylesheet", "context", "declaration", "convention", 
                   "pattern", "fork_pattern", "node_declaration", "semantic_node", 
                   "type_expression", "whitespace_variation", "whitespace_node", 
                   "logic_expr", "type_expr", "calls_expr", "element", "call_expression", 
                   "repeater", "convention_group", "list_", "list_element" ]

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
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.Identifier:
                self.state = 40 
                self.context()
                self.state = 45
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
            self.state = 46
            localctx.name = self.match(self.Identifier)
            self.state = 47
            self.match(self.T__28)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__30) | (1 << self.T__24) | (1 << self.T__17))) != 0):
                self.state = 48 
                self.declaration()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
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
            self.state = 56 
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
        self.enterRule(localctx, 6, self.RULE_convention)
        self._la = 0 # Token type
        try:
            self.state = 75
            token = self._input.LA(1)
            if token in [self.T__24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                localctx.action = self.match(self.T__24)
                self.state = 59 
                localctx.target = self.pattern()
                self.state = 60
                self.match(self.T__4)
                self.state = 61
                localctx.message = self.match(self.String)

            elif token in [self.T__30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                localctx.action = self.match(self.T__30)
                self.state = 64 
                localctx.requirement = self.logic_expr(0)
                self.state = 65
                self.match(self.T__4)
                self.state = 66
                localctx.message = self.match(self.String)

            elif token in [self.T__17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                localctx.find = self.match(self.T__17)
                self.state = 69 
                localctx.target = self.pattern()
                self.state = 70
                localctx.action = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==cocoParser.T__30 or _la==cocoParser.T__24):
                    localctx.action = self._errHandler.recoverInline(self)
                self.consume()
                self.state = 71 
                localctx.requirement = self.logic_expr(0)
                self.state = 72
                self.match(self.T__4)
                self.state = 73
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
        self.enterRule(localctx, 8, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.state = 93
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77 
                localctx.simple = self.node_declaration()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cocoParser.T__15 or _la==cocoParser.T__5:
                    self.state = 78
                    localctx.relation = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==cocoParser.T__15 or _la==cocoParser.T__5):
                        localctx.relation = self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 79 
                    self.node_declaration()
                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85 
                localctx.fork = self.fork_pattern()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cocoParser.T__5:
                    self.state = 86
                    localctx.relation = self.match(self.T__5)
                    self.state = 87 
                    self.node_declaration()
                    self.state = 92
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
        self.enterRule(localctx, 10, self.RULE_fork_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(self.T__23)
            self.state = 96 
            self.node_declaration()
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self.match(self.T__20)
                self.state = 98 
                self.node_declaration()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cocoParser.T__20):
                    break

            self.state = 103
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
        self.enterRule(localctx, 12, self.RULE_node_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 105
                localctx.variable = self.match(self.Identifier)
                self.state = 106
                self.match(self.T__27)


            self.state = 109 
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
        self.enterRule(localctx, 14, self.RULE_semantic_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111 
            localctx.node_type = self.type_expression(0)
            self.state = 116
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 112
                self.match(self.T__28)
                self.state = 113 
                localctx.constraint = self.logic_expr(0)
                self.state = 114
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_type_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            token = self._input.LA(1)
            if token in [self.T__1]:
                self.state = 119
                localctx.operator = self.match(self.T__1)
                self.state = 120 
                localctx.operand = self.type_expression(4)

            elif token in [self.T__23]:
                self.state = 121
                self.match(self.T__23)
                self.state = 122 
                localctx.parenthesis = self.type_expression(0)
                self.state = 123
                self.match(self.T__3)

            elif token in [self.Identifier]:
                self.state = 125
                localctx.primary = self.match(self.Identifier)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 129
                        localctx.operator = self.match(self.T__2)
                        self.state = 130 
                        localctx.right = self.type_expression(4)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 132
                        localctx.operator = self.match(self.T__7)
                        self.state = 133 
                        localctx.right = self.type_expression(3)
                        pass

             
                self.state = 138
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
        self.enterRule(localctx, 18, self.RULE_whitespace_variation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139 
            self.whitespace_node()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__7:
                self.state = 140
                self.match(self.T__7)
                self.state = 141 
                self.whitespace_node()
                self.state = 146
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
        self.enterRule(localctx, 20, self.RULE_whitespace_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            localctx.node_type = self.match(self.Identifier)
            self.state = 152
            _la = self._input.LA(1)
            if _la==cocoParser.T__28:
                self.state = 148
                self.match(self.T__28)
                self.state = 149 
                localctx.quantifier = self.repeater()
                self.state = 150
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 155
                localctx.operator = self.match(self.T__1)
                self.state = 156 
                localctx.operand = self.logic_expr(5)
                pass

            elif la_ == 2:
                self.state = 157
                self.match(self.T__23)
                self.state = 158 
                localctx.parenthesis = self.logic_expr(0)
                self.state = 159
                self.match(self.T__3)
                pass

            elif la_ == 3:
                self.state = 161 
                localctx.operand = self.calls_expr(0)
                self.state = 162
                localctx.operator = self.match(self.T__21)
                self.state = 163
                localctx.node_type = self.match(self.Identifier)
                pass

            elif la_ == 4:
                self.state = 165 
                localctx.primary_type = self.type_expr()
                pass

            elif la_ == 5:
                self.state = 166 
                localctx.primary_call = self.calls_expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 175
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Logic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 170
                        localctx.operator = self.match(self.T__2)
                        self.state = 171 
                        localctx.right = self.logic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Logic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 173
                        localctx.operator = self.match(self.T__7)
                        self.state = 174 
                        localctx.right = self.logic_expr(4)
                        pass

             
                self.state = 179
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
        self.enterRule(localctx, 24, self.RULE_type_expr)
        try:
            self.state = 203
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180 
                localctx.variation = self.whitespace_variation()
                self.state = 181
                localctx.operator = self.match(self.T__16)
                self.state = 184
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 182
                    localctx.variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 183 
                    localctx.operand = self.semantic_node()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186 
                localctx.variation = self.whitespace_variation()
                self.state = 187
                localctx.operator = self.match(self.T__18)
                self.state = 190
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 188
                    localctx.variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 189 
                    localctx.operand = self.semantic_node()
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192 
                localctx.variation = self.whitespace_variation()
                self.state = 193
                localctx.operator = self.match(self.T__22)
                self.state = 196
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 194
                    localctx.variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 195 
                    localctx.operand = self.semantic_node()
                    pass


                self.state = 198
                self.match(self.T__2)
                self.state = 201
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 199
                    localctx.second_variable = self.match(self.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 200 
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
            self.primary = None # ElementContext
            self.right = None # Calls_exprContext

        def call_expression(self):
            return self.getTypedRuleContext(cocoParser.Call_expressionContext,0)


        def element(self):
            return self.getTypedRuleContext(cocoParser.ElementContext,0)


        def calls_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Calls_exprContext)
            else:
                return self.getTypedRuleContext(cocoParser.Calls_exprContext,i)


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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_calls_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            token = self._input.LA(1)
            if token in [self.T__0]:
                self.state = 206
                localctx.operator = self.match(self.T__0)
                self.state = 207 
                localctx.operand = self.calls_expr(5)

            elif token in [self.Identifier]:
                self.state = 208 
                localctx.primary_call = self.call_expression(0)

            elif token in [self.T__13, self.Integer, self.String]:
                self.state = 209 
                localctx.primary = self.element()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 218
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Calls_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_calls_expr)
                        self.state = 212
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 213
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__29) | (1 << self.T__25) | (1 << self.T__12) | (1 << self.T__11) | (1 << self.T__10) | (1 << self.T__8))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 214 
                        localctx.right = self.calls_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Calls_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_calls_expr)
                        self.state = 215
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 216
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__31) | (1 << self.T__14) | (1 << self.T__6) | (1 << self.T__5))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 217 
                        localctx.right = self.calls_expr(4)
                        pass

             
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.primary_int = None # Token
            self.primary_str = None # Token
            self.primary_list = None # List_Context

        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

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
        self.enterRule(localctx, 28, self.RULE_element)
        try:
            self.state = 226
            token = self._input.LA(1)
            if token in [self.Integer]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                localctx.primary_int = self.match(self.Integer)

            elif token in [self.String]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                localctx.primary_str = self.match(self.String)

            elif token in [self.T__13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225 
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

    class Call_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.operand = None # Call_expressionContext
            self.call = None # Token
            self.argument = None # ElementContext
            self.abstract = None # Semantic_nodeContext

        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


        def call_expression(self):
            return self.getTypedRuleContext(cocoParser.Call_expressionContext,0)


        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def element(self):
            return self.getTypedRuleContext(cocoParser.ElementContext,0)


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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_call_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            localctx.call = self.match(self.Identifier)
            self.state = 237
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 230
                self.match(self.T__23)
                self.state = 233
                token = self._input.LA(1)
                if token in [self.T__13, self.Integer, self.String]:
                    self.state = 231 
                    localctx.argument = self.element()

                elif token in [self.T__23, self.T__1, self.Identifier]:
                    self.state = 232 
                    localctx.abstract = self.semantic_node()

                else:
                    raise NoViableAltException(self)

                self.state = 235
                self.match(self.T__3)


            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cocoParser.Call_expressionContext(self, _parentctx, _parentState)
                    localctx.operand = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_call_expression)
                    self.state = 239
                    if not self.precpred(self._ctx, 2):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 240
                    self.match(self.T__19)
                    self.state = 241
                    localctx.call = self.match(self.Identifier)
                    self.state = 249
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 242
                        self.match(self.T__23)
                        self.state = 245
                        token = self._input.LA(1)
                        if token in [self.T__13, self.Integer, self.String]:
                            self.state = 243 
                            localctx.argument = self.element()

                        elif token in [self.T__23, self.T__1, self.Identifier]:
                            self.state = 244 
                            localctx.abstract = self.semantic_node()

                        else:
                            raise NoViableAltException(self)

                        self.state = 247
                        self.match(self.T__3)

             
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_repeater)
        try:
            self.state = 264
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                localctx.exact = self.match(self.Integer)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                localctx.lower = self.match(self.Integer)
                self.state = 258
                self.match(self.T__20)
                self.state = 259
                localctx.upper = self.match(self.Integer)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.match(self.T__20)
                self.state = 261
                localctx.upper = self.match(self.Integer)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                localctx.lower = self.match(self.Integer)
                self.state = 263
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
        self.enterRule(localctx, 34, self.RULE_convention_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(self.T__28)
            self.state = 268 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 267 
                self.convention()
                self.state = 270 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__30) | (1 << self.T__24) | (1 << self.T__17))) != 0)):
                    break

            self.state = 272
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
        self.enterRule(localctx, 36, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(self.T__13)
            self.state = 275 
            self.list_element()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__20:
                self.state = 276
                self.match(self.T__20)
                self.state = 277 
                self.list_element()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 283
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
        self.enterRule(localctx, 38, self.RULE_list_element)
        try:
            self.state = 289
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                localctx.element_int = self.match(self.Integer)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                localctx.element_str = self.match(self.String)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287 
                localctx.element_desc = self.semantic_node()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 288
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
        self._predicates[11] = self.logic_expr_sempred
        self._predicates[13] = self.calls_expr_sempred
        self._predicates[15] = self.call_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def calls_expr_sempred(self, localctx:Calls_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

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
         



