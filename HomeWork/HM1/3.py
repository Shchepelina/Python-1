x = int(input("Введите координату х: "))
y = int(input("Введите координату y: "))
if x > 0:
    if y > 0:
        print('1 четверть')
    else:
        print('4четверть')

if x < 0: 
    if y > 0:
        print('2 четверть')
    else:  
        print('3 четверть')
               
