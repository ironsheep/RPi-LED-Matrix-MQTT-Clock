import random
import board
import adafruit_dotstar as dotstar

panelWidth = 40
panelHeight = 10
dotCount = panelWidth * panelHeight

dots = dotstar.DotStar(
        board.SCK,
        board.MOSI,
        dotCount,
        auto_write=False,
        brightness=0.01
        )


for x in range(0, 400):
    dots[x] = (0, 0, 0)

dots[0] = (255,255,255)
dots[79] = (255,255,255)
#for x in range(0, dotCount):
    #if (x) % panelWidth == 0:
        #dots[x] = (255, 255, 255)
    #else:
        #dots[x] = (0, 0, 0)

dots.show()
