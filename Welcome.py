import pygame
import time as t
import pigpio

pygame.mixer.init()
pygame.mixer.music.load('hello.mp3')

pi = pigpio.pi()
        
s1 = 14
s2 = 23
step = 20
sleep_time = 0.01

for pulse_width in range(1500, 1000, -1*step):
    pi.set_servo_pulsewidth(s2, pulse_width)
    t.sleep(sleep_time)
t.sleep(0.3)
for pulse_width in range(1000, 2000, step):
    pi.set_servo_pulsewidth(s2, pulse_width)
    t.sleep(sleep_time)
t.sleep(0.3)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s2, pulse_width)
    t.sleep(sleep_time)
t.sleep(0.5)

for pulse_width in range(1500, 1000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
pygame.mixer.music.play()
t.sleep(3)
pygame.mixer.music.stop()
for pulse_width in range(1000, 1500, step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)

