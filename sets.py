my_set = {"January", "February", "March"}
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)

my_set.remove("January")
print(my_set)

#sets having ability to not to allowing the duplicate value in inside the set and
# we can't have particular order in each time we run the programm set may be changed not like privious one
#in the list we can have the duplicate value in a particular order


my_list = ["January", "February", "March"]
my_list.remove("January")
print(my_list)