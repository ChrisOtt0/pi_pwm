import RPi.GPIO as GPIO
led_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

while True:
    d = input("Enter brightness 0 to 100 or 'quit' to exit: ")
    if d == "quit":
        break
    duty = int(d)
    pwm_led.ChangeDutyCycle(duty)

GPIO.cleanup()
