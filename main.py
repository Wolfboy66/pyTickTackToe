print("Tick Tack Toe")
print("by Wolfboy66")
print("https://github.com/kquatsch/pyTickTackToe/")


while True:  # GameStart

    x = input("Start a game? (y/n):  ")  # GameStart Question

    if x.lower() in ("y", "yes"):  # Start
        print("starting game")
        break

    elif x.lower() in ("n", "no"):  # Don't start
        exit("Exiting")

    else:  # Invalid input
        print("Not a valid input")
        print("try again")
        print("")

gamedata = [0, 0, 0]  # initialise Gamedata
i = 0
player = 1
while i < 3:
    gamedata[i] = [0, 0, 0]
    i += 1


def delzero(posible):  # only pass trought full lines
    paz = []
    i1_1 = 0
    while i1_1 < 3:
        i1_2 = 0
        subst = posible[i1_1]
        if i1_1 == 2:
            while i1_2 < 2:
                subst1 = subst[i1_2]
                if (subst1[0] != 0) and (subst1[1] != 0) and (subst1[2] != 0):
                    paz += [[subst1[0], subst1[1], subst1[2]]]
                i1_2 += 1
        else:
            while i1_2 < 3:
                subst1 = subst[i1_2]
                if (subst1[0] != 0) and (subst1[1] != 0) and (subst1[2] != 0):
                    paz += [[subst1[0], subst1[1], subst1[2]]]
                i1_2 += 1
        i1_1 += 1
    return paz


def game(stand):  # posstble wins

    poswins = [[0, 0, 0], [0, 0, 0], [0, 0]]

    i2 = 0
    while i2 < 3:
        add = poswins[0]
        s1 = stand[i2]
        add[i2] = [s1[0], s1[1], s1[2]]
        i2 += 1

    i2 = 0
    while i2 < 3:
        add = poswins[1]
        add[i2] = [stand[0][i2], stand[1][i2], stand[2][i2]]
        i2 += 1

    add = poswins[2]
    add[0] = [stand[0][0], stand[1][1], stand[2][2]]
    add[1] = [stand[0][2], stand[1][1], stand[2][0]]
    ret = win(delzero(poswins))
    return ret


def win(delzeroo):
    array_len = len(delzeroo)
    i3 = 0
    while i3 < array_len:
        array = delzeroo[i3]
        if (array[0] + array[1] + array[2]) == 3:
            exit("player 1 Won")
        elif (array[0] + array[1] + array[2]) == 6:
            exit("player 2 won")
        else:
            return True
    return True


while game(gamedata):
    game(gamedata)
    curp = player
    text = "It is player " + str(curp) + " turn. select a place from 3*3:  "
    i4 = 0
    while i4 < 3:
        i4_1 = 0
        gsp = gamedata[i4]
        line = ""
        while i4_1 < 3:
            if int(gsp[i4_1]) == 0:
                line += "   "
            elif int(gsp[i4_1]) == 1:
                line += " X "
            elif int(gsp[i4_1]) == 2:
                line += " O "
            if i4_1 < 2:
                line += " | "
            i4_1 += 1
        print(line)
        if i4 < 2:
            print("---------------")
        i4 += 1
    print()
    print()
    valid = 0
    while valid == 0:
        inp = input(text)
        inp = str.split(inp)
        if len(inp) != 2:
            print("invalid input")
        else:
            if int(inp[0]) == 1 or int(inp[0]) == 2 or int(inp[0]) == 3 and \
                    int(inp[1]) == 1 or int(inp[1]) == 2 or int(inp[1]) == 3:
                print("valid input")
                valid = 1
            else:
                print("invalid input")

        if valid == 1:
            inp1 = inp[0]
            inp2 = inp[1]
            inp1 = int(inp1) - 1
            inp2 = int(inp2) - 1
            if player == 1:
                s = gamedata[inp1]
                if s[inp2] == 0:
                    s[inp2] = 1
                else:
                    valid = 1
                    print("select an other place")
            else:
                s = gamedata[inp1]
                if s[inp2] == 0:
                    s[inp2] = 2
                else:
                    valid = 1
                    print("select an other place")
            if player == 1:
                player = 2
            else:
                player = 1
