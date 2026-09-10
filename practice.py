import numpy as np


def calculate_statistics(numbers):
    numbers_array = np.array(numbers)

    mean = np.mean(numbers_array)
    maximum = np.max(numbers_array)
    minimum = np.min(numbers_array)
    total = np.sum(numbers_array)

    print("Array:", numbers_array)
    print("Mean:", mean)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Sum:", total)


numbers = [10, 20, 30, 40, 50]

calculate_statistics(numbers)