class RectCorrectError(Exception):
   pass
from Task2 import isCorrectRect
def isCollisionRect(list1, list2):
    if isCorrectRect(list1[0], list1[1]) and isCorrectRect(list2[0], list2[1]):
        if list1[0][0]<list2[1][0] and list1[0][1]<list2[1][1]:
            return True
        else:
            return False
    else:
        raise RectCorrectError('1й прямоугольник некоректный')