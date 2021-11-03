# --------------------
# File      : .py
# Created   : 03-11-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

class PERSON:
    def __init__(self, name):
        self._name = name # cannot be accessed outside of class
        print("Init ran successfully")

    @property
    def name(self):
        print('In property')
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        print('In Setter')

    @property
    def display_person_details(self):
        print("Name: ".format(self._name))