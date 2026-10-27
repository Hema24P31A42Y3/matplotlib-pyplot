from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
x=[1,2,3,4]
y=[35,40,60,75]
x1=[1,2,3,4]
y1=[20,35,65,60]
plt.scatter(x,y,color='r',linewidth=1)
plt.scatter(x1,y1,color='g',linewidth=1)
plt.legend(['red','green'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
