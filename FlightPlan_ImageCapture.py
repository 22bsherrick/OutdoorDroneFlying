from djitellopy import Tello
import time
import cv2
global img

tello = Tello()

tello.connect()
print(tello.get_battery())

tello.streamon()
frame_read = tello.get_frame_read()

#take off 6 feet
tello.takeoff()
tello.move_up(91)
time.sleep(2)

#fly forward 116 feet
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
time.sleep(2)

#turn towards cafeteria
tello.rotate_counter_clockwise(90)
time.sleep(2)

#photo
cv2.imwrite("picture.png", frame_read.frame)

#turn to library
tello.rotate_counter_clockwise(90)
sleep(2)

#fly forward 116 feet
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(2)

#move up to middle school library
tello.move_up(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(.005)
tello.move_forward(500)
sleep(2)

#take photo
cv2.imwrite("picture.png", frame_read.frame)

tello.land()
tello.end()