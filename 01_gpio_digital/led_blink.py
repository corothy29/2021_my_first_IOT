import RPi.GPIO as GPIO
import time

R_PIN = 7
Y_PIN = 8
G_PIN = 9
GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(Y_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)

GPIO.output(R_PIN, GPIO.HIGH)
print("red on")
time.sleep(2)
GPIO.output(R_PIN, GPIO.LOW)
GPIO.output(Y_PIN, GPIO.HIGH)
print("red off")
print("yellow on")
time.sleep(2)
GPIO.output(Y_PIN, GPIO.LOW)
GPIO.output(G_PIN, GPIO.HIGH)
print("yellow off")
print("green on")
time.sleep(2)
GPIO.output(G_PIN, GPIO.LOW)
print("green off")

GPIO.cleanup() #GPIO 핀상태 초기화

