import tkinter as tk
import math
import random
import sys

canvas = None
i = 0
game_over_switch = 0
v = -1
launch_count = 0
bom_sum = 60
number_color = ['00f','0f0','f00','c0d','fc0','ed3','f0f','d00']
canvas_num = []
bom_place = []
bom_number = []
first_click_place = []
around_click_list = []
opened_canvas = []
flag_place = []
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
  global opened_canvas, number_color
  center_x = POSITION["x"] + BORDER_WIDTH * x + BORDER_WIDTH / 2 + SQUARE_LENGTH * x + SQUARE_LENGTH / 2
  center_y = POSITION["y"] + BORDER_WIDTH * y + BORDER_WIDTH / 2 + SQUARE_LENGTH * y + SQUARE_LENGTH / 2

#Install rectangle and red circle button
  #canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill="#fff", width=0)
  if kind != None:
    if kind == "bom":
      canvas.create_oval(center_x - RADIUS, center_y - RADIUS, center_x + RADIUS, center_y + RADIUS, fill="#f00", width=0)
    elif kind == "0" or kind == 0:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill="#fda", width=0)
    elif kind == canvas_num[ canvas_place(x, y) ]:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      for i in range(1, 9):
        if canvas_num[ canvas_place(x, y) ] != i:
          pass
        elif canvas_num[ canvas_place(x, y) ] == i:
          canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="" + "#" + number_color[i-1])
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
  global i, launch_count, game_over_switch, canvas, first_click_place, canvas_num, bom_number, opened_canvas
  x, y = point_to_numbers(event.x, event.y)
  if launch_count < 1 :
    first_click(x, y)
    launch_count += 1
    while i < bom_sum:
     set_bom()
     i += 1  

  elif launch_count == 1 and canvas_num[ canvas_place(x,y) ] <= 8 and flag_place[ canvas_place(x, y) ] == 0:
    for p in range(0, bom_sum):
     if bom_number[p] ==  canvas_place(x,y):
      return end_game()
  
  if flag_place[ canvas_place(x,y) ] == 1:
    pass
  elif flag_place[ canvas_place(x, y)] == 0:
    if -9 <= canvas_num[ canvas_place(x,y) ] < 0 :
      set_item( "bom", x, y ) 
    elif canvas_num[ canvas_place(x,y) ] == 0:
        around_click( x, y )
        set_item("0", x, y)
    elif canvas_num[ canvas_place(x,y) ] >= 1:
        set_item( canvas_num[ canvas_place(x, y)], x, y)
        opened_canvas.append( canvas_place(x,y) )

  opened_canvas = list(dict.fromkeys(opened_canvas))

  if game_over_switch == 0:
    print("LAST:", 400 - len(opened_canvas) - i, "squares")
  if len(opened_canvas) == NUMBER * NUMBER - i :
    print("congratulation!!")
    canvas = tk.Canvas(state = 'disable')
    retry_game()

def flag_click(event2):
  global flag_place 
  x, y = point_to_numbers(event2.x, event2.y)
  blocks = 0
  while blocks < len(opened_canvas):
   if canvas_place(x, y) == opened_canvas[blocks]:
    pass
    blocks += 1
   else:
    if flag_place[ canvas_place(x, y) ] == 0:
     set_item("F", x, y)
     flag_place[ canvas_place(x, y) ] += 1
     flag_place.append( canvas_place(x, y) )
    elif flag_place[ canvas_place(x, y) ] == 1:
     set_item("block", x, y)
     flag_place[ canvas_place(x, y) ] -= 1
    blocks += 1
  
def first_click(x, y):
  global first_click_place
  for i in range(-1, 2):
    for j in range(-1, 2):
      if x+j < 0 or x+j > NUMBER-1 or y+i < 0 or y+i > NUMBER-1: 
        continue
      else:
       first_click_place.append( canvas_place(x+j, y+i) )

