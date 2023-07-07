def plusMinus(arr, n):
    negative = 0
    positive = 0
    zero = 0

    for i in arr:
        if(i<0):
            negative = negative + 1
        elif(i==0):
            zero = zero + 1
        else:
            positive = positive + 1

    proportionNegative = negative/n
    proportionPositive = positive/n
    proportionZero = zero/n

    print('{:06f}'.format(proportionPositive))
    print('{:06f}'.format(proportionNegative))
    print('{:06f}'.format(proportionZero))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
