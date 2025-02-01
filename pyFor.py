import numpy as np

for i in range (1, 11, 1):
	print(i)
print("That's for-loop with range")

for i in np.arange(-0.5, 0.6, 0.1):
	print("{:.2f}".format(i))
print("This is for-loop with np.arange")

for i in np.linspace(1, 10, 25):
	print(i)
print("That is for-loop with np.linspace")

