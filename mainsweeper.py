import tkinter as tk
import math
import random
import sys

canvas = None
bom_count = 0
around_open_sum = -1
launch_judgement = False
playing_judgement = False
bom_sum = 60
number_color = ['00f','0f0','f00','c0d','fc0','ed3','f0f','d00']
canvas_number = []
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
  global canvas, playing_judgement 
  print("congratulation!!")
  playing_judgement += 1
  canvas = tk.Canvas(state = 'disable')
  retry_game()

def canvas_place(x, y):
  canvas_place_number = x + y * NUMBER
  return canvas_place_number

def first_click_function(event):
  global launch_judgement, canvas_number, bom_number, flag_place, playing_judgement
  x, y = point_to_numbers(event.x, event.y)
  if launch_judgement == False :
    first_click(x, y)
    launch_judgement += 1
    create_bom()

  elif launch_judgement == True and canvas_number[ canvas_place(x, y) ] == BOM and flag_place[ canvas_place(x, y) ] == False and playing_judgement == False: 
    for i in range(0, bom_sum):
     if bom_number[i] ==  canvas_place(x, y):
      return end_game(bom_number)
  
  second_click_function(event)
  
def second_click_function(event):
  global bom_count, playing_judgement, canvas_number, opened_canvas, flag_place
  x, y = point_to_numbers(event.x, event.y)
  if flag_place[ canvas_place(x, y) ] == True:
    pass
  elif playing_judgement == False: 
    if canvas_number[ canvas_place(x, y) ] == 9:
      set_item( "bom", x, y ) 
    elif canvas_number[ canvas_place(x, y) ] == 0:
        around_open( x, y )
        set_item("0", x, y)
    elif 1 <= canvas_number[ canvas_place(x,y) ] <= 8:
        set_item( canvas_number[ canvas_place(x, y)], x, y)
        opened_canvas.append( canvas_place(x, y) )

  opened_canvas = list(dict.fromkeys(opened_canvas))
  in_game_message(bom_count, opened_canvas)
 
def in_game_message(bom_count, opened_canvas):
  global playing_judgement
  if playing_judgement == False: 
    print("LAST:", NUMBER * NUMBER - len(opened_canvas) - bom_count, "squares")
  if len(opened_canvas) == NUMBER * NUMBER - bom_count and playing_judgement == False: 
    decision_clear()

def flag_click(event2):
  global flag_place, opened_canvas
  x, y = point_to_numbers(event2.x, event2.y)
  for i in range(0, len(opened_canvas)):
    if add_opened_canvas[ opened_canvas[i] ] != True:
      add_opened_canvas[opened_canvas[i]] += 1
    else:
      pass

  if add_opened_canvas[ canvas_place(x, y) ] == True:
    pass
  else:   
    if flag_place[ canvas_place(x, y) ] == False:
     set_item("F", x, y)
     flag_place[ canvas_place(x, y) ] += 1
     flag_place.append( canvas_place(x, y) )
    elif flag_place[ canvas_place(x, y) ] == True:
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
          if flag_place[ canvas_place(x+j, y+i) ] == False:
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
  global first_click_place, bom_count, bom_sum
  while bom_sum > bom_count:
   x_bom = random.randint(0, NUMBER-1)
   y_bom = random.randint(0, NUMBER-1)
   detect_double_bom_1(x_bom, y_bom)
   bom_count += 1
  detect_double_bom_2()

def detect_double_bom_1(x_bom, y_bom):
  global first_click_place
  for i in range(0, len(first_click_place)):
    if first_click_place[i] == canvas_place(x_bom, y_bom):
     x_bom = random.randint(0, NUMBER-1)
     y_bom = random.randint(0, NUMBER-1)
     detect_double_bom_1(x_bom, y_bom)
    else:
      continue
  bom_number.append( canvas_place(x_bom, y_bom) )

def detect_double_bom_2():
  global bom_count, bom_number
  bom_number = list(dict.fromkeys(bom_number))
  if len(bom_number) != bom_sum:
    bom_count = len(bom_number)
    create_bom()
  else:
    put_numbers_in_all_squares(bom_number)

def put_numbers_in_all_squares(bom_number):
  global canvas_number
  for l in range(0, len(bom_number)):
   canvas_number[ bom_number[l] ] = BOM
   for i in range(-1, 2):
    for j in range(-1, 2):
      if bom_number[l]%NUMBER+j < 0 or bom_number[l]%NUMBER+j > NUMBER-1 or bom_number[l]//NUMBER+i < 0 or bom_number[l]//NUMBER+i > NUMBER-1: 
        continue
      elif j == 0 and i == 0:
        continue
      elif canvas_number[ canvas_place(bom_number[l]%NUMBER+j, bom_number[l]//NUMBER+i) ] < BOM:
        canvas_number[ canvas_place(bom_number[l]%NUMBER+j, bom_number[l]//NUMBER+i) ] += 1

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
      add_opened_canvas[ element ] = False
  
def end_game(bom_number):
  global canvas, playing_judgement
  for i in range(0, len(bom_number)):
    set_item("end", bom_number[i] % NUMBER, bom_number[i] // NUMBER)
  opened_all_canvas()
  print("game_over")
  playing_judgement += 1
  canvas = tk.Canvas(state = 'disable')
  retry_game()

def opened_all_canvas():
  for i in range(0, NUMBER*NUMBER):
    if canvas_number[ i ] == 9:
      pass
    else:
      set_item(canvas_number[ i ] , i % NUMBER, i // NUMBER)


def retry_game():
  input_message = "RETRY GAME ? (Y or N):"
  retry_answer = input(input_message)
  while not enable_retry_answer(retry_answer):
    retry_answer = input(input_message)
  if retry_answer == 'Y':
    clear_function()
    play()
  elif retry_answer == 'N':
    sys.exit()

def enable_retry_answer(string):
  if string == 'Y' or string == 'N':
    return True
  else:
    return False
  
def clear_function():
  global canvas_number, bom_number, first_click_place, opened_canvas, add_opened_canvas, flag_place, launch_judgement, playing_judgement, bom_count
  canvas_number.clear()
  bom_number.clear()
  first_click_place.clear()
  opened_canvas.clear()
  add_opened_canvas.clear()
  flag_place.clear()
  launch_judgement = False
  playing_judgement = False
  bom_count = 0
  around_open_sum == -1

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
