# Any I/O operation is exception prone
# therefore, we ought to handle the errors and take
# necessary corrective measures

# we emulate an erroneous situation by misspelt file name

try:
    file_object = open('po23em.txt', 'rt', encoding='utf-8')
    contents = file_object.read()
    print(contents)
    file_object.close()

except FileNotFoundError as e:
    print('Oops, we could not find the file')


# read all content
