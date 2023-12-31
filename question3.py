def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


# Exemplo de uso:
arr = [4, 2, 5, 1, 3]
counting_sort(arr)
print("Array ordenado:", arr)
