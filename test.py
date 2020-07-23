from PIL import Image
import numpy as np
y = np.array([[1,2,3],[2,3,4]],[[2,3,4],[3,4,5]])
print(y)

for i in range(1,len(y)):
    for j in range(1,len(y[0])):
        y[i][j]+=(y[i-1][j]+y[i][j-1]+y[i-1]

print(y)

