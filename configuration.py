import tkinter

config = {'width' : 9,
          'height' : 9,
          'radius' : 25,
          'print_board' : True}

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

root = tkinter.Tk()
canvas = tkinter.Canvas(root, bg = "white", height = config['height'] * 2 * config['radius'],
                        width = config['width'] * 2 * config['radius'], background = 'gray')