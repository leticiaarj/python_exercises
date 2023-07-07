import sys

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return




if __name__ == '__main__':
    fptr = sys.stdout

    test_cases = int(input().strip())

    for cs in range (test_cases):
        n = int(input())
        a = list(map(int, input().split()))

    result = findZigZagSequence(a, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


