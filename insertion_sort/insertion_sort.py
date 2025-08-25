def insertion_sort(arr):
    size = len(arr)
    for run in range(1, size):
        for i in range(1, size):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)