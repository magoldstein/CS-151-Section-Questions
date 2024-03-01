from pgl import GWindow, GRect, GArc, GOval
import random

def stamps():
    gw = GWindow(500, 500)
    square = GRect(0,0,50,50)
    gw.add(square)
    square.set_filled(True)

    def stamp(pos):
        choice = random.randint(0,1)
        if choice == 1:
            stamp_shape = GRect(pos.get_x()-25,pos.get_y()-25,50,50)
        else:
            stamp_shape =  GOval(pos.get_x()-25,pos.get_y()-25,50,50)   
        gw.add(stamp_shape)    
        color_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E","F"]
        color = "#"
        for i in range(0,6):
            color += random.choice(color_options)
        stamp_shape.set_fill_color(color)
        stamp_shape.set_filled(True)
        stamp_shape.send_backward()

    def position_square(mouse):
        square.set_location(mouse.get_x()-25, mouse.get_y()-25)

    gw.add_event_listener ("mousemove", position_square)
    gw.add_event_listener("click", stamp)

if __name__ == '__main__':
    stamps()