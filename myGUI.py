from tkinter import *
import math
import random
import classes
import copy

#basic functions
def reset():
    global startingcolors
    global currentcolors
    startingcolors = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    currentcolors = copy.deepcopy(startingcolors)

    clock_list = [
        {"button": Button(root, text="top clock", bg = colors[0]), "function": makemove, "arg1": 0},
        {"button": Button(root, text="top counter clock", bg = colors[0]), "function": makemove, "arg1": 1},
        {"button": Button(root, text="second clock", bg = colors[0]), "function": makemove, "arg1": 2},
        {"button": Button(root, text="second counter clock", bg = colors[0]), "function": makemove, "arg1": 3},
        {"button": Button(root, text="bottom clock", bg = colors[0]), "function": makemove, "arg1": 4},
        {"button": Button(root, text="bottom counter clock", bg = colors[0]), "function": makemove, "arg1": 5},
        {"button": Button(root, text="top clock", bg = colors[1]), "function": makemove, "arg1": 6},
        {"button": Button(root, text="top counterclock", bg = colors[1]), "function": makemove, "arg1": 7},
        {"button": Button(root, text="second clock", bg = colors[1]), "function": makemove, "arg1": 8},
        {"button": Button(root, text="second counter clock", bg = colors[1]), "function": makemove, "arg1": 9},
        {"button": Button(root, text="bottom clock", bg = colors[1]), "function": makemove, "arg1": 10},
        {"button": Button(root, text="bottom counter clock", bg = colors[1]), "function": makemove, "arg1": 11},
        {"button": Button(root, text="top clock", bg = colors[2]), "function": makemove, "arg1": 12},
        {"button": Button(root, text="top counter clock", bg = colors[2]), "function": makemove, "arg1": 13},
        {"button": Button(root, text="second clock", bg = colors[2]), "function": makemove, "arg1": 14},
        {"button": Button(root, text="second counter clock", bg = colors[2]), "function": makemove, "arg1": 15},
        {"button": Button(root, text="bottom clock", bg = colors[2]), "function": makemove, "arg1": 16},
        {"button": Button(root, text="bottom counter clock", bg = colors[2]), "function": makemove, "arg1": 17},
        {"button": Button(root, text="top clock", bg = colors[3]), "function": makemove, "arg1": 18},
        {"button": Button(root, text="top counter clock", bg = colors[3]), "function": makemove, "arg1": 19},
        {"button": Button(root, text="second clock", bg = colors[3]), "function": makemove, "arg1": 20},
        {"button": Button(root, text="second counter clock", bg = colors[3]), "function": makemove, "arg1": 21},
        {"button": Button(root, text="bottom clock", bg = colors[3]), "function": makemove, "arg1": 22},
        {"button": Button(root, text="bottom counter clock", bg = colors[3]), "function": makemove, "arg1": 23},
        #{"button": Button(root, text="Randomize!!", bg = "grey"), "function": entry_func, "arg1": 0},
    ]

    yval = 50
    for button_info in clock_list:
        button_info["button"].place(x=1100, y=yval)
        button_info["button"].config(command=lambda b=button_info: (
        update_current_button(b),
        b["function"](b["arg1"],)
        ))
        yval = yval + 30

    updateGui()

def makemove(move):
    match move:
        case 0:
            r1(currentcolors)
        case 1:
            r1p(currentcolors)
        case 2:
            r2(currentcolors)
        case 3:
            r2p(currentcolors)
        case 4:
            r3(currentcolors)
        case 5:
            r3p(currentcolors)
        case 6:
            b1(currentcolors)
        case 7:
            b1p(currentcolors)
        case 8:
            b2(currentcolors)
        case 9:
            b2p(currentcolors)
        case 10:
            b3(currentcolors)
        case 11:
            b3p(currentcolors)
        case 12:
            g1(currentcolors)
        case 13:
            g1p(currentcolors)
        case 14:
            g2(currentcolors)
        case 15:
            g2p(currentcolors)
        case 16:
            g3(currentcolors)
        case 17:
            g3p(currentcolors)
        case 18:
            y1(currentcolors)
        case 19:
            y1p(currentcolors)
        case 20:
            y2(currentcolors)
        case 21:
            y2p(currentcolors)
        case 22:
            y3(currentcolors)
        case 23:
            y3p(currentcolors)
        case _:
            print("ERROR")
    updateGui()

