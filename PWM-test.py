

from machine import Pin, PWM
import time

LED_BUITLTIN = 2 # For ESP32

pwm_led = PWM(Pin(LED_BUITLTIN, mode=Pin.OUT)) # Attach PWM object on the LED pin
pwm_led.freq(1_000)

while True:
    for duty in range(100): # Duty from 0 to 100 %
        pwm_led.duty(int((duty/100)*1024))
        time.sleep_ms(5)
