s = set()
print(type(s))

s_from_list = set([1,2,3,4])
print(s_from_list)
print(type(s_from_list))

l = [1,2,3,4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))

s = set()
s.add(1)
s.add(2)
print(s)

# union function
s = set()
s.add(1)
s.add(2)
print(s.union({1,2,3}))

# intersection section
s = set()
s.add(1)
s.add(2)
print(s.intersection({1,2,3}))

s = set()
s.add(1)
s.add(2)
print(len(s))

# isdisjoint function
s = set()
s.add(1)
s.add(2)
s1 = {4,6}
print(s.isdisjoint(s1))

# remove function
s = set()
s.add(1)
s.add(2)
s.remove(2)
print(s)

