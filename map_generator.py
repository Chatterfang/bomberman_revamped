from configuration import *
import random

#generate empty map

def map_empty():
    for y in range(config['height']):
        board.append([]*config['width'])
        for x in range(config['width']):
            board[y].append([' '])

#wall bounds

def map_walls():
    for y in range(config['height']):
        for x in range(config['width']):

            if x%2 == 1 and y%2 == 1 and board[y-1][x-1][0] != '#':
                board[y-1][x-1][0] = '#'

            if y == 0 or y == config['height'] - 1:
                board[y][x][0] = '#'

            if x == 0 or x == config['width'] - 1:
                board[y][x][0] = '#'

#populate board

def map_populate():
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

# generate final map

def map_final():
    map_empty()
    map_walls()
    map_populate()

# draw map

def draw_board():
    if config['print_board']:
            print('#######     board    ########')

            for i in board:
                print(*i)

            print(f'bombs: {player["bombs"]}')

# test

if __name__ == "__main__":
    map_final()

    draw_board()