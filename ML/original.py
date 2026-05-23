import numpy as np
array=np.arange(15).reshape(3,5)
print("original array",array)
print("ravel array",array.ravel())
print("\n numpy.ravel=== =numpy.reshape(-1)")
print("reshape array",array.reshape(-1))