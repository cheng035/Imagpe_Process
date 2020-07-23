from PIL import Image
import numpy as np
c = np.array([[[1,2,3],[2,3,4]],[[2,3,4],[3,4,5]]])
y=c
print(y)
n=len(y)
m=len(y[0])
for i in range(1,n):
    y[i][0]+=y[i-1][0]

for j in range(1,m):
    y[0][j]+=y[0][j-1]

for i in range(1,n):
    for j in range(1,m):
        y[i][j]+=(y[i-1][j]+y[i][j-1]-y[i-1][j-1])
print(c)


