import time

print("НИЖНИЙ ДИАПАЗОН (n=1)")
arr_min = [5]
print("Массив:", arr_min)

start_time = time.time()

for i in range(1, len(arr_min)):
    key = arr_min[i]
    j = i - 1
    while j >= 0 and arr_min[j] < key:
        arr_min[j + 1] = arr_min[j]
        j -= 1
    arr_min[j + 1] = key

end_time = time.time()

print("Результат:", arr_min)
time_min = end_time - start_time
print(f"Время: {time_min:.6f} сек")

memory_min = 1 * 28 / 1024 / 1024
print(f"Память: {memory_min:.6f} МБ")

print("\n=ПРИМЕР ИЗ ЗАДАЧИ (n=6)")
arr_example = [31, 41, 59, 26, 41, 58]
print("Массив:", arr_example)

start_time = time.time()

for i in range(1, len(arr_example)):
    key = arr_example[i]
    j = i - 1
    while j >= 0 and arr_example[j] < key:
        arr_example[j + 1] = arr_example[j]
        j -= 1
    arr_example[j + 1] = key

end_time = time.time()

print("Результат:", arr_example)
time_example = end_time - start_time
print(f"Время: {time_example:.6f} сек")

memory_example = 6 * 28 / 1024 / 1024
print(f"Память: {memory_example:.6f} МБ")

print("\n=ВЕРХНИЙ ДИАПАЗОН (n=1000)")
memory_max = 1000 * 28 / 1024 / 1024
estimated_time_max = time_example * (1000/6) * (1000/6)

print(f"Память: {memory_max:.6f} МБ")
print(f"Примерное время: {estimated_time_max:.3f} сек")

print("\n=ОГРАНИЧЕНИЯ")
print(f"Лимит времени: 2 сек")
print(f"Лимит памяти: 256 МБ")
print(f"Диапазон n: 1-1000")

print("\n=ПРОВЕРКА ОГРАНИЧЕНИЙ ")
if estimated_time_max < 2:
    print("Время в пределах лимита")
else:
    print("Превышено время")

if memory_max < 256:
    print("Память в пределах лимита")
else:
    print("Превышена память")
