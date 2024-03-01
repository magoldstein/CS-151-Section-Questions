
from pgl import GWindow, GRect, GArc, GOval

def yinyang():
    gw = GWindow(500, 500)
    layer1 = GOval(100,100,300,300)
    gw.add(layer1)
    layer1.set_filled(True)

    layer2 = GRect(250,100,150,300)
    gw.add(layer2)
    layer2.set_filled(True)
    layer2.set_fill_color('#FFFFFF')
    layer2.set_color('#FFFFFF')

    layer3 = GOval(100,100,300,300)
    gw.add(layer3)

    layer4 = GOval(175,250,150,150)
    gw.add(layer4)
    layer4.set_filled(True)
    layer4.set_fill_color('#FFFFFF')
    layer4.set_color('#FFFFFF')

    layer5 = GOval(175,100,150,150)
    gw.add(layer5)
    layer5.set_filled(True)

    layer6 = GOval(220,300,50,50)
    gw.add(layer6)
    layer6.set_filled(True)

    layer7 = GOval(220,150,50,50)
    gw.add(layer7)
    layer7.set_filled(True)
    layer7.set_fill_color('#FFFFFF')
    layer7.set_color('#FFFFFF')











if __name__ == '__main__':
    yinyang()