import string

alfabe = string.ascii_letters + string.punctuation
# print(alfabe)
alfabechar = [*alfabe]


def sifre(txt):
    textchar = [*txt]
    yeniint = []
    ciphertxt = ""
    # print(textchar)
    # print(alfabechar)
    for first in textchar:
        for sc in alfabechar:
            if first == sc:
                asciint = alfabechar.index(sc)
                yeniint.append(asciint + 66)
    # print(yeniint)
    for i in yeniint:
        ciphertxt = ciphertxt + "".join(chr(i))

    return ciphertxt


def sifreCoz(cozulecekMesaj):
    cozint = []
    coztext = ""
    for t in cozulecekMesaj:
        cozint.append("".join(str(ord(t))))
    gec = [int(item) for item in cozint]
    yeni = [int(z - 66) for z in gec]
    # print(yeni)
    for son in yeni:
        coztext = coztext + alfabechar[son]
    return coztext


secim = input("Şifre oluşturmak için 1, şifre çözmek için 2 yazınız.")
if secim =="1":
    txt = input("Şifrelemek istediğiniz mesajı giriniz :")
    print("Şifrelenmiş mesaj :",sifre(txt))
elif secim =="2":
    txt1 = input("Çözmek istediğiniz mesajı giriniz :")
    print("Çözülmüş mesaj :",sifreCoz(txt1))