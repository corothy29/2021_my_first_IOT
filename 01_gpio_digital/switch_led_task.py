import RPi.GPIO as GPIO

R = 9
Y = 8
G = 18
R_s = 5
Y_s = 4
G_s = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(R_s, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Y, GPIO.OUT)
GPIO.setup(Y_s, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(G_s, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val1 = GPIO.input(R_s)
        val2 = GPIO.input(Y_s)
        val3 = GPIO.input(G_s)
        print(val1, val2, val3)
        GPIO.output(R, val1)
        GPIO.output(Y, val2)
        GPIO.output(G, val3)

finally:
    GPIO.cleanup()
    print('cleanup and exit')