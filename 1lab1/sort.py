def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    numbers = list(map(int, file.readline().strip().split()))

sorted_numbers = insertion_sort(numbers)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, sorted_numbers)))

print("Готово! Результат в output.txt")