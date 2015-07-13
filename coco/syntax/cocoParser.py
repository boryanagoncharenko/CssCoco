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
        buf.write("\u012d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\7\2,\n\2\f\2\16\2/\13\2\3\3\3")
        buf.write("\3\3\3\7\3\64\n\3\f\3\16\3\67\13\3\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5K\n\5\3\6\3\6\3\6\7\6P\n\6\f\6\16\6S\13\6\3\6\3\6\7")
        buf.write("\6W\n\6\f\6\16\6Z\13\6\5\6\\\n\6\3\7\3\7\5\7`\n\7\3\7")
        buf.write("\3\7\5\7d\n\7\3\b\3\b\3\b\3\b\3\b\5\bk\n\b\3\t\3\t\3\t")
        buf.write("\3\t\5\tq\n\t\3\t\3\t\3\t\6\tv\n\t\r\t\16\tw\7\tz\n\t")
        buf.write("\f\t\16\t}\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u0089\n\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u0091\n\n")
        buf.write("\f\n\16\n\u0094\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a4\n\13\3")
        buf.write("\13\3\13\3\13\5\13\u00a9\n\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00bd\n\13\3\13\3\13\5\13\u00c1\n\13\7")
        buf.write("\13\u00c3\n\13\f\13\16\13\u00c6\13\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00d6\n\f")
        buf.write("\3\r\3\r\5\r\u00da\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u00e5\n\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00ef\n\17\3\17\3\17\5\17\u00f3\n")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00f9\n\17\3\17\3\17\5\17")
        buf.write("\u00fd\n\17\5\17\u00ff\n\17\3\20\3\20\3\20\3\21\3\21\6")
        buf.write("\21\u0106\n\21\r\21\16\21\u0107\3\21\3\21\3\22\3\22\3")
        buf.write("\22\7\22\u010f\n\22\f\22\16\22\u0112\13\22\3\23\3\23\3")
        buf.write("\23\5\23\u0117\n\23\3\23\5\23\u011a\n\23\3\24\3\24\3\24")
        buf.write("\3\24\7\24\u0120\n\24\f\24\16\24\u0123\13\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u012b\n\25\3\25\2\5\20\22\24")
        buf.write("\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(\2\5\3")
        buf.write("\2!#\6\2\5\5\t\t\26\30\32\32\6\2\3\3\r\r\24\24\34\35\u014b")
        buf.write("\2-\3\2\2\2\4\60\3\2\2\2\6:\3\2\2\2\bJ\3\2\2\2\nL\3\2")
        buf.write("\2\2\fc\3\2\2\2\16e\3\2\2\2\20p\3\2\2\2\22\u0088\3\2\2")
        buf.write("\2\24\u00a8\3\2\2\2\26\u00d5\3\2\2\2\30\u00d9\3\2\2\2")
        buf.write("\32\u00db\3\2\2\2\34\u00fe\3\2\2\2\36\u0100\3\2\2\2 \u0103")
        buf.write("\3\2\2\2\"\u010b\3\2\2\2$\u0113\3\2\2\2&\u011b\3\2\2\2")
        buf.write("(\u012a\3\2\2\2*,\5\4\3\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2")
        buf.write("\2-.\3\2\2\2.\3\3\2\2\2/-\3\2\2\2\60\61\7$\2\2\61\65\7")
        buf.write("\6\2\2\62\64\5\6\4\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63")
        buf.write("\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\7\b")
        buf.write("\2\29\5\3\2\2\2:;\5\b\5\2;\7\3\2\2\2<=\7\n\2\2=>\5\n\6")
        buf.write("\2>?\5\36\20\2?K\3\2\2\2@A\7\4\2\2AB\5\24\13\2BC\5\36")
        buf.write("\20\2CK\3\2\2\2DE\7\21\2\2EF\5\n\6\2FG\7\4\2\2GH\5\24")
        buf.write("\13\2HI\5\36\20\2IK\3\2\2\2J<\3\2\2\2J@\3\2\2\2JD\3\2")
        buf.write("\2\2K\t\3\2\2\2L[\5\f\7\2MN\7\35\2\2NP\5\f\7\2OM\3\2\2")
        buf.write("\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\\\3\2\2\2SQ\3\2\2\2")
        buf.write("TU\7\23\2\2UW\5\f\7\2VT\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY")
        buf.write("\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2[Q\3\2\2\2[X\3\2\2\2\\\13")
        buf.write("\3\2\2\2]^\7$\2\2^`\7\7\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2")
        buf.write("\2\2ad\5\16\b\2bd\5\20\t\2c_\3\2\2\2cb\3\2\2\2d\r\3\2")
        buf.write("\2\2ej\5\22\n\2fg\7\6\2\2gh\5\24\13\2hi\7\b\2\2ik\3\2")
        buf.write("\2\2jf\3\2\2\2jk\3\2\2\2k\17\3\2\2\2lm\b\t\1\2mn\7$\2")
        buf.write("\2nq\5\32\16\2oq\7$\2\2pl\3\2\2\2po\3\2\2\2q{\3\2\2\2")
        buf.write("ru\f\5\2\2st\7\33\2\2tv\5\20\t\2us\3\2\2\2vw\3\2\2\2w")
        buf.write("u\3\2\2\2wx\3\2\2\2xz\3\2\2\2yr\3\2\2\2z}\3\2\2\2{y\3")
        buf.write("\2\2\2{|\3\2\2\2|\21\3\2\2\2}{\3\2\2\2~\177\b\n\1\2\177")
        buf.write("\u0080\7\"\2\2\u0080\u0089\5\22\n\7\u0081\u0082\7\13\2")
        buf.write("\2\u0082\u0083\5\22\n\2\u0083\u0084\7\37\2\2\u0084\u0089")
        buf.write("\3\2\2\2\u0085\u0086\7$\2\2\u0086\u0089\5\32\16\2\u0087")
        buf.write("\u0089\7$\2\2\u0088~\3\2\2\2\u0088\u0081\3\2\2\2\u0088")
        buf.write("\u0085\3\2\2\2\u0088\u0087\3\2\2\2\u0089\u0092\3\2\2\2")
        buf.write("\u008a\u008b\f\6\2\2\u008b\u008c\7 \2\2\u008c\u0091\5")
        buf.write("\22\n\7\u008d\u008e\f\5\2\2\u008e\u008f\7\33\2\2\u008f")
        buf.write("\u0091\5\22\n\6\u0090\u008a\3\2\2\2\u0090\u008d\3\2\2")
        buf.write("\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\23\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096")
        buf.write("\b\13\1\2\u0096\u0097\t\2\2\2\u0097\u00a9\5\24\13\r\u0098")
        buf.write("\u0099\7\13\2\2\u0099\u009a\5\24\13\2\u009a\u009b\7\37")
        buf.write("\2\2\u009b\u00a9\3\2\2\2\u009c\u00a9\5&\24\2\u009d\u00a9")
        buf.write("\7&\2\2\u009e\u00a9\7%\2\2\u009f\u00a0\7$\2\2\u00a0\u00a3")
        buf.write("\7\13\2\2\u00a1\u00a4\5\24\13\2\u00a2\u00a4\5\16\b\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a6\7\37\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a9")
        buf.write("\7$\2\2\u00a8\u0095\3\2\2\2\u00a8\u0098\3\2\2\2\u00a8")
        buf.write("\u009c\3\2\2\2\u00a8\u009d\3\2\2\2\u00a8\u009e\3\2\2\2")
        buf.write("\u00a8\u009f\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00c4\3")
        buf.write("\2\2\2\u00aa\u00ab\f\f\2\2\u00ab\u00ac\t\3\2\2\u00ac\u00c3")
        buf.write("\5\24\13\r\u00ad\u00ae\f\13\2\2\u00ae\u00af\t\4\2\2\u00af")
        buf.write("\u00c3\5\24\13\f\u00b0\u00b1\f\t\2\2\u00b1\u00b2\7 \2")
        buf.write("\2\u00b2\u00c3\5\24\13\n\u00b3\u00b4\f\b\2\2\u00b4\u00b5")
        buf.write("\7\33\2\2\u00b5\u00c3\5\24\13\t\u00b6\u00b7\f\n\2\2\u00b7")
        buf.write("\u00b8\7\17\2\2\u00b8\u00c0\7$\2\2\u00b9\u00bc\7\13\2")
        buf.write("\2\u00ba\u00bd\5\24\13\2\u00bb\u00bd\5\16\b\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\7\37\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00b9\3\2\2")
        buf.write("\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00aa")
        buf.write("\3\2\2\2\u00c2\u00ad\3\2\2\2\u00c2\u00b0\3\2\2\2\u00c2")
        buf.write("\u00b3\3\2\2\2\u00c2\u00b6\3\2\2\2\u00c3\u00c6\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\25\3\2")
        buf.write("\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\5\20\t\2\u00c8\u00c9")
        buf.write("\7\22\2\2\u00c9\u00ca\5\30\r\2\u00ca\u00d6\3\2\2\2\u00cb")
        buf.write("\u00cc\5\20\t\2\u00cc\u00cd\7\20\2\2\u00cd\u00ce\5\30")
        buf.write("\r\2\u00ce\u00d6\3\2\2\2\u00cf\u00d0\5\20\t\2\u00d0\u00d1")
        buf.write("\7\f\2\2\u00d1\u00d2\5\30\r\2\u00d2\u00d3\7 \2\2\u00d3")
        buf.write("\u00d4\5\30\r\2\u00d4\u00d6\3\2\2\2\u00d5\u00c7\3\2\2")
        buf.write("\2\u00d5\u00cb\3\2\2\2\u00d5\u00cf\3\2\2\2\u00d6\27\3")
        buf.write("\2\2\2\u00d7\u00da\5\16\b\2\u00d8\u00da\5\34\17\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\31\3\2\2\2\u00db")
        buf.write("\u00e4\7\6\2\2\u00dc\u00e5\7%\2\2\u00dd\u00de\7%\2\2\u00de")
        buf.write("\u00df\7\16\2\2\u00df\u00e5\7%\2\2\u00e0\u00e1\7\16\2")
        buf.write("\2\u00e1\u00e5\7%\2\2\u00e2\u00e3\7%\2\2\u00e3\u00e5\7")
        buf.write("\16\2\2\u00e4\u00dc\3\2\2\2\u00e4\u00dd\3\2\2\2\u00e4")
        buf.write("\u00e0\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\3\2\2\2")
        buf.write("\u00e6\u00e7\7\b\2\2\u00e7\33\3\2\2\2\u00e8\u00e9\5\24")
        buf.write("\13\2\u00e9\u00ea\7\17\2\2\u00ea\u00f2\7$\2\2\u00eb\u00ee")
        buf.write("\7\13\2\2\u00ec\u00ef\5\24\13\2\u00ed\u00ef\5\16\b\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f1\7\37\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00eb")
        buf.write("\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00ff\3\2\2\2\u00f4")
        buf.write("\u00fc\7$\2\2\u00f5\u00f8\7\13\2\2\u00f6\u00f9\5\24\13")
        buf.write("\2\u00f7\u00f9\5\16\b\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\7\37\2\2\u00fb")
        buf.write("\u00fd\3\2\2\2\u00fc\u00f5\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\u00ff\3\2\2\2\u00fe\u00e8\3\2\2\2\u00fe\u00f4\3")
        buf.write("\2\2\2\u00ff\35\3\2\2\2\u0100\u0101\7\36\2\2\u0101\u0102")
        buf.write("\7&\2\2\u0102\37\3\2\2\2\u0103\u0105\7\6\2\2\u0104\u0106")
        buf.write("\5\b\5\2\u0105\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2")
        buf.write("\u0109\u010a\7\b\2\2\u010a!\3\2\2\2\u010b\u0110\7$\2\2")
        buf.write("\u010c\u010d\7\17\2\2\u010d\u010f\5\"\22\2\u010e\u010c")
        buf.write("\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111#\3\2\2\2\u0112\u0110\3\2\2\2\u0113")
        buf.write("\u0119\7$\2\2\u0114\u0116\7\13\2\2\u0115\u0117\5\24\13")
        buf.write("\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\u011a\7\37\2\2\u0119\u0114\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a%\3\2\2\2\u011b\u011c\7\25\2\2\u011c")
        buf.write("\u0121\5(\25\2\u011d\u011e\7\16\2\2\u011e\u0120\5(\25")
        buf.write("\2\u011f\u011d\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0124\u0125\7\31\2\2\u0125\'\3\2\2\2\u0126")
        buf.write("\u012b\7%\2\2\u0127\u012b\7&\2\2\u0128\u012b\5\16\b\2")
        buf.write("\u0129\u012b\7$\2\2\u012a\u0126\3\2\2\2\u012a\u0127\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b)")
        buf.write("\3\2\2\2%-\65JQX[_cjpw{\u0088\u0090\u0092\u00a3\u00a8")
        buf.write("\u00bc\u00c0\u00c2\u00c4\u00d5\u00d9\u00e4\u00ee\u00f2")
        buf.write("\u00f8\u00fc\u00fe\u0107\u0110\u0116\u0119\u0121\u012a")
        return buf.getvalue()
		

class cocoParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__32=1
    T__31=2
    T__30=3
    T__29=4
    T__28=5
    T__27=6
    T__26=7
    T__25=8
    T__24=9
    T__23=10
    T__22=11
    T__21=12
    T__20=13
    T__19=14
    T__18=15
    T__17=16
    T__16=17
    T__15=18
    T__14=19
    T__13=20
    T__12=21
    T__11=22
    T__10=23
    T__9=24
    T__8=25
    T__7=26
    T__6=27
    T__5=28
    T__4=29
    T__3=30
    T__2=31
    T__1=32
    T__0=33
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
                   "')'", "'and'", "'+'", "'not'", "'-'", "Identifier", 
                   "Integer", "String", "Comment", "LineComment", "WS" ]

    RULE_stylesheet = 0
    RULE_context = 1
    RULE_declaration = 2
    RULE_convention = 3
    RULE_pattern = 4
    RULE_node = 5
    RULE_abstract_node = 6
    RULE_parse_node = 7
    RULE_type_expression = 8
    RULE_attr_expression = 9
    RULE_query_expression = 10
    RULE_whitespace_argument = 11
    RULE_repeater = 12
    RULE_call_expression = 13
    RULE_message = 14
    RULE_convention_group = 15
    RULE_api_call = 16
    RULE_method_call = 17
    RULE_list_ = 18
    RULE_list_element = 19

    ruleNames =  [ "stylesheet", "context", "declaration", "convention", 
                   "pattern", "node", "abstract_node", "parse_node", "type_expression", 
                   "attr_expression", "query_expression", "whitespace_argument", 
                   "repeater", "call_expression", "message", "convention_group", 
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
            self.match(self.T__29)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__31) | (1 << self.T__25) | (1 << self.T__18))) != 0):
                self.state = 48 
                self.declaration()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(self.T__27)
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
            self.state = 72
            token = self._input.LA(1)
            if token in [self.T__25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(self.T__25)
                self.state = 59 
                localctx.target = self.pattern()
                self.state = 60 
                localctx.msg = self.message()

            elif token in [self.T__31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(self.T__31)
                self.state = 63 
                localctx.requirement = self.attr_expression(0)
                self.state = 64 
                localctx.msg = self.message()

            elif token in [self.T__18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.match(self.T__18)
                self.state = 67 
                localctx.target = self.pattern()
                self.state = 68
                self.match(self.T__31)
                self.state = 69 
                localctx.requirement = self.attr_expression(0)
                self.state = 70 
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
            self.semantic = None # NodeContext
            self.relation = None # Token

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
            self.state = 74 
            localctx.semantic = self.node()
            self.state = 89
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cocoParser.T__6:
                    self.state = 75
                    localctx.relation = self.match(self.T__6)
                    self.state = 76 
                    self.node()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cocoParser.T__16:
                    self.state = 82
                    localctx.relation = self.match(self.T__16)
                    self.state = 83 
                    self.node()
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

    class NodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.decl = None # Token
            self.abstract = None # Abstract_nodeContext
            self.parse = None # Parse_nodeContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def abstract_node(self):
            return self.getTypedRuleContext(cocoParser.Abstract_nodeContext,0)


        def parse_node(self):
            return self.getTypedRuleContext(cocoParser.Parse_nodeContext,0)


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
        try:
            self.state = 97
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 91
                    localctx.decl = self.match(self.Identifier)
                    self.state = 92
                    self.match(self.T__28)


                self.state = 95 
                localctx.abstract = self.abstract_node()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96 
                localctx.parse = self.parse_node(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abstract_nodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node_type = None # Type_expressionContext
            self.constraint = None # Attr_expressionContext

        def attr_expression(self):
            return self.getTypedRuleContext(cocoParser.Attr_expressionContext,0)


        def type_expression(self):
            return self.getTypedRuleContext(cocoParser.Type_expressionContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_abstract_node

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitAbstract_node(self)
            else:
                return visitor.visitChildren(self)




    def abstract_node(self):

        localctx = cocoParser.Abstract_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_abstract_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            localctx.node_type = self.type_expression(0)
            self.state = 104
            _la = self._input.LA(1)
            if _la==cocoParser.T__29:
                self.state = 100
                self.match(self.T__29)
                self.state = 101 
                localctx.constraint = self.attr_expression(0)
                self.state = 102
                self.match(self.T__27)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parse_nodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.operand = None # Parse_nodeContext
            self.primary = None # Token
            self.quantifier = None # RepeaterContext
            self.right = None # Parse_nodeContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def parse_node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Parse_nodeContext)
            else:
                return self.getTypedRuleContext(cocoParser.Parse_nodeContext,i)


        def repeater(self):
            return self.getTypedRuleContext(cocoParser.RepeaterContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_parse_node

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitParse_node(self)
            else:
                return visitor.visitChildren(self)



    def parse_node(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cocoParser.Parse_nodeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_parse_node, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 107
                localctx.primary = self.match(self.Identifier)
                self.state = 108 
                localctx.quantifier = self.repeater()
                pass

            elif la_ == 2:
                self.state = 109
                localctx.primary = self.match(self.Identifier)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cocoParser.Parse_nodeContext(self, _parentctx, _parentState)
                    localctx.operand = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parse_node)
                    self.state = 112
                    if not self.precpred(self._ctx, 3):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 115 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 113
                            self.match(self.T__8)
                            self.state = 114 
                            localctx.right = self.parse_node(0)

                        else:
                            raise NoViableAltException(self)
                        self.state = 117 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
             
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def repeater(self):
            return self.getTypedRuleContext(cocoParser.RepeaterContext,0)


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
            self.state = 134
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 125
                localctx.operator = self.match(self.T__1)
                self.state = 126 
                localctx.operand = self.type_expression(5)
                pass

            elif la_ == 2:
                self.state = 127
                self.match(self.T__24)
                self.state = 128 
                localctx.parenthesis = self.type_expression(0)
                self.state = 129
                self.match(self.T__4)
                pass

            elif la_ == 3:
                self.state = 131
                localctx.primary = self.match(self.Identifier)
                self.state = 132 
                self.repeater()
                pass

            elif la_ == 4:
                self.state = 133
                localctx.primary = self.match(self.Identifier)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 142
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 136
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 137
                        localctx.operator = self.match(self.T__3)
                        self.state = 138 
                        localctx.right = self.type_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Type_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expression)
                        self.state = 139
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 140
                        localctx.operator = self.match(self.T__8)
                        self.state = 141 
                        localctx.right = self.type_expression(4)
                        pass

             
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            self.operand = None # Attr_expressionContext
            self.operator = None # Token
            self.parenthesis = None # Attr_expressionContext
            self.primary_list = None # List_Context
            self.primary_str = None # Token
            self.primary_int = None # Token
            self.primary_call = None # Token
            self.argument = None # Attr_expressionContext
            self.abstract = None # Abstract_nodeContext
            self.primary_id = None # Token
            self.right = None # Attr_expressionContext
            self.call = None # Token

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def attr_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Attr_expressionContext)
            else:
                return self.getTypedRuleContext(cocoParser.Attr_expressionContext,i)


        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def abstract_node(self):
            return self.getTypedRuleContext(cocoParser.Abstract_nodeContext,0)


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
            self.state = 166
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 148
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__2) | (1 << self.T__1) | (1 << self.T__0))) != 0)):
                    localctx.operator = self._errHandler.recoverInline(self)
                self.consume()
                self.state = 149 
                localctx.operand = self.attr_expression(11)
                pass

            elif la_ == 2:
                self.state = 150
                self.match(self.T__24)
                self.state = 151 
                localctx.parenthesis = self.attr_expression(0)
                self.state = 152
                self.match(self.T__4)
                pass

            elif la_ == 3:
                self.state = 154 
                localctx.primary_list = self.list_()
                pass

            elif la_ == 4:
                self.state = 155
                localctx.primary_str = self.match(self.String)
                pass

            elif la_ == 5:
                self.state = 156
                localctx.primary_int = self.match(self.Integer)
                pass

            elif la_ == 6:
                self.state = 157
                localctx.primary_call = self.match(self.Identifier)
                self.state = 158
                self.match(self.T__24)
                self.state = 161
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 159 
                    localctx.argument = self.attr_expression(0)
                    pass

                elif la_ == 2:
                    self.state = 160 
                    localctx.abstract = self.abstract_node()
                    pass


                self.state = 163
                self.match(self.T__4)
                pass

            elif la_ == 7:
                self.state = 165
                localctx.primary_id = self.match(self.Identifier)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 192
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 10):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 169
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__30) | (1 << self.T__26) | (1 << self.T__13) | (1 << self.T__12) | (1 << self.T__11) | (1 << self.T__9))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 170 
                        localctx.right = self.attr_expression(11)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 171
                        if not self.precpred(self._ctx, 9):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 172
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__32) | (1 << self.T__22) | (1 << self.T__15) | (1 << self.T__7) | (1 << self.T__6))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 173 
                        localctx.right = self.attr_expression(10)
                        pass

                    elif la_ == 3:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 174
                        if not self.precpred(self._ctx, 7):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 175
                        localctx.operator = self.match(self.T__3)
                        self.state = 176 
                        localctx.right = self.attr_expression(8)
                        pass

                    elif la_ == 4:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 177
                        if not self.precpred(self._ctx, 6):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 178
                        localctx.operator = self.match(self.T__8)
                        self.state = 179 
                        localctx.right = self.attr_expression(7)
                        pass

                    elif la_ == 5:
                        localctx = cocoParser.Attr_expressionContext(self, _parentctx, _parentState)
                        localctx.operand = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attr_expression)
                        self.state = 180
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 181
                        self.match(self.T__20)
                        self.state = 182
                        localctx.call = self.match(self.Identifier)
                        self.state = 190
                        la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                        if la_ == 1:
                            self.state = 183
                            self.match(self.T__24)
                            self.state = 186
                            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                            if la_ == 1:
                                self.state = 184 
                                localctx.argument = self.attr_expression(0)
                                pass

                            elif la_ == 2:
                                self.state = 185 
                                localctx.abstract = self.abstract_node()
                                pass


                            self.state = 188
                            self.match(self.T__4)


                        pass

             
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Query_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Parse_nodeContext
            self.operator = None # Token
            self.right = None # Whitespace_argumentContext
            self.first = None # Whitespace_argumentContext
            self.second = None # Whitespace_argumentContext

        def whitespace_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Whitespace_argumentContext)
            else:
                return self.getTypedRuleContext(cocoParser.Whitespace_argumentContext,i)


        def parse_node(self):
            return self.getTypedRuleContext(cocoParser.Parse_nodeContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_query_expression

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitQuery_expression(self)
            else:
                return visitor.visitChildren(self)




    def query_expression(self):

        localctx = cocoParser.Query_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_query_expression)
        try:
            self.state = 211
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197 
                localctx.left = self.parse_node(0)
                self.state = 198
                localctx.operator = self.match(self.T__17)
                self.state = 199 
                localctx.right = self.whitespace_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201 
                localctx.left = self.parse_node(0)
                self.state = 202
                localctx.operator = self.match(self.T__19)
                self.state = 203 
                localctx.right = self.whitespace_argument()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205 
                localctx.left = self.parse_node(0)
                self.state = 206
                localctx.operator = self.match(self.T__23)
                self.state = 207 
                localctx.first = self.whitespace_argument()
                self.state = 208
                self.match(self.T__3)
                self.state = 209 
                localctx.second = self.whitespace_argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Whitespace_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.abstract = None # Abstract_nodeContext
            self.call = None # Call_expressionContext

        def call_expression(self):
            return self.getTypedRuleContext(cocoParser.Call_expressionContext,0)


        def abstract_node(self):
            return self.getTypedRuleContext(cocoParser.Abstract_nodeContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_whitespace_argument

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitWhitespace_argument(self)
            else:
                return visitor.visitChildren(self)




    def whitespace_argument(self):

        localctx = cocoParser.Whitespace_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whitespace_argument)
        try:
            self.state = 215
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213 
                localctx.abstract = self.abstract_node()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214 
                localctx.call = self.call_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 24, self.RULE_repeater)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(self.T__29)
            self.state = 226
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 218
                localctx.exact = self.match(self.Integer)
                pass

            elif la_ == 2:
                self.state = 219
                localctx.lower = self.match(self.Integer)
                self.state = 220
                self.match(self.T__21)
                self.state = 221
                localctx.upper = self.match(self.Integer)
                pass

            elif la_ == 3:
                self.state = 222
                self.match(self.T__21)
                self.state = 223
                localctx.upper = self.match(self.Integer)
                pass

            elif la_ == 4:
                self.state = 224
                localctx.lower = self.match(self.Integer)
                self.state = 225
                self.match(self.T__21)
                pass


            self.state = 228
            self.match(self.T__27)
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
            self.operand = None # Attr_expressionContext
            self.call = None # Token
            self.argument = None # Attr_expressionContext
            self.abstract = None # Abstract_nodeContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def attr_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Attr_expressionContext)
            else:
                return self.getTypedRuleContext(cocoParser.Attr_expressionContext,i)


        def abstract_node(self):
            return self.getTypedRuleContext(cocoParser.Abstract_nodeContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_call_expression

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitCall_expression(self)
            else:
                return visitor.visitChildren(self)




    def call_expression(self):

        localctx = cocoParser.Call_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call_expression)
        self._la = 0 # Token type
        try:
            self.state = 252
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230 
                localctx.operand = self.attr_expression(0)
                self.state = 231
                self.match(self.T__20)
                self.state = 232
                localctx.call = self.match(self.Identifier)
                self.state = 240
                _la = self._input.LA(1)
                if _la==cocoParser.T__24:
                    self.state = 233
                    self.match(self.T__24)
                    self.state = 236
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        self.state = 234 
                        localctx.argument = self.attr_expression(0)
                        pass

                    elif la_ == 2:
                        self.state = 235 
                        localctx.abstract = self.abstract_node()
                        pass


                    self.state = 238
                    self.match(self.T__4)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                localctx.call = self.match(self.Identifier)
                self.state = 250
                _la = self._input.LA(1)
                if _la==cocoParser.T__24:
                    self.state = 243
                    self.match(self.T__24)
                    self.state = 246
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        self.state = 244 
                        localctx.argument = self.attr_expression(0)
                        pass

                    elif la_ == 2:
                        self.state = 245 
                        localctx.abstract = self.abstract_node()
                        pass


                    self.state = 248
                    self.match(self.T__4)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 28, self.RULE_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(self.T__5)
            self.state = 255
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
        self.enterRule(localctx, 30, self.RULE_convention_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(self.T__29)
            self.state = 259 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 258 
                self.convention()
                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__31) | (1 << self.T__25) | (1 << self.T__18))) != 0)):
                    break

            self.state = 263
            self.match(self.T__27)
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
        self.enterRule(localctx, 32, self.RULE_api_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(self.Identifier)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 266
                    self.match(self.T__20)
                    self.state = 267 
                    self.api_call() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            localctx.method_name = self.match(self.Identifier)
            self.state = 279
            _la = self._input.LA(1)
            if _la==cocoParser.T__24:
                self.state = 274
                self.match(self.T__24)
                self.state = 276
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__24) | (1 << self.T__14) | (1 << self.T__2) | (1 << self.T__1) | (1 << self.T__0) | (1 << self.Identifier) | (1 << self.Integer) | (1 << self.String))) != 0):
                    self.state = 275 
                    self.attr_expression(0)


                self.state = 278
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
        self.enterRule(localctx, 36, self.RULE_list_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(self.T__14)
            self.state = 282 
            self.list_element()
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__21:
                self.state = 283
                self.match(self.T__21)
                self.state = 284 
                self.list_element()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
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
            self.element_desc = None # Abstract_nodeContext
            self.element_id = None # Token

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def String(self):
            return self.getToken(cocoParser.String, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def abstract_node(self):
            return self.getTypedRuleContext(cocoParser.Abstract_nodeContext,0)


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
            self.state = 296
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                localctx.element_int = self.match(self.Integer)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                localctx.element_str = self.match(self.String)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294 
                localctx.element_desc = self.abstract_node()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
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
        self._predicates[7] = self.parse_node_sempred
        self._predicates[8] = self.type_expression_sempred
        self._predicates[9] = self.attr_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def attr_expression_sempred(self, localctx:Attr_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         

    def parse_node_sempred(self, localctx:Parse_nodeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def type_expression_sempred(self, localctx:Type_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         



