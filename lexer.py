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
            try:
                thisValue=int(value)
            except ValueError:
                if value=='A':
                    thisValue=1
                elif value=='J':
                    # TODO: continue
                    pass
            if valueSoFar==None:
                valueSoFar= thisValue
            valueSoFar = valueSoFar*13 + thisValue
        # if it's a var name, lex it all
        elif suit=='♦':
            thisValue= None# TODO lex value
            if valueSoFar==None:
                valueSoFar = thisValue
            valueSoFar = valueSoFar + thisValue
        else:
            if value=='A' and suit=='♠':
                thisOne=TokenTypes.End
            thisOne=1# TODO: look up card in card mapping and return the appropriate token
            lexedProgram.append(Token(thisone))
        i+=1


class Token(object):
    def __init__(self, tokenType, tokenValue=None):
        self.tokenType=tokenType
        self.tokenValue=tokenValue

    def __str__(self):
        return str(self.tokenType)+','+str(self.tokenValue)

    def __repr__(self):
        return str(self)


class TokenTypes(Enum):
    Varname=1
    Number=2
    End=3
    Open=4
    Close=5
    Call=6
    Def=7
    If=8
    While=9
    Return=10
    Chr=11
    Deal=12
    Plus=13
    Minus=14
    And=15
    Or=16
    Not=17
    Eq=18
    Gt=19
    Lt=20
