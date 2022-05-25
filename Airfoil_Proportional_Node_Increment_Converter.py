import matplotlib
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import UnivariateSpline
from matplotlib import pyplot as plt

inputx = [0, 0.2, 0.6, 0.9, 1.0]
inputy = [0, 0.5, 1.0, 0.4, 0]
l1 = len(inputx)
l2 = 7
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

xintv = []
for i in range(len(inputx)-1):
    xintv.append([inputx[i], inputx[i+1]])

def find_interval(num):
    for left, right in xintv:
        if left <= num <= right:
            return [left, right]

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
print(r)

x = np.array(inputx)
y = np.array(inputy)
x_smooth = np.linspace(x.min(), x.max(), 400)
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth,y_smooth)
plt.scatter(x, y, marker='o')

spl = UnivariateSpline(x_smooth, y_smooth, k=5, s=0)
ylist = [round(num, 12) for num in (spl(r).tolist())]
youtput = [abs(ele) for ele in ylist]
print(youtput)







