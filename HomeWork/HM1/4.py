#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#*Пример:*
#- 1 -> x > 0, y > 0
#- 8 -> нет такой четверти
x = int(input("Введите четверть (от одного до четырех): "))
if x == 1:
    print("x > 0; y > 0")
if x == 2:           
    print("x < 0; y > 0")
if x == 3:        
    print("x < 0; y < 0")
if x == 4:
    print("x > ; y < 0")
         
