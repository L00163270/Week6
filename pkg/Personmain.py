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

if __name__ == '__main__':

    Joe = PERSON("Joe Bloggs")
    Joe.display_person_details()

    Jane = PERSON("Jane Doe")
    Jane.name = "Jane Doe"
    Jane.display_person_details()