import array as arr

numbers = arr.array('i', [10, 20, 13, 25, 67, 110])

# changing first element
numbers[0] = 0    
print(numbers)     

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)    
