import time

print("НИЖНИЙ ДИАПАЗОН (n=1)")
arr_min = [5]
print("Массив:", arr_min)

start_time = time.time()

sorted_min = arr_min.copy()
positions_min = [1]

end_time = time.time()

print("Результат:", sorted_min)
print("Позиции:", positions_min)
time_min = end_time - start_time
print(f"Время: {time_min:.6f} сек")

memory_min = 1 * 28 / 1024 / 1024
print(f"Память: {memory_min:.6f} МБ")

print("\n=ПРИМЕР ИЗ ЗАДАЧИ (n=10)")
arr_example = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
print("Массив:", arr_example)

start_time = time.time()

sorted_example = arr_example.copy()
positions = [0] * len(arr_example)
positions[0] = 1

for i in range(1, len(arr_example)):
    key = sorted_example[i]
    j = i - 1
    while j >= 0 and sorted_example[j] > key:
        sorted_example[j + 1] = sorted_example[j]
        j -= 1
    sorted_example[j + 1] = key
    positions[i] = j + 2

end_time = time.time()

print("Результат:", sorted_example)
print("Позиции:", positions)
time_example = end_time - start_time
print(f"Время: {time_example:.6f} сек")

memory_example = 10 * 28 / 1024 / 1024
print(f"Память: {memory_example:.6f} МБ")

print("\n=ВЕРХНИЙ ДИАПАЗОН (n=1000)")
memory_max = 1000 * 28 / 1024 / 1024
estimated_time_max = time_example * (1000/10) * (1000/10)

print(f"Память: {memory_max:.6f} МБ")
print(f"Примерное время: {estimated_time_max:.3f} сек")

print("\n=ОГРАНИЧЕНИЯ")
print(f"Лимит времени: 2 сек")
print(f"Лимит памяти: 256 МБ")
print(f"Диапазон n: 1-1000")

print("\n=ПРОВЕРКА ОГРАНИЧЕНИЙ")
if estimated_time_max < 2:
    print("Время в пределах лимита")
else:
    print("Превышено время")

if memory_max < 256:
    print("Память в пределах лимита")
else:
    print("Превышена память")
