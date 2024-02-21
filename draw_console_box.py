
def draw_console_box(width, height):
    print("+", "-"*(width-2), "+")
    while height > 2:
        print ("|", " "*width, "|")
        height -= 1
    print("+", "-"*(width-2), "+")    


if __name__ == '__main__':
    draw_console_box(5,5)
    draw_console_box(52,6)
