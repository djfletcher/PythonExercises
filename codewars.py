# Given an array of one's and zero's convert the equivalent binary value to an integer.
def binary_array_to_number(arr):
  num = 0
  for i in range(len(arr)):
    num += arr[len(arr) - 1 - i] * (2 ** i)
  return num
