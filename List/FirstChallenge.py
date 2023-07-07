import sys
from statistics import median

fptr = sys.stdout
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

arr.sort()
print(arr)

med = median(arr)
print(med)

fptr.close()
