# Basics:
# File I/O is achieved by using the built-in open() function
# Reference: https://docs.python.org/3/library/functions.html#open

# Task 1: Read a file

# Steps:
# a. open with r for reading and t for text
# b. get the file object
# c. read the content to a string variable
# d. close when done

file_object = open('poem.txt', 'rt', encoding='utf-8')

# read all content
contents = file_object.read()

print(contents)

file_object.close()
