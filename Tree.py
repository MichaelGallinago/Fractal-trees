#---- MicG ---------
# генерация дерева с листьями
import turtle
import sys
import re
from random import randint

def drawTree():
    screen = turtle.Screen()
    screen.bgpic('xp.png')
    turtle.setheading(0)
    turtle.hideturtle()
    turtle.tracer(0)
    turtle.penup()
    thick = 16
    turtle.pensize(thick)
    turtle.setposition(0,-300)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor(col1)

    time = 0
    
    translate={"1":"21","0":"1[-20]+20"}
    axiom = "22220"
    axmTemp = ""
    itr = 12
    angl = 16
    dl = 10
    stc = []
    for k in range(itr):
        for ch in axiom:
            if ch in translate:
                axmTemp+=translate[ch]
            else:
                axmTemp+=ch
        axiom = axmTemp
        axmTemp = ""

    for ch in axiom:
        if show:
            time+=1
        if   ch == "+":
            turtle.right(angl - randint(-13,13))
        elif ch == "-":
            turtle.left(angl - randint(-13,13))
        elif ch == "2":
            if randint(0,10)>4:
                turtle.forward(dl)        
        elif ch == "1":
            if randint(0,10)>4:
                turtle.forward(dl) 
        elif ch == "0" and leafs == True:
            stc.append(turtle.pensize())
            turtle.pensize(4)
            r = randint(0,10)
            if r<3:
                    turtle.pencolor(col2)
            elif r>6:
                    turtle.pencolor(col3)
            else:
                    turtle.pencolor(col4)
            turtle.forward(dl-2)
            turtle.pensize(stc.pop())   
            turtle.pencolor(col1)
        elif ch == "[":
            thick = thick*0.75
            turtle.pensize(thick)
            stc.append(thick)
            stc.append(turtle.xcor())
            stc.append(turtle.ycor())
            stc.append(turtle.heading())
        elif ch == "]":
            turtle.penup()
            turtle.setheading(stc.pop())
            turtle.sety(stc.pop())
            turtle.setx(stc.pop())
            thick = stc.pop()
            turtle.pensize(thick)
            turtle.pendown()
        if show and time % timer == 0:
            turtle.update()
    turtle.update()
    #turtle.mainloop()

timer = 120
show = True
leafs = True   
col1 = '#351000'
col2 = '#009900'
col3 = '#667900'
col4 = '#20BB00'
print("Данную программу подготовил ученик 11А класса \nМАОУ СОШ№41 г.Челябинска - Бекасов Михаил Юрьевич")
print("help - список команд")
while True:
    act = input("Введите команду: ")
    if act == "help":
        print("help:  список команд\nexit:  завершить работу\ndraw:  нарисовать дерево\nshow:  показывать рисование да/нет (True/False)\nshowtimer: задержка обновления экрана\nclear: стереть дерево\ncol1:  цвет ствола\ncol2:  цвет тёмных листьев\ncol3:  цвет листьев\ncol4:  цвет светлых листьев\nleafs: листья есть/нет (True/False)\nreset: сбросить настройки")
    elif act == "exit":
        turtle.bye()
        raise SystemExit
    elif act == "draw":
        turtle.clear()
        drawTree()
    elif act == "clear":
        turtle.clear()
        turtle.update()
    elif act == "col1":
        col = "#" + input("Введите цвет в HEX (6 символов): ")
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', col)
        if match:
            col1 = col
        else:
            print("Введён неправильный цвет в " + act)
    elif act == "col2":
        col = "#" + input("Введите цвет в HEX (6 символов): ")
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', col)
        if match:
            col2 = col
        else:
            print("Введён неправильный цвет в " + act)
    elif act == "col3":
        col = "#" + input("Введите цвет в HEX (6 символов): ")
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', col)
        if match:
            col3 = col
        else:
            print("Введён неправильный цвет в " + act)
    elif act == "col4":
        col = "#" + input("Введите цвет в HEX (6 символов): ")
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', col)
        if match:
            col4 = col
        else:
            print("Введён неправильный цвет в " + act)
    elif act == "leafs":
        if leafs == True:
            leafs = False
        else:
            leafs = True
        print("Cостояние листьев: " + str(leafs))
    elif act == "reset":
        turtle.clear()
        turtle.update()
        leafs = True
        col1 = '#351000'
        col2 = '#009900'
        col3 = '#667900'
        col4 = '#20BB00'
    elif act == "show":
        if show == True:
            show = False
        else:
            show = True
        print("Cостояние демонстрации рисования: " + str(show))
    elif act == "showtimer":
        timer = int(input("Введите задержку в кадрах для обновления дерева: "))
    else:
        print("Неизвестная команда")








