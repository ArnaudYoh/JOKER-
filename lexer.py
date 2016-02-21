import sys
from enum import Enum

def lexEVERYTHING(data):
    # read program from inputted file and remove whitespace
    rawProgram = data
    rawProgram = [c for c in rawProgram if not c.isspace() and c!='\n' and c!=' ' and c!='\t']
    # list of tokens in program
    lexedProgram=[]

    lexedProgram = lexProgram(rawProgram, lexedProgram)
    print(lexedProgram)



cardValues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0]

def lexProgram(rawProgram, lexedProgram):
    # if not in the middle of parsing a number
    currentlyLexingNumber=False
    # if not in the middle of parsing a var/function name
    currentlyLexingName=False
    # value so far if in the middle of parsing a multicard thing
    valueSoFar=None

    i=0
    while i<len(rawProgram):
        try:
            value=rawProgram[i]
            if rawProgram[i+2]=='0':
                value+='0'
                i+=2
            suit="".join(rawProgram[i+1:i+4])
            if suit=='\x00e&':
                suit='♥'
            elif suit=='\x00f&':
                suit='♦'
            elif suit=='\x00`&':
                suit='♠'
            elif suit=="\x00c&":
                suit='♣'
            #print(suit)
        except IndexError:
            print("Invalid program")
            return
        if suit!='♦' and currentlyLexingName:
            lexedProgram.append(Token(TokenTypes.Varname, valueSoFar))
            valueSoFar=None
            currentlyLexingName=False
        elif suit!='♥' and currentlyLexingNumber:
            lexedProgram.append(Token(TokenTypes.Number, valueSoFar))
            valueSoFar=None
            currentlyLexingNumber=False
        # if it's a number, lex it all
        if suit=='♥':
            thisValue=readNumber(value)
            if valueSoFar==None:
                valueSoFar= thisValue
            else:
                valueSoFar = valueSoFar*13 + thisValue
            currentlyLexingNumber=True
        # if it's a var name, lex it all
        elif suit=='♦':
            if value in cardValues:
                if valueSoFar==None:
                    valueSoFar = 'v'+value
                else:
                    valueSoFar = valueSoFar + value
                currentlyLexingName=True
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
            elif value=='5' and suit=='♣':
                thisOne=TokenTypes.Times
            elif value=='3' and suit=='♠':
                thisOne=TokenTypes.Def
            elif value=='3' and suit=='♣':
                thisOne=TokenTypes.Minus
            elif value=='2' and suit=='♠':
                thisOne=TokenTypes.Call
            elif value=='2' and suit=='♣':
                thisOne=TokenTypes.Plus
            elif value=='10' and suit=='♣':
                thisOne=TokenTypes.Lt
            elif value=='10' and suit=='♠':
                thisOne==TokenTypes.Return
            
            if thisOne!=None:
                # TODO: look up card in card mapping and return the appropriate token
                lexedProgram.append(Token(thisOne))
        i+=4
    return lexedProgram

def readNumber(value):
    # convert card value to decimal
    if value in cardValues:
        return nums[cardValues.index(value)]


class Token(object):
    def __init__(self, tokenType, tokenValue=None):
        self.tokenType=tokenType
        self.tokenValue=tokenValue

    def __str__(self):
        return '<'+str(self.tokenType)+(','+str(self.tokenValue) if self.tokenValue!=None else '')+'>'

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
    Times=21
