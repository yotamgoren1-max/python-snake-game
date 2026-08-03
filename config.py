#colors settings:
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#screen settings:
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 20  #set the pixel size

#clock settings: 5 leve, for every 5 apples boost the speed by 3 FPS
INITIAL_FPS=8
MAX_FPS=20
APPLES_PER_LEVEL=5
SPEED_BOOST_PER_LEVEL=3

# directions
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)