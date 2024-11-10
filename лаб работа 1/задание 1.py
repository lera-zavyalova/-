numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_of_none = 4
sum_without_none = sum(numbers[:index_of_none] + numbers[index_of_none+1:])
count_of_numbers = len(numbers)
average_value = sum_without_none / count_of_numbers
numbers[index_of_none] = average_value
print("Измененный список:", numbers)
