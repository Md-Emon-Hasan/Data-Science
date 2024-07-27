# numpy
# height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
# weight = [81.65, 97.52, 95.25, 92.98, 86,18, 88.45]
# import numpy as np
# np_height = np.array(height)
# np_width = np.array(weight)
# print(type(np_height))
# print(type(np_width))

height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86,18, 88.45]
import numpy as np
np_height = np.array(height)
np_width = np.array(weight)
bmi = np_width / np_height
print(bmi)

# exercise
print("exercise:")
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
import numpy as np
np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2
print(np_weight_lbs)
