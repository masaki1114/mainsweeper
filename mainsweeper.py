import tkinter as tk
import math
import random
import sys

canvas = None
bom_count = 0
game_over_switch = 0
around_open_sum = -1
launch_count = 0
clear_point = 0
bom_sum = 60
number_color = ['00f','0f0','f00','c0d','fc0','ed3','f0f','d00']
canvas_number = []
bom_place = []
bom_number = []
first_click_place = []
around_open_list = []
opened_canvas = []
add_opened_canvas = []
flag_place = []
BOM = 9
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
    elif kind == "F":
      canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="#f00")
    elif kind == canvas_number[ canvas_place(x, y) ]:
      canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill='#fda', width=0)
      for i in range(1, BOM):
        if canvas_number[ canvas_place(x, y) ] != i:
          pass
        elif canvas_number[ canvas_place(x, y) ] == i:
          canvas.create_text(center_x, center_y, text=kind, justify="center", font=("", 25), tag="count_text", fill="" + "#" + number_color[i-1])
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

def decision_clear():
  global canvas, clear_point
  print("congratulation!!")
  clear_point += 1
  canvas = tk.Canvas(state = 'disable')
  retry_game()

def canvas_place(x, y):
  canvas_place_number = x + y * NUMBER
  return canvas_place_number

def first_click_function(event):
  global bom_count, launch_count, game_over_switch, canvas_number, bom_number, flag_place
  x, y = point_to_numbers(event.x, event.y)
  if launch_count < 1 :
    first_click(x, y)
    launch_count += 1
    while bom_count < bom_sum:
     create_bom()
     bom_count += 1  

  elif launch_count == 1 and canvas_number[ canvas_place(x, y) ] < BOM and flag_place[ canvas_place(x, y) ] == 0 and game_over_switch == 0:
    for i in range(0, bom_sum):
     if bom_number[i] ==  canvas_place(x, y):
      return end_game()
  
  second_click_function(event)
  
def second_click_function(event):
  global bom_count, launch_count, game_over_switch, canvas_number, opened_canvas, flag_place, canvas, clear_point
  x, y = point_to_numbers(event.x, event.y)
  if flag_place[ canvas_place(x, y) ] == 1:
    pass
  elif flag_place[ canvas_place(x, y) ] == 0 and clear_point == 0 and game_over_switch == 0:
    if canvas_number[ canvas_place(x, y) ] < 0 :
      set_item( "bom", x, y ) 
    elif canvas_number[ canvas_place(x, y) ] == 0:
        around_open( x, y )
        set_item("0", x, y)
    elif canvas_number[ canvas_place(x,y) ] >= 1:
        set_item( canvas_number[ canvas_place(x, y)], x, y)
        opened_canvas.append( canvas_place(x, y) )

  opened_canvas = list(dict.fromkeys(opened_canvas))
  
  if game_over_switch == 0 and clear_point == 0:
    print("LAST:", NUMBER * NUMBER - len(opened_canvas) - bom_count, "squares")
  if len(opened_canvas) == NUMBER * NUMBER - bom_count and clear_point == 0:
    decision_clear()

def flag_click(event2):
  global flag_place, opened_canvas
  x, y = point_to_numbers(event2.x, event2.y)
  for i in range(0, len(opened_canvas)):
    if add_opened_canvas[ opened_canvas[i] ] != 1:
      add_opened_canvas[opened_canvas[i]] += 1
    else:
      pass

  if add_opened_canvas[ canvas_place(x, y) ] == 1:
    pass
  else:   
    if flag_place[ canvas_place(x, y) ] == 0:
     set_item("F", x, y)
     flag_place[ canvas_place(x, y) ] += 1
     flag_place.append( canvas_place(x, y) )
    elif flag_place[ canvas_place(x, y) ] == 1:
     set_item("block", x, y)
     flag_place[ canvas_place(x, y) ] -= 1
  
def first_click(x, y):
  global first_click_place
  for i in range(-1, 2):
    for j in range(-1, 2):
      if x+j < 0 or x+j > NUMBER-1 or y+i < 0 or y+i > NUMBER-1: 
        pass
      else:
       first_click_place.append( canvas_place(x+j, y+i) )

