# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:02:46 2019

@author: CEC
"""

def isYearLeap(year):

    if  year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True
  #      return False

print(isYearLeap(2200))

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
