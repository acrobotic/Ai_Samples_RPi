import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)     # use the same GPIO convention as the Broadcom SoC

GPIO.setup(2, GPIO.OUT)    # set GPIO2 as output

pwm_obj = GPIO.PWM(2, 100) # create PWM object associated with GPIO2; 100Hz

pwm_obj.start(50)          # start the PWM with the duty cycle at 50%

delay_ms = 0.02            # delay time in milliseconds for holding each duty
                           # cycle value

# while maintaining the same frequency (100Hz) we'll increase and decrease
# the duty cycle (high-to-low ratio) between 0% and 100%.
try:
    while True:
        for i in range(101):
            pwm_obj.ChangeDutyCycle(i) 
            sleep(delay_ms)
        for i in range(100,-1,-1):
            pwm_obj.ChangeDutyCycle(i)
            sleep(delay_ms)
# we'll repeat the duty cycle change forever. when/if the user presses CTRL+C to
# stop, we'll handle the created exception
except KeyboardInterrupt:
    pwm_obj.stop()
    GPIO.cleanup()
