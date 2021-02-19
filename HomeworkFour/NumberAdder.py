from graphics import *

#Init graphics window
win = GraphWin("Number Addition",500,500)
win.setCoords(0,0,20,20)

percentage = 0
sum = 0
product = 0
number_one_entry,number_two_entry,number_three_entry = None,None,None

def main():    

  init_window()

  while(True):
      click_event = win.getMouse()

      mouse_x = click_event.getX()
      mouse_y = click_event.getY()

      if (mouse_y >= 3 and mouse_y <= 5 and mouse_x >= 3 and mouse_x <= 7):
        calculate_vals()
      elif (mouse_y >= 3 and mouse_y <= 5 and mouse_x >= 13 and mouse_x <= 17):
        clear_window()
      else:
        print("Bad Click")

def init_window():
   #Define Alignment Values
  label_alignment_x = 5
  label_alignment_y = 19
  center_alignment_x = 10
  entry_alignment_x = 15
  entry_alignment_y = 17
  entry_width = 5
  button_alignment_y = 3

  
  #win = GraphWin("Number Addition",500,500,autoflush=False)
  #win.setCoords(0,0,20,20)

  #Init prompts
  welcome_prompt = Text(Point(center_alignment_x,label_alignment_y),"Welcome!\nI can add three numbers for you")
  number_one_prompt = Text(Point(label_alignment_x,label_alignment_y-2),  "Enter number one:")
  number_two_prompt = Text(Point(label_alignment_x,label_alignment_y-4),  "Enter number two:")
  number_three_prompt = Text(Point(label_alignment_x,label_alignment_y-6),"Enter number three:")
  percentage_prompt = Text(Point(label_alignment_x,label_alignment_y-8),"Percentage: ")
  output_sum = Text(Point(label_alignment_x,label_alignment_y-10),"The sum:")
  output_product = Text(Point(label_alignment_x,label_alignment_y-12),"The product:")


  #Init Entries
  number_one_entry = Entry(Point(entry_alignment_x,entry_alignment_y),entry_width)
  number_two_entry = Entry(Point(entry_alignment_x,entry_alignment_y-2),entry_width)
  number_three_entry = Entry(Point(entry_alignment_x,entry_alignment_y-4),entry_width)
  percentage_display = Text(Point(entry_alignment_x,entry_alignment_y-6),percentage)
  sum_display = Text(Point(entry_alignment_x,entry_alignment_y-8),sum)
  product_display = Text(Point(entry_alignment_x,entry_alignment_y-10),product)

  #Init Buttons
  calculate_rectangle = Rectangle(Point(label_alignment_x-2,button_alignment_y), Point(label_alignment_x+2,button_alignment_y+2))
  reset_rectangle = Rectangle(Point(entry_alignment_x-2,button_alignment_y), Point(entry_alignment_x+2,button_alignment_y+2))
  calculate_rectangle.setFill("gray")
  reset_rectangle.setFill("gray")
  calculate_button = Text(calculate_rectangle.getCenter(),"Calculate")
  reset_button = Text(reset_rectangle.getCenter(),"Reset")

  #Draw window
  welcome_prompt.draw(win) 
  number_one_prompt.draw(win)
  number_one_entry.draw(win)
  number_two_prompt.draw(win)
  number_two_entry.draw(win)
  number_three_prompt.draw(win)
  number_three_entry.draw(win)
  percentage_prompt.draw(win)
  output_sum.draw(win)
  output_product.draw(win)
  calculate_rectangle.draw(win)
  reset_rectangle.draw(win)
  calculate_button.draw(win)
  reset_button.draw(win)
def calculate_vals():
  percentage = 100
  sum = 100
  product = 100
def clear_window():
  percentage = 0 
  sum = 0
  product = 0

main()
