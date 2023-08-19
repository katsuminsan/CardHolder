import led
import beep
import photoregist
import random
import time
import math

# power_on after count 3 seconds
led.color_set(255, 255, 255)
time.sleep_ms(2000)

light_threshold = 70
rainbow_brightness = 50

while True:
    card_on = photoregist.check_light(light_threshold)
    if card_on:
        led.color_set(255, 0, 0)
        beep.famimaloop()
        print('beep_end')
    elif not(card_on):
        r = random.randint(0, math.floor(255 * rainbow_brightness))
        g = random.randint(0, math.floor(255 * rainbow_brightness))
        b = random.randint(0, math.floor(255 * rainbow_brightness))
        led.color_set(r, g, b)
        print('rainbow')
    time.sleep_ms(500)