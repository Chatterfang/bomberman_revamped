from configuration import *
import tkinter

# generate coords for canvas drawing:

# coordinates are on a grid system,
# 1 grid cell has dimensions of 2*config['radius']

# range: 'radius' around cell (default is 0, uses only specified cell)
# offset: when checking collision, enable offset

def coord_conversion(x, y, range = 0, offset_bool = False):
    if offset_bool:
        offset = config['radius']/2
    else:
        offset = 0

    x0 = config['radius']*2*(x-range) + offset
    y0 = config['radius']*2*(y-range) + offset
    x1 = config['radius']*2*(x+range+1) - offset
    y1 = config['radius']*2*(y+range+1) - offset
    return (x0, y0, x1, y1)

# sprites:

# round

def entity_round(x, y, color = 'black', tag = None):
    x0, y0, x1, y1 = coord_conversion(x, y)    
    canvas.create_oval(x0, y0, x1, y1, fill = color, tag = tag)

# square

def entity_square(x, y, color = 'black', tag = None):
    x0, y0, x1, y1 = coord_conversion(x, y)    
    canvas.create_rectangle(x0, y0, x1, y1, fill = color, tag = tag)

# draw canvas

def draw_canvas():
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

# test:

if __name__ == "__main__":
    print(coord_conversion(5,5))

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, bg = "white", height = 100, width = 100)

    entity_round(0,0, color = 'red')
    entity_square(1,0, color = 'green')

    canvas.pack()
    root.mainloop()