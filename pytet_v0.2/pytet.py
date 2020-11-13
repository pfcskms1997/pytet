from matrix import *
import random

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###

# I-Block
I = [ [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ],
      [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ] ],
      [ [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ] ],
      [ [ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ] ]
# O-Block
O = [ [ [ 1, 1 ], [ 1, 1 ] ],
      [ [ 1, 1 ], [ 1, 1 ] ],
      [ [ 1, 1 ], [ 1, 1 ] ],
      [ [ 1, 1 ], [ 1, 1 ] ] ]
# T-Block
T = [ [ [ 0, 1, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ] ],
      [ [ 0, 1, 0 ], [ 0, 1, 1 ], [ 0, 1, 0 ] ],
      [ [ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 1, 0 ] ],
      [ [ 0, 1, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ] ] ]
# J-Block
J = [ [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 1, 1, 0 ] ],
      [ [ 1, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ] ],
      [ [ 0, 1, 1 ], [ 0, 1, 0 ], [ 0, 1, 0 ] ],
      [ [ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 1 ] ] ]
# L-Block
L = [ [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 1 ] ],
      [ [ 0, 0, 0 ], [ 1, 1, 1 ], [ 1, 0, 0 ] ],
      [ [ 1, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ] ],
      [ [ 0, 0, 1 ], [ 1, 1, 1 ], [ 0, 0, 0 ] ] ]
# S-Block
S = [ [ [ 0, 1, 1 ], [ 1, 1, 0 ], [ 0, 0, 0 ] ],
      [ [ 0, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 1 ] ],
      [ [ 0, 0, 0 ], [ 0, 1, 1 ], [ 1, 1, 0 ] ],
      [ [ 1, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ] ] ]
# Z-Block
Z = [ [ [ 1, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 0 ] ],
      [ [ 0, 0, 1 ], [ 0, 1, 1 ], [ 0, 1, 0 ] ],
      [ [ 0, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 1 ] ],
      [ [ 0, 1, 0 ], [ 1, 1, 0 ], [ 1, 0, 0 ] ] ]

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

rand_num = random.randint(0, 6)
i = 0
arrayBlk = [I, O, T, J, L, S, Z]

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk[rand_num][i])
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        i = (i + 1) % 4
        currBlk = Matrix(arrayBlk[rand_num][i])
    elif key == ' ': # drop the block
        while tempBlk.anyGreaterThan(1) is False:
            top += 1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            i = (i - 1) % 4
            currBlk = Matrix(arrayBlk[rand_num][i])
        elif key == ' ': # undo: move up
            top -= 1
            newBlockNeeded = True
            # print('Not implemented')

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False

        rand_num = random.randint(0, 6)
        i = 0
        
        currBlk = Matrix(arrayBlk[rand_num][i])
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
