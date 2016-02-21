from lexer import Token, TokenTypes#, lexedProgram as program

program = [ Token(TokenTypes.Varname, 'x') , Token(TokenTypes.Open), Token(TokenTypes.Number, 3), Token(TokenTypes.Close) , Token(TokenTypes.End),
            Token(TokenTypes.Varname, 'x') , Token(TokenTypes.Open), Token(TokenTypes.Number, 3), Token(TokenTypes.Plus), Token(TokenTypes.Number, 4), Token(TokenTypes.Close) , Token(TokenTypes.End),
            Token(TokenTypes.Deal) , Token(TokenTypes.Varname, 'x')]


# Program => (Stmt END)*
def parseProgram():
    while True:
        try:
            token = program[0]
            parseStmt()
            end = program.pop(0)
            if end.tokenType!=TokenTypes.End:
                raise ParsingError(end)
        except IndexError:
            return


# Stmt => Assignment | Deal | Funcall | FunDef | If | While | Return
def parseStmt():
    token = program[0]
    tokentype = token.tokenType
    # if this is an invalid token
    if tokentype not in [TokenTypes.Varname, TokenTypes.Deal, TokenTypes.Call, TokenTypes.Def, TokenTypes.If, TokenTypes.While, TokenTypes.Return]:
        raise ParsingError(tokentype)
    if tokentype==TokenTypes.Varname:
        parseAssignment()
    elif tokentype==TokenTypes.Deal:
        parseDeal()
    elif tokentype==TokenTypes.Call:
        parseFunCall()
    elif tokentype==TokenTypes.Def:
        parseFunDef()
    elif tokentype==TokenTypes.If:
        parseIf()
    elif tokentype==TokenTypes.While:
        parseWhile()
    elif tokentype==TokenTypes.Return:
        parseReturn()


# Assignment => VARNAME OPEN MathExpr CLOSE
def parseAssignment():
    varname=program.pop(0)
    if varname.tokenType!=TokenTypes.Varname:
        raise ParsingError(varname)
    o=program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    parseMathExpr()
    c=program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)

# MathExpr => Value AddSub
def parseMathExpr():
    parseValue()
    parseAddSub()

# Value => (VARNAME|VALUE|Funcall)
def parseValue():
    token = program.pop(0)
    if token.tokenType==TokenTypes.Varname or token.tokenType==TokenTypes.Number:
        pass
    elif token.tokenType==TokenTypes.Call:
        parseFunCall()
    else:
        raise ParsingError(token)


# AddSub => empty | (PLUS | MINUS) Value AddSub
def parseAddSub():
    if program[0].tokenType in [TokenTypes.Plus, TokenTypes.Minus]:
        symbol = program.pop(0)
        parseValue()
        parseAddSub()


# Deal => DEAL VARNAME
def parseDeal():
    deal = program.pop(0)
    if deal.tokenType!=TokenTypes.Deal:
        raise ParsingError(deal)
    varname = program.pop(0)
    if varname.tokenType!=TokenTypes.Varname:
        raise ParsingError(varname)


# FunCall => CALL FVARNAME OPEN (VARNAME END)* CLOSE //(VARNAME END)* being the parameters
def parseFunCall():
    callToken = program.pop(0)
    if callToken.tokenType!=TokenTypes.Call:
        raise ParsingError(callToken)
    fName = program.pop(0)
    if fName.tokenType!=TokenTypes.Varname:
        raise ParsingError(fName)
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    t=program[0]
    while t.tokenType!=TokenType.Close:
        pName = program.pop(0)
        if pName.tokenType!=TokenTypes.Varname:
            raise ParsingError(pName)
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)


# FunDef => DEF FVARNAME OPEN (VARNAME END)* CLOSE OPEN Stmt* CLOSE
def parseFunDef():
    defToken = program.pop(0)
    if defToken.tokenType!=TokenTypes.Call:
        raise ParsingError(defToken)
    fName = program.pop(0)
    if fName.tokenType!=TokenTypes.Varname:
        raise ParsingError(fName)
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    t=program[0]
    while t.tokenType!=TokenType.Close:
        pName = program.pop(0)
        if pName.tokenType!=TokenTypes.Varname:
            raise ParsingError(pName)
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    while t.tokenType!=TokenType.Close:
        parseStmt()
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)

# If => IF BoolExprs OPEN (Stmt END)* CLOSE // No else for now
def parseIf():
    ifToken = program.pop(0)
    if ifToken.tokenType!=TokenTypes.Deal:
        raise ParsingError(ifToken)
    parseBoolExprs()
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    t=program[0]
    while t.tokenType!=TokenType.Close:
        parseStmt()
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)


# While => WHILE BoolExprs OPEN (Stmt END)* CLOSE
def parseWhile():
    whileToken = program.pop(0)
    if whileToken.tokenType!=TokenTypes.Deal:
        raise ParsingError(whileToken)
    parseBoolExprs()
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    t=program[0]
    while t.tokenType!=TokenType.Close:
        parseStmt()
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)


# BoolExprs => NOT? BoolExpr AndOr
def parseBoolExprs():
    t = program[0]
    # if there is the optional not
    if t.tokenType==TokenTypes.Not:
        notToken=program.pop(0)
    parseBoolExpr()
    parseAndOr()


# AndOr => empty | (AND | OR) BoolExprs
def parseAndOr():
    if program[0].tokenType in [TokenTypes.And, TokenTypes.Or]:
        symbol = program.pop(0)
        parseBoolExprs()


# BoolExpr => Value (GT | LT | EQ) Value
def parseBoolExpr():
    parseValue()
    symbol = program.pop(0)
    if symbol.tokenType not in [TokenTypes.Gt, TokenTypes.Lt, TokenTypes.Eq]:
        raise ParsingError(symbol)
    parseValue()


# Return => RETURN OPEN Value? CLOSE
def parseReturn():
    retSymbol = program.pop(0)
    if retSymbol.tokenType!=TokenTypes.Return:
        raise ParsingError(retSymbol)
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    if program[0].tokenType!=TokenTypes.Close:
        parseValue()
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)


# TODO improve
class ParsingError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

parseProgram()
