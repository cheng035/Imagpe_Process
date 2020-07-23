import copy

from PIL import Image
import numpy as np
# to reduce the image intensity level
## Intensity refers to the amount of light or the numerical value of a pixel. For example, in grayscale images,
# it's depicted by the grey level value at each pixel (e.g., 127 is darker than 220) .
def change_image_intensity(url,level):
    a = np.array(Image.open(url))
    print(a)

    b = a//level*level
    im = Image.fromarray(b.astype('uint8'))
    im.save('2.jpg')

def inbound(x,y,n,m):
    return x>=0 and x<n and y>=0 and y<m

def blur_image(url,area):
    a = np.array(Image.open(url),dtype=np.int)
    n=len(a)
    m=len(a[0])
    b= copy.deepcopy(a)
    dp=a
    for i in range(1,n):
        dp[i][0]+=dp[i-1][0]

    for j in range(1,m):
        dp[0][j]+=dp[0][j-1]


    for i in range(1,n):
        for j in range(1,m):
            dp[i][j]+=(dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1])
    print(dp-a)
    for i in range(n):
        for j in range(m):
            print(i,j)
            x1=max(i-area-1,0)
            x2=min(i+area,n-1)
            y1=max(j-area-1,0)
            y2=min(j+area,m-1)
            count=(y2-y1+1)*(x2-x1+1)
            new=dp[x2][y2]-dp[x2][y1]-dp[x1][y2]+dp[x1][y1]
            new=new//count
            b[i][j]=new
    print(b)
    im = Image.fromarray(b.astype('uint8'))
    im.save('4.jpg')

    for i in range(n):
        for j in range(m):
            x1 = max(i - area - 1, 0)
            x2 = min(i + area, n - 1)
            y1 = max(j - area - 1, 0)
            y2 = min(j + area, m - 1)
            count = (y2 - y1 + 1) * (x2 - x1 + 1)
            new=(0,0,0)
            for k in range(x1,x2):
                for q in range(y1,y2):
                    new+=a



blur_image('1.jpg',20)
