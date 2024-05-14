import random
import tkinter

config = {'width' : 9,
          'height' : 9,
          'radius' : 25}

config_items = {'P' : (1, 'blue'),
                'M' : (2, 'purple'),
                'W' : (10, 'orange'),
                'B' : (3, 'black'),
                '#' : (0, 'gray')}

player = {'x' : None,
          'y' : None,
          'bombs': 3}

bomb = {'x' : None,
        'y' : None,
        'fuse' : 0}

board = []

#generate empty map

for y in range(config['height']):
    board.append([]*config['width'])
    for x in range(config['width']):
        board[y].append([' '])

#wall bounds

for y in range(config['height']):
    for x in range(config['width']):

        if x%2 == 1 and y%2 == 1 and board[y-1][x-1][0] != '#':
            board[y-1][x-1][0] = '#'

        if y == 0 or y == config['height'] - 1:
            board[y][x][0] = '#'

        if x == 0 or x == config['width'] - 1:
            board[y][x][0] = '#'

#populate board

for item in config_items:

    for number in range(config_items[item][0]):

        overlap = True

        while overlap:
            x = random.randint(1, config['width']-1)
            y = random.randint(1, config['height']-1)

            if board[y][x][0] == ' ':
                board[y][x][0] =  item

                overlap = False

    if item == 'P':
        player['x'] = x
        player['y'] = y


# draw

def draw_board():
    print('#######     board    ########')

    for i in board:
        print(*i)

    print(f'bombs: {player["bombs"]}')

draw_board()

# tkinter section

def coord_conversion(x, y):
    x0 = config['radius']*2*x
    y0 = config['radius']*2*y
    x1 = config['radius']*2*(x+1)
    y1 = config['radius']*2*(y+1)

    return x0, y0, x1, y1

# sprites

def entity_round(x, y, color = 'black', tag = None):
    x0, y0, x1, y1 = coord_conversion(x, y)    
    canvas.create_oval(x0, y0, x1, y1, fill = color, tag = tag)

def entity_square(x, y, color = 'black', tag = None):
    x0, y0, x1, y1 = coord_conversion(x, y)    
    canvas.create_rectangle(x0, y0, x1, y1, fill = color, tag = tag)

# bombs

def bomb_check(x, y):

    x0 = config['radius']*2*x + config['radius']/2
    y0 = config['radius']*2*y + config['radius']/2
    x1 = config['radius']*2*(x+1) - config['radius']/2
    y1 = config['radius']*2*(y+1) - config['radius']/2

    bomb = canvas.find_overlapping(x0, y0, x1, y1)[1:]

    canvas.delete(bomb)

    player['bombs'] += 1

def bomb_explode(x, y):

    x0 = config['radius']*2*(x-1) + config['radius']/2
    y0 = config['radius']*2*(y-1) + config['radius']/2
    x1 = config['radius']*2*(x+2) - config['radius']/2
    y1 = config['radius']*2*(y+2) - config['radius']/2

    destroy = set(canvas.find_overlapping(x0, y0, x1, y1))

    exclude = set(canvas.find_withtag('#'))
    
    # exclude grass
    exclude.add(1)

    destroy = destroy.difference(exclude)

    for id in destroy:
        canvas.delete(id)

    entity_round(x, y, color = 'red', tag = 'bomb')
    canvas.create_oval(x0, y0, x1, y1, fill = 'red', tag = 'bomb')


    # board update
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if not board[i][j][0] == '#':
                board[i][j][0] = ' '

    draw_board()

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

def bomb_fuse():
    bomb['fuse'] -= 1

    if bomb['fuse'] == 0:
        bomb_explode(bomb['x'], bomb['y'])

    if bomb['fuse'] == -1:
        canvas.delete('bomb')

# controls

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

def move_up(event):
    move(y_direction = -1)

def move_down(event):
    move(y_direction = 1)

def move_left(event):
    move(x_direction = -1)

def move_right(event):
    move(x_direction = 1)

# canvas draw

root = tkinter.Tk()
canvas = tkinter.Canvas(root, bg = "white", height = config['height'] * 2 * config['radius'],
                        width = config['width'] * 2 * config['radius'], background = 'gray')

# grass (could be made for every emoty 'tile', but this reduces number of objects on canvas)

canvas.create_rectangle(config['radius'] * 2, config['radius'] * 2,
                        (config['width']-1) * 2 * config['radius'],
                        (config['height']-1) * 2 * config['radius'],
                        fill = 'green')

# populate canvas

for y in range(1, config['height']-1):
    for x in range(1, config['width']-1):
        entity = board[y][x][0]

        if entity in ('P', 'M', 'B'):
            entity_round(x, y, color = config_items[entity][1], tag = entity)

        elif entity in ('W', '#'):
            entity_square(x, y, color = config_items[entity][1], tag = entity)

# detect player

player['id'] = canvas.find_withtag('P')[0]

# text info

canvas.create_text(30, 20, text = f'bombs : {player["bombs"]}', tag = 'bomb_count')

# binds

root.bind('<Up>', move_up)
root.bind('<Down>', move_down)
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)
root.bind('<space>', bomb_use)

canvas.pack()
root.mainloop()
