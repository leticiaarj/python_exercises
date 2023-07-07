import sys

def flippingMatrix(matrix):
    n = int(len(matrix)/2)
        
    maxSum = sum([max(matrix[i][j], matrix[i][(2*n-1)-j], matrix[(2*n-1)-i][j], matrix[(2*n-1)-i][(2*n-1)-j]) for i in range(n) for j in range(n)])
     
    return maxSum 

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
