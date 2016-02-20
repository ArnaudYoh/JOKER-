import sys
from enum import Enum

# read program from inputted file and remove whitespace
fileName = sys.argv[1]
inputFile = open(fileName)
rawProgram = inputFile.read()
rawProgram = [c for c in rawProgram if not c.isspace()]

# list of tokens in program
parsedProgram=[]


def parseProgram():
    # if not in the middle of parsing a number
    currentlyParsingNumber=False
    # if not in the middle of parsing a var/function name
    currentlyParsingName=False
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
        if suit!='♦' and currentlyParsingName:
            parsedProgram.append(Token(TokenTypes.varname, valueSoFar))
            valueSoFar=None
        elif suit!='♥' and currentlyParsingNumber:
            parsedProgram.append(Token(TokenTypes.number, valueSoFar))
            valueSoFar=None
        # if it's a number, parse it all
        if suit=='♥':
            thisValue=# TODO parse value
            if valueSoFar==None:
                valueSoFar= thisValue#TODO replace with newly parsed value
            valueSoFar = valueSoFar*13 + thisValue#TODO replace with newly parsed value
        # if it's a var name, parse it all
        elif suit=='♦':
            thisValue=# TODO parse value
            if valueSoFar==None:
                valueSoFar= thisValue#TODO replace with newly parsed value
            valueSoFar = valueSoFar + thisValue#TODO replace with  newly parsed value
        else:
            thisOne=# TODO: look up card in card mapping and return the appropriate token
            parsedProgram.append(Token(thisone))
        i+=1


class Token(object):
    def __init__(self, tokenType, tokenValue=None):
        self.tokenType=tokenType
        self.tokenValue=tokenValue


class TokenTypes(Enum):
    varname=1
    number=2
    # TODO the rest
