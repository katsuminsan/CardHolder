import machine
import led
import beep
import photoregist
import random
import time
import math

# preparation function, add button.
btn_rst = machine.Pin(0, machine.Pin.IN)
btn_ent = machine.Pin(1, machine.Pin.IN)

# power_on after count 3 seconds
led.color_set(255, 255, 255)
time.sleep_ms(3000)

light_threshold = 70
rainbow_brightness = 50
first_on = False

sec_per_loop = 500 # msec

# calc 180sec loops
three_min = int(180000 / sec_per_loop)
step = 0

while True:
    card_off = photoregist.check_light(light_threshold)
    
    if card_off:
        led.color_set(255, 0, 0)
        if first_on:
            step += 1
            if step >= three_min:
                beep.famimaloop()
                print('beep_end')
                step = 0
        else:
            beep.famimaloop()
            print('beep_end')
            
    elif not(card_off):
        first_on = True
        step = 0
        r, g, b = [random.randint(0, math.floor(255 * rainbow_brightness)) for i in range(3)]
        led.color_set(r, g, b)
        print('rainbow')
    
    time.sleep_ms(sec_per_loop) # 0.5 sec
