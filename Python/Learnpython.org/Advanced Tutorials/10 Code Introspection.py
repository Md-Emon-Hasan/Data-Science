# Code Introspection
print("Code Introspection:")
class vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." %(self.name, self.color, self.kind, self.value)
        return desc_str
print(dir(vehicle))
