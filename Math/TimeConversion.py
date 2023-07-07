from datetime import datetime
import sys

def timeConversion(s):
    inputTime =  datetime.strptime(s.replace("'", ""), "%I:%M:%S%p")
    outputTime = datetime.strftime(inputTime, "%H:%M:%S")

    return outputTime

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = timeConversion(s)

    fptr.write(str(result) + '\n')

    fptr.close()
