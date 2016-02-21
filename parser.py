import os

from lexer import Token, TokenTypes, lexedProgram as program

indent=0
outputProgram=''

# Program => (Stmt END)*
def parseProgram():
    global outputProgram
    while True:
        try:
            token = program[0]
            parseStmt()
            end = program.pop(0)
            if end.tokenType!=TokenTypes.End:
                raise ParsingError(end)
            outputProgram+='\n'
        except IndexError:
            return


# Stmt => Assignment | Deal | Funcall | FunDef | If | While | Return
def parseStmt():
    global outputProgram
    global indent
    token = program[0]
    tokentype = token.tokenType
    # if this is an invalid token
    if tokentype not in [TokenTypes.Varname, TokenTypes.Deal, TokenTypes.Call, TokenTypes.Def, TokenTypes.If, TokenTypes.While, TokenTypes.Return]:
        raise ParsingError(tokentype)
    outputProgram+=' '*(indent*4)
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
    global outputProgram
    global indent
    varname=program.pop(0)
    if varname.tokenType!=TokenTypes.Varname:
        raise ParsingError(varname)
    outputProgram+=varname.tokenValue+'='
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
    global outputProgram
    global indent
    token = program[0]
    if token.tokenType==TokenTypes.Varname or token.tokenType==TokenTypes.Number:
        token = program.pop(0)
        outputProgram+=str(token.tokenValue)
    elif token.tokenType==TokenTypes.Call:
        parseFunCall()
    else:
        raise ParsingError(token)


# AddSub => empty | (PLUS | MINUS) Value AddSub
def parseAddSub():
    global outputProgram
    global indent
    if program[0].tokenType in [TokenTypes.Plus, TokenTypes.Minus]:
        symbol = program.pop(0)
        if symbol.tokenType==TokenTypes.Plus:
            outputProgram+='+'
        else:
            outputProgram+='-'
        parseValue()
        parseAddSub()


# Deal => DEAL Value
def parseDeal():
    global outputProgram
    global indent
    deal = program.pop(0)
    if deal.tokenType!=TokenTypes.Deal:
        raise ParsingError(deal)
    outputProgram+='print('
    parseValue()
    outputProgram+=")"


# FunCall => CALL FVARNAME OPEN (VARNAME END)* CLOSE //(VARNAME END)* being the parameters
def parseFunCall():
    global outputProgram
    global indent
    callToken = program.pop(0)
    if callToken.tokenType!=TokenTypes.Call:
        raise ParsingError(callToken)
    fName = program.pop(0)
    # if this is actually a Chr, use the chr function instead
    if fName.tokenType==TokenTypes.Chr:
        parseChr()
        return
    if fName.tokenType!=TokenTypes.Varname:
        raise ParsingError(fName)
    outputProgram+=fName.tokenValue
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    outputProgram+="("
    t=program[0]
    firstTime=True
    while t.tokenType!=TokenType.Close:
        if firstTime:
            firstTime=False
        else:
            outputProgram+=','
        pName = program.pop(0)
        if pName.tokenType!=TokenTypes.Varname:
            raise ParsingError(pName)
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
        outputProgram+=pName.tokenValue
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)
    outputProgram+=')'

# OPEN Value END CLOSE
def parseChr():
    global outputProgram
    global indent
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    outputProgram+='chr('
    parseValue()
    end = program.pop(0)
    if end.tokenType!=TokenTypes.End:
        raise ParsingError(end)
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)
    outputProgram+=')'
    


