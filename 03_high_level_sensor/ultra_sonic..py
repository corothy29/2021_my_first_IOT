import RPi.GPIO as GPIO
import time

TREGGER_PIN = 4
ECHO_PIN = 14

GPIO.setmod(GPIO.BCM)
GPIO.setup(TREGGER_PIN_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True:
        GPIO.output(TRIGGER_PIN, True)
        time.sleep(0.00001) #10us,  10마이크로세컨드
        GPIO.output(TRIGGER_PIN, False)

        while GPIO.input(ECHO_PIN) == 0: #펄스발생중
            pass
        start = time.time() #ECHO PIN HIGH 측정시작시간

        while GPIO.input(ECHO_PIN) == 1: #펄스발생종료
            pass
        stop = time.time() #ECHO PIN LOW 측정종료시간

        duration_time = stop - start
        distance = duration_time * 17160 # 34321/2

        print('Distance : %.1fcm' % distance)
        time.sleep(0.1)
        
finally:
    GPIO.cleanup()
    print('cleanup and exit')


