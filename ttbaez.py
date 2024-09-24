#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl


class muchasTortugas:
  #init Method
  def __init__(self, numTurtles, shapes, colors):
    self.numTurtles = numTurtles
    self.shapes = shapes
    self.colors = colors
    self.turtles = []
    for each in range(self.numTurtles):
      t = trtl.Turtle(shape=self.shapes[each])
      t.color(colors[each])
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
    






# create an empty list of turtles

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

turtles = muchasTortugas(6, turtle_shapes, turtle_colors)
turtles.draw()

#	
# startx = startx + 50
# starty = starty + 50

wn = trtl.Screen()
wn.mainloop()
