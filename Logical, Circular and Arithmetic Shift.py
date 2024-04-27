print("""
    1-> Logical Shift
    2-> Circle Shift
    3-> Arithmetic Shift
""")
girdi = input("Enter an 8 Bit Binary Number")
if len(girdi) == 8 :
    secim = input("Select a Shift Type")
    if secim == '1':
        dizi = [] ; yeniDizi = [] ; dizi1 = []
        print("""
            R1 <- Shr R1
            R2 <- Shl R2
            """)
        for i in girdi:
            dizi.append(int(i))
            dizi1.append(int(i))
        for j in range(8):
            if j == 0:
                yeniDizi.append(0)
                del dizi1[0]
            if j == 7:
                del dizi[7]
        a = yeniDizi + dizi
        b = dizi1 + yeniDizi
        print("Right Shift of a Given 8 Bit Binary Number(R1<-Shr R1)= {}".format(a))
        print("Right Shift of a Given 8 Bit Binary Number (R2<-Shl R2)= {}".format(b))
    if secim == '2':
        circle = [] ; circle1 = []
        print("""
            R <- cir R
            R <- cil R
        """)
        for i in girdi:
            circle.append(int(i))
        for n in girdi[9 : 0 : -1]:
            circle1.append(int(n))
        circle1.append(circle[0])
        for j in range(1):
            a = circle[int(j)]
            del circle[int(j)]
            circle.append(a)
            print("Rotated 1st Time: {}".format(circle))
        for x in range(1):
            a = circle[int(x)]
            del circle[int(x)]
            circle.append(a)
            print("Rotated 2nd Time: {}".format(circle))
        for y in range(1):
            a = circle[int(y)]
            del circle[int(y)]
            circle.append(a)
            print("Rotated 3rd time: {}".format(circle))
        for z in range(1):
            a = circle[int(z)]
            del circle[int(z)]
            circle.append(a)
            print("Rotated 4th time: {}".format(circle))
        for t in range(1):
            a = circle[int(t)]
            del circle[int(t)]
            circle.append(a)
            print("Rotated 5th time: {}".format(circle))
        for k in range(1):
            a = circle[int(k)]
            del circle[int(k)]
            circle.append(a)
            print("Rotated 6th time: {}".format(circle))
        for l in range(1):
            a = circle[int(l)]
            del circle[int(l)]
            circle.append(a)
            print("Rotated 7th time: {}".format(circle))
        for m in range(1):
            a = circle[int(m)]
            del circle[int(m)]
            circle.append(a)
            print("Right Circularly Tilted to the Right(R <- cir R): {}".format(circle))
        for j in range(1):
            a = circle1[int(j)]
            del circle1[int(j)]
            circle1.append(a)
        for x in range(1):
            a = circle1[int(x)]
            del circle1[int(x)]
            circle1.append(a)
        for y in range(1):
            a = circle1[int(y)]
            del circle1[int(y)]
            circle1.append(a)
        for z in range(1):
            a = circle1[int(z)]
            del circle1[int(z)]
            circle1.append(a)
        for t in range(1):
            a = circle1[int(t)]
            del circle1[int(t)]
            circle1.append(a)
        for k in range(1):
            a = circle1[int(k)]
            del circle1[int(k)]
            circle1.append(a)
        for l in range(1):
            a = circle1[int(l)]
            del circle1[int(l)]
            circle1.append(a)
        for m in range(1):
            a = circle1[int(m)]
            del circle1[int(m)]
            circle1.append(a)
        yeniCircle = []
        for n in circle1[9 : 0 : -1]:
            yeniCircle.append(int(n))
        yeniCircle.append(circle[7])
        print("Circular Left Circularized Version(R <- cil R): {}".format(yeniCircle))
    if secim == '3':
        print("""
                    R <- ashr R
                    R <- ashl R
                """)
        dizi = [] ; yeniDizi = [] ; dizi1 = []
        for i in girdi:
            dizi.append(int(i))
            dizi1.append(int(i))
        for j in range(8):
            if j == 0:
                yeniDizi.append(dizi[0])
                del dizi1[0]
            if j == 7:
                del dizi[7]
        a = yeniDizi + dizi
        b = dizi1 + yeniDizi
        print("Right Shift of a Given 8 Bit Binary Number(R <- ashr R)= {}".format(a))
        print("Right Shift of a Given 8 Bit Binary Number(R <- ashl R)= {}".format(b))
else:
    print("Please Enter 8 Bit Number")