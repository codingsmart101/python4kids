# Solution for wk4 homework


```python

from microbit import *
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

def display_show_graph(level):
    # set of images for simple bar chart
    graph5 = Image("99999:"
                "99999:"
                "99999:"
                "99999:"
                "99999")

    graph4 = Image("00000:"
                "99999:"
                "99999:"
                "99999:"
                "99999")

    graph3 = Image("00000:"
                "00000:"
                "99999:"
                "99999:"
                "99999")

    graph2 = Image("00000:"
                "00000:"
                "00000:"
                "99999:"
                "99999")

    graph1 = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "99999")
                
    graph0 = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")

    allGraphs = [graph0, graph1, graph2, graph3, graph4, graph5]
    graph_id = int(level)
    display.show(allGraphs[graph_id])
    


# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

start_time = 0
diff_time = 0

while True:
    if button_a.was_pressed():
        start_time = 0
        diff_time = 0
        display.clear()
    # map sound levels from range 0-255 to range 0-5 for choosing graph image
    soundLevel = microphone.sound_level()
    print(soundLevel)
    if soundLevel > 20:
        if start_time == 0:
            start_time = running_time()
            print(running_time())
    if soundLevel < 2:
        if start_time != 0 and diff_time == 0:
            diff_time = running_time() - start_time
            print("diff time = ", diff_time)
            display.show(int(diff_time/1000))
            # end of game
            
    graph_level = scale(soundLevel, 0, 30, 0, 5)
    
    if diff_time == 0:
        display_show_graph(graph_level)

```