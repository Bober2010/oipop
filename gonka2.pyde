x = 550
y = 270
v = 700
n = 200
c = 100
p = 100
def setup():
    size(600,600)
def draw():
    global x,y,v,n,p,c
    m = loadImage("gonk.jpg")
    image(m,0,0,650,650)
    m = loadImage("nnn.jpg")
    image(m,x,y,p,c)
    m = loadImage("images.jpg")
    image(m,v,n,100,100)
    x = x - 3
    y = y + 4
    p = p + 2
    c = c + 2
   
