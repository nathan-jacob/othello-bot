import numpy as np
mycolor = True
# white -> true (recomended)
# black -> false
board = np.array([3,3,3,3,3,3,3,3,3,3,
                      3,0,0,0,0,0,0,0,0,3,
                      3,0,0,0,0,0,0,0,0,3,
                      3,0,0,0,0,0,0,0,0,3,
                      3,0,0,0,1,2,0,0,0,3,
                      3,0,0,0,2,1,0,0,0,3,
                      3,0,0,0,0,0,0,0,0,3,
                      3,0,0,0,0,0,0,0,0,3,
                      3,0,0,0,0,0,0,0,0,3,
                      3,3,3,3,3,3,3,3,3,3])
visualizer = np.reshape(board, (-1, 10))
oneloc = np.argwhere(board==1)
twoloc = np.argwhere(board==2)
# 1 is white
# 2 is black
def around(board, pt):
    if pt==1:
        s=2
        n=1
    else:
        s=1
        n=2
    i=0
    totalsum=0
    arrazzy = []
    arrazzzy = []
    while i < 90:
        if board[i]==0:
            summer = 0
            f=1
            b=1
            u = 10
            d=10
            drd = 11
            dru = 9
            dld = 9
            dlu = 11
            totalsum=0
            while True:
                if board[i + f] == s:
                    summer = summer + 1
                    maxandruby = summer
                    f=f+1

                if board[i + f] == n:
                    break
                if board[i + f] == 3 or board[i + f] == 0:
                    summer = 0
                    break
            totalsum=totalsum+summer
            summer=0
            while True:
                if board[i - b] == s:
                     summer = summer + 1
                     maxandruby = summer
                     b=b+1

                if board[i - b] == n:
                   break
                if board[i - b] == 3 or board[i - b] == 0:
                    summer = 0
                    break
            totalsum=totalsum+summer
            summer=0
            while True:
                if board[i - u] == s:
                    summer = summer + 1
                    maxandruby = summer
                    u=u+10

                if board[i - u] == n:
                    break
                if board[i - u] == 3 or board[i - u] == 0:
                    summer = 0
                    break
            totalsum=totalsum+summer
            summer=0
            while True:
                if board[i + d] == s:
                    summer = summer + 1
                    maxandruby = summer
                    d=d+10
                if board[i + d] == n:
                    break
                if board[i + d] == 3 or board[i + d] == 0:
                    summer = 0
                    break
            totalsum=totalsum+summer
            summer=0
            while True:
                if board[i - drd] == s:
                    summer = summer + 1
                    maxandruby = summer
                    drd = drd+11

                if board[i - drd] == n:
                    break
                if board[i - drd] == 3 or board[i - drd] == 0:
                    summer = 0
                    break
            totalsum=totalsum+summer
            summer=0
            while True:
               if board[i + dru] == s:
                    summer = summer + 1
                    maxandruby = summer
                    dru = dru+9
               if board[i + dru] == n:
                    break
               if board[i + dru] == 3 or board[i + dru] == 0:
                    summer = 0
                    break
            totalsum=totalsum+summer
            summer=0
            while True:
                if board[i - dld] == s:
                    summer = summer + 1
                    maxandruby = summer
                    dld = 9 + dld


                if board[i - dld] == n:
                    break
                if board[i - dld] == 3 or board[i - dld] == 0:
                    summer = 0
                    break
            totalsum=totalsum+summer
            summer=0
            while True:
                if board[i + dlu] == s:
                    summer = summer + 1
                    maxandruby = summer
                    dlu = dlu + 11

                if board[i + dlu] == n:
                    break
                if board[i + dlu] == 3 or board[i + dlu] == 0:
                    summer = 0
                    break
            totalsum=totalsum+summer
            summer=0
            arrazzy.append(i)
            arrazzzy.append(totalsum)

        try:
            #print(str(arrazzy[arrazzzy.index(max(arrazzzy))]) + " yields " + str(max(arrazzzy)))
            tom = 1
        except:
            t=1
        i = i + 1
    arazzys=[arrazzy for _,arrazzy in sorted(zip(arrazzzy,arrazzy), reverse=True)]
    return sorted(arrazzzy, reverse=True), arazzys
