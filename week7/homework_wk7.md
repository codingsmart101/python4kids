# Homework for Week 7

We have two tasks for this week - week 7. 


## Task 1 – A security monitor with radio alarm

### Software Requirement

* Design a remote security system that monitors surrounding activities. 
* Micro:bit has a sound sensor that can detect if some motion occurs.
* As a challenge, you can optionally have an accelerator to detect if there is any movement.
* One micro:bit acts as a sensor, which activates acceleration sensor and microphone. Once it detects some motion, or sound. It should send a message to another micro:bit via radio.
* The receiver micro:bit will sound beep to the alarm, and display some message on LED.  

### Instructions

Note: this homework task revisits what we have covered in the previous weeks about sensors, you can have a review from these websites:

* [micro:bit website](https://microbit.org/get-started/first-steps/sensors/)
* [Micropython for micro:bit](https://microbit-micropython.readthedocs.io/en/v2-docs/)
* [Microphone](https://microbit-micropython.readthedocs.io/en/v2-docs/microphone.html?highlight=sound#sound-events)

You can have one micro:bit function as transmitter, and functions as a monitor, listening to the surroundings. If the sound level is higher than some value, it should trigger sending a message to the radio receiver.

The code could be like this:

```python

alarm = False

while True:
    # ignore first sound level reading
    soundLevel = microphone.sound_level()

    if soundLevel > 50: # set up this threshold per your preference. 
        alarm = True
        radio.send("alarm")

    if soundLevel < 30: # Question, why I set 30 there as the lower threshold? 
        alarm = False
        radio.send("clear")

    sleep(1000) # check every one second. 
```

You can have a test with this code( plus your setup code for radio as we have done in the class.). Think about what you can improve?

* Well, your surroundings maybe quite noisy in the day time, and being quiet at night, and your monitor has to detect abnormal noices. How could you do that? Hint: we learned about the average value in the class, could you levage it to improve your monitor function?
* The above code checks the sound level every one second. Is it frequent enough? in other words, is it sentitive enough to detect any suspicious activities?
* To solve the above problem, you may shorten the time of "sleep", to make the loop go faster. As a result, it will keep sending the radio more frequently, thus the monitor will consume a lot of battery. A new issue! Could you solve it? Hint you may need a solution so that if the alarm has been sent, then stop sending a repeat alarm? Same case for the clear message. 

Using accelerometer is a challenge part of this task. However, it is similar to sound detection. Read the [document](https://microbit-micropython.readthedocs.io/en/v2-docs/accelerometer.html?highlight=accelerometer) to learn how to use x,y,z value from accelerometer. We will have in-depth discussion in the next class.

#### Manage the radio sender and receiver

Maybe it's easier for now to keep both radio send and receive, as long as your code is manageable. To make things easier, try to use a `global variable` called `I_AM_TX` to indicate the role of radio. I post example code here: 

```python

# indicating I'm the transimitter.
I_AM_TX = True

while True:
    if I_AM_TX:
        
        c = temperature()

        # print the reading and view on plotter/REPL for debugging.
        print((c,))
        radio.send(str(c))
        sleep(1000)

    else:
        # the receiver do the following:
        c = radio.receive()
        if c is not None:
            print((c,))
            display.scroll(c)
        sleep(200)
```

## Task 1 - Prepare for the next class

As we learned radio, now we can make a lot more things using micro:bit. We can have one micro:bit attached to a moving object and read sensor data from it.
This [video](https://www.youtube.com/watch?v=2XXqs2T5mZ4) is an example, and [this one](https://www.youtube.com/watch?v=dlu5OfKmZY8) as well. We will do a similar experiment next week. 

You will have to prepare a little car (or any vehicle) that can carry your micro:bit (with battery). We will see how to get sensor data from your car. It could be made from lego parts, or wooden pieces, or cardboard. 


