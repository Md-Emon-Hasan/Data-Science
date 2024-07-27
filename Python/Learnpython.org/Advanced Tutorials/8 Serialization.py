# serialition
print("seralization:")

# dumps method
print("dumps method:")
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

# use pickle function
print("use pickled function:")
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

# Example
print("example:")
import json
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
