import time
import matplotlib.pyplot as plt
import numpy as np


def bubble_sort(arr):
    # Временная сложность: O(n^2) в худшем и среднем случаях
    # Простая сортировка, сравнивающая и меняющая местами соседние элементы
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def merge_sort_recursive(arr):
    # Временная сложность: O(n log n) в худшем, среднем и лучшем случаях
    # Рекурсивный метод, который разбивает массив на половины и затем объединяет их
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_recursive(left_half)
        merge_sort_recursive(right_half)

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


def merge_sort_iterative(arr):
    # Временная сложность: O(n log n) в худшем, среднем и лучшем случаях
    # Итеративный метод сортировки слиянием
    size = 1
    while size < len(arr):
        left = 0
        while left < len(arr) - 1:
            mid = min(left + size - 1, len(arr) - 1)
            right = min(left + 2 * size - 1, len(arr) - 1)
            merge(arr, left, mid, right)
            left += 2 * size
        size *= 2


def quick_sort(arr):
    # Временная сложность: O(n^2) в худшем случае, O(n log n) в среднем и лучшем случаях
    # Быстрая сортировка, разделяет массив на части и рекурсивно сортирует их
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr):
    # Временная сложность: O(n^2) в худшем случае, O(n) в лучшем случае
    # Сортировка, вставляющая элементы в отсортированную часть массива
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    # Временная сложность: O(n^2) в худшем случае, O(n^2) в среднем случае, O(n^2) в лучшем случае
    # Сортировка выбором, выбирает минимальный элемент и помещает его в начало
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def heapify(arr, n, i):
    # Вспомогательная функция для heap_sort
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    # Временная сложность: O(n log n) в худшем, среднем и лучшем случаях
    # Сортировка кучей, строит max-heap и затем извлекает элементы
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def shell_sort(arr):
    # Временная сложность: O(n^2) в худшем случае, в лучшем случае зависит от выбранной последовательности шагов
    # Сортировка Шелла, улучшенная версия сортировки вставками с изменяемым интервалом
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def gnome_sort(arr):
    # Временная сложность: O(n^2) в худшем случае, O(n) в лучшем случае
    # Гномья сортировка, сравнивает соседние элементы и перемещает указатель назад при необходимости
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


def measure_time_complexity(sorting_func, data_size):
    # Измерение времени выполнения для заданной сортировки и размера данных
    data = np.random.rand(data_size)
    start_time = time.time()
    sorting_func(data)
    end_time = time.time()
    return end_time - start_time


def plot_time_complexities(data_sizes, time_complexities, title):
    # Построение графика временной сложности
    plt.plot(data_sizes, time_complexities,
             marker='o', linestyle='-', color='red')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Размер данных')
    plt.ylabel('Время выполнения (секунды)')
    plt.title(title)
    plt.grid(True)
    plt.show()


def main():
    data_sizes = [10, 100, 1000, 10000, 100000]

    choice = input("Выберите тип сортировки ('bubble', 'merge_recursive', 'merge_iterative', 'quick', "
                   "'insertion', 'selection', 'heap', 'shell', 'gnome'): ")

    if choice == 'bubble':
        sorting_func = bubble_sort
        title = 'Рост временной сложности сортировки пузырьком'
    elif choice == 'merge_recursive':
        sorting_func = merge_sort_recursive
        title = 'Рост временной сложности сортировки слиянием (рекурсивная версия)'
    elif choice == 'merge_iterative':
        sorting_func = merge_sort_iterative
        title = 'Рост временной сложности сортировки слиянием (итеративная версия)'
    elif choice == 'quick':
        sorting_func = quick_sort
        title = 'Рост временной сложности быстрой сортировки'
    elif choice == 'insertion':
        sorting_func = insertion_sort
        title = 'Рост временной сложности сортировки вставками'
    elif choice == 'selection':
        sorting_func = selection_sort
        title = 'Рост временной сложности сортировки выборкой'
    elif choice == 'heap':
        sorting_func = heap_sort
        title = 'Рост временной сложности сортировки кучей'
    elif choice == 'shell':
        sorting_func = shell_sort
        title = 'Рост временной сложности сортировки Шелла'
    elif choice == 'gnome':
        sorting_func = gnome_sort
        title = 'Рост временной сложности гномьей сортировки'
    else:
        print("Некорректный выбор. Выбрана сортировка пузырьком.")
        sorting_func = bubble_sort
        title = 'Рост временной сложности сортировки пузырьком'

    time_complexities = [measure_time_complexity(
        sorting_func, size) for size in data_sizes]
    plot_time_complexities(data_sizes, time_complexities, title)


if __name__ == "__main__":
    main()
