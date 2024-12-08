from Task2 import isCorrectRect
from Task3 import isCollisionRect
class ValueError(Exception):
   pass
def intersectionAreaRect(list1, list2):
    if isCorrectRect:
        if isCollisionRect:
            res = abs((list2[1][0]-list1[0][0])*(list2[1][1]-list1[0][1]))
            return res
        else:
            return 0
    else:
        raise ValueError("Передан некорректный прямоугольник")