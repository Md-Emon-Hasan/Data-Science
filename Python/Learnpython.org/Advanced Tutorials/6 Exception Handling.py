# Exception Handling
print("Exception Handling:")
def do_stuff_with_nunber(n):
    print(n)
def catch_this():
    the_list = (1, 2, 3, 4, 5)
    for i in range(20):
        try:
            do_stuff_with_nunber(the_list[i])
        except IndexError:
            do_stuff_with_nunber(0)
catch_this()

# Exercise:
print("Exercise:")
actor = {"name":"John Cleese", "rank": "awesome"}
def get_last_name():
    return actor["name"].split()[1]
get_last_name()
print("All exception caught! Good job!")
print("The actor's last name is %s" % get_last_name())

