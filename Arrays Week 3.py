import numpy as np

array = np.random.randint(0, 101, size=(5, 5))    # get random number

print("Entire 5x5 Array:\n", array)  # print array

print("\nElement at 2nd row, 3rd column:", array[1, 2])

print("\nSum of all elements:", np.sum(array))

print("\nMean of each row:", np.mean(array, axis=1))

print("\nMax value in each column:", np.max(array, axis=0))