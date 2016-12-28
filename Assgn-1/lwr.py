import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def extended(ax, x, y, **args):
    #Function to extend line segment
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    x_ext = np.linspace(xlim[0], xlim[1], 100)
    p = np.polyfit(x, y , deg=1)
    y_ext = np.poly1d(p)(x_ext)
    ax.plot(x_ext, y_ext, **args)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    return ax

train_float = list()
test_float = list()
with open('quasar_train.csv', 'rb') as csvfile:
    reader_ = csv.reader(csvfile, delimiter=',')
    rows = list()
    for row in reader_:
        rows.append(row)

    for row in rows:
        arr = [float(x) for x in row]
        train_float.append(arr)

with open('quasar_test.csv', 'rb') as csvfile:
    reader_ = csv.reader(csvfile, delimiter = ',')
    rows = list()
    for row in reader_:
        rows.append(row)

    for row in rows:
        arr = [float(x) for x in row]
        test_float.append(arr)

lamda = np.matrix(train_float[0]).transpose()
train_qso = np.matrix(train_float[1: ])

X = lamda
Y = train_qso[0].transpose()
print X.shape, Y.shape

data = list()
for i in range(0, 100):
    num = np.random.randint(1150, 1599)
    data.append(num)

data = train_float[0]
print data
interpolate = list()
for wave in data:
    W = np.zeros((450, 450))
    for i in range(0, 450):
        W[i, i] = math.exp(-((wave - lamda.item((i, 0)))**2)/1000000)
    theta = np.linalg.inv(np.matmul(np.matmul(X.transpose(), W), X))
    theta = np.matmul(theta, Y.transpose())
    theta = np.matmul(theta, np.matmul(W, X))
    interpolate.append(theta.item((0, 0))*wave)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(train_float[0], train_float[1], c='r', label='raw-data')
ax1.set_xlim([1150, 1600])
ax1.set_ylim([-2.0, 8.0])

X_ = data
Y_ = interpolate
f = interp1d(X_, Y_, kind='cubic')
plt.plot(X_, Y_,'-', label='tau=1000')
plt.legend()
plt.show()