def randompyraminx(moves):
    reset()
    print('Moves')
    for i in range(moves):
        move = random.randint(0,23)
        print(move)
        makemove(move)

def clockwise_randompyraminx(moves):
    reset()
    for i in range(moves):
        move = random.randint(0,11)
        match move:
            case 0:
                r1(currentcolors)
            case 1:
                r2(currentcolors)
            case 2:
                r3(currentcolors)
            case 3:
                b1(currentcolors)
            case 4:
                b2(currentcolors)
            case 5:
                b3(currentcolors)
            case 6:
                g1(currentcolors)
            case 7:
                g2(currentcolors)
            case 8:
                g3(currentcolors)
            case 9:
                y1(currentcolors)
            case 10:
                y2(currentcolors)
            case 11:
                y3(currentcolors)
            case _:
                print("ERROR")
    updateGui()

def triangle(x,y):
    x1 = x
    x2 = x - 30
    x3 = x + 30
    y1 =  y - 50
    y2 =  y
    y3 = y2
    return [x1,y1, x2,y2, x3,y3]

def triangle_upsidedown(x,y):
    x1 = x
    x2 = x - 30
    x3 = x + 30
    y1 =  y 
    y2 =  y - 50
    y3 = y2
    return [x1,y1, x2,y2, x3,y3]

    startingcolors = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    currentcolors = startingcolors

def update_current_button(button_info):
    global current_button_info
    current_button_info = button_info

def solved(a, b):
    heuristic = 0.0
    for i in range(63):
        if a[i] != b[i]:
            heuristic = heuristic + 1

    heuristic = heuristic / 21
    heuristic = math.ceil(heuristic)

    return heuristic

