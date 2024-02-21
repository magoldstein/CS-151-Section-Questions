from pgl import GWindow, GRect

gw = GWindow(200,200)
for c in range(0,10):
    for r in range(0,10):
        rect = GRect(20*c,20*r,20,20)
        if (r+c) % 2 != 0:
            rect.set_filled(True)
    gw.add(rect)

def func1(x,y):	
    return z + func2(x,y)
    print ("func 1 done")
	
def func2(x,y):	
    def func3(x):	
        return (y + x) ** 2
    z = x - func3(y)
    return z - y
	 
if __name__ == '__main__':	
    z = 1	
    print(func1(2,z))