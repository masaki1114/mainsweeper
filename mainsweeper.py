import tkinter as tk
import math
import random
import sys

canvas = None
i = 0
k = 0
a = 0
v = -1
bom_sum = 60
canvas_num = []
bom_place = []
bom_number = []
first_click_place = []
around_click_list = []
opened_canvas = []
SQUARE_LENGTH = 30
RADIUS = SQUARE_LENGTH / 2 - 5
POSITION = {"x": 8, "y": 8}
BORDER_WIDTH = 2
NUMBER = 20 
LENGTH = SQUARE_LENGTH * NUMBER + BORDER_WIDTH * NUMBER
FIRST_LENGTH = LENGTH 

def set_field():
  canvas.create_rectangle(POSITION["x"], POSITION["y"], LENGTH  + POSITION["x"], LENGTH + POSITION["y"] , fill='#af6', width=BORDER_WIDTH )
                         
#create vertical and horizontal lines
  for i in range(NUMBER - 1):
    x = POSITION["x"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    y = POSITION["y"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    canvas.create_line(x, POSITION["y"], x, LENGTH + POSITION["y"], width=BORDER_WIDTH, fill='#000')
    canvas.create_line(POSITION["x"], y, LENGTH  + POSITION["x"], y, width=BORDER_WIDTH, fill='#000')

def set_item(kind, x, y):              
  global opened_canvas
  center_x = POSITION["x"] + BORDER_WIDTH * x + BORDER_WIDTH / 2 + SQUARE_LENGTH * x + SQUARE_LENGTH / 2
  center_y = POSITION["y"] + BORDER_WIDTH * y + BORDER_WIDTH / 2 + SQUARE_LENGTH * y + SQUARE_LENGTH / 2

#Install rectangle and red circle button
  #canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill="#fff", width=0)
  if kind != None:
    if kind == "bom":
      canvas.create_oval(center_x - RADIUS, center_y - RADIUS, center_x + RADIUS, center_y + RADIUS, fill="#f00", width=0)
    elif kind == "0" or kind == 0:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill="#fda", width=0)
    elif kind == "1" or kind == 1:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#00f")
    elif kind == "2" or kind == 2:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#0f0")
    elif kind == "3" or kind == 3:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#f00")
    elif kind == "4" or kind == 4:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#c0d")
    elif kind == "5" or kind == 5:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#fc0")
    elif kind == "6" or kind == 6:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#ed3")
    elif kind == "7" or kind == 7:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#f0f")
    elif kind == "8" or kind == 8:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#d00")
    elif kind == "F":
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#f00")
    elif kind == "end":
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill="#ccc", width=0)
    elif kind == "block":
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill="#af6", width=0)
    else:
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text",fill="#fff")

def point_to_numbers(event_x, event_y):
    x = math.floor((event_x - POSITION["x"]) / (SQUARE_LENGTH + BORDER_WIDTH))
    y = math.floor((event_y - POSITION["y"]) / (SQUARE_LENGTH + BORDER_WIDTH))
    return x, y

def create_canvas():
  root = tk.Tk()
  root.geometry(f"""{LENGTH + POSITION["x"] * 2}x{LENGTH + POSITION["y"] * 2}""")
  root.title("mainsweeper")
  canvas = tk.Canvas(root, width=(LENGTH + POSITION["x"]), height=(LENGTH + POSITION["y"]))
  canvas.place(x=0, y=0)

  return root, canvas

def canvas_place(x, y):
  canvas_place_number = x + y * 20
  return canvas_place_number

def click(event):
  global i, k, a, canvas, first_click_place, canvas_num, bom_number, opened_canvas
  x, y = point_to_numbers(event.x, event.y)
  if k < 1 :
    first_click(x, y)
    k += 1
    while i < bom_sum:
     set_bom()
     i += 1  

  
  elif k == 1 and canvas_num[ canvas_place(x,y) ] <= 8:
    for p in range(0, bom_sum):
     if bom_number[p] ==  canvas_place(x,y):
      return end_game()

  if -9 <= canvas_num[ canvas_place(x,y) ] < 0 :
    set_item( "bom", x, y ) 
  elif canvas_num[ canvas_place(x,y) ] == 0:
    around_click( x, y )
    set_item("0", x, y)
  elif canvas_num[ canvas_place(x,y) ] == 1:
    set_item( "1", x, y)
    opened_canvas.append( canvas_place(x,y) )
  elif canvas_num[ canvas_place(x,y) ] == 2:
    set_item( "2", x, y)
    opened_canvas.append( canvas_place(x,y) )
  elif canvas_num[ canvas_place(x,y) ] == 3:
    set_item( "3", x, y)
    opened_canvas.append( canvas_place(x,y) )
  elif canvas_num[ canvas_place(x,y) ] == 4:
    set_item( "4", x, y)
    opened_canvas.append( canvas_place(x,y) )
  elif canvas_num[ canvas_place(x,y) ] == 5:
    set_item( "5", x, y)
    opened_canvas.append( canvas_place(x,y) )
  elif canvas_num[ canvas_place(x,y) ] == 6:
    set_item( "6", x, y)  
    opened_canvas.append( canvas_place(x,y) )
  elif canvas_num[ canvas_place(x,y) ] == 7:
    set_item( "7", x, y)
    opened_canvas.append( canvas_place(x,y) )
  elif canvas_num[ canvas_place(x,y) ] == 8:
    set_item( "8", x, y)
    opened_canvas.append( canvas_place(x,y) )
  elif canvas_num[ canvas_place(x,y) ] >= 9:
    pass

  opened_canvas = list(dict.fromkeys(opened_canvas))
  for add in range(len(opened_canvas)):
    canvas_num[opened_canvas[add]] += 27
  if a == 0:
    print("LAST:", 400 - len(opened_canvas) - i, "squares")
  if len(opened_canvas) == 400 - i :
    print("congratulation!!")
    canvas = tk.Canvas(state = 'disable')
    retry_game()

