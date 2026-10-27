from matplotlib import pyplot plt
import numpy as np
import pandas as pd
x=[1,2,3,4]
y=[35,40,6.0,75]
x1=[1,2,3,4]
y1=[20,35,60,7.5]
plt.bar(x,y,color='c',)
plt.bar(x1,y1,color='g')
plt.legend(['x,y','x1,y1'])
plt.title('graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
