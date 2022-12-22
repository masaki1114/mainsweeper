import tkinter as tk
import math
import random

canvas = None
i = 0
k = 0
c = 0
d = 0
s = 0
v = -1
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
  global num, opened_canvas
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

def click(event):
  global i, k, first_click_place, canvas_num, bom_number, opened_canvas
  x, y = point_to_numbers(event.x, event.y)
  if k < 1 :
    first_click(x, y)
    k += 1
    while i < 60:
     set_bom()
     i += 1  

  elif k == 1 :
    for p in range(0, d):
     if bom_number[p] == x + y * 20 :
      return end_game()
  
  
  if -9 <= canvas_num[ x + y * 20 ] < 0 :
    set_item( "bom", x, y ) 
  elif canvas_num[ x + y * 20 ] == 0:
    around_click( x, y )
    set_item("0", x, y)
  elif canvas_num[ x + y * 20 ] == 1:
    set_item( "1", x, y)
    opened_canvas.append( x + y * 20 )
  elif canvas_num[ x + y * 20 ] == 2:
    set_item( "2", x, y)
    opened_canvas.append( x + y * 20 )
  elif canvas_num[ x + y * 20 ] == 3:
    set_item( "3", x, y)
    opened_canvas.append( x + y * 20 )
  elif canvas_num[ x + y * 20 ] == 4:
    set_item( "4", x, y)
    opened_canvas.append( x + y * 20 )
  elif canvas_num[ x + y * 20 ] == 5:
    set_item( "5", x, y)
    opened_canvas.append( x + y * 20 )
  elif canvas_num[ x + y * 20 ] == 6:
    set_item( "6", x, y)  
    opened_canvas.append( x + y * 20 )
  elif canvas_num[ x + y * 20 ] == 7:
    set_item( "7", x, y)
    opened_canvas.append( x + y * 20 )
  elif canvas_num[ x + y * 20 ] == 8:
    set_item( "8", x, y)
    opened_canvas.append( x + y * 20 )

  opened_canvas = list(dict.fromkeys(opened_canvas))

  print("LAST:", 400 - len(opened_canvas) - i - 1, "squares")
  if len(opened_canvas) == 400 - i - 1  :
    print("congratulation!!")

def click2(event):
  x, y = point_to_numbers(event.x, event.y)

  set_item("F", x, y)


def first_click(x, y):
  global first_click_place, d, k
  u = x + y * 20
  first_click_place = [ u ]
  if x < 19 :
    first_click_place.append( u + 1 )
  if x > 0 :
    first_click_place.append( u - 1 )
  if y > 0 :
    first_click_place.append( u - 20 )
  if y < 19 :
    first_click_place.append( u + 20 )
  if x < 19 and y < 19 :
    first_click_place.append( u + 21 )
  if x > 0 and y < 19 :
    first_click_place.append( u + 19 )
  if x < 19 and y > 0 :
    first_click_place.append( u - 19 )
  if x > 0 and y > 0 :
    first_click_place.append( u - 21 )

