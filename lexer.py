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
                    thisValue=11
                elif value=='Q':
                    thisValue=12
                elif value=='K':
                    thisValue=0
    # TODO: continue?? Or should we not?
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
            thisOne=None
            if value=='A' and suit=='♠':
                thisOne=TokenTypes.End
            elif value=='A' and suit=='♣':
                thisOne=TokenTypes.Deal
            elif value=='Q' and suit=='♠':
                thisOne=TokenTypes.Open
            elif value=='K' and suit=='♠':
                thisOne=TokenTypes.Close
            elif value=='K' and suit=='♣':
                thisOne=TokenTypes.Chr
            elif value=='9' and suit=='♣':
                thisOne=TokenTypes.Gt
            elif value=='8' and suit=='♠':
                thisOne=TokenTypes.While
            elif value=='8' and suit=='♣':
                thisOne=TokenTypes.Eq
            elif value=='7' and suit=='♣':
                thisOne=TokenTypes.Not
            elif value=='6' and suit=='♠':
                thisOne=TokenTypes.If
            elif value=='6' and suit=='♣':
                thisOne=TokenTypes.Or
            elif value=='5' and suit=='♣':
                thisOne=TokenTypes.And
            elif value=='3' and suit=='♠':
                thisOne=TokenValue.Def
            elif value=='3' and suit=='♣':
                thisOne=TokenTypes.Minus
            elif value=='2' and suit=='♠':
                thisOne=TokenValue.Call
            elif value=='2' and suit=='♣':
                thisOne=TokenTypes.Plus
            """
            elif value=='10' and suit=='♣':
                thisOne=TokenTypesself.Lt
            elif value=='10' and suit=='♠':
                thisOne==TokenTypes.Return
            """
            elif thisOne!=None:
                # TODO: look up card in card mapping and return the appropriate token
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
