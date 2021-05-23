from microbit import *

def get_fahrenheit(c):
  f = (c * 9/5) + 32.0
  return f

# function to map any range of numbers to another range
def scale(value, fromMin, fromMax, toMin, toMax):
    if value > fromMax:
        value = fromMax
    if value < fromMin:
        value = fromMin
 
    fromRange = fromMax - fromMin
    toRange = toMax - toMin
    valueScaled = float(value - fromMin) / float(fromRange)
    return toMin + (valueScaled * toRange)

def value_to_led_image(c):
    v = int(c)
    n = int(v/9)
    r = v%9
    pix = ""
    for i in range(25):
      if i > 0 and i % 5 == 0:
        pix += ":"
      if i < n:
        pix += "9"
      elif i == n:
        pix +=str(r)
      else:
        pix += "0"
    return Image(pix)


while True:    
    c = temperature()
    print((c,))
    
    if button_a.is_pressed():
        f = get_fahrenheit(c)
        display.scroll(str(f) + "'F")
        
    if button_b.is_pressed():

        display.scroll(str(c) + "'C")

    ledv = scale(c, 15, 40, 0, 225)
    
    img = value_to_led_image(ledv)
    display.clear()
    display.show(img)
    sleep(300)