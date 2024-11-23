# 11/18/24, Kennon Sauter, U3Project , The Recursive Tree
import turtle
angle = 30
minus = 15
t = turtle.Turtle()
"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""
def drawtree(distance,size):
  if distance < 1:
    size = size + 3
    t.pensize(size)
    t.color('green')
    t.forward(5)
    t.backward(5)
    t.color('brown')
    
    return t
  
  t.forward(distance)
  t.lt(angle)
  size = size - 1
  t.pensize(size)
  
  drawtree(distance-minus,size)
 
  t.rt(angle*2)
  
  drawtree(distance-minus,size)
  
  t.lt(angle)
  size = size + 1
  t.pensize(size)
  t.backward(distance)
  
  
  
  
  
  
  
  
  
  
  
  #t.forward(distance)
  #t.lt(angle)

  #drawtree(t,distance-minus)
  #t.rt(angle*2)
  
  #drawtree(t,distance-minus)
  #t.lt(angle)
  
  #t.backward(distance)

     


def main():
  
  size = 7
  t.pensize(size)
  t.lt(90)
  t.color('brown')
  drawtree(100,size)
  turtle.mainloop()
if __name__ == "__main__":
  main()  