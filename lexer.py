import sys
from enum import Enum

# read program from inputted file and remove whitespace
fileName = sys.argv[1]
inputFile = open(fileName)
rawProgram = inputFile.read()
rawProgram = [c for c in rawProgram if not c.isspace()]
print(rawProgram)
# list of tokens in program
lexedProgram=[]


cardValues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0]

def lexProgram():
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
            if rawProgram[i+1]=='0':
                value+='0'
                i+=1
            print(value)
            suit="".join(rawProgram[i+1:i+4])
            if suit=='\x00e&':
                suit='♥'
            elif suit=='\x00f&':
                suit='♦'
            elif suit=="\x00'&":
                suit='♠'
            elif suit=="\x00e&":
                suit='♣'
            #print(suit)
        except IndexError:
            print("Invalid program")
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
            if value=='A' and suit=='♠':
                thisOne=TokenTypes.End
            elif value=='Q' and suit=='♠':
                thisOne=TokenTypes.Open
            thisOne=1# TODO: look up card in card mapping and return the appropriate token
            lexedProgram.append(Token(thisOne))
        i+=4

def readNumber(value):
    # convert card value to decimal
    if value in cardValues:
        return nums[cardValues.index(value)]


class Token(object):
    def __init__(self, tokenType, tokenValue=None):
        self.tokenType=tokenType
        self.tokenValue=tokenValue

    def __str__(self):
        return '<'+str(self.tokenType)+','+str(self.tokenValue)+'>'

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

lexProgram()
print(lexedProgram)
