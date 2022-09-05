print("Bir sayı giriniz")
x = int(input())
y = 0
toplamcift = 0
toplamtek = 0

while y<x:
    y += 1
    if (y%2 == 0):
     toplamcift += y**3
    else:
     toplamtek += y**2
print("Girilen sayıya kadar olan tek sayıların karesi: ",toplamtek,"çift sayıların kübü: ",toplamcift)
