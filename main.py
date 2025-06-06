import random
from browser import timer 

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

set_size(SCREEN_WIDTH, SCREEN_HEIGHT)

CIRCLE_DIAMETER = 37

CIRCLE_COLOR_ONE = "green"
CIRCLE_COLOR_TWO = "blue"
CIRCLE_COLOR_THREE = "teal"
CIRCLE_COLOR_FOUR = "orange"
CIRCLE_COLOR_FIVE = "purple"
CIRCLE_COLOR_SIX = "black"
CIRCLE_COLOR_SEVEN = "maroon"
CIRCLE_COLOR_EIGHT = "red"
CIRCLE_COLOR_NINE = "pink"
CIRCLE_COLOR_TEN = "gold"


columns = SCREEN_WIDTH // CIRCLE_DIAMETER
rows = SCREEN_HEIGHT // CIRCLE_DIAMETER

excesscolumns = SCREEN_WIDTH % CIRCLE_DIAMETER
excessrows = SCREEN_HEIGHT % CIRCLE_DIAMETER

colorslist = [CIRCLE_COLOR_ONE, CIRCLE_COLOR_TWO, CIRCLE_COLOR_THREE, CIRCLE_COLOR_FOUR, CIRCLE_COLOR_FIVE, CIRCLE_COLOR_SIX, CIRCLE_COLOR_SEVEN, CIRCLE_COLOR_EIGHT, CIRCLE_COLOR_NINE, CIRCLE_COLOR_TEN]

def draw_circles():
    firstrandnum = random.randint(0,9)
    secondrandnum = random.randint(0,9)
    
    color1 = colorslist[firstrandnum]
    color2 = colorslist[secondrandnum]
    
    yposition = CIRCLE_DIAMETER / 2 + excessrows / 2
    
    for row in range(rows):
        for i in range(columns):
            circle = Circle(CIRCLE_DIAMETER / 2)
            if row % 2 == 0:
                if i % 2 == 0:
                    circle.set_color(color1)
                else:
                    circle.set_color(color2)
            else:
                if i % 2 == 0:
                    circle.set_color(color2)
                else:
                    circle.set_color(color1)
            
            circle.set_position(CIRCLE_DIAMETER * i + CIRCLE_DIAMETER / 2 + (excesscolumns / 2), yposition)
            add(circle)
        yposition += CIRCLE_DIAMETER
         
timer_id = timer.set_interval(draw_circles, 250)