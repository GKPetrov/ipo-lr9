class RectCorrectError(Exception):
   pass
from collision import Task2
def isCollisionRect(list1, list2):
    if Task2.isCorrectRect(list1[0], list1[1]) and Task2.isCorrectRect(list2[0], list2[1]):
        if list1[0][0]<list2[1][0] and list1[0][1]<list2[1][1]:
            return True
        else:
            return False
    else:
        raise RectCorrectError('1й прямоугольник некоректный')