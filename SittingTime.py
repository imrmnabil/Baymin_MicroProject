import pygame
import pigpio
import time as t

pygame.mixer.init()
pygame.mixer.music.load('break.mp3')

with open('data/time.txt', 'r') as f:
    count = 0
    for line in f:
        line = line.rstrip('\n')
        count += 1

person = open('data/isFace.txt', 'r').readlines()[0]

if person=="True":
    person = True
else:
    person=False

if not person:
    file=open('data/time.txt', 'r')
    lines = file.readlines()
    if lines and lines[0] == "F":
        file = open('data/time.txt', 'w')
        file.write('F\n')
    elif not lines:
        file = open('data/time.txt', 'w')
        file.write('F\n')
    elif count == 6:
        with open('data/time.txt', 'w') as file:
            file.write('F\n')
    else:
        print(person)
        with open('data/time.txt', 'r+') as file:
            file.seek(0, 2)
            file.write('F\n')
            file.seek(0)
            lines = file.readlines()
            time = int(lines[1])
            lines[1]=time+1

else:
    with open('data/time.txt', 'r+') as file:
        lines = file.readlines()
        if lines:
            if lines[0] == "F\n":
                file.seek(0, 0)
                if count < 6:
                    file.write("T\n")
                    file.write("1\n")
            else:
                file=open('data/time.txt', 'w')
                time = int(lines[1])
                file.write("T\n")
                file = open('data/time.txt', 'a')
                file.write(str(time + 1)+'\n')
                file.seek(0, 0)
                # file.writelines(lines)
        else:
            file.write("T\n")
            file.write("1\n")
###############################################################################

if count>=2:
    file = open('data/time.txt', 'r')
    lines = file.readlines()
    if lines:
        time = int(lines[1])
    if time>29:
        file=open('data/time.txt', 'w')
        file.write("T\n")
        file.write("1\n")
        print("Here")
        pi = pigpio.pi()
        
        s1 = 14
        step = 20
        sleep_time = 0.02
        for pulse_width in range(1500, 1000, -1*step):
            pi.set_servo_pulsewidth(s1, pulse_width)
            t.sleep(sleep_time)
        pygame.mixer.music.play()
        t.sleep(4.0)
        pygame.mixer.music.stop()
        for pulse_width in range(1000, 1500, step):
            pi.set_servo_pulsewidth(s1, pulse_width)
            t.sleep(sleep_time)
        
    else:
        print("Thakte paris pera nai")
else:
    print("boshli to kebol kiser ber howa?")
