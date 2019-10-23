from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview(fullscreen=False, window = (100, 20, 200, 200))
g = input("click any button : ") 
for i in range(6):
   camera.capture(str(i)+'.jpg')
camera.stop_preview()
