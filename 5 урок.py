1.
my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв абв вбмбваббвабб текста все вававбвбв слова, содерабващие содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)

2.
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
3.
maps = [1,2,3,
        4,5,6,
        7,8,9]
 

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 

def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
     

def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 

def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win
 

def check_line(sum_O,sum_X):
 
    step = ""
    for line in victories:
        o = 0
        x = 0
 
        for j in range(0,3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1
 
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]
                 
    return step
 

def AI():        
 
    step = ""
 
    
    step = check_line(2,0)
 
    
    if step == "":
        step = check_line(0,2)        
 
    
    if step == "":
        step = check_line(1,0)           
 
    
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5           
 
    
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1           
   
    return step
 

game_over = False
human = True
 
while game_over == False:
 
    
    print_maps()
 
    
    if human == True:
        symbol = "X"
        step = int(input("Человек,ваш ход: "))
    else:
        print("Компьютер делает ход: ")
        symbol = "O"
        step = AI()
 
    
    if step != "":
        step_maps(step,symbol) 
        win = get_result() 
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("Ничья!")
        game_over = True
        win = "дружба"
 
    human = not(human)        
 
        
print_maps()
print("Победил", win)   

4.
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")