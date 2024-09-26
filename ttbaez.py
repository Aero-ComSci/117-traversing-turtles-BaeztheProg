#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
import random as rand


class muchasTortugas:
  #init Method
  def __init__(self, numTurtles, shapes, colors):
    self.numTurtles = numTurtles
    self.shapes = shapes
    self.colors = colors
    self.turtles = []
    for each in range(self.numTurtles):
      t = trtl.Turtle(shape=self.shapes[each])
      #random color per color list
      t.color(colors.pop(rand.randint(0, len(colors)-1)))
      self.turtles.append(t)
  def draw(self):
    startx = 0
    starty = 0
    for t in self.turtles:
      t.penup()
      t.goto(startx, starty)
      t.pendown()
      t.right(45)     
      t.forward(50)
      startx = startx + 50
      starty = starty + 50
   
  def drawOnLast(self):
    startx = 0
    starty = 0
    for t in self.turtles:
      t.penup()
      t.goto(startx, starty)
      t.pendown()
      t.right(45)     
      t.forward(50)
      startx = t.xcor()
      starty = t.ycor()







# create an empty list of turtles

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

turtles = muchasTortugas(6, turtle_shapes, turtle_colors)
turtles.drawOnLast()

#	
# startx = startx + 50
# starty = starty + 50

wn = trtl.Screen()
wn.mainloop()
