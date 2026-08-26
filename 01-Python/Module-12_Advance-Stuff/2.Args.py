# *args -> special keywords in Python used in function definitions to ccept a flexible number of arguments.
#         *args becomes a tuple
# only * is to be paased in function, name can be changed, we can write *args or *a, or *abc etc whatever we want


def addition(*a):
    sum = 0
    for i in a:
        sum += i

    print (sum)

addition(12,34,56,72,65,56,675,90)
