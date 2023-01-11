print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => "))))  #добавила 2 скобки в конце строки
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0:     #добавила двоеточие
            if b % 2 == 0:       #добавила ровно
                    paaris += 1    #поменяла местами знаки + и =
            else:
                    paaritu += 1    #поменяла местами знаки + и =
            b = b // 10
    print("Paarisarvud:", paaris)   #добавила запятую
    print("paarituid numbreid:", paaritu)   #добавила запятую
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake * sisestatud number")
    print()
    b=0
    while a > 0:       #добавила двоеточие
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #поменяла местами знаки + и =   
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine")    #удалила лишнюю скобку
    print()
    if c % 2 == 0:   #добавила ровно
        print(c," - paarisarv. Jagage poolt 2.")
    else:
        print(c," - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2.")
    while c != 1:
            if c % 2 == 0:   #добавила ровно
                    c = c / 2   #удалила ровно
            else:
                    c = (3*c + 1) / 2   #удалила ровно
            print(round(c), end=" ")   #добавила верный знак препинания
    print()
    print("Hüpotees on õige")   #добавила верный знак препинания
