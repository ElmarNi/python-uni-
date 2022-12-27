import random

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]

while True:
    print(("----->") + "Adam Asmaca Oyunu" + ("<-----"))
    
    kelime = random.choice(["insan", "cemiyyet", "sosial", "texniki", "fiziki", "tedqiqat","ferdi","kollec","gimnaziya","distant","ceyran",])
    adim = 0
    tahmin = []
	 
    
    while True:
        print(resim[adim])
        
        for i, char in enumerate(kelime):
            print(char if i in tahmin else "_"),
            
        cevap = input("\nSozu texmin edin: ")
        
        if cevap == kelime:
            print("Qazandiniz!\n\n")
            break
        else:
            while True:
                rastgele = random.randint(0, len(kelime))
                if not rastgele in tahmin:
                    tahmin.append(rastgele)
                    break
            
            adim += 1
        
        if adim >= len(resim):
            print("Uduzdunuz!\n\n")
            break
        
    if not "y" == input("Yeniden oynamaq isteyirsiniz? (y/n): "):
        break
