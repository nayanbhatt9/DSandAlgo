# # -*- coding: utf-8 -*-
# """
# Created on Thu Feb  6 08:49:43 2020

# @author: Nayan Bhatt
# """

# # Import date-time module for timing 
# from datetime import datetime
# # Program for gcd
# def gcd(m,n):    
#     if m<n:
#         (m,n)=(n,m)
#     if (m%n==0):
#         return n
#     else:
#         return(gcd(n,m%n))
    
# def gcd_naive(m,n):
#     fm=[]
#     for i in range(min(m,n)+1):
#         if m%n==0:
#             return n
        
    
    
# ## Main method
# start_time=datetime.now()
# Q=gcd(10000000000,22600)
# stop_time=datetime.now()
# print (datetime.now()-start_time)
        
# def f(x):
#     d=0
#     while(x>=1):
#         (x,d)=(x/5,d+1)
#         return d
    
# Q=f(4000)

# def h(n):
#     s = 0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+i
#     return(s)

# q1=h(36)
# q2=h(34)

def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)

Qq=g(637,)