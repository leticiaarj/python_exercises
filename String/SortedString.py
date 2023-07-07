import sys

def splitString(sortedString):
    digit = []
    text_temp = []
    textUp = []
    textLo = []

    for sortedStr in sortedString:
        if(sortedStr.isdigit()):
            digit.append(int(sortedStr))
        else:
            text_temp.append(sortedStr)

    for t in text_temp:
        if(t.isupper()):
            textUp.append(t)
        else:
            textLo.append(t)                   
    text_temp.clear()

    text_temp = textLo + textUp

    return text_temp, digit

def oddOrEven(digit):
    odd_digit = []
    even_digit = []
    digitToString = []

    for dig in digit:
        if(dig%2 == 0):
            even_digit.append(dig)
            even_digit.sort()
        else:
            odd_digit.append(dig)
            odd_digit.sort()

    sum = odd_digit + even_digit

    for s in sum:
        digitToString.append(str(s))

    return digitToString

def sortedStringAndNumbers(stringInput):
    output = []
    sortedString = sorted(stringInput)

    text, digit = splitString(sortedString)
    digitToString = oddOrEven(digit)

    output = text + digitToString
    outputStr = ''.join(output)

    return outputStr

if __name__ == '__main__':
    fptr = sys.stdout 
    stringInput = sys.stdin.readline().rstrip('\n')

    result = sortedStringAndNumbers(stringInput)

    fptr.write(result + '\n')

    fptr.close()
