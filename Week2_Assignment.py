# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 07:00:34 2020

@author: Nayan Bhatt
"""
import numpy as np
out=[]
def threesquares(m):
    if m<=0:
        print('Negative number')
        return(False)
    for i in range(0,int(np.sqrt(m))+1):
        temp1=m-i**2                           # temp1 is m-z^2
        for count in range(0,int(np.sqrt(temp1))+1):
            temp2=(temp1-count**2)**0.5                   # temp2 is temp1-y^2
            if (temp2) is int(temp2):
                Flag=True                      # if, temp2's sqrt is perfect int, raise the flag as true
                # out.append(temp2)
                # out.append(count)
                if Flag is True:
                    break
                else:
                    print('Not found')
                
                
Q=threesquares(6)