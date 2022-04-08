import array as arr

odd = arr.array('i', [11, 13, 5])
even = arr.array('i', [12, 14, 16])

numbers = arr.array('i')   # creating empty array of integer
numbers = odd + even

print(numbers)
