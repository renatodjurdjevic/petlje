# while petlja

secret = 25
guess = 1

while guess != secret:

        guess = int(input("Pogodi broj izmedju 1 i 30: "))

        if guess == secret:
            print("Bravo, pogodio si tajni broj!")
        else:
            print("Sorry, fulao si! Probaj ponovno!")