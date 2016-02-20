import sys
from enum import Enum

# read program from inputted file and remove whitespace
fileName = sys.argv[1]
inputFile = open(fileName)
rawProgram = inputFile.read()
rawProgram = [c for c in rawProgram if not c.isspace()]

# list of tokens in program
lexedProgram=[]


def lexProgram():
    # if not in the middle of parsing a number
    currentlyLexingNumber=False
    # if not in the middle of parsing a var/function name
    currentlyLexingName=False
    # value so far if in the middle of parsing a multicard thing
    valueSoFar=None

    for i in range(0,len(rawProgram)):
        try:
            value=rawProgram[i]
            if rawProgram[i+1]=='0':
                value+='0'
                i+=1
            suit=rawProgram[i+1]
        except IndexError:
            print("Invalid program")
        if suit!='♦' and currentlyLexingName:
            lexedProgram.append(Token(TokenTypes.Varname, valueSoFar))
            valueSoFar=None
        elif suit!='♥' and currentlyLexingNumber:
            lexedProgram.append(Token(TokenTypes.Number, valueSoFar))
            valueSoFar=None
        # if it's a number, lex it all
        if suit=='♥':
            thisValue=# TODO lex value
            if valueSoFar==None:
                valueSoFar= thisValue#TODO replace with newly lexed value
            valueSoFar = valueSoFar*13 + thisValue#TODO replace with newly lexed value
        # if it's a var name, lex it all
        elif suit=='♦':
            thisValue=# TODO lex value
            if valueSoFar==None:
                valueSoFar= thisValue#TODO replace with newly lexed value
            valueSoFar = valueSoFar + thisValue#TODO replace with newly lexed value
        else:
            thisOne=# TODO: look up card in card mapping and return the appropriate token
            lexedProgram.append(Token(thisone))
        i+=1


class Token(object):
    def __init__(self, tokenType, tokenValue=None):
        self.tokenType=tokenType
        self.tokenValue=tokenValue


class TokenTypes(Enum):
    Varname=1
    Number=2
    # TODO the rest
