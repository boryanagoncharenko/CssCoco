# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .cocoListener import cocoListener
else:
    from cocoListener import cocoListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\6")
        buf.write("\n\4\2\t\2\3\2\6\2\6\n\2\r\2\16\2\7\3\2\2\2\3\2\2\2\t")
        buf.write("\2\5\3\2\2\2\4\6\7\3\2\2\5\4\3\2\2\2\6\7\3\2\2\2\7\5\3")
        buf.write("\2\2\2\7\b\3\2\2\2\b\3\3\2\2\2\3\7")
        return buf.getvalue()
		

class cocoParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    Word=1
    Comment=2
    LineComment=3
    WS=4

    tokenNames = [ "<INVALID>", "Word", "Comment", "LineComment", "WS" ]

    RULE_start_rule = 0

    ruleNames =  [ "start_rule" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Start_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(cocoParser.Word)
            else:
                return self.getToken(cocoParser.Word, i)

        def getRuleIndex(self):
            return cocoParser.RULE_start_rule

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.enterStart_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, cocoListener ):
                listener.exitStart_rule(self)




    def start_rule(self):

        localctx = cocoParser.Start_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                self.match(self.Word)
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cocoParser.Word):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




