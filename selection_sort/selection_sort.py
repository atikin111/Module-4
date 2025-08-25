def selection_sort(arr):
    size = len(arr)
    for run in range(size):
        min_index = run
        for i in range(run + 1, size):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[run], arr[min_index] = arr[min_index], arr[run]


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)