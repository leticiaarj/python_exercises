import sys

def diagonalDifference(arr):
    leftToRight = sum(arr[i][i] for i in range(len(arr)))

    rightToLeft = sum(l for l in[(arr[0][len(arr)-1] if i == 0 
                                  else arr[i][len(arr)-1-i]) for i in range(len(arr))])

    return abs(leftToRight - rightToLeft)

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
