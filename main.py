from collision import Task2, Task3, Task4, Task5

print(Task2.isCorrectRect((-3.4, 1),(9.2, 10))) # Вернет True

print(Task2.isCorrectRect((-7, 9),(3, 6))) # Вернет False

print(Task3.isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)])) # Вернет True

print(Task3.isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)])) # Вернет False

print(Task4.intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)])) # Вернет некоторое положительное число

print(Task4.intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)])) # Вернет 0

rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
result = Task5.intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")

