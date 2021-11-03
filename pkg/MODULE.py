# --------------------
# File      : .py
# Created   : 03-11-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

class MODULE:

    def __init__(self, mod_num, mod_name):
        self._mod_name = mod_name
        self._mod_num = mod_num

    @property
    def mod_details(self):
        return self._mod_name, self._mod_num

    @mod_details.setter
    def mod_details(self, value):
        print('Inside mod_details')
        self._mod_name = value

    @property
    def display_mod_details(self):
        print("Module name: ".format(self._mod_name))
        print("Module number: ".format(self._mod_num))