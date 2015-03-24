#!/usr/bin/env python
import cv2

Keycode = {
  'ESCAPE' : 27,
  'SPACE'  : 32,
}

def camera_save_frame(img):
  cv2.imwrite("capture.jpg",img)

cv2.namedWindow("camera",1)
capture = cv2.VideoCapture(0)

while True:
  ret, img = capture.read()
  cv2.imshow("camera",img)
  keyinput = cv2.waitKey(10) & 0xFF
  if keyinput == Keycode['ESCAPE']:
    break
  if keyinput == Keycode['SPACE']:
    camera_save_frame(img)

capture.release()
cv2.destroyWindow("camera")