def click2(event2):
  x, y = point_to_numbers(event2.x, event2.y)
  if canvas_num[ canvas_place(x,y) ] <= 8 :
    set_item("F", x, y)
    canvas_num[ canvas_place(x,y) ] += 18
  elif 9 <= canvas_num[ canvas_place(x,y) ] <= 26:
    set_item("block", x, y)
    canvas_num[ canvas_place(x,y) ] -= 18 

def first_click(x, y):
  global first_click_place, k
  first_click_place = [ canvas_place(x,y) ]
  if x < 19 :
    first_click_place.append( canvas_place(x+1,y) )
  if x > 0 :
    first_click_place.append( canvas_place(x-1,y) )
  if y > 0 :
    first_click_place.append( canvas_place(x,y-1) )
  if y < 19 :
    first_click_place.append( canvas_place(x,y+1) )
  if x < 19 and y < 19 :
    first_click_place.append( canvas_place(x+1,y+1) )
  if x > 0 and y < 19 :
    first_click_place.append( canvas_place(x-1,y+1) )
  if x < 19 and y > 0 :
    first_click_place.append( canvas_place(x+1,y-1) )
  if x > 0 and y > 0 :
    first_click_place.append( canvas_place(x-1,y-1) )
  
def around_click(x, y):
    global around_click_list, v, opened_canvas
    if canvas_num[ canvas_place(x,y) ] == 0:
        opened_canvas.append(canvas_place(x,y))
        if x < 19 and canvas_num[ canvas_place(x + 1,y) ] <= 8:
            set_item( canvas_num[ canvas_place(x + 1,y) ], x + 1, y )
            opened_canvas.append( canvas_place(x + 1,y) )
            if canvas_num[ canvas_place(x + 1,y) ] == 0:
              around_click_list.append( canvas_place(x + 1,y) )
        if x < 19 and y > 0 and canvas_num[ canvas_place(x + 1,y - 1) ] <= 8:
            set_item( canvas_num[ canvas_place(x + 1,y - 1) ], x + 1, y - 1 )
            opened_canvas.append( canvas_place(x + 1,y - 1) )
            if canvas_num[ canvas_place(x + 1,y - 1) ] == 0:
              around_click_list.append( canvas_place(x + 1,y - 1) )
        if x < 19 and y < 19 and canvas_num[ canvas_place(x + 1,y + 1) ] <= 8:
            set_item( canvas_num[ canvas_place(x + 1,y + 1) ], x + 1, y + 1 )
            opened_canvas.append( canvas_place(x + 1,y + 1) )
            if canvas_num[ canvas_place(x + 1,y + 1) ] == 0: 
              around_click_list.append( canvas_place(x + 1,y + 1) )
        if y < 19 and canvas_num[ canvas_place(x,y + 1) ] <= 8:
            set_item( canvas_num[ canvas_place(x,y + 1) ], x, y + 1 )
            opened_canvas.append( canvas_place(x,y + 1) )
            if canvas_num[ canvas_place(x,y + 1) ] == 0 :
              around_click_list.append( canvas_place(x,y + 1) ) 
        if y > 0 and canvas_num[ canvas_place(x,y - 1) ] <= 8:
            set_item( canvas_num[ canvas_place(x,y - 1) ], x, y - 1 )
            opened_canvas.append( canvas_place(x,y - 1) )
            if canvas_num[ canvas_place(x,y - 1) ] == 0 :
              around_click_list.append( canvas_place(x,y - 1) )
        if x > 0 and canvas_num[ canvas_place(x - 1,y) ] <= 8:
            set_item( canvas_num[ canvas_place(x - 1,y) ], x - 1, y )
            opened_canvas.append( canvas_place(x - 1,y) )
            if canvas_num[ canvas_place(x - 1,y) ] == 0 :
             around_click_list.append( canvas_place(x - 1,y) )  
        if x > 0 and y > 0 and canvas_num[ canvas_place(x - 1,y - 1) ] <= 8:
            set_item( canvas_num[ canvas_place(x - 1,y - 1) ], x - 1, y - 1 )
            opened_canvas.append( canvas_place(x - 1,y - 1) )
            if canvas_num[ canvas_place(x - 1,y - 1) ] == 0 :
              around_click_list.append( canvas_place(x - 1,y - 1) )  
        if x > 0 and y < 19 and canvas_num[ canvas_place(x - 1,y + 1) ] <= 8:
            set_item( canvas_num[ canvas_place(x - 1,y + 1) ], x - 1, y + 1 )
            opened_canvas.append( canvas_place(x - 1,y + 1) )
            if canvas_num[ canvas_place(x - 1,y + 1) ] == 0 :
              around_click_list.append( canvas_place(x - 1,y + 1) )
        v  += 1
        around_click_list = list(dict.fromkeys(around_click_list))
        opened_canvas = list(dict.fromkeys(opened_canvas))
        if v < len(around_click_list) :
          around_click(around_click_list[v] % 20, around_click_list[v] // 20)
    around_click_list.clear()
    v = -1


def set_bom():
  global bom_place, canvas_num, bom_number, first_click_place, m, n, i, d
  m = random.randint(0, 19)
  n = random.randint(0, 19)
  for c in range(0, len(first_click_place)):
    if first_click_place[c] ==  canvas_place(m,n):
      m = random.randint(0, 19)
      n = random.randint(0, 19)
    else:
      continue
  bom_place = [m, n] 
  bom_number.append( canvas_place(m,n) )
  bom_number[i] = canvas_place(m,n)
  canvas_num[ canvas_place(m,n) ] -= 9
  if m > 0 and n > 0 :
    canvas_num[ canvas_place(m-1,n-1) ] += 1
  if m > 0 and n < 19 :
    canvas_num[ canvas_place(m-1,n+1) ] += 1
  if m < 19 and n < 19 :
    canvas_num[ canvas_place(m+1,n+1) ] += 1
  if m < 19 and n > 0 :
    canvas_num[ canvas_place(m+1,n-1) ] += 1
  if m > 0 :
    canvas_num[ canvas_place(m-1,n) ] += 1
  if m < 19 :
    canvas_num[ canvas_place(m+1,n) ] += 1
  if n > 0 :
    canvas_num[ canvas_place(m,n-1) ] += 1
  if n < 19 :
   canvas_num[ canvas_place(m,n+1) ] += 1

  if i > 0:  #comfirm not to putting bom same place
    cor = 0
    e = 0
    while cor < i:
     if bom_number[i] != bom_number[cor]:
      cor += 1
     elif bom_number[i] == bom_number[cor]:
      canvas_num[ canvas_place(m,n) ] += 9
      e += 1
      if m > 0 and n > 0 :
       canvas_num[ canvas_place(m-1,n-1) ] -= 1
      if m > 0 and n < 19 :
       canvas_num[ canvas_place(m-1,n+1) ] -= 1
      if m < 19 and n < 19 :
       canvas_num[ canvas_place(m+1,n+1) ] -= 1  
      if m < 19 and n > 0 :
        canvas_num[ canvas_place(m+1,n-1) ] -= 1
      if m > 0 :
        canvas_num[ canvas_place(m-1,n) ] -= 1
      if m < 19 :
        canvas_num[ canvas_place(m+1,n) ] -= 1
      if n > 0 :
        canvas_num[ canvas_place(m,n-1) ] -= 1
      if n < 19 :
        canvas_num[ canvas_place(m,n+1) ] -= 1
 
      set_bom()

def before_set_number():
  global canvas_num
  for col in range(0,20):
    for row in range(0,20):
      ele = canvas_place(row, col)
      canvas_num.append( ele )
      canvas_num[ ele ] = 0
  return canvas_num


def end_game():
  global canvas, a
  for out in range(0, bom_sum):
    set_item("end", bom_number[out] % 20, bom_number[out] // 20)
  
  print("game_over")
  a += 1
  canvas = tk.Canvas(state = 'disable')
  retry_game()

def retry_game():
  global k, i, a
  input_message = "RETRY GAME ? (Y or N):"
  retry_answer = input(input_message)
  while not enable_retry_answer(retry_answer):
    retry_answer = input(input_message)
  if retry_answer == 'Y':
    canvas_num.clear()
    bom_place.clear()
    bom_number.clear()
    first_click_place.clear()
    opened_canvas.clear()
    k -= 1
    a -= 1
    i = 0
    play()
  elif retry_answer == 'N':
    sys.exit()

def enable_retry_answer(string):
  if string == 'Y' or string == 'N':
    return True
  else:
    return False

def play():
  global canvas, i
  root, canvas = create_canvas()
  set_field()
  before_set_number()
  canvas.bind("<Button-1>", lambda event1: click(event1))
  canvas.bind("<Button-2>", lambda event2: click2(event2))
  root.mainloop()


play()
