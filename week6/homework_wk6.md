# Homework for Week 6

## Task – Temperature Monitor

### Software Requirement

* Build a temperature monitor device which can track max temperature, min temperature and average temperature.
* When button_a is pressed, LED display scrolls these min/max/average values.
* When you press button b, you start a new monitoring session, so that the previous min/max/average values are cleared.
* Add an alarm feature, when the monitor detects a high temperature ( > 70’C ). So that micro:bit can help people avoid getting burned.

### Instruction

Note: Micro:bit can could be damaged by water and high temperature ( over 120’C), please take care of your micro:bit when you do your experiment. Never put the micro:bit in water, or bake it in oven.

#### How to calculate Mim/Max?

After button_a is pressed, a new "session" of measurement starts. So the temperature variable `celsius` kept updates, and you should compare it with a `max_celsius` value. If any new temperature reading `celsius` is greater than `max_celsius`, then the `max_celsius` should be updated. Here is the example code that may help you: 

```python

while True:
    celsius = temperature()
    if button_b.is_pressed():
        # start a new session. 
        # initially, the max value equals the first reading. 
        max_celsius = celsius

    if celsius > max_celsius:
        max_celsius = celsius

    if button_a.is_pressed():
        # show the max value: 
        display.scroll("MAX: " + str(max_celsius) + "'C")

```

I will leave you to solve the `min` and `average`, which shares similar logic. 

 * Send me your solution via email: codingsmart101@gmail.com


#### Other Reference Code

I did a function called `value_to_led_image` that maps the temperature value to LED pixels. You can find it in the source code [`themometer.py`](themometer.py). Now you can use the new tool `mu` we introduced in this class to test and flash the code to micro:bit. After flash, you can click `plot` to view the temperature value plot. Test your themometer close to a room heater and see the measurement and LED glows and dims. Feel free to change the code and test your own ideas. You can share it in the class next week.

To understand how the code works, and learn to use LED matrix to indicate temperature values, see [this document](https://microbit-challenges.readthedocs.io/en/latest/tutorials/display.html#advanced-functions)
