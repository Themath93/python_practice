def show_list(my_list) :
    print(my_list)
    print("1. id: ", id(my_list))

my_list = [1,2,3,4]
show_list(my_list)
print(my_list)
print("2. id: ",id(my_list))

print(id(show_list(my_list)))