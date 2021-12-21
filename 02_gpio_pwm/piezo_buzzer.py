import RPi.GPIO as GPIO
import time

BUZZER_PIN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#pwm 인스턴스 생성
#주파수설정 (4옥타브 도 : 262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(50) #duty cycle (0~100)

melody = [262, 294, 330, 349, 392, 440, 494, 523]

def note(mel):
    pwm.ChangeFrequency(melody[mel])

try:
    mel_list = list(input().split())
    note_list = list(map(float, input().split()))
    print(mel_list)
    
    for val in range(len(mel_list)):
        if mel_list[val] == "도":
            note(0)
        elif mel_list[val] == "레":
            note(1)
        elif mel_list[val] == "미":
            note(2)
        elif mel_list[val] == "파":
            note(3)
        elif mel_list[val] == "솔":
            note(4)
        elif mel_list[val] == "라":
            note(5)
        elif mel_list[val] == "시":
            note(6)
        elif mel_list[val] == "높은도":
            note(7)
        time.sleep(note_list[val])
        pwm.ChangeFrequency(30)
        time.sleep(0.001)
#   솔 솔 라 라 솔 솔 미 솔 솔 미 미 레 솔 솔 라 라 솔 솔 미 솔 미 레 미 도
#   0.5 0.5 0.5 0.5 0.5 0.5 1 0.5 0.5 0.5 0.5 1 0.5 0.5 0.5 0.5 0.5 0.5 1 0.5 0.5 0.5 0.5 2
finally:
    pwm.stop()
    GPIO.cleanup()
