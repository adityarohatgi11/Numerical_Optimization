#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:45:20 2024

@author: adityarohatgi
"""

#GridSearch Function
def gridsearch(xmin, xmax, p, f):
    # Initialize variables
    # Storing value of x to give max f
    x_val = None
    #Setting max value of f to neg infinity
    max_f_value = -float('inf')
    #Counting no. of times f called
    numf = 0

    #Setting min value for x1   
    x1 = xmin[0]
    while x1 <= xmax[0]:
        #Setting min value for x2
        x2 = xmin[1]
        while x2 <= xmax[1]:
            #Checking f at the point x1,x2
            f_new = f([x1, x2])
            #Incrementing the call counter
            numf += 1              
            #Getting for max value of f
            if f_new > max_f_value:
                max_f_value = f_new
                #Changing the value of x
                x_val = [x1, x2]
            #Incrementing to new value of x2
            x2 += p
        #Incrementing to new value of x1
        x1 += p
    print("x_val_gs", x_val)
    print("numf_gs", numf)     
    return x_val, numf


#Newton Raphson Function
def newton(xinit, e, f, f1, f2):
    #Initializing xinit with x_val to avoid changing it later on 
    x_val = xinit
    #Counting no. of times f1 &f2 called
    numf = 1
    #Gradient at the x_val 
    gradient = f1(x_val)

    while (gradient[0]**2 + gradient[1]**2)**0.5 > e:
        #Hessian at the x_val
        hessian = f2(x_val)
        #Hessian matrix from the list returned by f2
        H = [[hessian[0], hessian[1]], [hessian[2], hessian[3]]]
        #Determinant of the Hessian to check if it's invertible
        det_H = H[0][0] * H[1][1] - H[0][1] * H[1][0]
        #Inverse of the Hessian
        H_inv = [[H[1][1] / det_H, -H[0][1] / det_H], [-H[1][0] / det_H, H[0][0] / det_H]]
        #Update step for Newton-Raphson method: x_new = x - H_inv * gradient
        x_val = [x_val[0] - (H_inv[0][0] * gradient[0] + H_inv[0][1] * gradient[1]),
                  x_val[1] - (H_inv[1][0] * gradient[0] + H_inv[1][1] * gradient[1])]
        gradient = f1(x_val)
        numf = numf+ 2
        
    print("x_val_nr", x_val)
    print("numf_nr", numf)
    return x_val, numf


def f(x):
    return -(x[0]-1)**2-2*(x[1]+2)**2

def f1(x):
    return [-2*(x[0]-1),-4*(x[1]+2)]

def f2(x):
    return [-2,0,0,-4]

#tests newton with initial guess of [0,0] and e=0.001
newton([0,0],0.001,f,f1,f2)   

#tests gridsearch with interval [-10,10] for both x and y and with precision=0.01
gridsearch([-10,-10],[10,10],0.01,f)  

