import requests
import os

#Zapytanie api do NBP
wynik=requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/last/1/?format=json').json()

kurs_dolara=float(wynik['rates'][0]['mid'])

print("--- Przelicznik PLN->USD, USD->PLN ---")


x=input("Podaj ilość oraz walute(np. 5 PLN, Obsługiwane waluty to: PLN, USD):\n")
x=x.split()

if x[1]=='USD':     #gdy na wejściu otrzymamy USD
    po_kursie=float(x[0])*kurs_dolara
    #zaokrąglamy do 2 miejsc po przecinku
    po_kursie=round(po_kursie,2)
    print("Jest to ",po_kursie,end=' PLN\n')
elif x[1]=='PLN':   #gdy na wejściu otrzymamy PLN     
    po_kursie=float(x[0])/kurs_dolara
    #zaokrąglamy do 2 miejsc po przecinku
    po_kursie=round(po_kursie,2)
    print("Jest to ",po_kursie,end=' USD\n')
else:
    print("Nieobsługiwana waluta!")
os.system("PAUSE")