from configuration import *
from map_generator import draw_board
from graphics import entity_round

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


if __name__ == "__main__":
    pass