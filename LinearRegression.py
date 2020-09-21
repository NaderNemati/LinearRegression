import numpy as np
import matplotlib.pyplot as plt

#We use a simple favorite data set for Linear Regression code.
x = [1.1,1.3,1.5,2,2.2,2.9,3,3.2,3.2,3.7,3.9,4,4,4.1,4.5,4.9,5.1,5.3,5.9,6,6.8,7.1,7.9,8.2,8.7,9,9.5,9.6,10.3,10.5]
y = [39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]




#Model setup
#This function try to sum some stafs for example compute elements of x. 
def find_sum(a,b):
    res = 0
    for i in a:
        res += i**b
    return(res)


#This function try to compute product of elements of to vector for example sum of product of x and y
def find_mul_sum(a1,b1):
    res = 0
    for i in range(len(a1)):
        res+= (a1[i]*b1[i])
    return(res)


sum_x = find_sum(x,1)
sum_y = find_sum(y,1)
sum_x2 = find_sum(x,2)
sum_xy = find_mul_sum(x,y)

#This function try to compute a the system of equations.
def solve_equ(sum_x , sum_y , sum_x2 , sum_xy):
    n = 30
    p = np.array([[sum_x,n], [sum_x2,sum_x]])
    q = np.array([sum_y,sum_xy])
    res = np.linalg.solve(p,q)
    return(res)
res = solve_equ(sum_x , sum_y , sum_x2 , sum_xy)  

#This fuction try to predict amounts of y
def predict(x,res):
    y_pred = []
    for i in x:
        y_pred.append(res[0]*i +res[1])
    return (y_pred)


y_pred = predict(x,res)

#we can plot x and y in addition we plot line of x and y_pred.
plt.scatter(x, y, color = 'red')
plt.plot(x, y_pred, color = 'blue')
plt.title('MyLinearRegressionProgramProject')
plt.xlabel('X')
plt.ylabel('Y')