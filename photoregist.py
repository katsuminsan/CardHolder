import machine


photoresistor = machine.ADC(28)

def check_light(threshold=50):
    light_value  = int(((65535 - photoresistor.read_u16()) / 65535) * 100)
    
    rtn = False
    if light_value >= threshold:
        rtn = True
    print(f'light_value: {photoresistor.read_u16()}')
    print(f'light: {str(light_value)} %')
    print(f'chk_boolean is {str(rtn)}')
    return rtn

