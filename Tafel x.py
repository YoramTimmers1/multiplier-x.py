def tafel():
    Tafel = input("van welk getal wil je een tafel zien :")

    Tafel = int(Tafel)
    for i in range(1,11):
        print(i * Tafel)
    print()
    
tafel()