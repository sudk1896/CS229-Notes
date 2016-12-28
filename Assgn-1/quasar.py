import csv
import numpy as np
import matplotlib.pyplot as plt

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

tmp_lamda = list()
for num in train_float[0]:
    z = [1.0]
    z.append(num)
    tmp_lamda.append(z)

lamda = np.matrix(tmp_lamda)
train_qso = train_float[1: ]

train_qso = np.matrix(train_qso)
#Of sizes, (1, 450) (200, 450) (50, 450)

#For sub-problem (b)
X = lamda
Y = train_qso[0].transpose()
print X.shape, Y.shape

theta = np.linalg.inv(np.matmul(X.transpose(), X))
theta = np.matmul(theta, X.transpose())
theta = np.matmul(theta, Y)
print theta, theta.item((0, 0)), theta.item((1, 0))
print X.item((0, 0)), X.item((0, 1))


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(train_float[0], train_float[1], c='r', label='raw-data')
ax1.set_xlim([1150, 1600])
ax1.set_ylim([-2.0, 8.0])
ax1 = extended(ax1, train_float[0], train_float[1], color='b', linestyle='-', linewidth=2, label='regression-line')
plt.plot([0, X.item((0, 1))], [theta.item((0, 0)), theta.item((0, 0)) + theta.item((1, 0))*X.item((0, 1))], color='b',
         linestyle='-', linewidth=2)
ax1.set_xlabel('Wavelength')
ax1.set_ylabel('Flux')
ax1.legend()
plt.show()  
