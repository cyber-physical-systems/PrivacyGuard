import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:/penv/PGOnline/data/threshold/labeled/result/naiveBayes.csv')
x = df['Threshold']
x = np.array(x)
print('x is :\n',x)
num = df['MCC']
y = np.array(num)
print('y is :\n',y)

f1 = np.polyfit(x, y, 5)
print('f1 is :\n',f1)

p1 = np.poly1d(f1)
print('p1 is :\n',p1)

yvals = p1(x)
print('yvals is :\n',yvals)

plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')

plt.title('NaiveBayes')
plt.show()
