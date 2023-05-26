#The bonus question 10 of part 1 is incorporated.
#Part 1 question 1:
def getPositions(board,color):
    pos=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == color:
                pos.append((i,j))
    return pos
#Part 1 question 2:
def isTouching(board,color1,color2, isTrue=True):
    pos1=getPositions(board,color1)
    pos2=getPositions(board,color2)
    if isTrue:
        if pos1==pos2 and (len(pos1)>1):
            for i in range(len(pos1)-1):
                if (-2<pos1[i][0]-pos1[i+1][0]<2 and -2<pos1[i][1]-pos1[i+1][1]<2) and (pos1[i][0]==pos1[i+1][0] or pos1[i][1]==pos2[i+1][1]):
                    return True
        elif pos1!=pos2:
            for i in range(len(pos1)):
                for j in range(len(pos2)):
                    if (-2<pos1[i][0]-pos2[j][0]<2 and -2<pos1[i][1]-pos2[j][1]<2) and (pos1[i][0]==pos2[j][0] or pos1[i][1]==pos2[j][1]):
                        return True
        return False
    else:
        return not isTouching(board,color1,color2)
#Part 1 question 3:
def sameRow(board, color1, color2,isTrue=True):
    pos1 = getPositions(board, color1)
    pos2 = getPositions(board, color2)
    if isTrue:
        if pos1 == pos2:
                for i in range(len(pos1)):
                    for j in range(len(pos2)):
                        if len(pos1)>1 and pos1[i][0]==pos1[j][0]:
                            return True
        else:
            for i in range(len(pos1)):
                    for j in range(len(pos2)):
                        if pos1[i][0]==pos2[j][0]:
                            return True
        return False
    else:
        return not sameRow(board, color1,color2)
#part 1 question 4:
def sameColumn(board, color1, color2, isTrue=True):
    pos1 = getPositions(board, color1)
    pos2 = getPositions(board, color2)
    if isTrue:
        if pos1 == pos2:
            for i in range(len(pos1)):
                for j in range(len(pos2)):
                    if len(pos1) > 1 and pos1[i][1] == pos1[j][1]:
                        return True
        else:
            for i in range(len(pos1)):
                for j in range(len(pos2)):
                    if pos1[i][1] == pos2[j][1]:
                        return True
        return False
    else:
        return not sameColumn(board, color1, color2)
#part 1 question 5:
def inRow(board, pos, color, N, isTrue=True):
    pos1=getPositions(board, color)
    row=100
    if isTrue:
        if pos=='top':
            row=0
        elif pos=='bottom':
            row=2
        elif pos=='middle':
            row=1
        occurs=0
        for i in range(len(pos1)):
            if pos1[i][0]==row:
                occurs+=1
        if occurs>=N:
            return True
        else:
            return False
    else:
       return not inRow(board, pos, color, N)
#part 1 question 6:
def inColumn(board, pos, color, N, isTrue=True):
    pos1 = getPositions(board, color)
    col=100
    if isTrue:
        if pos == 'left':
            col = 0
        elif pos == 'right':
            col = 2
        elif pos == 'middle':
            col = 1
        occurs = 0
        for i in range(len(pos1)):
            if pos1[i][1] == col:
                occurs += 1
        if occurs >= N:
            return True
        else:
            return False
    else:
        return not inColumn(board, pos, color, N)
#part 1 question 7:
def isBetween(board, color, betweencol1, betweencol2, isTrue=True):
    pos1=getPositions(board, color)
    pos2=getPositions(board,betweencol1)
    pos3=getPositions(board,betweencol2)
    if isTrue:
        if pos1==pos2==pos3:
            r=['top','bottom','middle']
            c=['left','middle','right']
            for i in range(3):
                if inRow(board, r[i],color,3):
                    return True
                if inColumn(board, c[i],color,3):
                    return True
        else:
            for i in range(len(pos1)):
                for j in range(len(pos2)):
                    for k in range(len(pos3)):
                        if (pos1[i][0]==pos2[j][0]==pos3[k][0]) and (pos2[j][1]>pos1[i][1]>pos3[k][1] or pos2[j][1]<pos1[i][1]<pos3[k][1]):
                            return True
                        elif (pos1[i][1]==pos2[j][1]==pos3[k][1]) and (pos2[j][0]>pos1[i][0]>pos3[k][0] or pos2[j][0]<pos1[i][0]<pos3[k][0]):
                            return True
        return False
    else:
        return not isBetween(board, color, betweencol1, betweencol2)
