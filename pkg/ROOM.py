# --------------------
# File      : .py
# Created   : 03-11-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

class ROOM:

    def __init__(self, class_num):
        self._class_num = class_num

    @property
    def class_details(self):
        return self._class_num

    @class_details.setter
    def class_details(self, class_num):
        print('Inside class details')
        self._class_num = class_num
        # class_no: int = 4209

    @property
    def display_class_details(self):
        print('Class number: '.format(self._class_num))