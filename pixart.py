from pixart_start import *
import turtle 
turtle.speed(0)

def get_color(character : str):
    """returns the colours name corresponding to the colours value"""

    colarr = ['black', 'white', 'red', 'yellow', 'orange', 'green', 'yellowgreen', 'sienna', 'tan', 'gray', 'darkgray']
    if character.isdigit():

        if int(character) <= len(colarr) - 1:
            return colarr[int(character)]
        
    elif character == 'A':
        return colarr[10]
    
    return None

def draw_color_pixel(color, turta):
    """creates a square pixel with colour"""
    turta.fillcolor(color)
    turta.begin_fill()

    for i in range(5):
        turta.forward(PIXEL_SIZE)
        turta.left(90)
        

    #turta.left(90)
    #turta.forward(50)
    #turta.left(90)
    #turta.forward(50)
    turta.right(90)
    turta.end_fill()


def draw_pixel(color_string, turta):
    """fetches the colour's name and the calls the draw pixel function"""

    color = get_color(color_string)
    draw_color_pixel(color, turta)


def draw_line_string(color_string, turta):
    """for every corresponding colour given in -draw_pixel- it draws one pixel """

    for color_code in color_string:
        draw_pixel(color_code, turta)
    


def draw_shape_from_string(turta):
    """It asks the user to input the colour-code and if the colour-code is valid 
    it will draw a pxel with the corresponding colour if the colour is invalid then 
    the loop will break."""


    colarr = '0123456789A'

    while True:

        turta.pendown()
        x, y = turta.xcor(), turta.ycor()
        color_string = input('Enter a color string: ')

        if False in [i in colarr for i in color_string]:
            break

        draw_line_string(color_string, turta)
        
        turta.penup()
        turta.goto(x, y - 50)
    

def draw_grid(turta):
    """Function to draw black and red checkboard"""

    x = turta.xcor()
    for i in range(10):
        turta.pendown()
        y =  turta.ycor()
        draw_line_string("02020202020202020202",turta)
        turta.penup()
        turta.goto(x, y - 30)
        draw_line_string("20202020202020202020",turta)
        turta.pendown()
        y =  turta.ycor()
        turta.penup()
        turta.goto(x, y - 30)
    
def draw_shape_from_file(turta):
    """Function to take colour-code order from the user inputted file and to then draw the corresponding image"""
    
    text_file_name = input("Enter the path of the file that you want to read its content: ")
    file = open(text_file_name)
    x = turta.xcor()
    for line in file:
        turta.pendown()
        y =  turta.ycor()
        l = line.strip()
        draw_line_string(l,turta)
        turta.penup()
        turta.goto(x, y - 30)
    file.close()

    



turta = turtle.Turtle()
initialization(turta)