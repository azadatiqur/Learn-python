# number_one = 2
# number_two = 2
#
# print(id(number_one))
# print(id(number_two))
#
# print(number_one is number_two)
#
#
# my_list = []
# my_list_two = []
#
# print(id(my_list))
# print(id(my_list_two))
#
# print(my_list is my_list_two)
# print(my_list == my_list_two)
# print(my_list is not my_list_two)
#
# #this is comment
# "this is comment too"
# '''
# this is a multiline
# comment
# '''
# x = 10
#
# y = 10 if x == 15 else 100
# print(y)

#list comprehension
# numbers = [number for number in range(1, 11)]
#
# odd_numbers = [number for number in numbers if number%2 != 0]
#
# for number in odd_numbers:
#     print(number)

# #string
# p = 4
# paragraph = """Lorem ipsum Lorem ipsum
# Lorem ipsum Lorem ipsum Lorem ipsum
# Lorem  ipsum Lorem ipsum
# Lorem ipsum Lorem ipsum
# Lorem ipsum Lorem ipsum
#  """
# pp = '{0} is great!'.format(p)
# firstName = "Fazle"
# lastName = "Rahat"
# print("{first} {last}".format(first=firstName, last=lastName))
# print(paragraph, pp)


# import os
# #os.listdir() method
# path = 'dataset'
# #print(os.listdir(path))
# files = os.listdir(path)
# for file in files:
#     if os.path.isfile(os.path.join(path, file)):
#         print("{} is a file".format(file))

#os.scandir(path)
# all_files = os.scandir(path)
#
# for file in all_files:
#     if file.is_file():
#         print("{} is a file".format(file))
#
# #using pathlib module
#
# import pathlib
#
# path_obj = pathlib.Path(path)
#
# for file in path_obj.iterdir():
#     if file.is_file():
#         print(file.name)

# file = open('lesson_2/test.txt', 'r')

# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line) #prints every line separately

# all_lines = file.readlines()#all lines in a list as element
#
# print(all_lines)


#close the file
# file = open('lesson_2/test.txt', 'r')
# print(file.read())
# file.close()

#this one is better
# with open('lesson_2/test.txt', 'r') as file:
#     print(file.read())


#write in a file
# with open('lesson_2/test.txt', 'w') as file:
#     file.write('This is a program file.') #this will overwrite if mode is 'w'

# with open('lesson_2/test.txt', 'a') as file:
#     file.write('\nThis is append line')
#     line_list = ['\nThis is first line', '\nThis is second line', '\nThis is third line']
#     file.writelines(line_list)

# user_data = [
#     {
#         'file_name' : 'user_1.txt',
#         'context' : "Hello, This is from User 1"
#     },
#     {
#         'file_name' : 'user_2.txt',
#         'context' : "Hello, This is from User 2"
#     },
#     {
#         'file_name' : 'user_3.txt',
#         'context' : "Hello, This is from User 3"
#     }
# ]
#
# for data in user_data:
#     with open("lesson_2/{}".format(data['file_name']), 'w') as file:
#         file.write(data['context'])


#check if a file exists
#path = 'lesson_2/test.txt'
# import os
# print(os.path.isfile(path))

# import pathlib
# file = pathlib.Path(path)
# print(file.is_file())


#deleting a file
# import os
#
# path = 'lesson_2/test.txt'
#
# if os.path.isfile(path):
#     os.remove(file)
# else:
#     print("file doesn't exist")


#deleting a folder

# import os
# path = 'dataset/a'
# if os.path.exists(path):
# #print(os.listdir(path))
#     for file in os.listdir(path):
#         os.remove(path+"/"+file)
#     os.removedirs(path)
# else:
#     print("folder doesn't exist")