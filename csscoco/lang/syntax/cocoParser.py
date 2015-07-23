# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3*")
        buf.write("\u0128\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\7\2,\n\2\f\2\16\2/\13\2\3\3\3")
        buf.write("\3\5\3\63\n\3\3\3\3\3\7\3\67\n\3\f\3\16\3:\13\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4O\n\4\3\5\3\5\3\5\7\5T\n\5\f\5\16")
        buf.write("\5W\13\5\3\5\3\5\3\5\7\5\\\n\5\f\5\16\5_\13\5\5\5a\n\5")
        buf.write("\3\6\3\6\3\6\3\6\6\6g\n\6\r\6\16\6h\3\6\3\6\3\7\3\7\5")
        buf.write("\7o\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\bx\n\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\t\u0082\n\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\7\t\u008a\n\t\f\t\16\t\u008d\13\t\3\n\3\n\3\n\7")
        buf.write("\n\u0092\n\n\f\n\16\n\u0095\13\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13\u009c\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00a7\n\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00af\n\f")
        buf.write("\f\f\16\f\u00b2\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c2\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00c9\n\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u00d1\n\16\f\16\16\16\u00d4\13\16\3\17\3\17\3\17")
        buf.write("\5\17\u00d9\n\17\3\20\3\20\3\20\3\20\5\20\u00df\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u00e6\n\21\3\21\3\21\5\21")
        buf.write("\u00ea\n\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00f2\n")
        buf.write("\21\3\21\3\21\5\21\u00f6\n\21\7\21\u00f8\n\21\f\21\16")
        buf.write("\21\u00fb\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u0105\n\22\3\23\3\23\6\23\u0109\n\23\r\23\16\23")
        buf.write("\u010a\3\23\3\23\6\23\u010f\n\23\r\23\16\23\u0110\7\23")
        buf.write("\u0113\n\23\f\23\16\23\u0116\13\23\3\24\3\24\3\24\3\24")
        buf.write("\7\24\u011c\n\24\f\24\16\24\u011f\13\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\5\25\u0126\n\25\3\25\2\6\20\26\32 \26\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(\2\7\4\2\5\5\7")
        buf.write("\7\3\2\t\n\3\2\23\24\3\2\27\34\4\2\t\t\35\37\u0141\2-")
        buf.write("\3\2\2\2\4\60\3\2\2\2\6N\3\2\2\2\b`\3\2\2\2\nb\3\2\2\2")
        buf.write("\fn\3\2\2\2\16r\3\2\2\2\20\u0081\3\2\2\2\22\u008e\3\2")
        buf.write("\2\2\24\u0096\3\2\2\2\26\u00a6\3\2\2\2\30\u00c1\3\2\2")
        buf.write("\2\32\u00c8\3\2\2\2\34\u00d8\3\2\2\2\36\u00de\3\2\2\2")
        buf.write(" \u00e0\3\2\2\2\"\u0104\3\2\2\2$\u0106\3\2\2\2&\u0117")
        buf.write("\3\2\2\2(\u0125\3\2\2\2*,\5\4\3\2+*\3\2\2\2,/\3\2\2\2")
        buf.write("-+\3\2\2\2-.\3\2\2\2.\3\3\2\2\2/-\3\2\2\2\60\62\7%\2\2")
        buf.write("\61\63\5$\23\2\62\61\3\2\2\2\62\63\3\2\2\2\63\64\3\2\2")
        buf.write("\2\648\7\3\2\2\65\67\5\6\4\2\66\65\3\2\2\2\67:\3\2\2\2")
        buf.write("8\66\3\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2\2;<\7\4\2\2<")
        buf.write("\5\3\2\2\2=>\7\5\2\2>?\5\b\5\2?@\7\6\2\2@A\7\'\2\2AO\3")
        buf.write("\2\2\2BC\7\7\2\2CD\5\26\f\2DE\7\6\2\2EF\7\'\2\2FO\3\2")
        buf.write("\2\2GH\7\b\2\2HI\5\b\5\2IJ\t\2\2\2JK\5\26\f\2KL\7\6\2")
        buf.write("\2LM\7\'\2\2MO\3\2\2\2N=\3\2\2\2NB\3\2\2\2NG\3\2\2\2O")
        buf.write("\7\3\2\2\2PU\5\f\7\2QR\t\3\2\2RT\5\f\7\2SQ\3\2\2\2TW\3")
        buf.write("\2\2\2US\3\2\2\2UV\3\2\2\2Va\3\2\2\2WU\3\2\2\2X]\5\n\6")
        buf.write("\2YZ\7\t\2\2Z\\\5\f\7\2[Y\3\2\2\2\\_\3\2\2\2][\3\2\2\2")
        buf.write("]^\3\2\2\2^a\3\2\2\2_]\3\2\2\2`P\3\2\2\2`X\3\2\2\2a\t")
        buf.write("\3\2\2\2bc\7\13\2\2cf\5\f\7\2de\7\f\2\2eg\5\f\7\2fd\3")
        buf.write("\2\2\2gh\3\2\2\2hf\3\2\2\2hi\3\2\2\2ij\3\2\2\2jk\7\r\2")
        buf.write("\2k\13\3\2\2\2lm\7%\2\2mo\7\16\2\2nl\3\2\2\2no\3\2\2\2")
        buf.write("op\3\2\2\2pq\5\16\b\2q\r\3\2\2\2rw\5\20\t\2st\7\3\2\2")
        buf.write("tu\5\26\f\2uv\7\4\2\2vx\3\2\2\2ws\3\2\2\2wx\3\2\2\2x\17")
        buf.write("\3\2\2\2yz\b\t\1\2z{\7\17\2\2{\u0082\5\20\t\6|}\7\13\2")
        buf.write("\2}~\5\20\t\2~\177\7\r\2\2\177\u0082\3\2\2\2\u0080\u0082")
        buf.write("\7%\2\2\u0081y\3\2\2\2\u0081|\3\2\2\2\u0081\u0080\3\2")
        buf.write("\2\2\u0082\u008b\3\2\2\2\u0083\u0084\f\5\2\2\u0084\u0085")
        buf.write("\7\20\2\2\u0085\u008a\5\20\t\6\u0086\u0087\f\4\2\2\u0087")
        buf.write("\u0088\7\21\2\2\u0088\u008a\5\20\t\5\u0089\u0083\3\2\2")
        buf.write("\2\u0089\u0086\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\21\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008e\u0093\5\24\13\2\u008f\u0090\7\21\2\2\u0090")
        buf.write("\u0092\5\24\13\2\u0091\u008f\3\2\2\2\u0092\u0095\3\2\2")
        buf.write("\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\23\3")
        buf.write("\2\2\2\u0095\u0093\3\2\2\2\u0096\u009b\7%\2\2\u0097\u0098")
        buf.write("\7\3\2\2\u0098\u0099\5\"\22\2\u0099\u009a\7\4\2\2\u009a")
        buf.write("\u009c\3\2\2\2\u009b\u0097\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c\25\3\2\2\2\u009d\u009e\b\f\1\2\u009e\u009f\7\17")
        buf.write("\2\2\u009f\u00a7\5\26\f\7\u00a0\u00a1\7\13\2\2\u00a1\u00a2")
        buf.write("\5\26\f\2\u00a2\u00a3\7\r\2\2\u00a3\u00a7\3\2\2\2\u00a4")
        buf.write("\u00a7\5\30\r\2\u00a5\u00a7\5\32\16\2\u00a6\u009d\3\2")
        buf.write("\2\2\u00a6\u00a0\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\u00b0\3\2\2\2\u00a8\u00a9\f\6\2\2\u00a9")
        buf.write("\u00aa\7\20\2\2\u00aa\u00af\5\26\f\7\u00ab\u00ac\f\5\2")
        buf.write("\2\u00ac\u00ad\7\21\2\2\u00ad\u00af\5\26\f\6\u00ae\u00a8")
        buf.write("\3\2\2\2\u00ae\u00ab\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0")
        buf.write("\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\27\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b3\u00b4\5\32\16\2\u00b4\u00b5\7\22")
        buf.write("\2\2\u00b5\u00b6\5\16\b\2\u00b6\u00c2\3\2\2\2\u00b7\u00b8")
        buf.write("\5\22\n\2\u00b8\u00b9\t\4\2\2\u00b9\u00ba\5 \21\2\u00ba")
        buf.write("\u00c2\3\2\2\2\u00bb\u00bc\5\22\n\2\u00bc\u00bd\7\25\2")
        buf.write("\2\u00bd\u00be\5 \21\2\u00be\u00bf\7\20\2\2\u00bf\u00c0")
        buf.write("\5 \21\2\u00c0\u00c2\3\2\2\2\u00c1\u00b3\3\2\2\2\u00c1")
        buf.write("\u00b7\3\2\2\2\u00c1\u00bb\3\2\2\2\u00c2\31\3\2\2\2\u00c3")
        buf.write("\u00c4\b\16\1\2\u00c4\u00c5\7\26\2\2\u00c5\u00c9\5\32")
        buf.write("\16\7\u00c6\u00c9\5 \21\2\u00c7\u00c9\5\36\20\2\u00c8")
        buf.write("\u00c3\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2")
        buf.write("\u00c9\u00d2\3\2\2\2\u00ca\u00cb\f\6\2\2\u00cb\u00cc\t")
        buf.write("\5\2\2\u00cc\u00d1\5\32\16\7\u00cd\u00ce\f\5\2\2\u00ce")
        buf.write("\u00cf\t\6\2\2\u00cf\u00d1\5\32\16\6\u00d0\u00ca\3\2\2")
        buf.write("\2\u00d0\u00cd\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\33\3\2\2\2\u00d4\u00d2")
        buf.write("\3\2\2\2\u00d5\u00d6\7\26\2\2\u00d6\u00d9\5\32\16\2\u00d7")
        buf.write("\u00d9\5\36\20\2\u00d8\u00d5\3\2\2\2\u00d8\u00d7\3\2\2")
        buf.write("\2\u00d9\35\3\2\2\2\u00da\u00df\7$\2\2\u00db\u00df\7&")
        buf.write("\2\2\u00dc\u00df\7\'\2\2\u00dd\u00df\5&\24\2\u00de\u00da")
        buf.write("\3\2\2\2\u00de\u00db\3\2\2\2\u00de\u00dc\3\2\2\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00df\37\3\2\2\2\u00e0\u00e1\b\21\1\2\u00e1")
        buf.write("\u00e9\7%\2\2\u00e2\u00e5\7\13\2\2\u00e3\u00e6\5\34\17")
        buf.write("\2\u00e4\u00e6\5\16\b\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\7\r\2\2\u00e8")
        buf.write("\u00ea\3\2\2\2\u00e9\u00e2\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00f9\3\2\2\2\u00eb\u00ec\f\4\2\2\u00ec\u00ed\7")
        buf.write(" \2\2\u00ed\u00f5\7%\2\2\u00ee\u00f1\7\13\2\2\u00ef\u00f2")
        buf.write("\5\34\17\2\u00f0\u00f2\5\16\b\2\u00f1\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\7\r\2\2")
        buf.write("\u00f4\u00f6\3\2\2\2\u00f5\u00ee\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00eb\3\2\2\2\u00f8\u00fb")
        buf.write("\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("!\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u0105\7&\2\2\u00fd")
        buf.write("\u00fe\7&\2\2\u00fe\u00ff\7\f\2\2\u00ff\u0105\7&\2\2\u0100")
        buf.write("\u0101\7\f\2\2\u0101\u0105\7&\2\2\u0102\u0103\7&\2\2\u0103")
        buf.write("\u0105\7\f\2\2\u0104\u00fc\3\2\2\2\u0104\u00fd\3\2\2\2")
        buf.write("\u0104\u0100\3\2\2\2\u0104\u0102\3\2\2\2\u0105#\3\2\2")
        buf.write("\2\u0106\u0108\7!\2\2\u0107\u0109\5\24\13\2\u0108\u0107")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0108\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u0114\3\2\2\2\u010c\u010e\7\f\2\2")
        buf.write("\u010d\u010f\5\24\13\2\u010e\u010d\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0113\3\2\2\2\u0112\u010c\3\2\2\2\u0113\u0116\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115%\3\2\2")
        buf.write("\2\u0116\u0114\3\2\2\2\u0117\u0118\7\"\2\2\u0118\u011d")
        buf.write("\5(\25\2\u0119\u011a\7\f\2\2\u011a\u011c\5(\25\2\u011b")
        buf.write("\u0119\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e\u0120\3\2\2\2\u011f\u011d\3")
        buf.write("\2\2\2\u0120\u0121\7#\2\2\u0121\'\3\2\2\2\u0122\u0126")
        buf.write("\7&\2\2\u0123\u0126\7\'\2\2\u0124\u0126\5\16\b\2\u0125")
        buf.write("\u0122\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2")
        buf.write("\u0126)\3\2\2\2%-\628NU]`hnw\u0081\u0089\u008b\u0093\u009b")
        buf.write("\u00a6\u00ae\u00b0\u00c1\u00c8\u00d0\u00d2\u00d8\u00de")
        buf.write("\u00e5\u00e9\u00f1\u00f5\u00f9\u0104\u010a\u0110\u0114")
        buf.write("\u011d\u0125")
        return buf.getvalue()


class cocoParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"'forbid'", u"'message'", 
                     u"'require'", u"'find'", u"'in'", u"'next-to'", u"'('", 
                     u"','", u"')'", u"'='", u"'not'", u"'and'", u"'or'", 
                     u"'is'", u"'before'", u"'after'", u"'between'", u"'-'", 
                     u"'<'", u"'>'", u"'<='", u"'>='", u"'=='", u"'!='", 
                     u"'not in'", u"'match'", u"'not match'", u"'.'", u"'ignore'", 
                     u"'['", u"']'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"Boolean", u"Identifier", 
                      u"Integer", u"String", u"Comment", u"LineComment", 
                      u"WS" ]

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
    RULE_basic_expr = 13
    RULE_element = 14
    RULE_call_expr = 15
    RULE_repeater = 16
    RULE_ignore_clause = 17
    RULE_list_ = 18
    RULE_list_element = 19

    ruleNames =  [ "stylesheet", "context", "convention", "pattern", "fork_pattern", 
                   "node_declaration", "semantic_node", "node_type", "whitespace_variation", 
                   "whitespace_node", "logic_expr", "type_expr", "arithmetic_expr", 
                   "basic_expr", "element", "call_expr", "repeater", "ignore_clause", 
                   "list_", "list_element" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    Boolean=34
    Identifier=35
    Integer=36
    String=37
    Comment=38
    LineComment=39
    WS=40

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
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
            self.ignore = None # Ignore_clauseContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def convention(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.ConventionContext)
            else:
                return self.getTypedRuleContext(cocoParser.ConventionContext,i)


        def ignore_clause(self):
            return self.getTypedRuleContext(cocoParser.Ignore_clauseContext,0)


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
            localctx.name = self.match(cocoParser.Identifier)
            self.state = 48
            _la = self._input.LA(1)
            if _la==cocoParser.T__30:
                self.state = 47
                localctx.ignore = self.ignore_clause()


            self.state = 50
            self.match(cocoParser.T__0)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cocoParser.T__2) | (1 << cocoParser.T__4) | (1 << cocoParser.T__5))) != 0):
                self.state = 51
                self.convention()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(cocoParser.T__1)
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
            self.state = 76
            token = self._input.LA(1)
            if token in [cocoParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                localctx.action = self.match(cocoParser.T__2)
                self.state = 60
                localctx.target = self.pattern()
                self.state = 61
                self.match(cocoParser.T__3)
                self.state = 62
                localctx.message = self.match(cocoParser.String)

            elif token in [cocoParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                localctx.action = self.match(cocoParser.T__4)
                self.state = 65
                localctx.requirement = self.logic_expr(0)
                self.state = 66
                self.match(cocoParser.T__3)
                self.state = 67
                localctx.message = self.match(cocoParser.String)

            elif token in [cocoParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                localctx.find = self.match(cocoParser.T__5)
                self.state = 70
                localctx.target = self.pattern()
                self.state = 71
                localctx.action = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==cocoParser.T__2 or _la==cocoParser.T__4):
                    localctx.action = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 72
                localctx.requirement = self.logic_expr(0)
                self.state = 73
                self.match(cocoParser.T__3)
                self.state = 74
                localctx.message = self.match(cocoParser.String)

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
            self.state = 94
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                localctx.simple = self.node_declaration()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cocoParser.T__6 or _la==cocoParser.T__7:
                    self.state = 79
                    localctx.relation = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==cocoParser.T__6 or _la==cocoParser.T__7):
                        localctx.relation = self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 80
                    self.node_declaration()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                localctx.fork = self.fork_pattern()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cocoParser.T__6:
                    self.state = 87
                    localctx.relation = self.match(cocoParser.T__6)
                    self.state = 88
                    self.node_declaration()
                    self.state = 93
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
            self.state = 96
            self.match(cocoParser.T__8)
            self.state = 97
            self.node_declaration()
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.match(cocoParser.T__9)
                self.state = 99
                self.node_declaration()
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cocoParser.T__9):
                    break

            self.state = 104
            self.match(cocoParser.T__10)
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
            self.state = 108
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 106
                localctx.variable = self.match(cocoParser.Identifier)
                self.state = 107
                self.match(cocoParser.T__11)


            self.state = 110
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
            self.state = 112
            localctx.type_ = self.node_type(0)
            self.state = 117
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 113
                self.match(cocoParser.T__0)
                self.state = 114
                localctx.constraint = self.logic_expr(0)
                self.state = 115
                self.match(cocoParser.T__1)


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

        def node_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Node_typeContext)
            else:
                return self.getTypedRuleContext(cocoParser.Node_typeContext,i)


        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

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
            self.state = 127
            token = self._input.LA(1)
            if token in [cocoParser.T__12]:
                self.state = 120
                localctx.operator = self.match(cocoParser.T__12)
                self.state = 121
                localctx.operand = self.node_type(4)

            elif token in [cocoParser.T__8]:
                self.state = 122
                self.match(cocoParser.T__8)
                self.state = 123
                localctx.parenthesis = self.node_type(0)
                self.state = 124
                self.match(cocoParser.T__10)

            elif token in [cocoParser.Identifier]:
                self.state = 126
                localctx.primary = self.match(cocoParser.Identifier)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 135
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Node_typeContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_node_type)
                        self.state = 129
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 130
                        localctx.operator = self.match(cocoParser.T__13)
                        self.state = 131
                        localctx.right = self.node_type(4)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Node_typeContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_node_type)
                        self.state = 132
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 133
                        localctx.operator = self.match(cocoParser.T__14)
                        self.state = 134
                        localctx.right = self.node_type(3)
                        pass

             
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            self.state = 140
            self.whitespace_node()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__14:
                self.state = 141
                self.match(cocoParser.T__14)
                self.state = 142
                self.whitespace_node()
                self.state = 147
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            localctx.type_ = self.match(cocoParser.Identifier)
            self.state = 153
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 149
                self.match(cocoParser.T__0)
                self.state = 150
                localctx.quantifier = self.repeater()
                self.state = 151
                self.match(cocoParser.T__1)


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

        def logic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Logic_exprContext)
            else:
                return self.getTypedRuleContext(cocoParser.Logic_exprContext,i)


        def type_expr(self):
            return self.getTypedRuleContext(cocoParser.Type_exprContext,0)


        def arithmetic_expr(self):
            return self.getTypedRuleContext(cocoParser.Arithmetic_exprContext,0)


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
            self.state = 164
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 156
                localctx.operator = self.match(cocoParser.T__12)
                self.state = 157
                localctx.operand = self.logic_expr(5)
                pass

            elif la_ == 2:
                self.state = 158
                self.match(cocoParser.T__8)
                self.state = 159
                localctx.parenthesis = self.logic_expr(0)
                self.state = 160
                self.match(cocoParser.T__10)
                pass

            elif la_ == 3:
                self.state = 162
                localctx.type_ = self.type_expr()
                pass

            elif la_ == 4:
                self.state = 163
                localctx.call = self.arithmetic_expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 172
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Logic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 167
                        localctx.operator = self.match(cocoParser.T__13)
                        self.state = 168
                        localctx.right = self.logic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Logic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 170
                        localctx.operator = self.match(cocoParser.T__14)
                        self.state = 171
                        localctx.right = self.logic_expr(4)
                        pass

             
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.target_type = None # Semantic_nodeContext
            self.variation = None # Whitespace_variationContext
            self.second_operand = None # Call_exprContext

        def arithmetic_expr(self):
            return self.getTypedRuleContext(cocoParser.Arithmetic_exprContext,0)


        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


        def whitespace_variation(self):
            return self.getTypedRuleContext(cocoParser.Whitespace_variationContext,0)


        def call_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Call_exprContext)
            else:
                return self.getTypedRuleContext(cocoParser.Call_exprContext,i)


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
            self.state = 191
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                localctx.operand = self.arithmetic_expr(0)
                self.state = 178
                localctx.operator = self.match(cocoParser.T__15)
                self.state = 179
                localctx.target_type = self.semantic_node()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                localctx.variation = self.whitespace_variation()
                self.state = 182
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==cocoParser.T__16 or _la==cocoParser.T__17):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 183
                localctx.operand = self.call_expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                localctx.variation = self.whitespace_variation()
                self.state = 186
                localctx.operator = self.match(cocoParser.T__18)
                self.state = 187
                localctx.operand = self.call_expr(0)
                self.state = 188
                self.match(cocoParser.T__13)
                self.state = 189
                localctx.second_operand = self.call_expr(0)
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

        def arithmetic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(cocoParser.Arithmetic_exprContext,i)


        def call_expr(self):
            return self.getTypedRuleContext(cocoParser.Call_exprContext,0)


        def element(self):
            return self.getTypedRuleContext(cocoParser.ElementContext,0)


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
            self.state = 198
            token = self._input.LA(1)
            if token in [cocoParser.T__19]:
                self.state = 194
                localctx.operator = self.match(cocoParser.T__19)
                self.state = 195
                localctx.operand = self.arithmetic_expr(5)

            elif token in [cocoParser.Identifier]:
                self.state = 196
                localctx.call = self.call_expr(0)

            elif token in [cocoParser.T__31, cocoParser.Boolean, cocoParser.Integer, cocoParser.String]:
                self.state = 197
                localctx.primary = self.element()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 206
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = cocoParser.Arithmetic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 200
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 201
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cocoParser.T__20) | (1 << cocoParser.T__21) | (1 << cocoParser.T__22) | (1 << cocoParser.T__23) | (1 << cocoParser.T__24) | (1 << cocoParser.T__25))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 202
                        localctx.right = self.arithmetic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = cocoParser.Arithmetic_exprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 203
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 204
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cocoParser.T__6) | (1 << cocoParser.T__26) | (1 << cocoParser.T__27) | (1 << cocoParser.T__28))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 205
                        localctx.right = self.arithmetic_expr(4)
                        pass

             
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Basic_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.operator = None # Token
            self.operand = None # Arithmetic_exprContext
            self.primary = None # ElementContext

        def arithmetic_expr(self):
            return self.getTypedRuleContext(cocoParser.Arithmetic_exprContext,0)


        def element(self):
            return self.getTypedRuleContext(cocoParser.ElementContext,0)


        def getRuleIndex(self):
            return cocoParser.RULE_basic_expr

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitBasic_expr(self)
            else:
                return visitor.visitChildren(self)




    def basic_expr(self):

        localctx = cocoParser.Basic_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_basic_expr)
        try:
            self.state = 214
            token = self._input.LA(1)
            if token in [cocoParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                localctx.operator = self.match(cocoParser.T__19)
                self.state = 212
                localctx.operand = self.arithmetic_expr(0)

            elif token in [cocoParser.T__31, cocoParser.Boolean, cocoParser.Integer, cocoParser.String]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                localctx.primary = self.element()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.primary_bool = None # Token
            self.primary_int = None # Token
            self.primary_str = None # Token
            self.primary_list = None # List_Context

        def Boolean(self):
            return self.getToken(cocoParser.Boolean, 0)

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def String(self):
            return self.getToken(cocoParser.String, 0)

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
            self.state = 220
            token = self._input.LA(1)
            if token in [cocoParser.Boolean]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                localctx.primary_bool = self.match(cocoParser.Boolean)

            elif token in [cocoParser.Integer]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                localctx.primary_int = self.match(cocoParser.Integer)

            elif token in [cocoParser.String]:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                localctx.primary_str = self.match(cocoParser.String)

            elif token in [cocoParser.T__31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
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
            self.argument = None # Basic_exprContext
            self.abstract = None # Semantic_nodeContext

        def Identifier(self):
            return self.getToken(cocoParser.Identifier, 0)

        def basic_expr(self):
            return self.getTypedRuleContext(cocoParser.Basic_exprContext,0)


        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_call_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            localctx.call = self.match(cocoParser.Identifier)
            self.state = 231
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 224
                self.match(cocoParser.T__8)
                self.state = 227
                token = self._input.LA(1)
                if token in [cocoParser.T__19, cocoParser.T__31, cocoParser.Boolean, cocoParser.Integer, cocoParser.String]:
                    self.state = 225
                    localctx.argument = self.basic_expr()

                elif token in [cocoParser.T__8, cocoParser.T__12, cocoParser.Identifier]:
                    self.state = 226
                    localctx.abstract = self.semantic_node()

                else:
                    raise NoViableAltException(self)

                self.state = 229
                self.match(cocoParser.T__10)


            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cocoParser.Call_exprContext(self, _parentctx, _parentState)
                    localctx.operand = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_call_expr)
                    self.state = 233
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 234
                    self.match(cocoParser.T__29)
                    self.state = 235
                    localctx.call = self.match(cocoParser.Identifier)
                    self.state = 243
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 236
                        self.match(cocoParser.T__8)
                        self.state = 239
                        token = self._input.LA(1)
                        if token in [cocoParser.T__19, cocoParser.T__31, cocoParser.Boolean, cocoParser.Integer, cocoParser.String]:
                            self.state = 237
                            localctx.argument = self.basic_expr()

                        elif token in [cocoParser.T__8, cocoParser.T__12, cocoParser.Identifier]:
                            self.state = 238
                            localctx.abstract = self.semantic_node()

                        else:
                            raise NoViableAltException(self)

                        self.state = 241
                        self.match(cocoParser.T__10)

             
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
            self.state = 258
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                localctx.exact = self.match(cocoParser.Integer)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                localctx.lower = self.match(cocoParser.Integer)
                self.state = 252
                self.match(cocoParser.T__9)
                self.state = 253
                localctx.upper = self.match(cocoParser.Integer)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.match(cocoParser.T__9)
                self.state = 255
                localctx.upper = self.match(cocoParser.Integer)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                localctx.lower = self.match(cocoParser.Integer)
                self.state = 257
                self.match(cocoParser.T__9)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ignore_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whitespace_node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cocoParser.Whitespace_nodeContext)
            else:
                return self.getTypedRuleContext(cocoParser.Whitespace_nodeContext,i)


        def getRuleIndex(self):
            return cocoParser.RULE_ignore_clause

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, cocoVisitor ):
                return visitor.visitIgnore_clause(self)
            else:
                return visitor.visitChildren(self)




    def ignore_clause(self):

        localctx = cocoParser.Ignore_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ignore_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(cocoParser.T__30)
            self.state = 262 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 261
                self.whitespace_node()
                self.state = 264 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cocoParser.Identifier):
                    break

            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__9:
                self.state = 266
                self.match(cocoParser.T__9)
                self.state = 268 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 267
                    self.whitespace_node()
                    self.state = 270 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==cocoParser.Identifier):
                        break

                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 277
            self.match(cocoParser.T__31)
            self.state = 278
            self.list_element()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoParser.T__9:
                self.state = 279
                self.match(cocoParser.T__9)
                self.state = 280
                self.list_element()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 286
            self.match(cocoParser.T__32)
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

        def Integer(self):
            return self.getToken(cocoParser.Integer, 0)

        def String(self):
            return self.getToken(cocoParser.String, 0)

        def semantic_node(self):
            return self.getTypedRuleContext(cocoParser.Semantic_nodeContext,0)


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
            self.state = 291
            token = self._input.LA(1)
            if token in [cocoParser.Integer]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                localctx.element_int = self.match(cocoParser.Integer)

            elif token in [cocoParser.String]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                localctx.element_str = self.match(cocoParser.String)

            elif token in [cocoParser.T__8, cocoParser.T__12, cocoParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
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
        self._predicates[15] = self.call_expr_sempred
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
         

    def logic_expr_sempred(self, localctx:Logic_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

    def arithmetic_expr_sempred(self, localctx:Arithmetic_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

    def call_expr_sempred(self, localctx:Call_exprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         



