# --------------------
# File      : .py
# Created   : 01-11-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

from STUDENT import STUDENT
from ROOM import ROOM
from MODULE import MODULE

if __name__ == '__main__':
    print('First Step')
    StudName = STUDENT('Sreejith JP', 'L00163270')
    print(StudName.display_person_details())
    # print('Second')
    # ModName = MODULE(1, 'Python')
    # print(ModName.display_mod_details())
    # print('Third')
    # RoomDet = ROOM(4209)
    # print(RoomDet.display_class_details())
    print( StudName.stud_details )
    print( StudName.display_person_details )

    print("Thank you for using my application")