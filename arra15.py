#operation  on array
from array import *
#create an array with int values
arr=array('i',[10,20,30,40,50,60,70,80,90])
print('Original array: ',arr)
#apend 45 to array
arr.append(45)
arr.append(65)
print('after appending 45 and 65:',arr)
#insert 99 at position number 1 in arr
print('After inserting 99 in the first position: ', arr)
#remove elements froma array
arr.remove(20)
print('after remove 20: ',arr)
#remove last elements using pop() methods
n=arr.pop()
print('array after using pop():',arr)
print('popped elements :',  n)
n=arr.index(30)
print('first occurance of elements 30 is at ', n)
lst=arr.tolist()
print('list:', lst)
print('array : ', arr)
