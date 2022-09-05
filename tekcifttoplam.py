tektoplam = 0
cifttoplam = 0
n=0

while n <= 1000:
    n += 1
    if (n%2)==0:
        cifttoplam += n
    else:
        tektoplam += n
print ("Tek sayıların toplamı: ",tektoplam,"Çift sayıların toplamı: ",cifttoplam)