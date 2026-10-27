from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
programming_lans=[9.54,11.08,10.36,23.85]
labels=['c','c++','java','python']
explode=(0.01,0.01,0.01,0.01)
plt.pie(programming_lans,labels=labels,explode=explode,startangle=90,autopct='%.2f%%')
plt.show()
