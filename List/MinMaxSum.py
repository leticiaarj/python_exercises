def miniMaxSum(arr):
    minMaxArr = []

    for i in arr:
        sumAux = sum(arr)
        sumArr = sumAux - i
        minMaxArr.append(sumArr)
 
    minimus = min(minMaxArr)
    maximus = max(minMaxArr)

    print(minimus, maximus)
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
