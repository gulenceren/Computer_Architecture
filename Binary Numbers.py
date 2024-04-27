print("""
  Menü
    1-> Program to Write Octal, Decimal and Hexadecimal
    2-> Program to Add and Subtract Binary Numbers
   """) #Menü Seçimi
sec = int(input("Menu Selection:"))
if sec == 1:
    girdi = input("Number in base 2 to be entered:")
    uzunluk = len(girdi)
    print("Length of the entered Number System: {} bit".format(uzunluk))
    if (16 >= uzunluk):
        def fonk(bit):
            us = 16 ; conclusion = 0
            for i in bit:
                for j in range(us):  # us alma
                    top = int(i) *(2 ** j)
                conclusion = conclusion + top
                us = us - 1
            print("Equivalent of a base of 10: {}".format(conclusion))
            print("Equivalent to base 8: {:o}".format(conclusion))
            print("Equivalent to base 16: {:x}h".format(conclusion))
        fark = 16 - uzunluk
        if fark == 0:
            print("Completion of the Entered Number System to 16 Bits: ", girdi)
            us = 16
            fonk(girdi)
        if fark == 1:
            sayi = "0" + girdi
            print("Completion of the Entered Number System to 16 Bits:: ", sayi)
            fonk(sayi)
        if fark == 2:
            sayi = "00" + girdi
            print("Completion of the Entered Number System to 16 Bits:: ", sayi)
            fonk(sayi)
        if fark == 3:
            sayi = "000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 4:
            sayi = "0000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 5:
            sayi = "00000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 6:
            sayi = "000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 7:
            sayi = "0000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 8:
            sayi = "00000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 9:
            sayi = "000000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 10:
            sayi = "0000000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 11:
            sayi = "00000000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 12:
            sayi = "000000000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 13:
            sayi = "0000000000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 14:
            sayi = "00000000000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
        if fark == 15:
            sayi = "000000000000000" + girdi
            print("Completion of the Entered Number System to 16 Bits: ", sayi)
            fonk(sayi)
if sec == 2:
    sayi1 = input("Enter the 1st Number (Please Enter 8 Bits)")
    sayi2 = input("Enter the 2nd Number (Please Enter 8 Bits):")
    sayilar = [] ; sayilar1 = []  ; conclusion = 0 ; total = 0
    def topla(a, b):
        a = a + b
        print("Addition of Two Binary Numbers, One Negative and the Other Positive: {:b} ,Equivalent in Base 10: {}".format(a,a))
    def fonk1(sayilar):
        us = 8 ; top =0 ; conclusion = 0
        for s in sayilar:
            for t in range(us):
                top = int(s) * (2 ** t)
            conclusion = conclusion + top
            us = us - 1
        conclusion += 1
        print("The inverse of a negative number added to the number 1: {}".format(conclusion))
        return conclusion
    def fonk2(sayilar1):
        us = 8 ; top = 0 ; total = 0
        for s in sayilar1:
            for t in range(us):
                top = int(s) * (2 ** t)
            total = total + top
            us = us - 1
        return total
    for x in sayi1:
        sayilar.append(int(x))
    for i in sayi1:
        if int(i) == 1: #Girilen İlk Sayı Negatif
            for x in range(8):
                if  sayilar[x] == 0:
                    sayilar[x] = 1
                elif sayilar[x] == 1:
                    sayilar[x] = 0;
            conclusion = fonk1(sayilar)
        else: #Girilen İlk Sayı Pozitif
            total = fonk2(sayilar)
        break
    for y in sayi2:
        sayilar1.append(int(y))
    for j in sayi2:
        if int(j) == 1: #Girilen ikinci Sayı Negatif
            for x in range(8):
                if  sayilar1[x] == 0:
                    sayilar1[x] = 1
                elif sayilar1[x] == 1:
                    sayilar1[x] = 0;
            conclusion = fonk1(sayilar1)
            print("The inverse of a negative number added to the number 1: {}".format(conclusion))
        else:   #Girilen ikinci Sayı Pozitif
            total = fonk2(sayilar1)
        break
    def islem(c, d):
        if c >= d:
            c = c - d
            print("Subtracted Form of Two Binary Numbers, One Negative, The Other Positive: {:b} ,Equivalent in Base 10: {}".format(c, c))
        elif d > c:
            d = d - c
            print("Subtracted Form of Two Binary Numbers, One Negative, The Other Positive: {:b} ,Equivalent in Base 10: {}".format(d, d))
    topla(conclusion,total)
    islem(conclusion,total)