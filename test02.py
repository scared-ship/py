# import json
# from test03 import *


# import test03
#

# print("helloworld")

# username = input("what is your name")
# file_path='F:\.temp\新建文本文档1.txt'
# with open(file_path,'w') as file_object:
#     json.dump(username, file_object)
#     print("We'll remember yo when you come back," + username + "!")
    # contents = file_object.read()
    # for line in file_object:
    #     print(line.rstrip())


# try:
# #     print(5/0)
# # except ZeroDivisionError:
# #     pass
# #     print("you can't divide by zero")

filename = 'F:\.temp\新建文本文档.txt'


# try:
#     with open(filename) as f_obj:
#        contents= f_obj.readlines()
# except FileNotFoundError:
#      msg = "Sorry,the file" + filename +" does not exist "
#      print(msg)
# else:
#     pi_string = ''
#     for line in contents:
#         pi_string +=line.rstrip()
#
#     birthday = input("birthday")
#     if birthday in pi_string:
#         print(1)
#     else:
#         print(2)
    # words = contents.split()
    # new_words = len(words)
    # print("The file" + filename + "has about" + str(new_words) + "words")

with open(filename,'a') as file_obj:
    file_obj.write("i love programming.\n")