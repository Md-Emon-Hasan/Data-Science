# pandas
print("pandas:")
dict = {"country": ["Brazil", "Russia",   "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# brics
print("brics:")
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# pandas with csv file
import pandas as pd
cars = pd.read_csv('cars.csv')
print(cars)

# example
print("example:")
import pandas as pd
cars = pd.read_csv("cars.csv", index_col = 0)
print(cars["cars_per_cap"])
print(cars[["cars_per_cap"]])
print(cars[["cars_per_cap","country"]])

import pandas as pd
cars = pd.read_csv("cars.csv", index_col = 0)
print(cars[0:4])
print(cars[4:6])

import pandas as pd
cars = pd.read_csv("cars.csv", index_col = 0)
print(cars.iloc[2])
print(cars.loc[["AUS","EG"]])
