from antlr4.error.ErrorListener import ErrorListener


class CocoErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def has_errors(self):
        return self.errors

    def print_errors(self):
        if not self.has_errors():
            return ''
        res = 'Error log:\n'
        for e in self.errors:
            res = ''.join([res, e, '\n'])
        return res[:-1]

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        error = ''.join(['Error on line ', str(line), ': ', msg])
        self.errors.append(error)