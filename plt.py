from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
x=[1,2.3,3,4.2]
y=[5,6,7.6,8.1]
plt.plot(x,y,color='#f00880',linewidth=3)
plt.title('metro route sheet')
plt.xlabel('time')
plt.ylabel('station')
plt.legend(['miyapur lane'])
plt.show()