def updateGui():
    canvas.delete("all")
    if solved(startingcolors, currentcolors) == 0:
        canvas.create_text(300, 50, text="SOLVED!!!", fill="black", font=('Helvetica 15 bold'))
    else:
        canvas.create_text(220, 50, text="Heuristic:", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(300, 50, text= solved(startingcolors, 
        currentcolors), fill="black", font=('Helvetica 15 bold'))

    #1 Red
    canvas.create_polygon(triangle(500, 150), fill=colors[currentcolors[0]], outline = "black")
    #2
    canvas.create_polygon(triangle(460, 210), fill=colors[currentcolors[1]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(500, 210), fill=colors[currentcolors[2]], outline = "black")
    canvas.create_polygon(triangle(540, 210), fill=colors[currentcolors[3]], outline = "black")
    #3
    canvas.create_polygon(triangle(420, 270), fill=colors[currentcolors[4]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(460, 270), fill=colors[currentcolors[5]], outline = "black")
    canvas.create_polygon(triangle(500, 270), fill=colors[currentcolors[6]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540, 270), fill=colors[currentcolors[7]], outline = "black")
    canvas.create_polygon(triangle(580, 270), fill=colors[currentcolors[8]], outline = "black")
    #4
    canvas.create_polygon(triangle(380, 330), fill=colors[currentcolors[9]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(420, 330), fill=colors[currentcolors[10]], outline = "black")
    canvas.create_polygon(triangle(460, 330), fill=colors[currentcolors[11]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(500, 330), fill=colors[currentcolors[12]], outline = "black")
    canvas.create_polygon(triangle(540, 330), fill=colors[currentcolors[13]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(580, 330), fill=colors[currentcolors[14]], outline = "black")
    canvas.create_polygon(triangle(620, 330), fill=colors[currentcolors[15]], outline = "black")

    #1 Blue
    canvas.create_polygon(triangle_upsidedown(500, 610), fill=colors[currentcolors[16]], outline = "black")
    #2
    canvas.create_polygon(triangle_upsidedown(460, 550), fill=colors[currentcolors[17]], outline = "black")
    canvas.create_polygon(triangle(500, 550), fill=colors[currentcolors[18]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540, 550), fill=colors[currentcolors[19]], outline = "black")
    #3
    canvas.create_polygon(triangle_upsidedown(420, 490), fill=colors[currentcolors[20]], outline = "black")
    canvas.create_polygon(triangle(460, 490), fill=colors[currentcolors[21]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(500, 490), fill=colors[currentcolors[22]], outline = "black")
    canvas.create_polygon(triangle(540, 490), fill=colors[currentcolors[23]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(580, 490), fill=colors[currentcolors[24]], outline = "black")
    #4
    canvas.create_polygon(triangle_upsidedown(380, 430), fill=colors[currentcolors[25]], outline = "black")
    canvas.create_polygon(triangle(420, 430), fill=colors[currentcolors[26]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(460, 430), fill=colors[currentcolors[27]], outline = "black")
    canvas.create_polygon(triangle(500, 430), fill=colors[currentcolors[28]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540, 430), fill=colors[currentcolors[29]], outline = "black")
    canvas.create_polygon(triangle(580, 430), fill=colors[currentcolors[30]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(620, 430), fill=colors[currentcolors[31]], outline = "black")


    #1 Green
    canvas.create_polygon(triangle_upsidedown(500-200, 330), fill=colors[currentcolors[32]], outline = "black")
    #2
    canvas.create_polygon(triangle_upsidedown(460-200, 270), fill=colors[currentcolors[33]], outline = "black")
    canvas.create_polygon(triangle(500-200, 270), fill=colors[currentcolors[34]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540-200, 270), fill=colors[currentcolors[35]], outline = "black")
    #3
    canvas.create_polygon(triangle_upsidedown(420-200, 210), fill=colors[currentcolors[36]], outline = "black")
    canvas.create_polygon(triangle(460-200, 210), fill=colors[currentcolors[37]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(500-200, 210), fill=colors[currentcolors[38]], outline = "black")
    canvas.create_polygon(triangle(540-200, 210), fill=colors[currentcolors[39]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(580-200, 210), fill=colors[currentcolors[40]], outline = "black")
    #4
    canvas.create_polygon(triangle_upsidedown(380-200, 150), fill=colors[currentcolors[41]], outline = "black")
    canvas.create_polygon(triangle(420-200, 150), fill=colors[currentcolors[42]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(460-200, 150), fill=colors[currentcolors[43]], outline = "black")
    canvas.create_polygon(triangle(500-200, 150), fill=colors[currentcolors[44]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540-200, 150), fill=colors[currentcolors[45]], outline = "black")
    canvas.create_polygon(triangle(580-200, 150), fill=colors[currentcolors[46]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(620-200, 150), fill=colors[currentcolors[47]], outline = "black")


    #1 Yellow
    canvas.create_polygon(triangle_upsidedown(500+200, 330), fill=colors[currentcolors[48]], outline = "black")
    #2
    canvas.create_polygon(triangle_upsidedown(460+200, 270), fill=colors[currentcolors[49]], outline = "black")
    canvas.create_polygon(triangle(500+200, 270), fill=colors[currentcolors[50]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540+200, 270), fill=colors[currentcolors[51]], outline = "black")
    #3
    canvas.create_polygon(triangle_upsidedown(420+200, 210), fill=colors[currentcolors[52]], outline = "black")
    canvas.create_polygon(triangle(460+200, 210), fill=colors[currentcolors[53]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(500+200, 210), fill=colors[currentcolors[54]], outline = "black")
    canvas.create_polygon(triangle(540+200, 210), fill=colors[currentcolors[55]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(580+200, 210), fill=colors[currentcolors[56]], outline = "black")
    #4
    canvas.create_polygon(triangle_upsidedown(380+200, 150), fill=colors[currentcolors[57]], outline = "black")
    canvas.create_polygon(triangle(420+200, 150), fill=colors[currentcolors[58]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(460+200, 150), fill=colors[currentcolors[59]], outline = "black")
    canvas.create_polygon(triangle(500+200, 150), fill=colors[currentcolors[60]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540+200, 150), fill=colors[currentcolors[61]], outline = "black")
    canvas.create_polygon(triangle(580+200, 150), fill=colors[currentcolors[62]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(620+200, 150), fill=colors[currentcolors[63]], outline = "black")

def entry_func():
    entry_text = entry.get()
    randompyraminx(int(entry_text))

def addchildren(queue,current):
    tempc = copy.copy(current.arrangement)
    r1p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    r2p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    r3p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    b1p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    b2p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    b3p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    y1p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    y2p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    y3p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    g1p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    g2p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

    tempc = copy.copy(current.arrangement)
    g3p(tempc)
    tempnode = classes.asnode(current, tempc, current.d + 1, solved(startingcolors, tempc))
    queue.addn(tempnode)

def clockwise_entry_func():
    entry_text = entry.get()
    clockwise_randompyraminx(int(entry_text))

def clockwise_solve():
    global currentcolors
    rootnode = classes.asnode(0, copy.deepcopy(currentcolors), 0, solved(startingcolors, currentcolors))

    pqueue = classes.minheap()
    pqueue.addn(rootnode)

    if(len(pqueue.queue) == 0):
        print("ERROR")

    current = pqueue.queue.pop(0)
    while(current.h > 0):
        addchildren(pqueue,current)
        current = pqueue.queue.pop(0)


    currentcolors = current.arrangement
    print("Arrangement Path:")
    while(current.parent != 0):
        print(current.arrangement)
        current = current.parent
    updateGui()


#red base moves
def r1(pcolors):
    temp = pcolors[16]
    pcolors[16] = pcolors[63]
    pcolors[63] = pcolors[41]
    pcolors[41] = temp

def r1p(pcolors):
    temp = pcolors[41]
    pcolors[41] = pcolors[63]
    pcolors[63] = pcolors[16]
    pcolors[16] = temp

def r2(pcolors):
    temp = pcolors[36]
    pcolors[36] = pcolors[19]
    pcolors[19] = pcolors[61]
    pcolors[61] = temp

    temp = pcolors[42]
    pcolors[42] = pcolors[18]
    pcolors[18] = pcolors[62]
    pcolors[62] = temp

    temp = pcolors[43]
    pcolors[43] = pcolors[17]
    pcolors[17] = pcolors[56]
    pcolors[56] = temp

def r2p(pcolors):
    temp = pcolors[61]
    pcolors[61] = pcolors[19]
    pcolors[19] = pcolors[36]
    pcolors[36] = temp

    temp = pcolors[62]
    pcolors[62] = pcolors[18]
    pcolors[18] = pcolors[42]
    pcolors[42] = temp

    temp = pcolors[56]
    pcolors[56] = pcolors[17]
    pcolors[17] = pcolors[43]
    pcolors[43] = temp

def r3(pcolors):
    temp = pcolors[32]
    pcolors[32] = pcolors[31]
    pcolors[31] = pcolors[57]
    pcolors[57] = temp

    temp = pcolors[34]
    pcolors[34] = pcolors[30]
    pcolors[30] = pcolors[58]
    pcolors[58] = temp

    temp = pcolors[35]
    pcolors[35] = pcolors[29]
    pcolors[29] = pcolors[52]
    pcolors[52] = temp

    temp = pcolors[39]
    pcolors[39] = pcolors[28]
    pcolors[28] = pcolors[53]
    pcolors[53] = temp

    temp = pcolors[40]
    pcolors[40] = pcolors[27]
    pcolors[27] = pcolors[49]
    pcolors[49] = temp

    temp = pcolors[46]
    pcolors[46] = pcolors[26]
    pcolors[26] = pcolors[50]
    pcolors[50] = temp

    temp = pcolors[47]
    pcolors[47] = pcolors[25]
    pcolors[25] = pcolors[48]
    pcolors[48] = temp

    temp = pcolors[0]
    pcolors[0] = pcolors[9]
    pcolors[9] = pcolors[15]
    pcolors[15] = temp

    temp = pcolors[1]
    pcolors[1] = pcolors[11]
    pcolors[11] = pcolors[8]
    pcolors[8] = temp

    temp = pcolors[4]
    pcolors[4] = pcolors[13]
    pcolors[13] = pcolors[3]
    pcolors[3] = temp

    temp = pcolors[2]
    pcolors[2] = pcolors[10]
    pcolors[10] = pcolors[14]
    pcolors[14] = temp

    temp = pcolors[5]
    pcolors[5] = pcolors[12]
    pcolors[12] = pcolors[7]
    pcolors[7] = temp

def r3p(pcolors):
    temp = pcolors[57]
    pcolors[57] = pcolors[31]
    pcolors[31] = pcolors[32]
    pcolors[32] = temp

    temp = pcolors[58]
    pcolors[58] = pcolors[30]
    pcolors[30] = pcolors[34]
    pcolors[34] = temp

    temp = pcolors[52]
    pcolors[52] = pcolors[29]
    pcolors[29] = pcolors[35]
    pcolors[35] = temp

    temp = pcolors[53]
    pcolors[53] = pcolors[28]
    pcolors[28] = pcolors[39]
    pcolors[39] = temp

    temp = pcolors[49]
    pcolors[49] = pcolors[27]
    pcolors[27] = pcolors[40]
    pcolors[40] = temp

    temp = pcolors[50]
    pcolors[50] = pcolors[26]
    pcolors[26] = pcolors[46]
    pcolors[46] = temp

    temp = pcolors[48]
    pcolors[48] = pcolors[25]
    pcolors[25] = pcolors[47]
    pcolors[47] = temp

    temp = pcolors[15]
    pcolors[15] = pcolors[9]
    pcolors[9] = pcolors[0]
    pcolors[0] = temp

    temp = pcolors[8]
    pcolors[8] = pcolors[11]
    pcolors[11] = pcolors[1]
    pcolors[1] = temp

    temp = pcolors[3]
    pcolors[3] = pcolors[13]
    pcolors[13] = pcolors[4]
    pcolors[4] = temp

    temp = pcolors[14]
    pcolors[14] = pcolors[10]
    pcolors[10] = pcolors[2]
    pcolors[2] = temp

    temp = pcolors[7]
    pcolors[7] = pcolors[12]
    pcolors[12] = pcolors[5]
    pcolors[5] = temp

#blue base moves
def b1(pcolors):
    temp = pcolors[47]
    pcolors[47] = pcolors[0]
    pcolors[0] = pcolors[57]
    pcolors[57] = temp

def b1p(pcolors):
    temp = pcolors[57]
    pcolors[57] = pcolors[0]
    pcolors[0] = pcolors[47]
    pcolors[47] = temp

def b2(pcolors):
    temp = pcolors[45]
    pcolors[45] = pcolors[1]
    pcolors[1] = pcolors[52]
    pcolors[52] = temp

    temp = pcolors[46]
    pcolors[46] = pcolors[2]
    pcolors[2] = pcolors[58]
    pcolors[58] = temp

    temp = pcolors[40]
    pcolors[40] = pcolors[3]
    pcolors[3] = pcolors[59]
    pcolors[59] = temp

def b2p(pcolors):
    temp = pcolors[52]
    pcolors[52] = pcolors[1]
    pcolors[1] = pcolors[45]
    pcolors[45] = temp

    temp = pcolors[58]
    pcolors[58] = pcolors[2]
    pcolors[2] = pcolors[46]
    pcolors[46] = temp

    temp = pcolors[59]
    pcolors[59] = pcolors[3]
    pcolors[3] = pcolors[40]
    pcolors[40] = temp

def b3(pcolors):
    temp = pcolors[41]
    pcolors[41] = pcolors[9]
    pcolors[9] = pcolors[48]
    pcolors[48] = temp

    temp = pcolors[42]
    pcolors[42] = pcolors[10]
    pcolors[10] = pcolors[50]
    pcolors[50] = temp

    temp = pcolors[36]
    pcolors[36] = pcolors[11]
    pcolors[11] = pcolors[51]
    pcolors[51] = temp

    temp = pcolors[37]
    pcolors[37] = pcolors[12]
    pcolors[12] = pcolors[55]
    pcolors[55] = temp

    temp = pcolors[33]
    pcolors[33] = pcolors[13]
    pcolors[13] = pcolors[56]
    pcolors[56] = temp

    temp = pcolors[34]
    pcolors[34] = pcolors[14]
    pcolors[14] = pcolors[62]
    pcolors[62] = temp

    temp = pcolors[32]
    pcolors[32] = pcolors[15]
    pcolors[15] = pcolors[63]
    pcolors[63] = temp

    temp = pcolors[31]
    pcolors[31] = pcolors[25]
    pcolors[25] = pcolors[16]
    pcolors[16] = temp

    temp = pcolors[24]
    pcolors[24] = pcolors[27]
    pcolors[27] = pcolors[17]
    pcolors[17] = temp

    temp = pcolors[19]
    pcolors[19] = pcolors[29]
    pcolors[29] = pcolors[20]
    pcolors[20] = temp

    temp = pcolors[30]
    pcolors[30] = pcolors[26]
    pcolors[26] = pcolors[18]
    pcolors[18] = temp

    temp = pcolors[23]
    pcolors[23] = pcolors[28]
    pcolors[28] = pcolors[21]
    pcolors[21] = temp

def b3p(pcolors):
    temp = pcolors[48]
    pcolors[48] = pcolors[9]
    pcolors[9] = pcolors[41]
    pcolors[41] = temp

    temp = pcolors[50]
    pcolors[50] = pcolors[10]
    pcolors[10] = pcolors[42]
    pcolors[42] = temp

    temp = pcolors[51]
    pcolors[51] = pcolors[11]
    pcolors[11] = pcolors[36]
    pcolors[36] = temp

    temp = pcolors[55]
    pcolors[55] = pcolors[12]
    pcolors[12] = pcolors[37]
    pcolors[37] = temp

    temp = pcolors[56]
    pcolors[56] = pcolors[13]
    pcolors[13] = pcolors[33]
    pcolors[33] = temp

    temp = pcolors[62]
    pcolors[62] = pcolors[14]
    pcolors[14] = pcolors[34]
    pcolors[34] = temp

    temp = pcolors[63]
    pcolors[63] = pcolors[15]
    pcolors[15] = pcolors[32]
    pcolors[32] = temp

    temp = pcolors[16]
    pcolors[16] = pcolors[25]
    pcolors[25] = pcolors[31]
    pcolors[31] = temp

    temp = pcolors[17]
    pcolors[17] = pcolors[27]
    pcolors[27] = pcolors[24]
    pcolors[24] = temp

    temp = pcolors[20]
    pcolors[20] = pcolors[29]
    pcolors[29] = pcolors[19]
    pcolors[19] = temp

    temp = pcolors[18]
    pcolors[18] = pcolors[26]
    pcolors[26] = pcolors[30]
    pcolors[30] = temp

    temp = pcolors[21]
    pcolors[21] = pcolors[28]
    pcolors[28] = pcolors[23]
    pcolors[23] = temp

#green base moves
def g1(pcolors):
    temp = pcolors[48]
    pcolors[48] = pcolors[15]
    pcolors[15] = pcolors[31]
    pcolors[31] = temp

def g1p(pcolors):
    temp = pcolors[31]
    pcolors[31] = pcolors[15]
    pcolors[15] = pcolors[48]
    pcolors[48] = temp

def g2(pcolors):
    temp = pcolors[49]
    pcolors[49] = pcolors[13]
    pcolors[13] = pcolors[24]
    pcolors[24] = temp

    temp = pcolors[50]
    pcolors[50] = pcolors[14]
    pcolors[14] = pcolors[30]
    pcolors[30] = temp

    temp = pcolors[51]
    pcolors[51] = pcolors[8]
    pcolors[8] = pcolors[29]
    pcolors[29] = temp

def g2p(pcolors):
    temp = pcolors[24]
    pcolors[24] = pcolors[13]
    pcolors[13] = pcolors[49]
    pcolors[49] = temp

    temp = pcolors[30]
    pcolors[30] = pcolors[14]
    pcolors[14] = pcolors[50]
    pcolors[50] = temp

    temp = pcolors[29]
    pcolors[29] = pcolors[8]
    pcolors[8] = pcolors[51]
    pcolors[51] = temp

def g3(pcolors):
    temp = pcolors[63]
    pcolors[63] = pcolors[0]
    pcolors[0] = pcolors[25]
    pcolors[25] = temp

    temp = pcolors[62]
    pcolors[62] = pcolors[2]
    pcolors[2] = pcolors[26]
    pcolors[26] = temp

    temp = pcolors[61]
    pcolors[61] = pcolors[1]
    pcolors[1] = pcolors[20]
    pcolors[20] = temp

    temp = pcolors[60]
    pcolors[60] = pcolors[5]
    pcolors[5] = pcolors[21]
    pcolors[21] = temp

    temp = pcolors[59]
    pcolors[59] = pcolors[4]
    pcolors[4] = pcolors[17]
    pcolors[17] = temp

    temp = pcolors[58]
    pcolors[58] = pcolors[10]
    pcolors[10] = pcolors[18]
    pcolors[18] = temp

    temp = pcolors[57]
    pcolors[57] = pcolors[9]
    pcolors[9] = pcolors[16]
    pcolors[16] = temp

    temp = pcolors[47]
    pcolors[47] = pcolors[41]
    pcolors[41] = pcolors[32]
    pcolors[32] = temp

    temp = pcolors[40]
    pcolors[40] = pcolors[43]
    pcolors[43] = pcolors[33]
    pcolors[33] = temp

    temp = pcolors[35]
    pcolors[35] = pcolors[45]
    pcolors[45] = pcolors[36]
    pcolors[36] = temp

    temp = pcolors[46]
    pcolors[46] = pcolors[42]
    pcolors[42] = pcolors[34]
    pcolors[34] = temp

    temp = pcolors[39]
    pcolors[39] = pcolors[44]
    pcolors[44] = pcolors[37]
    pcolors[37] = temp

def g3p(pcolors):
    temp = pcolors[25]
    pcolors[25] = pcolors[0]
    pcolors[0] = pcolors[63]
    pcolors[63] = temp

    temp = pcolors[26]
    pcolors[26] = pcolors[2]
    pcolors[2] = pcolors[62]
    pcolors[62] = temp

    temp = pcolors[20]
    pcolors[20] = pcolors[1]
    pcolors[1] = pcolors[61]
    pcolors[61] = temp

    temp = pcolors[21]
    pcolors[21] = pcolors[5]
    pcolors[5] = pcolors[60]
    pcolors[60] = temp

    temp = pcolors[17]
    pcolors[17] = pcolors[4]
    pcolors[4] = pcolors[59]
    pcolors[59] = temp

    temp = pcolors[18]
    pcolors[18] = pcolors[10]
    pcolors[10] = pcolors[58]
    pcolors[58] = temp

    temp = pcolors[16]
    pcolors[16] = pcolors[9]
    pcolors[9] = pcolors[57]
    pcolors[57] = temp

    temp = pcolors[32]
    pcolors[32] = pcolors[41]
    pcolors[41] = pcolors[47]
    pcolors[47] = temp

    temp = pcolors[33]
    pcolors[33] = pcolors[43]
    pcolors[43] = pcolors[40]
    pcolors[40] = temp

    temp = pcolors[36]
    pcolors[36] = pcolors[45]
    pcolors[45] = pcolors[35]
    pcolors[35] = temp

    temp = pcolors[34]
    pcolors[34] = pcolors[42]
    pcolors[42] = pcolors[46]
    pcolors[46] = temp

    temp = pcolors[37]
    pcolors[37] = pcolors[44]
    pcolors[44] = pcolors[39]
    pcolors[39] = temp

#yellow base moves
def y1(pcolors):
    temp = pcolors[32]
    pcolors[32] = pcolors[25]
    pcolors[25] = pcolors[9]
    pcolors[9] = temp

def y1p(pcolors):
    temp = pcolors[9]
    pcolors[9] = pcolors[25]
    pcolors[25] = pcolors[32]
    pcolors[32] = temp

def y2(pcolors):
    temp = pcolors[27]
    pcolors[27] = pcolors[4]
    pcolors[4] = pcolors[33]
    pcolors[33] = temp

    temp = pcolors[26]
    pcolors[26] = pcolors[10]
    pcolors[10] = pcolors[34]
    pcolors[34] = temp

    temp = pcolors[20]
    pcolors[20] = pcolors[11]
    pcolors[11] = pcolors[35]
    pcolors[35] = temp

def y2p(pcolors):
    temp = pcolors[33]
    pcolors[33] = pcolors[4]
    pcolors[4] = pcolors[27]
    pcolors[27] = temp

    temp = pcolors[34]
    pcolors[34] = pcolors[10]
    pcolors[10] = pcolors[26]
    pcolors[26] = temp

    temp = pcolors[35]
    pcolors[35] = pcolors[11]
    pcolors[11] = pcolors[20]
    pcolors[20] = temp

def y3(pcolors):
    temp = pcolors[41]
    pcolors[41] = pcolors[31]
    pcolors[31] = pcolors[0]
    pcolors[0] = temp

    temp = pcolors[42]
    pcolors[42] = pcolors[30]
    pcolors[30] = pcolors[2]
    pcolors[2] = temp

    temp = pcolors[43]
    pcolors[43] = pcolors[24]
    pcolors[24] = pcolors[3]
    pcolors[3] = temp

    temp = pcolors[44]
    pcolors[44] = pcolors[23]
    pcolors[23] = pcolors[7]
    pcolors[7] = temp

    temp = pcolors[45]
    pcolors[45] = pcolors[19]
    pcolors[19] = pcolors[8]
    pcolors[8] = temp

    temp = pcolors[46]
    pcolors[46] = pcolors[18]
    pcolors[18] = pcolors[14]
    pcolors[14] = temp

    temp = pcolors[47]
    pcolors[47] = pcolors[16]
    pcolors[16] = pcolors[15]
    pcolors[15] = temp

    temp = pcolors[63]
    pcolors[63] = pcolors[57]
    pcolors[57] = pcolors[48]
    pcolors[48] = temp

    temp = pcolors[56]
    pcolors[56] = pcolors[59]
    pcolors[59] = pcolors[49]
    pcolors[49] = temp

    temp = pcolors[51]
    pcolors[51] = pcolors[61]
    pcolors[61] = pcolors[52]
    pcolors[52] = temp

    temp = pcolors[62]
    pcolors[62] = pcolors[58]
    pcolors[58] = pcolors[50]
    pcolors[50] = temp

    temp = pcolors[55]
    pcolors[55] = pcolors[60]
    pcolors[60] = pcolors[53]
    pcolors[53] = temp

def y3p(pcolors):
    temp = pcolors[0]
    pcolors[0] = pcolors[31]
    pcolors[31] = pcolors[41]
    pcolors[41] = temp

    temp = pcolors[2]
    pcolors[2] = pcolors[30]
    pcolors[30] = pcolors[42]
    pcolors[42] = temp

    temp = pcolors[3]
    pcolors[3] = pcolors[24]
    pcolors[24] = pcolors[43]
    pcolors[43] = temp

    temp = pcolors[7]
    pcolors[7] = pcolors[23]
    pcolors[23] = pcolors[44]
    pcolors[44] = temp

    temp = pcolors[8]
    pcolors[8] = pcolors[19]
    pcolors[19] = pcolors[45]
    pcolors[45] = temp

    temp = pcolors[14]
    pcolors[14] = pcolors[18]
    pcolors[18] = pcolors[46]
    pcolors[46] = temp

    temp = pcolors[15]
    pcolors[15] = pcolors[16]
    pcolors[16] = pcolors[47]
    pcolors[47] = temp

    temp = pcolors[48]
    pcolors[48] = pcolors[57]
    pcolors[57] = pcolors[63]
    pcolors[63] = temp

    temp = pcolors[49]
    pcolors[49] = pcolors[59]
    pcolors[59] = pcolors[56]
    pcolors[56] = temp

    temp = pcolors[52]
    pcolors[52] = pcolors[61]
    pcolors[61] = pcolors[51]
    pcolors[51] = temp

    temp = pcolors[50]
    pcolors[50] = pcolors[58]
    pcolors[58] = pcolors[62]
    pcolors[62] = temp

    temp = pcolors[53]
    pcolors[53] = pcolors[60]
    pcolors[60] = pcolors[55]
    pcolors[55] = temp



#MAIN
root = Tk()
root.title("4x4x4 Pyraminx")
canvas = Canvas(root, width=1500, height=1000)
colors = ["red3", "DeepSkyBlue2", "Dark Green", "goldenrod", "grey"]
canvas.pack()

reset()


Rbutton = Button(root, text="Randomize", command=entry_func, bg = colors[4])
Rbutton.place(x = 1100, y = 770)
Cbutton = Button(root, text="Clockwise Randomize", command=clockwise_entry_func, bg = colors[4])
Cbutton.place(x = 1100, y = 800)
Cbutton = Button(root, text="Counter Clockwise Solve", command=clockwise_solve, bg = colors[4])
Cbutton.place(x = 1100, y = 830)
entry = Entry(root)
entry.place(x = 950, y = 770)
root.mainloop()