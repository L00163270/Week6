# --------------------
# File      : .py
# Created   : 03-11-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

from Sample1 import PERSON
from sample2 import LECTURE

if __name__ == '__main__':
    Joe=PERSON("Joe Bloggs")
    # not Joe.display_person_details() as it is now treated as a property
    Joe.display_person_details

    Jane = PERSON("Jane")

    #print('1')
    Jane.name = "Jane Doe" # function called as if it were a property due to annotation

    lecturer1 = LECTURE("jo") # instance can be created with any name

    #print('2')
    print(lecturer1.lect_name)
    '''try:
        lecturer1.lect_name = "Pa" # set name to one of predefined values
    except ValueError:
        # here the static method is called without an instance of the class
        print("Pick a valid name such as {}!".format(LECTURER.random_lecturer))'''

    name_var = lecturer1.lect_name # get name using getter method
    print(name_var)
    del lecturer1.lect_name # delete variable not just the value of the variable