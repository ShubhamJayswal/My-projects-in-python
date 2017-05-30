# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:03:30 2017

@author: ss
"""

# My implementation of insertion sort

List=[5,4,3,2,1,11,23,12,45,665,34,656,343,23,4,54,6,576,7,
   8,43,42,54,55,64,34,382,3782,32,3,2,32,32,3,24,34,3,
   5,45,4,54,6,46,35,4,3,4,4,2,4,35,45,546,45534535,35,
   34,543,5,435,34,53,54,35,25342,6,56,536,2,24352,45,5,
   24,525,3,6,2656,7,735,3422,4,42,43,35,54,435,34,3,45,
   6,56,54,6,5436,62,4356,5635,7,5,4322,5,6,6763,24,
   4,5,6,54,654,7,8,8,76,4,535,475,65,74,7,576,56,57,4,43,
   23,243,35,463,6,57,64,858,9,5,54,632,251,7,76,4854,67,
   2,45,4573,4875,69,788,4589,6897,665476,47,46235,252]

"insertion sort is O(n^2)"
def insertion_sort(L):

    for i in range(1, len(L)):
     
         value=L[i]
         place=i   
         
         """the while loop will run for 1+2+3+4=5.....n-1 times in worst
         and average case, while in best case, it will not get 
         into the while loop"""
         
         while(place>0 and L[place-1]>value):
         
            L[place]=L[place-1]
            place=place-1
        
         L[place]=value
    
    print(L)        
      
insertion_sort(List)    
    


