import pygame
import time as t
import pigpio

pygame.mixer.init()
pygame.mixer.music.load('sleepy.mp3')

pi = pigpio.pi()
        
s1 = 16
s2 = 23
step = 30
sleep_time = 0.01


for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
pygame.mixer.music.play()
t.sleep(6)
pygame.mixer.music.stop()

for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(1500, 2000, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)
for pulse_width in range(2000, 1500, -1*step):
    pi.set_servo_pulsewidth(s1, pulse_width)
    t.sleep(sleep_time)

