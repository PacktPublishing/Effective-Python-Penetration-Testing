from PIL import ImageGrab
import time

time.sleep(5)
ImageGrab.grab(bbox=(10,10,510,510)).save("screen_capture.png", "png")
