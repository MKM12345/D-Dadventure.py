import pgzrun

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

pgzrun.go()

HEIGHT = GRID_HEIGHT * GRID_SIZE
def screen_chords:
  return (x * GRID_SIZE, y * GRID_SIZE)
def draw_background():
  for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
      screen.blit("floor1", screen_chords(x,y))
      
def draw():
  draw_background()
pgzrun.go()
HEIGHT = GRID_HEIGHT * GRID_SIZE
# Create the map
MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W  KG       W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W      P       W",
       "W              W",
       "W  WWWWWWWWWW  W",
       "W      GK   W  W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW",]
            screen.blit("floor1", screen_chords(x,y))
def draw_scenery():
    for y in range(GRID_HEIGHT):
      for x in range(GRID_WIDTH):
        square = MAP[y] [x]
        if square == "W":
