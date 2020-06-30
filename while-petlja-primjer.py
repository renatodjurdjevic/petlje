# while petlja

import random # importamo random library

secret = random.randint(1,30)

while True:

    guess = int(input("Pogodi jedan broj izmedju 1 i 30: "))

    if guess == secret:
        print("Bravo! Traženi broj je bio: " + str(secret))
        break
    elif guess > secret:
        print("Fulao si, probaj s manjim brojem.")
    elif guess < secret:
        print("Fulao si, probaj s većim brojem.")