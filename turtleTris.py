from turtle import *

# main
def main():
    global puntiX
    global puntiO
    global turno 
    turno = 0
    coord = [-100, 100]
    t.penup()
    t.goto(0,300)
    t.write("X"+" "*22+"O",align="center" ,font=("Courier New",45, "bold"))
    t.goto(0,230)
    spazio = 22-len(str(puntiX))-len(str(puntiO))
    t.write(str(puntiX)+" "*spazio+str(puntiO),align="center" , font=("Courier New",50, "normal"))
    t.pencolor("black")
    t.goto(400,300)
    t.home()

    t.goto(-307, 307)
    t.pensize(7)
    t.setheading(0)
    t.pendown()
    t.forward(614)
    t.right(90)
    t.forward(614)
    t.right(90)
    t.forward(614)
    t.right(90)
    t.forward(614)
    t.right(90)
    t.pensize(5)

    # disegna tabella
    t.right(90)
    for i in range(2):
        t.penup()
        t.goto(coord[i], 300)
        t.pendown()
        t.forward(600)

    t.right(90)
    for i in range(2):
        t.penup()
        t.goto(300, coord[i])
        t.pendown()
        t.forward(600)

    t.penup()


    print("TRIS".center(20, "-"))
    screen.onclick(on_click)
# disegna riquadro
def riquadro(frase, coordY_riq, coordY_testo):
    t.penup()
    t,speed(3)
    t.goto(-250,coordY_riq)
    t.fillcolor("black")
    t.begin_fill()
    t.setheading(0)
    t.forward(500)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.goto(0,coordY_testo)
    t.pencolor("white")
    t.write(frase,align="center", font=("Courier New",50, "bold"))
    t.pendown()        
    t.penup()
# cosa succede on click
def on_click(x, y):
    screen.onclick(None)  # disable handler inside handle
    global messaggioVittoria
    global XO
    if -300 <= x < 300 and -300 <= y < 300:
        if turno % 2 == XO:
            lett = "X"
            drawCross(x, y)

        else:
            lett = "O"
            drawCircle(x, y)

        w = checkWin(quadrante, lett)
    

        if not w[1] and turno < 9:
            screen.onclick(on_click)  # reenable handler
        else:
            
            for a in range(0, 7, 3):
                print("|", end="")
                for b in range(3):
                    
                    if quadrante[a+b] in ("X", "O"):
                        print(quadrante[a+b], end="|")
                    else:
                        print("-", end="|")
                print()
            print(w[0])
            print(f"Score X: {puntiX}")
            print(f"Score O: {puntiO}")
            riquadro(w[0].strip("-").upper().center(20), 150, 35)
            riquadro("CLICK TO".center(20)+"\n"+"RESET".center(20), -5, -155)
            screen.onclick(reset_click)
    else:
        screen.onclick(on_click)
# click per resettare
def reset_click(x, y):
    screen.onclick(None)  # disable handler inside handle
    reset()
# disegna cerchio
def drawCircle(v1, v2):
    global turno
    mossaCorretta = False
    for q in quadrante:
        if type(q) == type([]):
            if q[0][0] <= v1 < q[0][1]:
                X = int((q[0][0]+q[0][1])/2)
                if q[1][0] <= v2 < q[1][1]:
                    Y = q[1][1]
                    quadrante[quadrante.index(q)] = "O"
                    mossaCorretta = True
    
    if mossaCorretta:
        t.goto(X, Y-7)
        t.pencolor("blue")
        t.pendown()
        t.circle(91)
        t.penup()
        turno += 1