def around_click(x, y):
    global around_click_list, v, opened_canvas
    if canvas_num[ canvas_place(x, y) ] == 0:
        opened_canvas.append(canvas_place(x, y))
        if x < 19 and flag_place[ canvas_place(x + 1, y) ] == 0:
            set_item( canvas_num[ canvas_place(x + 1, y) ], x + 1, y )
            opened_canvas.append( canvas_place(x + 1, y) )
            if canvas_num[ canvas_place(x + 1, y) ] == 0:
              around_click_list.append( canvas_place(x + 1, y) )
        if x < 19 and y > 0 and flag_place[ canvas_place(x + 1, y - 1) ] == 0:
            set_item( canvas_num[ canvas_place(x + 1, y - 1) ], x + 1, y - 1 )
            opened_canvas.append( canvas_place(x + 1, y - 1) )
            if canvas_num[ canvas_place(x + 1, y - 1) ] == 0:
              around_click_list.append( canvas_place(x + 1, y - 1) )
        if x < 19 and y < 19 and flag_place[ canvas_place(x + 1, y + 1) ] == 0:
            set_item( canvas_num[ canvas_place(x + 1, y + 1) ], x + 1, y + 1 )
            opened_canvas.append( canvas_place(x + 1, y + 1) )
            if canvas_num[ canvas_place(x + 1, y + 1) ] == 0: 
              around_click_list.append( canvas_place(x + 1, y + 1) )
        if y < 19 and flag_place[ canvas_place(x, y + 1) ] == 0:
            set_item( canvas_num[ canvas_place(x, y + 1) ], x, y + 1 )
            opened_canvas.append( canvas_place(x, y + 1) )
            if canvas_num[ canvas_place(x, y + 1) ] == 0 :
              around_click_list.append( canvas_place(x, y + 1) ) 
        if y > 0 and flag_place[ canvas_place(x, y - 1) ] == 0:
            set_item( canvas_num[ canvas_place(x, y - 1) ], x, y - 1 )
            opened_canvas.append( canvas_place(x, y - 1) )
            if canvas_num[ canvas_place(x,y - 1) ] == 0 :
              around_click_list.append( canvas_place(x,y - 1) )
        if x > 0 and flag_place[ canvas_place(x - 1, y) ] == 0:
            set_item( canvas_num[ canvas_place(x - 1, y) ], x - 1, y )
            opened_canvas.append( canvas_place(x - 1, y) )
            if canvas_num[ canvas_place(x - 1, y) ] == 0 :
             around_click_list.append( canvas_place(x - 1, y) )  
        if x > 0 and y > 0 and flag_place[ canvas_place(x - 1, y - 1) ] == 0:
            set_item( canvas_num[ canvas_place(x - 1, y - 1) ], x - 1, y - 1 )
            opened_canvas.append( canvas_place(x - 1, y - 1) )
            if canvas_num[ canvas_place(x - 1, y - 1) ] == 0 :
              around_click_list.append( canvas_place(x - 1, y - 1) )  
        if x > 0 and y < 19 and flag_place[ canvas_place(x - 1, y + 1) ] == 0:
            set_item( canvas_num[ canvas_place(x - 1, y + 1) ], x - 1, y + 1 )
            opened_canvas.append( canvas_place(x - 1, y + 1) )
            if canvas_num[ canvas_place(x - 1, y + 1) ] == 0 :
              around_click_list.append( canvas_place(x - 1, y + 1) )
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
  for p in range(-1, 2):
    for q in range(-1, 2):
      if m+q < 0 or m+q > NUMBER-1 or n+p < 0 or n+p > NUMBER-1: 
        continue
      elif q == 0 and p == 0:
        continue
      else:
        canvas_num[ canvas_place(m+q, n+p) ] += 1

  if i > 0:  #comfirm not to putting bom same place
    col = 0
    while col < i:
     if bom_number[i] != bom_number[col]:
      col += 1
     elif bom_number[i] == bom_number[col]:
      canvas_num[ canvas_place(m, n) ] += 9
      for k in range(-1, 2):
       for j in range(-1, 2):
        if m+j < 0 or m+j > NUMBER-1 or n+k < 0 or n+k > NUMBER-1: 
         continue
        elif j == 0 and k == 0:
          continue
        else:
         canvas_num[ canvas_place(m+j, n+k) ] -= 1
      set_bom()

def before_set_number():
  global canvas_num
  for col in range(0,20):
    for row in range(0,20):
      ele = canvas_place(row, col)
      canvas_num.append( ele )
      canvas_num[ ele ] = 0
  return canvas_num

def flag_set_number():
  global flag_place
  for col in range(0,20):
    for row in range(0,20):
      ele = canvas_place(row, col)
      flag_place.append( ele )
      flag_place[ ele ] = 0
  return flag_place
  

def end_game():
  global canvas, game_over_switch
  for out in range(0, bom_sum):
    set_item("end", bom_number[out] % 20, bom_number[out] // 20)
  
  print("game_over")
  game_over_switch += 1
  canvas = tk.Canvas(state = 'disable')
  retry_game()

def retry_game():
  global launch_count, i, game_over_switch
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
    flag_place.clear()
    launch_count -= 1
    game_over_switch -= 1
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
  flag_set_number()
  canvas.bind("<Button-1>", lambda event1: click(event1))
  canvas.bind("<Shift-1>", lambda event2: flag_click(event2))
  root.mainloop()


play()