def around_click(x, y):
    global around_click_list, v, opened_canvas
    num = x + y * 20
    if canvas_num[x + y * 20] == 0:
        opened_canvas.append(num)
        if x < 19 :
            set_item( canvas_num[ x + y * 20 + 1 ], x + 1, y )
            opened_canvas.append(num + 1)
            if canvas_num[ x + y * 20 + 1 ] == 0 :
              around_click_list.append(num + 1)
        if x < 19 and y > 0 :
            set_item( canvas_num[ x + (y - 1) * 20 + 1 ], x + 1, y - 1 )
            opened_canvas.append(num - 19)
            if canvas_num[ x + (y - 1) * 20 + 1 ] == 0 :
              around_click_list.append(num - 19)
        if x < 19 and y < 19 :
            set_item( canvas_num[ x + (y + 1) * 20 + 1 ], x + 1, y + 1 )
            opened_canvas.append(num + 21)
            if canvas_num[ x + (y + 1) * 20 + 1 ] == 0 : 
              around_click_list.append(num + 21)
        if y < 19 :
            set_item( canvas_num[ x + (y + 1) * 20 ], x, y + 1 )
            opened_canvas.append(num + 20)
            if canvas_num[ x + (y + 1) * 20 ] == 0 :
              around_click_list.append(num + 20) 
        if y > 0:
            set_item( canvas_num[ x + (y - 1) * 20 ], x, y - 1 )
            opened_canvas.append(num - 20)
            if canvas_num[ x + (y - 1) * 20 ] == 0 :
              around_click_list.append(num - 20)
        if x > 0 :
            set_item( canvas_num[ x + y * 20 - 1 ], x - 1, y )
            opened_canvas.append(num - 1)
            if canvas_num[ x + y * 20 - 1 ] == 0 :
             around_click_list.append(num - 1)  
        if x > 0 and y > 0 :
            set_item( canvas_num[ x + (y - 1) * 20 - 1 ], x - 1, y - 1 )
            opened_canvas.append(num - 21)
            if canvas_num[ x + (y - 1) * 20 - 1 ] == 0 :
              around_click_list.append(num - 21)  
        if x > 0 and y < 19 :
            set_item( canvas_num[ x + (y + 1) * 20 - 1 ], x - 1, y + 1 )
            opened_canvas.append(num + 19)
            if canvas_num[ x + (y + 1) * 20 - 1 ] == 0 :
              around_click_list.append(num + 19)
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
    if first_click_place[c] == m + n * 20 :
      m = random.randint(0, 19)
      n = random.randint(0, 19)
    else:
      continue
  bom_place = [m, n] 
  num = m + n * 20
  bom_number.append( num )
  bom_number[i] = num 
  d += 1
  canvas_num[ m + n * 20 ] -= 9
  if m > 0 and n > 0 :
    canvas_num[ m - 1 + (n - 1) * 20 ] += 1
  if m > 0 and n < 19 :
    canvas_num[ m - 1 + (n + 1) * 20 ] += 1
  if m < 19 and n < 19 :
    canvas_num[ m + 1 + (n + 1) * 20 ] += 1
  if m < 19 and n > 0 :
    canvas_num[ m + 1 + (n - 1) * 20 ] += 1
  if m > 0 :
    canvas_num[ m - 1 + n * 20 ] += 1
  if m < 19 :
    canvas_num[ m + 1 + n * 20 ] += 1
  if n > 0 :
    canvas_num[ m + (n - 1) * 20 ] += 1
  if n < 19 :
   canvas_num[ m + (n + 1) * 20 ] += 1

  if i > 0:  #comfirm not to putting bom same place
    cor = 0
    e = 0
    while cor < i:
     if bom_number[i] != bom_number[cor]:
      cor += 1
     elif bom_number[i] == bom_number[cor]:
      canvas_num[ m + n * 20 ] += 9
      e += 1
      if m > 0 and n > 0 :
       canvas_num[ m - 1 + (n - 1) * 20 ] -= 1
      if m > 0 and n < 19 :
       canvas_num[ m - 1 + (n + 1) * 20 ] -= 1
      if m < 19 and n < 19 :
       canvas_num[ m + 1 + (n + 1) * 20 ] -= 1  
      if m < 19 and n > 0 :
        canvas_num[ m + 1 + (n - 1) * 20 ] -= 1
      if m > 0 :
        canvas_num[ m - 1 + n * 20 ] -= 1
      if m < 19 :
        canvas_num[ m + 1 + n * 20 ] -= 1
      if n > 0 :
        canvas_num[ m + (n - 1) * 20 ] -= 1
      if n < 19 :
        canvas_num[ m + (n + 1) * 20 ] -= 1
 
      set_bom()

def before_set_number():
  global canvas_num
  for col in range(0,20):
    for row in range(0,20):
      ele = row + col * 20
      canvas_num.append( ele )
      canvas_num[ ele ] = 0
  return canvas_num


def end_game():
  for out in range(0, 60):
    set_item("end", bom_number[out] % 20, bom_number[out] // 20)
  
  print("game_over")
  #display end game message in the center of monitor
  #label = tk.label(root, text="GAME OVER")
  #labal.pack(anchor='center',expand=1)
  #root.mainroop

def play():
  global canvas, i
  root, canvas = create_canvas()
  set_field()
  before_set_number()
  canvas.bind("<Button-1>", lambda event1: click(event1))
  canvas.bind("<Button-2>", lambda event2: click2(event2))
  root.mainloop()


play()
