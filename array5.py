import array as arr

numbers = arr.array('i', [12, 22, 31])

numbers.append(4)
print(numbers)     

numbers.extend([51, 16, 72])
print(numbers)     
