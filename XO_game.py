# создаем игровое поле
list_axes=['/ ','1','2','3']
list_1=['1','-','-','-']
list_2=['2','-','-','-']
list_3=['3','-','-','-']
print(list_axes,'\n',list_1,'\n',list_2,'\n',list_3)
# задаем условие работы, если "не 1", то игра останавливается
win=1
while win ==1 :
    # первый огрок делает ход
    x = int (input('Игрок "Х" введите номер строки (от 1 до 3): '))
    y = int(input('Игрок "Х" введите номер столбца (от 1 до 3): '))
    if x==1:
        list_1[y]='X'
        print(list_axes,'\n',list_1,'\n',list_2,'\n',list_3)
    elif x==2:
        list_2[y] = 'X'
        print(list_axes, '\n', list_1, '\n', list_2, '\n', list_3)
    elif x==3:
        list_3[y] = 'X'
        print(list_axes, '\n', list_1, '\n', list_2, '\n', list_3)
    else: print('Вы ввели некорректное число: ')
    # второй игрок делает ход
    o = int(input('Игрок "O" введите номер строки (от 1 до 3): '))
    y = int(input('Игрок "O" введите номер столбца (от 1 до 3): '))
    if o == 1:
        list_1[y] = 'O'
        print(list_axes, '\n', list_1, '\n', list_2, '\n', list_3)
    elif o == 2:
        list_2[y] = 'O'
        print(list_axes, '\n', list_1, '\n', list_2, '\n', list_3)
    elif o == 3:
        list_3[y] = 'O'
        print(list_axes, '\n', list_1, '\n', list_2, '\n', list_3)
    else: print('Вы ввели некорректное число: ')

    # win=0  # условия выполнения программы


