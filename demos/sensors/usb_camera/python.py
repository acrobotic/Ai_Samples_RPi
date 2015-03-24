#!/usr/bin/env python
import cv2

Keycode = {
  'ESCAPE' : 27,
  'SPACE'  : 32,
  'UP'     : 63232,
  'DOWN'   : 63233,
  'LEFT'   : 63234,
  'RIGHT'  : 63235,
}

def camera_save_frame(img):
  cv2.imwrite("capture.jpg",img)

def servo_up():
  pass

def servo_down():
  pass

def servo_left():
  pass

def servo_right():
  pass

cv2.namedWindow("camera",1)
capture = cv2.VideoCapture(0)

while True:
  ret, img = capture.read()
  cv2.imshow("camera",img)
  keyinput = cv2.waitKey(10)
  # not required on pcDuino Ubuntu target
  #keyinput -= 0x100000
  if keyinput == Keycode['ESCAPE']:
    break
  if keyinput == Keycode['SPACE']:
    camera_save_frame(img)

capture.release()
cv2.destroyWindow("camera")

