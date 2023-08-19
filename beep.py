import machine
import time
import Melody

# 事前定義
ml = Melody.MelodyLine(144)
buzzer = machine.PWM(machine.Pin(15))

# 関数
def pasbuzzer(pwm_pin,frequency,duration):
    if frequency > 0:
        pwm_pin.freq(frequency)
        pwm_pin.duty_u16(30000)
    else:
        pwm_pin.freq(999)
        pwm_pin.duty_u16(0)
    time.sleep_ms(duration)
    pwm_pin.duty_u16(0)

# 楽譜
# 見にくいので4音符ずつで区切っている

scores_famima = [
                [
                        ('ファ#4', (1,8)),
                        ('レ4', (1,8)),
                        ('ラ3', (1,8)),
                        ('レ4', (1,8)),
                        ('ミ4', (1,8)),
                        ('ラ4', (1,4)),
                        ('0', (1,8))
                ],
                [
                        ('ラ3', (1,8)),
                        ('ミ4', (1,8)),
                        ('ファ#4', (1,8)),
                        ('ミ4', (1,8)),
                        ('ラ3', (1,8)),
                        ('レ4', (1,4)),
                        ('0', (1,8))
                ]
        ]

# 楽譜ループで回して鳴らす
def famimaloop():
    scores_famima = [
            [
                    ('ファ#4', (1,8)),
                    ('レ4', (1,8)),
                    ('ラ3', (1,8)),
                    ('レ4', (1,8)),
                    ('ミ4', (1,8)),
                    ('ラ4', (1,4)),
                    ('--', (1,4))
            ],
            [
                    ('ラ3', (1,8)),
                    ('ミ4', (1,8)),
                    ('ファ#4', (1,8)),
                    ('ミ4', (1,8)),
                    ('ラ3', (1,8)),
                    ('レ4', (1,4)),
                    ('--', (1,8))
            ]
    ]
    
    for section in scores_famima:
        for nt in section:
            buf = ml.Note(nt[0], nt[1])
            pasbuzzer(buzzer, buf['freq'], buf['length'])
            time.sleep_ms(50)

if __name__ == '__main__':
    pasbuzzer(buzzer, 400, 0)

