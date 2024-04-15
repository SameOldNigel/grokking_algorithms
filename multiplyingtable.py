def multiply_table(array):
    for i in array:
        multiplied = []
        for n in range(1,11):
            multiplied.append(i*n)
        print ("Для "+str(i)+" таблица умножения выглядит так "+str(multiplied))

multiply_table([1,2,3,4])

