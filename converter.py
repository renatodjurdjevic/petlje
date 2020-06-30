# converter kilometri u milje

print("Pozdrav! Konvertriraj kilometre u milje!!")

while True:
    print("Unesite broj kilometara koji želite pretvoriti u milje")

    km = float(input("Kilometri: "))

    mile = km * 0.621371

    print(str(km) + " kilometara iznosi " + str(mile) + " milja.")

    nastavak = input("Želite li nastaviti pretvarati? yes/no")

    if nastavak.lower() == "no" or nastavak.lower() != "yes":
        break