import time
import random


def timed_execution(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time


def sequential_pivot_partition(arr):
    return sum(arr) / len(arr)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(arr, partition_fn):
    if len(arr) <= 1:
        return arr
    else:
        pivot = partition_fn(arr)
        left = [x for x in arr if x <= pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left, partition_fn) + quick_sort(right, partition_fn)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Exemplo de uso:
random_list = random.sample(range(1, 100), 10)
print("Original List:", random_list)

# Algoritmos O(n^2)
print("Bubble Sort:", random_list, "Tempo de execucao:",
      timed_execution(bubble_sort, random_list))

print("Insertion Sort:", random_list, "Tempo de execucao:",
      timed_execution(insertion_sort, random_list))

print("Selection Sort:", random_list, "Tempo de execucao:",
      timed_execution(selection_sort, random_list))

# Algoritmos O(nlogn)
print("Merge Sort:", random_list, "Tempo de execucao:",
      timed_execution(merge_sort, random_list))

print("Quick Sort:", random_list, "Tempo de execucao:", timed_execution(
    lambda x: quick_sort(x, sequential_pivot_partition), random_list))

print("Heap Sort:", random_list, "Tempo de execucao:",
      timed_execution(heap_sort, random_list))
