import string

alphabet = string.ascii_letters + string.punctuation
alphabetchar = [*alphabet]


def sifre(txt):
    textchar = [*txt]
    yeniint = []
    ciphertxt = ""
    for first in textchar:
        for sc in alfabechar:
            if first == sc:
                asciint = alphabetchar.index(sc)
                yeniint.append(asciint + 66)
    for i in yeniint:
        ciphertxt = ciphertxt + "".join(chr(i))

    return ciphertxt


def sifreCoz(msg):
    ascii_int = []
    coztext = ""
    for t in msg:
        ascii_int.append("".join(str(ord(t))))
    gec = [int(item) for item in ascii_int]
    final_ascii_number = [int(z - 66) for z in gec]
    for son in final_ascii_number:
        coztext = coztext + alfabechar[son]
    return coztext


secim = input("Şifre oluşturmak için 1, şifre çözmek için 2 yazınız.")
if secim =="1":
    txt = input("Şifrelemek istediğiniz mesajı giriniz :")
    print("Şifrelenmiş mesaj :",sifre(txt))
elif secim =="2":
    txt1 = input("Çözmek istediğiniz mesajı giriniz :")
    print("Çözülmüş mesaj :",sifreCoz(txt1))