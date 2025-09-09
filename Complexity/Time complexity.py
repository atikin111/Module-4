# 1. Алгоритм проверки наличия дубликатов в массиве.

def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
'''
Алгоритм имеет сложность O(n log n).
'''

# 2. Алгоритм поиска максимального элемента в неотсортированном массиве.

def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val
'''
Алгоритм имеет сложность O(n). Для проверки дубликатов в неотсортированном массиве необходимо пройти и проверить каждый 
элемент, поэтому это будет линейная сложность.
'''

# 3. Алгоритм сортировки выбором (Selection Sort).

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
'''
Алгоритм имеет сложность О(n^2). Алгоритм будет перебирать массив len(arr) количество раз и каждый раз будет перемещать
элементы массива влево по возрастанию на нужное место.
'''

# 4. Алгоритм быстрой сортировки (Quick Sort).

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
'''
Алгоритм быстрой сортировки имеет сложность О(n log n). 
'''

# 5. Алгоритм вычисления n-го числа Фибоначчи (рекурсивно).

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
'''

'''