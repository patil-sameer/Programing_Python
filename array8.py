import array as arr

number = arr.array('i', [11, 22, 33, 33, 44])

del number[2]  
print(number)  

del number  
print(number)  
