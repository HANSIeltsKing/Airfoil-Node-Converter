import matplotlib
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import UnivariateSpline
from matplotlib import pyplot as plt

x1 = [1, 0.9, 0.6, 0.2, 0, 0.2, 0.6, 0.9, 1] # your old airfoil x-coordinate
y1 = [0, 0.4, 1, 0.5, 0, -0.5, -1.0, -0.4, 0] # your old airfoil y-coordinate
node = 12 # desired number of nodes (must be larger)

"""
# if you want to use local airfoil dat in excel or csv
af = pd.read_excel("C:/Users/xxx/Desktop/yourexcelname.xlsx", sheet_name = "Sheet1", header = None) # use your path
x1 = af[0].tolist()
y1 = af[1].tolist()
node = 250
"""

# cut the positive half
inputx = []
for i in range(int(0.5 * len(x1) + 1)):
    inputx.append(x1[-int(0.5 * len(x1) - i + 1)])
inputy = []
for i in range(int(0.5 * len(y1) + 1)):
    inputy.append(-y1[-int(0.5 * len(y1) - i + 1)])

# uniform cut coincidence
l1 = len(inputx)
l2 = 1 + int(node / 2)
def partition(num):
    list = []
    list.append(0)
    for i in range(num):
        list.append(round((i+1) * (1/num), 12))
    return list
def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3
clean = [0, 1]
intsec_list = intersection(partition(l1-1), partition(l2-1))
intsec = [item for item in intsec_list if item not in clean]
ped = (l2 - 1) / (len(intersection(partition(l1-1), partition(l2-1))) - 1)

# open all intervals
xintv = []
for i in range(len(inputx)-1):
    xintv.append([inputx[i], inputx[i+1]])

# interval attribution of each data
def find_interval(num):
    for left, right in xintv:
        if left <= num <= right:
            return [left, right]

# output x-coordinate in scale
r = []
r.append(0)
z = 0
for i in range(l2-2):
    if (i + 1) / ped == int((i + 1) / ped):
        g = xintv[i - z][0]
        z = z + 1
    else:
        g = xintv[i - z][0] + (xintv[i - z][1] - xintv[i - z][0]) * (1 - (((i + 1) / ped) - int((i + 1) / ped)))
    r.append(round(g, 12))
r.append(1)

# equivalent matlab ppval
x = np.array(inputx)
y = np.array(inputy)
x_smooth = np.linspace(x.min(), x.max(), 400)
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth,y_smooth)
plt.scatter(x, y, marker='o')
"""
# if you want to see the graph
plt.show()
"""

# output y-coordinate in scale
spl = UnivariateSpline(x_smooth, y_smooth, k=5, s=0)
ylist = [round(num, 12) for num in (spl(r).tolist())]
youtput = [abs(ele) for ele in ylist]

# integrate into a complete airfoil
dim = 2 * len(r) - 1
x2 = []
for i in range(dim - len(r)):
    x2.append(r[-(i + 1)])
for j in range(len(r)):
    x2.append(r[j])
y2 = []
for i in range(dim - len(youtput)):
    y2.append(youtput[-(i + 1)])
y2.append(0)
for j in range(len(youtput) - 2):
    y2.append(-(youtput[j + 1]))
y2.append(0)
print(x2)
print(y2)






