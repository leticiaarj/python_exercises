import sys

def lonelyinteger(arr):
    if(len(arr) == 1):
        return arr[0]
    
    arr.sort()
    aux = []
    
    for i in len(arr):
        if(arr[i] == arr[i+1]):
            aux.append(i)
    
    arr = [value for value in arr if value not in aux]
    
    return arr[0]

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
