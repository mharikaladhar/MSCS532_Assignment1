def insertion_sort_descending(numbers):
    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i-1

        while j >= 0 and numbers[j] < current:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current

    return numbers

values = [45, 12, 78, 34, 23]

print("Before sorting:", values)
insertion_sort_descending(values)
print("After sorting: ", values)

duplicates = [5,2,5,1]
print("Before sorting duplicates:", duplicates)
insertion_sort_descending(duplicates)
print("After sorting duplicates:", duplicates)

mixed_numbers = [-3, 0, 8, -1, 5]
print("Before sorting:", mixed_numbers)
insertion_sort_descending(mixed_numbers)
print("After sorting:", mixed_numbers)
                   
                   