#part 1 question 8:
def atPlace(board, color, row, col, isTrue=True):
    pos1 = getPositions(board, color)
    r = 0
    c = 0
    if isTrue != False:
        if row == 'top':
            r = 0
        if row == 'middle':
            r = 1
        if row == 'bottom':
            r = 2
        if col == 'left':
            c = 0
        if col == 'middle':
            c = 1
        if col == 'right':
            c = 2
        posg = (r, c)
        for i in range(len(pos1)):
            if pos1[i] == posg:
                return True
        else:
            return False
    else:
        return not atPlace(board, color, row, col)
#part 1 question 9
def isTowards(board, color, direction, color2, isTrue=True):
    pos1=getPositions(board, color)
    pos2=getPositions(board, color2)
    if isTrue:
        if sameColumn(board, color, color2):
            if direction =='above':
                for i in range(len(pos1)):
                    for j in range(len(pos2)):
                        if pos1[i][0]<pos2[j][0] and pos1[i][1]==pos2[j][1]:
                            return True
                return False
            if direction =='under' or direction=='below':
                for i in range(len(pos1)):
                    for j in range(len(pos2)):
                        if pos1[i][0]>pos2[j][0] and pos1[i][1]==pos2[j][1]:
                            return True
                return False
        if sameRow(board, color, color2):
            if direction =='right':
                for i in range(len(pos1)):
                    for j in range(len(pos2)):
                        if pos1[i][1]>pos2[j][1] and pos1[i][0]==pos2[j][0]:
                            return True
                return False
            if direction =='left':
                for i in range(len(pos1)):
                    for j in range(len(pos2)):
                        if pos1[i][1]<pos2[j][1] and pos1[i][0]==pos2[j][0]:
                            return True
                return False
        return False
    else:
        return not isTowards(board, color, direction, color2)
#part 2 question 11:
def getColors(colors):
    return colors.split(' ')
#part 2 question 12:
def getRules(rules):
        nlst=rules.split('\n')
        rulesf=[]
        for i in range(len(nlst)):
            if nlst[i]==' ' or nlst[i]=='\n' or nlst[i]=='':
                continue
            else:
                rulesf.append(nlst[i])
        return rulesf
#part 2 question 13:
def inputFromFile(name):
    file=open(name,'r').read()
    lst=file.split('\n')
    rules='\n'.join(lst[2:])
    colors=lst[0]
    return (getColors(colors),getRules(rules))
#part 2 question 14:
def isValidBoard(board,colors):
    if len(board)!=3:
        return False
    if len(board[0])!=3 or len(board[1])!=3 or len(board[2])!=3:
        return False
    lst=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            lst.append(board[i][j])
    lst.sort()
    colors.sort()
    if colors!=lst:
        return False
    else:
        return True
