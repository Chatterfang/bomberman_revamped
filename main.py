from configuration import config
from map_generator import map_final
from map_generator import draw_board
from bomb_behavior import *
import controls
import graphics

map_final()

draw_board()

graphics.draw_canvas()

root.bind('<Up>', controls.move_up)
root.bind('<Down>', controls.move_down)
root.bind('<Left>', controls.move_left)
root.bind('<Right>', controls.move_right)
root.bind('<space>', bomb_use)

canvas.pack()
root.mainloop()