def simulate(boardy, pt, pos):
    summer = 0
    f=1
    b=1
    u = 10
    d=10
    drd = 11
    dru = 9
    dld = 9
    dlu = 11
    i = pos
    boardify = list(boardy)
    if pt == 1:
        s=2
        n=1
    else:
        s=1
        n=2
    while True:
        if boardify[i + f] == s:
            summer = summer + 1
            maxandruby = summer
            f=f+1

        if boardify[i + f] == n:
            cp = f + i
            while cp != i:
                cp = cp-1
                boardify[cp] = n
            boardify[i]=pt
            break
        if boardify[i + f] == 3 or boardify[i + f] == 0:
            summer = 0
            break
    summer=0
    while True:
        if boardify[i - b] == s:
             summer = summer + 1
             maxandruby = summer
             b=b+1

        if boardify[i - b] == n:
            cp = i - b
            while cp != i:
                cp = cp + 1
                boardify[cp] = n
            boardify[i]=pt
            break
        if boardify[i - b] == 3 or boardify[i - b] == 0:
            summer = 0
            break

    summer=0
    while True:
        if boardify[i - u] == s:
            summer = summer + 1
            maxandruby = summer
            u=u+10

        if boardify[i - u] == n:
            cp = i - u
            while cp != i:
                cp = cp+10
                boardify[cp] = n
            boardify[i]=pt
            break
        if boardify[i - u] == 3 or boardify[i - u] == 0:
            summer = 0
            break

    summer=0
    while True:
        if boardify[i + d] == s:
            summer = summer + 1
            maxandruby = summer
            d=d+10
        if boardify[i + d] == n:
                cp = d + i
                while cp != i:
                    cp = cp-10
                    boardify[cp] = n
                boardify[i]=pt
                break
        if boardify[i + d] == 3 or boardify[i + d] == 0:
            summer = 0
            break

    summer=0
    while True:
        if boardify[i+drd] == s:
            drd = drd+11
        if boardify[i+drd] == n:
            boardify[i]=pt
            cp=i+drd
            while cp != i:
                cp = cp - 11
                #print (cp)
                boardify[cp] = n
            break
        else:
            break
    summer=0
    while True:
       if boardify[i - dru] == s:
            summer = summer + 1
            maxandruby = summer
            dru = dru+9
       if boardify[i + dru] == n:
                boardify[i]=pt
                cp = i-dru
                while cp != i:
                    cp = cp+9
                    boardify[cp] = n
                boardify[i]=pt
                break
       else:
            break

    summer=0
    while True:
        if boardify[i + dld] == s:
            summer = summer + 1
            maxandruby = summer
            dld = 9 + dld


        if boardify[i + dld] == n:
            boardify[i]=pt
            cp = dld + i
            while cp != i:
                cp = cp - 9
                boardify[cp] = n
            boardify[i]=pt
            break
        if boardify[i - dld] == 3 or boardify[i - dld] == 0:
            summer = 0
            break
        else:
            break
    summer=0
    while True:
        if boardify[i - dlu] == s:
            summer = summer + 1
            maxandruby = summer
            dlu = dlu + 11
        cp=i-dlu
        if boardify[i - dlu] == n:
                boardify[i]=pt
                while cp != i:
                    boardify[cp] = n
                    cp = cp+11
                boardify[i]=pt
                break
        if boardify[i + dlu] == 3 or boardify[i + dlu] == 0:
            break

    summer=0
    return boardify
def oponent(boord):
    ch=int(input("where do you want to play"))
    print("Here is the new board:")
    print(np.reshape(simulate(boord, 2, ch), (-1, 10)))
    yourturn(simulate(boord, 2, ch))
def failure():
    print("Here is the starting board:")
    print(np.reshape(board, (-1, 10)))
    oponent(board)
def yourturn(poena):
    poena1 = list(poena)
    f, t = [], []
    f, t = around(poena1, 1)
    print("I played at position " + str(t[0]) + " which got me " + str(f[0]) + " flips")
    print(np.reshape(simulate(poena1, 1, t[0]), (-1,10)))
    oponent(simulate(poena1, 1, t[0]))

failure()
#test tree
