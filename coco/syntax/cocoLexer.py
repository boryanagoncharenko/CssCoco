# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\6")
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\r\n\2")
        buf.write("\r\2\16\2\16\3\3\3\3\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4#\n\4\f\4\16")
        buf.write("\4&\13\4\3\4\3\4\3\5\6\5+\n\5\r\5\16\5,\3\5\3\5\3\26\2")
        buf.write("\6\3\3\5\4\7\5\t\6\3\2\5\3\2c|\4\2\f\f\17\17\5\2\13\f")
        buf.write("\17\17\"\"\63\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\3\f\3\2\2\2\5\20\3\2\2\2\7\36\3\2\2\2\t*\3\2")
        buf.write("\2\2\13\r\t\2\2\2\f\13\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2")
        buf.write("\2\16\17\3\2\2\2\17\4\3\2\2\2\20\21\7\61\2\2\21\22\7,")
        buf.write("\2\2\22\26\3\2\2\2\23\25\13\2\2\2\24\23\3\2\2\2\25\30")
        buf.write("\3\2\2\2\26\27\3\2\2\2\26\24\3\2\2\2\27\31\3\2\2\2\30")
        buf.write("\26\3\2\2\2\31\32\7,\2\2\32\33\7\61\2\2\33\34\3\2\2\2")
        buf.write("\34\35\b\3\2\2\35\6\3\2\2\2\36\37\7\61\2\2\37 \7\61\2")
        buf.write("\2 $\3\2\2\2!#\n\3\2\2\"!\3\2\2\2#&\3\2\2\2$\"\3\2\2\2")
        buf.write("$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\b\4\2\2(\b\3\2\2\2")
        buf.write(")+\t\4\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-.\3")
        buf.write("\2\2\2./\b\5\2\2/\n\3\2\2\2\7\2\16\26$,\3\b\2\2")
        return buf.getvalue()
		

class cocoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Word = 1
    Comment = 2
    LineComment = 3
    WS = 4


    modeNames = [ "DEFAULT_MODE" ]

    tokenNames = [ "<INVALID>",
            "'\\u0000'", "'\\u0001'", "'\\u0002'", "'\\u0003'", "'\\u0004'" ]

    ruleNames = [ "Word", "Comment", "LineComment", "WS" ]

    grammarFileName = "coco.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


