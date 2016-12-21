# wiipaddle.py
# Maanas Manoj 

import cwiid, time, Tkinter

print 'Press 1 + 2'

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print 'cant connect'
  quit()

wii.rumble = 1
time.sleep(0.5)
wii.rumble = 0

wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

root = Tkinter.Tk()
root.title('Paddle')

w = Tkinter.Canvas(root, width=500, height = 500)
w.pack()

rect = w.create_rectangle(240,245,260,255,fill='blue')

while (True):

  if(wii.state['buttons'] & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_ACC | cwiid.RPT_BTN
    check = 0
    while check == 0:
      if(wii.state['acc'][0] < 110):
        w.move(rect, -3, 0)
      elif(wii.state['acc'][0] > 140):
        w.move(rect, 3, 0)
      elif(wii.state['acc'][1] < 115):
        w.move(rect, 0, 3)
      elif(wii.state['acc'][1] > 140):
        w.move(rect, 0, -3)
      time.sleep(0.001)
      check = (wii.state['buttons'] & cwiid.BTN_HOME)
    time.sleep(0.05)
  root.update_idletasks()
  root.update()
