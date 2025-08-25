def bubble_sort(arr):
    size = len(arr)
    for run in range(size - 1):
        for i in range(size - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)