with open('input.txt', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

sorted_arr = arr.copy()
positions = [0] * n

positions[0] = 1

for i in range(1, n):
    key = sorted_arr[i]
    j = i - 1
    
    while j >= 0 and sorted_arr[j] > key:
        sorted_arr[j + 1] = sorted_arr[j]
        j = j - 1
    
    sorted_arr[j + 1] = key
    positions[i] = j + 2

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, positions)) + '\n')
    f.write(' '.join(map(str, sorted_arr)))

print(" ")