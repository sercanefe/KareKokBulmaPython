"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem: ax^2 + bx + c

Deltayı Hesaplama: b**2 - 4*a*c

Birinci Kök: (-b - delta ** 0.5) / (2*a)
İkinci Kök: (-b + delta ** 0.5) / (2*a)
"""

a = int(input("A değerini giriniz: "))

b = int(input("B değerini giriniz: "))

c = int(input("C değerini giriniz: "))

delta = b**2 - 4*a*c

kok1 = (-b -delta**0.5) / (2*a)

kok2 = (-b + delta**0.5) / (2*a)

print("Birinci kök:{}\nikinci Kök:4{}".format(kok1,kok2))