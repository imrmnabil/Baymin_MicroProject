with open('myfile.txt', 'r') as f:
    count = 0
    for line in f:
        line = line.rstrip('\n')
        count += 1

person = open('person.txt', 'r').readlines()[0]

if person=="True":
    person = True
else:
    person=False

if not person:
    file=open('myfile.txt', 'r')
    lines = file.readlines()
    if lines and lines[0] == "F":
        file = open('myfile.txt', 'w')
        file.write('F\n')
    elif not lines:
        file = open('myfile.txt', 'w')
        file.write('F\n')
    elif count == 6:
        with open('myfile.txt', 'w') as file:
            file.write('F\n')
    else:
        print(person)
        with open('myfile.txt', 'r+') as file:
            file.seek(0, 2)
            file.write('F\n')
            file.seek(0)
            lines = file.readlines()
            time = int(lines[1])
            lines[1]=time+1

else:
    with open('myfile.txt', 'r+') as file:
        lines = file.readlines()
        if lines:
            if lines[0] == "F\n":
                file.seek(0, 0)
                if count < 6:
                    file.write("T\n")
                    file.write("1\n")
            else:
                file=open('myfile.txt', 'w')
                time = int(lines[1])
                file.write("T\n")
                file = open('myfile.txt', 'a')
                file.write(str(time + 1)+'\n')
                file.seek(0, 0)
                # file.writelines(lines)
        else:
            file.write("T\n")
            file.write("1\n")
###############################################################################

if count>=2:
    file = open('myfile.txt', 'r')
    lines = file.readlines()
    if lines:
        time = int(lines[1])
    if time>29:
        #eije tor bal ekhane
        print("Ar bosha jabe na")
    else:
        print("Thakte paris pera nai")
else:
    print("boshli to kebol kiser ber howa?")