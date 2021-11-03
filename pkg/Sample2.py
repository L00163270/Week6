# --------------------
# File      : .py
# Created   : 03-11-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

from random import randint

Lecturers = ["Pat", "Evelyn", "Priyank"]

class LECTURE:
 def __init__(self, name):
    self._lect_name = name

 @property
 def lnumber(self):
    """This is a getter function for lnumber"""
    return self._lnumber

 @property
 def lect_name(self):
    """The property (getter) must be created before a setter can be made"""
    return self._lect_name

 @lect_name.setter
 def lect_name(self, val):
    """restricting values to a predefined set"""
    if val not in Lecturers:
        raise ValueError("Invalid lecturer")
        self._lect_name = val

 @lect_name.deleter
 def lect_name(self):
    """The deleter is called when del is called"""
    print("del called")
    del self._lect_name

 @staticmethod
 def random_lecturer():
    return Lecturers[randint(0, 2)]