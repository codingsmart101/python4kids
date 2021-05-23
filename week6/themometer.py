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

def value_to_led_image(v):
    '''
    This function converts a float value to a Micro:bit Image. 
    The Micro:bit has 5 x 5 LEDs, and each LED has strength of illumination
    from 0 - 9. 
    The display will operate like this: 
    * The top left corner indicates the smallest value close to 0. 
    * When v increase, the led on the first row will turn on from left to right. 
    * then the second row, and on..
    * when value reaches (5 * 5 * 9 = 225), all the five rows are on.
    you can have a test by code like this: 

    while True:
        for i in range(0, 225):
            display.show(value_to_led_image(i))
            sleep(50)

    '''
    
    if v > 225: # limit the input value 
        v = 225 

    v = int(v) # convert to integer
    n = int(v/9)
    r = v%9

    pix = ""  # pix store the image string.
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
    
    # map tempearture 0 - 50'C to value of 0 - 225 for display. 
    ledv = scale(c, 0, 50, 0, 225)

    # at 0'C, no led is on, at 50'C all five row LEDs are on. at 30'C 
    # three rows are on. 
    # change the parameters of scale function for a different map.
    img = value_to_led_image(ledv)
    display.clear()
    display.show(img)
    sleep(300)