while True:
    sayi = input("Enter hexadecimal number 4 digits")
    diziler = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    binaryKarsiligi = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011","1100", "1101", "1110", "1111"]
    bellekİcra = ["bellekteki kelimeyi VE leyerek AC ye aktar", "Bellek kelimesinin toplayarak  AC ye aktar","Bellek kelimesinin AC ye yükler", "AC nin içeriğinin belleğe depola", "şartsız dallan","dallan ve geri dönüş adresini sakla", "arttır ve eğer sıfır ise atla"]
    bellekKomutlari = ["AND", "ADD", "LDA", "STA", "BUN", "BSA", "ISZ"]

    yazacKarsiligi = ["100000000000", "010000000000", "001000000000", "000100000000", "000010000000", "000001000000","000000100000", "000000010000", "000000001000", "000000000100", "000000000010", "000000000001"]
    yazacKomutlari = ["CLA", "CLE", "CMA", "CME", "CIR", "CIL", "INC", "SPA", "SNA", "SZA", "SZE", "HLT"]
    yazacİcra = ["AC`yi sil", "E`yi sil", "AC nin tümleyenini al", "E nin tümleyenini al", "AC ve E'nin içerigini sağa dairesel olarak kaydır","AC ve E'nin içeriğini sola dairesel olarak kaydır", "AC'nin degerini 1 arttır", "AC pozitif ise bir sonraki buyrugu atla", "AC negatif ise bir sonraki buyrugu atla", "AC sıfır ise bir sonraki buyrugu atla", "E sıfır ise bir sonraki buyrugu atla", "Programı durdur"]

    gcKomutlari = ["INP", "OUT", "SKI", "SKO", "ION", "IOF"]
    gcKarsiligi = ["100000000000", "010000000000", "001000000000", "000100000000", "000010000000", "000001000000"]
    gcİcra = ["giriş karakterinin AC`yi al", "AC'den çıkış karakterini al", "giriş bayrağını atla", "çıkış bayrağını atla", "kesmeyi aktif yap", "kesmeyi pasif yap"]

    dizi = []; toplam = ''; toplam1 = '';  toplam2 = ''
    for i in sayi:  # sayıların binarykarşılığı hesaplandı
        a = str(i)
        for x in str(a):
            for y in range(len(diziler)):
                if x == diziler[y]:
                    dizi.append(binaryKarsiligi[y])
                    toplam = toplam + binaryKarsiligi[y]
    print("Inputted Number Converted to 16 Bits {}".format(toplam))
    for j in dizi:  # 11 dan 15 kadar olan bit aralığını aldık
        ikiliKarsiligi = str(j)
        print("  11th to 15th Bit Range: {}".format(ikiliKarsiligi))
        break
    for s in dizi[1::]:  # 0 dan 11 kadar olan bit aralığını aldık
        kalanBitler = str(s)
        toplam2 = toplam2 + kalanBitler
    say = 0
    for k in ikiliKarsiligi:  # Kib bitini hesapladık
        if say == 0:
            kibBiti = str(k)
            say += 1
        else:
            toplam1 = toplam1 + str(k)
            say += 1
    print("    Kib Biti:{} ".format(kibBiti))
    print("    11th to 14th Bit Range: {}".format(toplam1))


    def fonk(sayi, kibBiti, a):
        print("  {} Memory Addressable Instruction Type".format(sayi))
        if kibBiti == "1":
            print("    Indirect Addressing")
        else:
            print("    Direct Addressing")
        print("    {} Command '{}' Realizes its Execution.".format(bellekKomutlari[a], bellekİcra[a]))


    if toplam1 == "000":
        fonk(sayi, kibBiti, 0)
    if toplam1 == "001":
        fonk(sayi, kibBiti, 1)
    if toplam1 == "010":
        fonk(sayi, kibBiti, 2)
    if toplam1 == "011":
        fonk(sayi, kibBiti, 3)
    if toplam1 == "100":
        fonk(sayi, kibBiti, 4)
    if toplam1 == "101":
        fonk(sayi, kibBiti, 5)
    if toplam1 == "110":
        fonk(sayi, kibBiti, 6)
    if toplam1 == "111":
        if kibBiti == "0":
            sayac = 0
            print("  {} Printer Addressable Command Type".format(sayi))
            for n in yazacKarsiligi:
                sayac += 1
                if str(n) == toplam2:
                    a = sayac
                    print("    {} Command '{}' Realizes its Execution.".format(yazacKomutlari[a - 1], yazacİcra[a - 1]))
        else:
            print("  {} is of Type Command with Printer Addressing".format(sayi))
            sayac = 0
            for n in gcKarsiligi:
                sayac += 1
                if str(n) == toplam2:
                    a = sayac
                    print("    {} Command '{}' Realizes its Execution.".format(gcKomutlari[a - 1], gcİcra[a - 1]))

    cikis = input("Press the 'q' or 'Q' key to exit.Press any key to continue ")
    if cikis in ("q", "Q"):
        break