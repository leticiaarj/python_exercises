import sys
import pandas as pd

fptr = sys.stdout
arr = list(map(int, input().rstrip().split()))

arr.sort()

arrDf = pd.DataFrame({'Array':(arr)})
    
grouped = arrDf.groupby('Array').size().reset_index(name='counts')
grouped = grouped[grouped['counts']==1]

print(grouped['Array'].values[0])