#part 2 question 15:
def checkRules(board, rules, isTrue = True):
    if isTrue:
        r1=[]
        for i in range(len(rules)):
            r1.append(rules[i].replace('.', ' '))
        for i in range(len(r1)):
            r=r1[i].split(' ')
            if r[0]=='col':
                if len(r)==5:
                    if r[4]=='not':
                        z=inColumn(board, r[3],r[1],int(r[2]),False)
                        if not z:
                            return z
                if len(r)==4:
                    z=inColumn(board, r[3],r[1],int(r[2]))
                    if not z:
                        return z
            if r[0]=='row':
                if len(r)==5:
                    if r[4]=='not':
                        z=inRow(board, r[3], r[1], int(r[2]), False)
                        if not z:
                            return False
                if len(r)==4:
                    z=inRow(board, r[3], r[1],int(r[2]))
                    if not z:
                        return z
            if r[0]=='place':
                if len(r)==5:
                    if r[4]=='not':
                        z=atPlace(board, r[1], r[2], r[3], False)
                        if not z:
                            return False
                if r[2]=='middle':
                    if len(r)==3:
                        z=atPlace(board,r[1],'middle','middle')
                        if not z:
                            return z
                    if len(r)==4:
                        z=atPlace(board, r[1], 'middle', 'middle', False)
                        if not z:
                            return False
                if len(r)==4:
                    z=atPlace(board, r[1], r[2], r[3])
                    if not z:
                        return z
            if r[0]=='samerow':
                if len(r)==4:
                    if r[3]=='not':
                        z=sameRow(board, r[1], r[2], False)
                        if not z:
                            return False
                if len(r)==3:
                    z=sameRow(board, r[1],r[2])
                    if not z:
                        return z
            if r[0]=='touches' or r[0]=='touch':
                if len(r)==3:
                    z=isTouching(board, r[1],r[2])
                    if not z:
                        return z
                if len(r)==4:
                    if r[3]=='not':
                        z=isTouching(board, r[1], r[2], False)
                        if not z:
                            return z
            if r[0]=='between':
                if len(r)==5:
                    if r[4]=='not':
                        z=isBetween(board, r[1], r[2], r[3], False)
                        if not z:
                            return False
                if len(r)==4:
                    z=isBetween(board, r[1], r[2],r[3])
                    if not z:
                        return z
            if r[0]=='towards':
                if len(r)==5:
                    if r[4]=='not':
                        z=isTowards(board,r[1],r[2],r[3],False)
                        if not z:
                            return z
                if len(r)==4:
                    z=isTowards(board,r[1],r[2],r[3])
                    if not z:
                        return z
            if r[0]=='samecolumn' or r[0]=='sameCol' or r[0]=='sameColumn':
                if len(r)==4:
                    if r[3]=='not':
                        z=sameColumn(board, r[1], r[2], False)
                        if not z:
                            return z
                if len(r)==3:
                    z=sameColumn(board, r[1],r[2])
                    if not z:
                        return z
        return True
    else:
        return not checkRules(board, rules)
def makePermutations(colors):
     import itertools
     c=[[],[],[]]
     possible=[]
     p= list(itertools.permutations(colors))
     for i in range(len(p)):
         c = [[p[i][0], p[i][1], p[i][2]], [p[i][3], p[i][4], p[i][5]], [p[i][6], p[i][7], p[i][8]]]
         possible.append(c)
     return possible
# Part 3
def GameSolver(filename):
    cr=inputFromFile(filename)
    al=makePermutations(cr[0])
    for i in range(len(al)):
        if checkRules(al[i], cr[1])==True and isValidBoard(al[i],cr[0]):
            return al[i]
    return []
def report(bhool, gaya = True):
    if gaya:
        return bhool
    else:
        return not bhool
def read_board():
    give = input().split(' ')
    board = []
    for j in range(0,9,3):
        board.append([give[i] for i in  range(j,j+3)])
    return board
def are_touching(board,color1,color2, isTrue=True):
    pos1=getPositions(board,color1)
    pos2=getPositions(board,color2)
    if isTrue:
        if pos1==pos2 and (len(pos1)>1):
            for i in range(len(pos1)-1):
                if (-2<pos1[i][0]-pos1[i+1][0]<2 and -2<pos1[i][1]-pos1[i+1][1]<2) and (pos1[i][0]==pos1[i+1][0] or pos1[i][1]==pos2[i+1][1]):
                    return True
        elif pos1!=pos2:
            for i in range(len(pos1)):
                for j in range(len(pos2)):
                    if (-2<pos1[i][0]-pos2[j][0]<2 and -2<pos1[i][1]-pos2[j][1]<2) and (pos1[i][0]==pos2[j][0] or pos1[i][1]==pos2[j][1]):
                        return True
        return False
    else:
        return not are_touching(board,color1,color2)