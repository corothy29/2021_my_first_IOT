import RPi.GPIO as GPIO
import time

LED_PIN=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#PWM인스턴스 생성  주파수 설정 (50hz)
#1초에 50번 사이클이 돌게 하겠다.
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0) #duty cycle (0~100)

try:
    while True:
        for i in range(0, 101, 5): #start, end, step
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
        for j in range(100, 1, -5):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)

finally:
    pwm.stop()
    GPIO.cleanup()
    print('cleanup and exit')
