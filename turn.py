import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin = 22

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)

while 1:
        i = input();
        if i == 1:
                GPIO.output(pin, GPIO.LOW)
        elif i == 0:
                GPIO.output(pin, GPIO.HIGH)
        else:
                print("No such option")
                GPIO.cleanup()
                break