# FunDef => DEF FVARNAME OPEN (VARNAME END)* CLOSE OPEN (Stmt END)* CLOSE
def parseFunDef():
    global outputProgram
    global indent
    defToken = program.pop(0)
    if defToken.tokenType!=TokenTypes.Call:
        raise ParsingError(defToken)
    outputProgram+='def '
    fName = program.pop(0)
    if fName.tokenType!=TokenTypes.Varname:
        raise ParsingError(fName)
    outputProgram+=fName.tokenValue
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    outputProgram+='('
    t=program[0]
    firstTime=True
    while t.tokenType!=TokenType.Close:
        if firstTime:
            firstTime=False
        else:
            outputProgram+=','
        pName = program.pop(0)
        if pName.tokenType!=TokenTypes.Varname:
            raise ParsingError(pName)
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
        outputProgram+=pName.tokenValue
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)
    outputProgram+='):'
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    indent+=1
    while t.tokenType!=TokenType.Close:
        parseStmt()
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
        outputProgram+='\n'
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)
    indent-=1


# If => IF BoolExprs OPEN (Stmt END)* CLOSE // No else for now
def parseIf():
    global outputProgram
    global indent
    ifToken = program.pop(0)
    if ifToken.tokenType!=TokenTypes.If:
        raise ParsingError(ifToken)
    outputProgram+='if '
    parseBoolExprs()
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    outputProgram+=':\n'
    indent+=1
    t=program[0]
    while t.tokenType!=TokenTypes.Close:
        parseStmt()
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
        outputProgram+='\n'
        t=program[0]
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)
    indent-=1


# While => WHILE BoolExprs OPEN (Stmt END)* CLOSE
def parseWhile():
    global outputProgram
    global indent
    whileToken = program.pop(0)
    if whileToken.tokenType!=TokenTypes.Deal:
        raise ParsingError(whileToken)
    outputProgram+="while "
    parseBoolExprs()
    o = program.pop(0)
    if o.tokenType!=TokenTypes.Open:
        raise ParsingError(o)
    outputProgram+=':\n'
    indent+=1
    t=program[0]
    while t.tokenType!=TokenType.Close:
        parseStmt()
        end = program.pop(0)
        if end.tokenType!=TokenTypes.End:
            raise ParsingError(end)
        outputProgram+='\n'
        t=program[0]
    c = program.pop(0)
    if c.tokenType!=TokenTypes.Close:
        raise ParsingError(c)
    indent-=1


# BoolExprs => NOT? BoolExpr AndOr
def parseBoolExprs():
    global outputProgram
    global indent
    t = program[0]
    # if there is the optional not
    if t.tokenType==TokenTypes.Not:
        notToken=program.pop(0)
        outputProgram+=' not '
    parseBoolExpr()
    parseAndOr()


# AndOr => empty | (AND | OR) BoolExprs
def parseAndOr():
    global outputProgram
    global indent
    if program[0].tokenType in [TokenTypes.And, TokenTypes.Or]:
        symbol = program.pop(0)
        if symbol.tokenType==TokenTypes.And:
            outputProgram+=' and '
        else:
            outputProgram+=' or '
        parseBoolExprs()


# BoolExpr => Value (GT | LT | EQ) Value
def parseBoolExpr():
    global outputProgram
    global indent
    outputProgram+='('
    parseValue()
    symbol = program.pop(0)
    if symbol.tokenType not in [TokenTypes.Gt, TokenTypes.Lt, TokenTypes.Eq]:
        raise ParsingError(symbol)
    if symbol.tokenType==TokenTypes.Gt:
        outputProgram+='>'
    elif symbol.tokenType==TokenTypes.Lt:
        outputProgram+='<'
    elif symbol.tokenType==TokenTypes.Eq:
        outputProgram+='=='
    parseValue()
    outputProgram+=')'


# Return => RETURN OPEN Value? CLOSE
def parseReturn():
    global outputProgram
    global indent
    retSymbol = program.pop(0)
    if retSymbol.tokenType!=TokenTypes.Return:
        raise ParsingError(retSymbol)
    outputProgram+='return '
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
#print(outputProgram)

# temporarily save this to a python file
tempFile = open('temp.py', 'w')
tempFile.truncate()
tempFile.write(outputProgram)
tempFile.close()
# run the generated python file
os.system("python temp.py")
# remove the temporary python file
os.remove('temp.py')
