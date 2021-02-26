import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d

x = [1, 2, 3, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
baby = [0.878509105, 0.876886953, 0.88745919, 0.891550149, 0.893045303, 0.89262694, 0.902972964, 0.90738434,
        0.903337113, 0.904961177, 0.900706013, 0.893021403, 0.893684185, 0.889092252, 0.893476694, 0.891584153]
amazon = [0.888904586, 0.898820209, 0.880617153, 0.84436803, 0.821510841, 0.811916242, 0.773280581, 0.764093464,
          0.749525182, 0.738886626, 0.721117069, 0.710251558, 0.716354522, 0.708745198, 0.705062829, 0.707232957]
movement = [0.837685321, 0.829818623, 0.821131593, 0.829562297, 0.803551003, 0.808102312, 0.796888393, 0.789135702,
            0.774331292, 0.777001729, 0.770226835, 0.768525941, 0.765571856, 0.764175988, 0.75796161, 0.759346899]
body = [0.825681031, 0.851663451, 0.839081347, 0.822849085, 0.811434888, 0.816430872, 0.780895413, 0.777469428,
        0.769683224, 0.749692438, 0.741780216, 0.743534778, 0.747292144, 0.75924666, 0.758865167, 0.760976297]
weather = [0.865246825, 0.878952731, 0.88386085, 0.889155753, 0.899152378, 0.904458346, 0.905088602, 0.906541629,
           0.896328548, 0.893962534, 0.887242199, 0.890329219, 0.88334003, 0.887678691, 0.873340322, 0.873757633]

f1 = np.polyfit(x, baby, 2)
p1 = np.poly1d(f1)
dp1 = p1.deriv(1)
#print(p1)
print('Baby', dp1)

f2 = np.polyfit(x, amazon, 2)
p2 = np.poly1d(f2)
dp2 = p2.deriv(1)
#print(p2)
print('amazon', dp2)

f3 = np.polyfit(x, movement, 2)
p3 = np.poly1d(f3)
dp3 = p3.deriv(1)
#print(p3)
print('movement', dp3)

f4 = np.polyfit(x, body, 2)
p4 = np.poly1d(f4)
dp4 = p4.deriv(1)
#print(p4)
print('body', dp4)

f5 = np.polyfit(x, weather, 2)
p5 = np.poly1d(f5)
dp5 = p5.deriv(1)
#print(p4)
print('weather', dp5)


y1 = p1(x)
dy1 = dp1(x)
y2 = p2(x)
dy2 = dp2(x)
y3 = p3(x)
dy3 = dp3(x)
y4 = p4(x)
dy4 = dp4(x)
y5 = p5(x)
dy5 = dp5(x)


#plot1 = plt.plot(dy2, 's', label='original values')
#plot2 = plt.plot(dy1, 'r', label='polyfit values')
plt.plot(x, dy1, 'y', label='Baby')
plt.plot(x, dy2, 'r', label='Amazon')
plt.plot(x, dy3, 'g', label='Movement')
plt.plot(x, dy4, 'b', label='Body')
plt.plot(x, dy5, 'c', label='weather')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)  # 指定legend的位置右下角
plt.title('polyfitting')
plt.show()

