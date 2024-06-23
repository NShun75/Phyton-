#!/usr/bin/env python

import random

def main():
    """JOM MULA PERMAINAN TEKA BENTUK."""
    print("Teka bentuk!!! Sila pilih satu (Segiempat, Bulat, Segitiga, Bujur, Poligon, Hexagon, Silinder, Ombak")

#Senarai bentuk untuk diteka
    bentuk = [
        "Segiempat",
        "Bulat",
        "Segitiga",
        "Bujur",
        "Poligon",
        "Hexagon",
        "Silinder",
        "Ombak"
        ]
    
#jawapan random 
    x = random.choice(bentuk)
    print(x)
    guess = None

#penggunaan while untuk ulangan selagi benar.
    while x != guess:

        guess = str(input("Bentuk apa yang saya fikirkan sekarang???"))
        
        if x == guess:
            print("Anda meneka {}. Tahniah.... anda betul!!!!".format(guess))
            break
        else:
            print("Anda meneka {}. Maaf!! Bukan bentuk itu yang saya fikirkan, cuba lagi.".format(guess))

main()