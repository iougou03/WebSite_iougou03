#!/usr/bin/python

def fibo(i):
    if(i==0 or i==1):
    	return 1
    else:
    	return fibo(i-1)+fibo(i-2)
