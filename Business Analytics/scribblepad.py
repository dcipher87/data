import math

# numbers = [1, 5, 10, 3, 8, 12, 4]

# mean = sum(numbers)/len(numbers)

# square_numbers = []

# for num in numbers:
# 	result = (mean - num) **2
# 	square_numbers.append(result)

# variance = sum(square_numbers)/len(square_numbers)
# print(variance)

# print(math.sqrt(variance))

numbers = [2, 3, 3, 3, 4, 6, 7, 8, 9, 12, 15, 15, 22]
mean = sum(numbers)/len(numbers)

squared_numbers = []

for num in numbers:
	result = (num - mean) ** 2
	squared_numbers.append(result)

variance = sum(squared_numbers)/len(squared_numbers)
print(variance)

print(math.sqrt(variance))