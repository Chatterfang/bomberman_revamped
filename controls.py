from configuration import *
from bomb_behavior import *

# universal move controller

def move(x_direction = 0, y_direction = 0):

    if board[player['y'] + y_direction][player['x'] + x_direction][0] in (' ', 'B'):

        if board[player['y'] + y_direction][player['x'] + x_direction][0] == 'B':
            bomb_check(player['x'] + x_direction, player['y'] + y_direction)

        board[player['y']][player['x']][0] = ' '
        board[player['y'] + y_direction][player['x'] + x_direction][0] = 'P'

        canvas.move(player['id'], x_direction*config['radius']*2, y_direction*config['radius']*2)

        player['x'] += x_direction
        player['y'] += y_direction

        bomb_fuse()

    draw_board()

##### READ ####
# strasny ojeb xdd pre additional argument pri event handler-i
# keypress bind/hociaky event neberie additional arguments, aspon neviem ako to spravit priamo
# tkitner dokumentacia ma '54.7. The extra arguments trick', ale netusim co sa tam deje
# namiesto toho (vid. nizsie) keypress event upresni extra arguments, a stale zredukuje mnozstvo kodu

# directions for move controler

def move_up(event):
    move(y_direction = -1)

def move_down(event):
    move(y_direction = 1)

def move_left(event):
    move(x_direction = -1)

def move_right(event):
    move(x_direction = 1)

# POZNAMKA:
# ked bude multiplayer tak ako additional argument aj passnut ktoreho hraca posunut
# relevantne aj v local, aj network play

# actions

def bomb_use(event):

    if player['bombs'] > 0:

        x = player['x']
        y = player['y']

        player['bombs'] -= 1

        canvas.itemconfigure('bomb_count', text = f'bombs : {player["bombs"]}')

        entity_round(x, y, color = 'black', tag = 'bomb')

        bomb['x'] = x
        bomb['y'] = y
        bomb['fuse'] = 3

if __name__ == "__main__":
    pass