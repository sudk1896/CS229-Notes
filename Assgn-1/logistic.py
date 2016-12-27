import numpy as np
import math
import matplotlib.pyplot as plt

#Take the input and create the Design matrix first
#Each column is one training sample.


array = list()
X1, X2 = list(), list() #Label as 1
Y1, Y2 = list(), list() #Label as -1
with open('logistic_x.txt', 'r') as ins:
    for line in ins:
        numbers = line.split()
        numbers = [float(var) for var in numbers]
        numbers.insert(0, 1.0) #theta_0,1,2
        array.append(numbers)

X = np.matrix(array)

Y = list()
with open('logistic_y.txt', 'r') as ins:
    for line in ins:
        num = line.split()
        num = [float(var) for var in num]
        if num[0]<0:
            num[0]=0.0
        Y.append(num[0])

Y = np.matrix(Y)

##print X
##print Y

tmp_trav = Y
for i in range(0, X.shape[0]):
    if Y.item((0, i)) > 0:
        X1.append(X.item((i, 1))), X2.append(X.item((i, 2)))
    else:
        Y1.append(X.item((i, 1))), Y2.append(X.item((i, 2)))


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(X1, X2, c='b')
ax1.scatter(Y1, Y2, c='r')

#Y is also a row vector.

def Sigmoid(theta, X):
    #Calculate Sigmoid Function
    #theta and X are row vectors.
    #theta^T dot X
    return 1.0/(1.0 + np.exp(-np.dot(theta, X.transpose()).item((0, 0))))

    
def Delta_Likelihood(X, Y, theta):
    #Design matrix, output labels, theta resp.
    #Calculate delta of log-likelihood
    #Returns a row vector, you need to transpose
    #to a column vector
    ret = list()
    no_samples = X.shape[0] #equal to length of Y
    no_features = X.shape[1]
    for j in range(0, no_features):
        elem = 0.0
        for i in range(0, no_samples):
            elem += (Y.item((0, i)) - Sigmoid(theta, X[i])*X.item((i, j)))
        ret.append(elem)
    ret = np.matrix(ret)
    return ret

def Hessian(theta, X):
    #returns the Hessian matrix
    no_samples = X.shape[0]
    no_features = X.shape[1]
    H = np.zeros((no_features, no_features))
    H = np.matrix(H)
    constant = 0.0
    for i in range(0, no_samples):
        H += (Sigmoid(theta, X[i])*(1 - Sigmoid(theta, X[i]))*np.matmul(X[i].transpose(), X[i]))
##        constant += Sigmoid(theta, X[i])*(1 - Sigmoid(theta, X[i]))
##    constant *= -1
##    mult = -1*constant
##    H = mult*H
##    print H
##    tmp = np.matmul(X.transpose(), H)
##    tmp1 = np.matmul(tmp, X)
##    tmp1 *= -1
##    print H.shape
    H *= -1
    return H

def Newton_Rhapson(X, Y, num_iterations = 5):
    no_features = X.shape[1]
    theta = [1]*no_features
    theta = np.matrix(theta)
    #Theta is a row vector
    for i in range(0, num_iterations):
        tmp_theta = theta - np.matmul(np.linalg.inv(Hessian(theta, X)), Delta_Likelihood(X, Y, theta).transpose()).transpose()
        theta = tmp_theta
    print theta.shape
    return theta
        
Theta = Newton_Rhapson(X, Y, 2)
print Theta
arr = Theta.tolist()
plt.plot([0, -arr[0][0]/arr[0][2]], [-arr[0][0]/arr[0][1], 0], color='g', linestyle='-', linewidth=2)
plt.show()
