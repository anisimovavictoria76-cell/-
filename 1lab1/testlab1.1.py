import time

arr_min = [5]
print("Нижний диапазон (n=1):", arr_min)

start_time_min = time.time()

for i in range(1, len(arr_min)):
    key = arr_min[i]
    j = i - 1
    while j >= 0 and arr_min[j] > key:
        arr_min[j + 1] = arr_min[j]
        j -= 1
    arr_min[j + 1] = key

end_time_min = time.time()

print("Результат:", arr_min)
time_min = end_time_min - start_time_min
print(f"Время для n=1: {time_min:.6f} сек")

arr_example = [31, 41, 59, 26, 41, 58]
print("\nПример из задачи (n=6):", arr_example)

start_time_example = time.time()

for i in range(1, len(arr_example)):
    key = arr_example[i]
    j = i - 1
    while j >= 0 and arr_example[j] > key:
        arr_example[j + 1] = arr_example[j]
        j -= 1
    arr_example[j + 1] = key

end_time_example = time.time()

print("Результат:", arr_example)
time_example = end_time_example - start_time_example
print(f"Время для n=6: {time_example:.6f} сек")

print("\nВерхний диапазон (n=1000):")
memory_min = 1 * 28 / 1024 / 1024
memory_example = 6 * 28 / 1024 / 1024
memory_max = 1000 * 28 / 1024 / 1024

estimated_time_max = time_example * (1000/6) * (1000/6)

print(f"Память для n=1: {memory_min:.6f} МБ")
print(f"Память для n=6: {memory_example:.6f} МБ")
print(f"Память для n=1000: {memory_max:.6f} МБ")
print(f"Примерное время для n=1000: {estimated_time_max:.3f} сек")

print("\nЛимит времени: 2 сек, Лимит памяти: 256 МБ")
