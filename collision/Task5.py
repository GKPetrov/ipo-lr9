class RectCorrectError(Exception):
    pass

from Task2 import isCorrectRect
from Task3 import isCollisionRect
from Task4 import intersectionAreaRect
def intersectionAreaMultiRect(rectangles):

    if not isCorrectRect(rect):
        raise RectCorrectError(f"Некорректный прямоугольник: {rect}")
    for rect in rectangles:
        isCorrectRect(rect)

    n = len(rectangles)
    if n == 0:
        return 0

    total_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_area += intersectionAreaRect(rectangles[i], rectangles[j])

    return total_area
