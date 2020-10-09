import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex

def sokszog(n, h, sz):
    for i in range (n):
        alex.color(sz)
        alex.forward(h)
        alex.left(360/n)
        
sokszog(3, 50, 'yellow')
sokszog(4, 50, 'black')
sokszog(5, 50, 'purple')
sokszog(6, 50, 'yellow')
sokszog(7, 50, 'black')
sokszog(8, 50, 'purple')
