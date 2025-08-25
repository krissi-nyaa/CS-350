# Initialize
import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setup(18,gp.OUT)

# Set initial duty cycle and direction
pwm_duty = 50
pwm_duty_max = 99
pwm_duty_min = 1
pwm_increasing = True

# Start PWM
pwm18 = gp.PWM(18,20)
pwm18.start(50)

# Loop through a pretty fading light forever
while(1):
    # Sleep for 10 ms (i know i said 20ms in the lab questions, but this looks prettier)
    time.sleep(0.01)
    if pwm_increasing:
        pwm_duty += 1
    else:
        pwm_duty -= 1

    # Reverse direction when reaching a max or min
    if pwm_duty <= pwm_duty_min:
        pwm_increasing = True
    elif pwm_duty >= pwm_duty_max:
        pwm_increasing = False

    # Set the duty cycle
    pwm18.ChangeDutyCycle(pwm_duty)