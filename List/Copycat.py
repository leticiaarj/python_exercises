from itertools import permutations

n = int(input())
arr = []
count = 0
countArr = []
item = []

for i in range(n):
    strInput = input()
    arr.append((strInput))

for s in arr:
    aux = list(set(permutations((s))))
    
    for j in range(len(aux)):          
        lenMatrix = len(list(aux[j]))     
        original = list(s)       

        for k in range(lenMatrix):
            if(original[k] != aux[j][k]):
                count = count + 1 
        countArr.append(count)
        count = 0
    print(max(countArr))
    countArr = []
