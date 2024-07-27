# sets
print("Sets:")
print(set("my name is Eric and Eric is my name".split()))

a = set(["jake", "john" , "eric"])
print(a)
b = set(["john", "jill"])
print(b)

# Intersection
print("intersection:")
a = set(["jake", "john", "eric"])
b = set(["john", "jill"])
print(a.intersection(b))
print(b.intersection(a))

# Symmetric difference
print("symmetric_differece:")
a = set(["jake", "john", "eric"])
b = set(["john", "jill"])
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# difference set
print("difference:")
a = set(["jake", "john", "eric"])
b = set(["john", "jill"])
print(a.difference(b))
print(b.difference(a))

# union methode
print("union methode:")
a = set(["jake", "john", "eric"])
b = set(["john", "jill"])
print(a.union(b))

# Exarcise
print("exercise:")
a = ["jake", "john", "eric"]
b = ["john", "jill"]
A = set(a)
B = set(b)
print(A.difference(B))
