number_one = 2
number_two = 2

print(id(number_one))
print(id(number_two))

print(number_one is number_two)


my_list = []
my_list_two = []

print(id(my_list))
print(id(my_list_two))

print(my_list is my_list_two)
print(my_list == my_list_two)
print(my_list is not my_list_two)

#this is comment
"this is comment too"
'''
this is a multiline
comment
'''
x = 10

y = 10 if x == 15 else 100
print(y)