# converter kilometri u milje

print("Pozdrav! Konvertriraj kilometre u milje!!")

while True:
    print("Unesite broj kilometara koji želite pretvoriti u milje")

    km = float(input("Kilometri: "))

    mile = km * 0.621371

    print(f"{km} kilometara iznosi {mile} milja.")

    nastavak = input("Želite li nastaviti pretvarati? yes/no")

    if nastavak.lower() == "no" or nastavak.lower() != "yes":
        break