from collision import Task2, Task3
class ValueError(Exception):
   pass
def intersectionAreaRect(list1, list2):
    if Task2.isCorrectRect(list1[0], list1[1]) and Task2.isCorrectRect(list2[0], list2[1]):
        if Task3.isCollisionRect(list1, list2):
            res = abs((list2[1][0]-list1[0][0])*(list2[1][1]-list1[0][1]))
            return res
        if not Task3.isCollisionRect(list1, list2):
            return 0
    else:
        raise ValueError("Передан некорректный прямоугольник")