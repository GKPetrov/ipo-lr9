def isCorrectRect(tuple1, tuple2):
    if len(tuple1) != 2 and len(tuple2) != 2:
        print('Неверные размеры кортежа')
    else:
        if(tuple1[0]>tuple2[0] or tuple1[1]>tuple2[1]):
            return False
        else:
            return True