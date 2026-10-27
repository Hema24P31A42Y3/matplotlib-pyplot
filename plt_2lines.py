from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
sumsung=[1,2,3,4]
sum_sales=[35,40,60,75]
oneplus=[1,2,3,4]
oneplus_sales=[20,35,65,60]
plt.plot(sumsung,sum_sales,color = '#44fc72',linewidth=2)
plt.plot(oneplus,oneplus_sales,color = '#edfc44',linewidth=2)
plt.legend(['sumsung','oneplus'])
plt.title("mobile sales")
plt.xlabel('mobiles')
plt.ylabel('sales')
plt.savefig("sales_mobile.png")
plt.show()