# disegna croce
def drawCross(v1, v2):
    global turno
    mossaCorretta = False
    for q in quadrante:
        if type(q) == type([]):
            if q[0][0] <= v1 < q[0][1]:
                X = q[0][0]
                if q[1][0] <= v2 < q[1][1]:
                    Y = q[1][1]
                    quadrante[quadrante.index(q)] = "X"
                    mossaCorretta = True
    
    if mossaCorretta:
        t.goto(X+7, Y-7)
        t.pencolor("red")
        t.right(225)
        t.pendown()
        t.forward(186*(2**0.5))
        t.right(225)
        t.penup()
        t.forward(186)
        t.pendown()
        t.right(225)
        t.forward(186*(2**0.5))
        t.right(45)
        t.penup()
        turno += 1
# disegna riga vittoria
def drawRiga(riga):
    t.penup()
    t.pensize(9)
    t.pencolor("green")
    t.goto(300,winY[riga])
    t.setheading(180)
    t.pendown()
    t.forward(600)
# disegna colonna vittoria
def drawColonna(col):
    t.penup()
    t.pensize(9)
    t.pencolor("green")
    t.goto(winX[col], 300)
    t.setheading(270)
    t.pendown()
    t.forward(600)
# disegna diagonale positiva vittoria
def drawDiag(d, n):
    t.penup()
    t.pensize(9)
    t.pencolor("green")
    t.goto(winD[n])
    t.setheading(90)
    if not n:
        t.right(135)
    else:
        t.right(225)
    t.pendown()
    t.forward(600*(2**0.5))
# disegna diagonale negativa vittoria
def checkWin(tab, l):
    global puntiX
    global puntiO
    global turno
    global XO
    messaggioVittoria = "Draw!".center(20, "-")
    win = False
    for x in range(3):
        col = (tab[x], tab[x+3], tab[x+6])
        if col == (l , l , l):
            drawColonna(x)
            win = True
        row = (tab[x*3], tab[x*3+1], tab[x*3+2])
        if row == (l , l , l):
            drawRiga(x)
            win = True
    d1 = (tab[0], tab[4], tab[8])
    d2 = (tab[2], tab[4], tab[6])
    if d1 == (l , l , l):
            drawDiag(x, 0)
            win = True
    if d2 == (l , l , l):
            drawDiag(x, 1)
            win = True

    if win:
        if (XO == 0 and turno % 2 == 1) or (XO == 1 and turno % 2 == 0):
            messaggioVittoria = "X WINS!".center(20, "-")
            XO = 1
            puntiX += 1
        else:
            messaggioVittoria = "O WINS!".center(20, "-")
            puntiO += 1
            XO = 0
    return (messaggioVittoria, win)
# reset
def reset():
    global turno
    global quadrante
    t.penup()
    screen.clear()
    t.home()
    t.pencolor("black")
    t.pendown()
    
    quadrante = [[(-300,-100),  (100,300)],[(-100,100),  (100,300)],[(100,300),  (100,300)],
                [(-300,-100), (-100,100)],[(-100,100), (-100,100)],[(100,300), (-100,100)],
                [(-300,-100),(-300,-100)],[(-100,100),(-300,-100)],[(100,300),(-300,-100)],]
    t.penup()
    t.goto(-307, 307)
    t.pensize(7)
    t.setheading(0)
    t.pendown()
    t.forward(614)
    t.right(90)
    t.forward(614)
    t.right(90)
    t.forward(614)
    t.right(90)
    t.forward(614)
    t.right(90)
    t.pensize(5)

    main()

winX = [-200,0,200]
winY = [200,0,-200]
winD = [(-300, 300), (300, 300)]
turno = 0
quadrante = [[(-300,-100),  (100,300)],[(-100,100),  (100,300)],[(100,300),  (100,300)],
             [(-300,-100), (-100,100)],[(-100,100), (-100,100)],[(100,300), (-100,100)],
             [(-300,-100),(-300,-100)],[(-100,100),(-300,-100)],[(100,300),(-300,-100)],]
puntiX = 0
puntiO = 0
XO = 0
screen = Screen()
screen.title("PYTHON TRIS")
screen.setup(1000,800)
t = Turtle()
t.hideturtle()
t.pensize(3)
t.speed(0)
colormode()
main()
screen.mainloop()