def around_open(x, y):
    global around_open_list, around_open_sum, opened_canvas
    for i in range(-1, 2):
      for j in range(-1, 2):
        if x+j < 0 or x+j > NUMBER-1 or y+i < 0 or y+i > NUMBER-1:
          pass
        else:
          if flag_place[ canvas_place(x+j, y+i) ] == 0:
            set_item( canvas_number[ canvas_place(x+j, y+i) ], x+j, y+i )
            opened_canvas.append( canvas_place(x+j, y+i) )
            if canvas_number[ canvas_place(x+j, y+i) ] == 0:
              around_open_list.append( canvas_place(x+j, y+i) )
    around_open_sum += 1
    around_open_list = list(dict.fromkeys(around_open_list))
    opened_canvas = list(dict.fromkeys(opened_canvas))
    if around_open_sum < len(around_open_list) :
      around_open(around_open_list[around_open_sum] % NUMBER, around_open_list[around_open_sum] // NUMBER)
    around_open_list.clear()
    around_open_sum = -1


def create_bom():
  global first_click_place, x_bom, y_bom
  x_bom = random.randint(0, NUMBER-1)
  y_bom = random.randint(0, NUMBER-1)
  for i in range(0, len(first_click_place)):
    if first_click_place[i] ==  canvas_place(x_bom, y_bom):
      x_bom = random.randint(0, NUMBER-1)
      y_bom = random.randint(0, NUMBER-1)
    else:
      continue
  set_bom()

def set_bom():
  global bom_place, canvas_number, bom_number, x_bom, y_bom
  bom_place = [x_bom, y_bom] 
  bom_number.append( canvas_place(x_bom, y_bom) )
  bom_number[bom_count] = canvas_place(x_bom, y_bom)
  canvas_number[ canvas_place(x_bom, y_bom) ] -= BOM
  for i in range(-1, 2):
    for j in range(-1, 2):
      if x_bom+j < 0 or x_bom+j > NUMBER-1 or y_bom+i < 0 or y_bom+i > NUMBER-1: 
        continue
      elif j == 0 and i == 0:
        continue
      else:
        canvas_number[ canvas_place(x_bom+j, y_bom+i) ] += 1
  search_bom()

def search_bom():
  if bom_count > 0:  #comfirm not to putting bom same place
    bom_check = 0
    while bom_check < bom_count:
     if bom_number[bom_count] != bom_number[bom_check]:
      bom_check += 1
     elif bom_number[bom_count] == bom_number[bom_check]:
      canvas_number[ canvas_place(x_bom, y_bom) ] += BOM
      for i in range(-1, 2):
       for j in range(-1, 2):
        if x_bom+j < 0 or x_bom+j > NUMBER-1 or y_bom+i < 0 or y_bom+i > NUMBER-1: 
         continue
        elif j == 0 and i == 0:
          continue
        else:
         canvas_number[ canvas_place(x_bom+j, y_bom+i) ] -= 1
      create_bom()

def before_set_number():
  global canvas_number
  for i in range(0,NUMBER):
    for j in range(0,NUMBER):
      element = canvas_place(j, i)
      canvas_number.append( element )
      canvas_number[ element ] = 0
  return canvas_number

def flag_set_number():
  global flag_place
  for i in range(0,NUMBER):
    for j in range(0,NUMBER):
      element = canvas_place(j, i)
      flag_place.append( element )
      flag_place[ element ] = 0
  return flag_place

def recognized_opened_canvas():
  global add_opened_canvas
  for i in range(0,NUMBER):
    for j in range(0,NUMBER):
      element = canvas_place(j, i)
      add_opened_canvas.append( element )
      add_opened_canvas[ element ] = 0
  
def end_game():
  global canvas, game_over_switch
  for i in range(0, bom_sum):
    set_item("end", bom_number[i] % NUMBER, bom_number[i] // NUMBER)
  opened_all_canvas()
  print("game_over")
  game_over_switch += 1
  canvas = tk.Canvas(state = 'disable')
  retry_game()

def opened_all_canvas():
  for i in range(0, NUMBER*NUMBER):
    if canvas_number[ i ] < 0:
      pass
    else:
      set_item(canvas_number[ i ] , i % NUMBER, i // NUMBER)


def retry_game():
  global bom_place, bom_number, first_click_place, opened_canvas, launch_count, clear_point, game_over_switch, flag_place, bom_count 
  input_message = "RETRY GAME ? (Y or N):"
  retry_answer = input(input_message)
  while not enable_retry_answer(retry_answer):
    retry_answer = input(input_message)
  if retry_answer == 'Y':
    bom_place.clear()
    bom_number.clear()
    first_click_place.clear()
    opened_canvas.clear()
    launch_count -= 1
    clear_point = 0
    game_over_switch = 0
    bom_count = 0
    play()
  elif retry_answer == 'N':
    sys.exit()

def enable_retry_answer(string):
  if string == 'Y' or string == 'N':
    return True
  else:
    return False

def play():
  global canvas
  root, canvas = create_canvas()
  set_field()
  before_set_number()
  flag_set_number()
  recognized_opened_canvas()
  canvas.bind("<Button-1>", lambda event1: first_click_function(event1))
  canvas.bind("<Shift-1>", lambda event2: flag_click(event2))
  root.mainloop()


play()
