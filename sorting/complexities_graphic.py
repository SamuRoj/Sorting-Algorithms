import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 100)

insertion_sort= x**2
bubble_sort = x**2
selection_sort = x**2
merge_sort = x * np.log2(x)
quick_sort = x * np.log2(x)

plt.plot(x, insertion_sort, label="Insertion Sort", color='blue')
plt.plot(x, bubble_sort, label="Bubble Sort", color='green')
plt.plot(x, selection_sort, label="Selection Sort", color='red')
plt.plot(x, merge_sort, label="Merge Sort", color='pink')
plt.plot(x, quick_sort, label="Quick Sort", color='purple')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)
plt.show()