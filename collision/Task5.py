class RectCorrectError(Exception):
    pass

from collision import Task2, Task3, Task4
def intersectionAreaMultiRect(rectangles):

    for rect in rectangles:
        Task2.isCorrectRect(rect[0], rect[1])

    n = len(rectangles)
    if n == 0:
        return 0

    total_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_area += Task4.intersectionAreaRect(rectangles[i], rectangles[j])

    return total_area
