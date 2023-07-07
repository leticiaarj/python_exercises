import sys

def countingSort(arr):

    freq = [0 for i in range(100)]

    for i in arr:
        freq[i] = freq[i] + 1

    return freq
        
if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
