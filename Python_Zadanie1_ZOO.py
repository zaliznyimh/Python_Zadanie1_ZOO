# Initialising a generic Zoo class with common values 
class Zoo:
    def __init__(self, name, height, length, weight, color, isHerbivore, noise):
        self.name = name
        self.height = height
        self.length = length 
        self.weight = weight
        self.color = color
        self.isHerbivore = isHerbivore
        self.noise = noise
        
    def ShowInfoAboutAnimals(self):
        pass

# Initialising a generic Birds class which contains "ZOO" values and unique value and the output of data on these animals is listed 
class Bird(Zoo):
    def __init__(self, name, height, length, weight, color, wingspan, isHerbivore, noise):

        super().__init__(name, height, length, weight, color, isHerbivore, noise)
        self.wingspan = wingspan

    def ShowInfoAboutAnimals(self):
        print(f"Bird's name is {self.name}")
        print(f"Bird's height is {self.height} m. and length {self.length} m.")
        print(f"Birds weight is {self.weight} kg. ")
        print(f"Birds color is {self.color}")
        print(f"Bird is {self.isHerbivore}")
        print(f"Birds wingspan is {self.wingspan}") 
        print(f"Bird is {self.noise} \n")
        
# Initialising a generic Mammals class which contains "ZOO" values and unique value and the output of data on these animals is listed
class Mammals(Zoo):
    def __init__(self, name, height, length, weight, color, isHerbivore, noise, NumberoOfLimbs):

        super().__init__(name, height, length, weight, color, isHerbivore, noise)
        self.NumberoOfLimbs = NumberoOfLimbs

    def ShowInfoAboutAnimals(self):
        print(f"Animal name is {self.name}")
        print(f"Animal's height is {self.height} m. and length {self.length} m.")
        print(f"Animal's weight is {self.weight} kg. ")
        print(f"Animal's color is {self.color}")
        print(f"Animal is {self.isHerbivore}")
        print(f"Animal is {self.noise}")
        print(f"Animal has {self.NumberoOfLimbs} \n") 
    
# Initialising a generic Insects class which contains "ZOO" values and unique value and the output of data on these animals is listed
class Insect(Zoo):
    def __init__(self, name, height, length, weight, color, isHerbivore, noise, isWings):
    
        super().__init__(name, height, length, weight, color, isHerbivore, noise)
        self.isWings = isWings

    def ShowInfoAboutAnimals(self):
        print(f"Insect name is {self.name}")
        print(f"Insect's height is {self.height} m. and length {self.length} m.")
        print(f"Insect's weight is {self.weight} kg. ")
        print(f"Insect's color is {self.color}")
        print(f"Insect is {self.isHerbivore}")
        print(f"Insect has {self.isWings}") 
        print(f"Insect is {self.noise} \n ")

# Initialising a generic Fishes class which contains "ZOO" values and unique value and the output of data on these animals is listed
class Fish(Zoo):
    def __init__(self, name, height, length, weight, color, isHerbivore, DepthWhereLives, noise):

        super().__init__(name, height, length, weight, color, isHerbivore, noise)
        self.DepthWhereLives = DepthWhereLives

    def ShowInfoAboutAnimals(self):
        print(f"Fish name is {self.name}")
        print(f"Fish height is {self.height} m. and length {self.length} m.")
        print(f"Fish weight is {self.weight} kg. ")
        print(f"Fish color is {self.color}")
        print(f"Fish is {self.isHerbivore}")
        print(f"Fish lives at {self.DepthWhereLives} depth ") 
        print(f"{self.noise} \n")


# Initialising a generic Amphibian class which contains "ZOO" values and unique value and the output of data on these animals is listed
class Amphibian(Zoo):
    def __init__(self, name, height, length, weight, color, isHerbivore, noise, skin):

        super().__init__(name, height, length, weight, color, isHerbivore, noise)
        self.skin = skin

    def ShowInfoAboutAnimals(self):
        print(f"Amphibian name is {self.name}")
        print(f"Amphibian height is {self.height} m. and length {self.length} m.")
        print(f"Amphibian weight is {self.weight} kg. ")
        print(f"Amphibian color is {self.color}")
        print(f"Amphibian is {self.isHerbivore}")
        print(f"{self.skin} \n ") 
        

# Initialising a generic Molluscs class which contains "ZOO" values and unique value and the output of data on these animals is listed
class Molluscs(Zoo):
    def __init__(self, name, height, length, weight, color, isHerbivore, SizeOfShell, noise):

        super().__init__(name, height, length, weight, color, isHerbivore, noise)
        self.SizeOfShell = SizeOfShell

    def ShowInfoAboutAnimals(self):
        print(f"Molluscs name is {self.name}")
        print(f"Molluscs height is {self.height} m. and length {self.length} m.")
        print(f"Molluscs weight is {self.weight} kg. ")
        print(f"Molluscs color is {self.color}")
        print(f"Molluscs is {self.isHerbivore}")
        print(f"{self.SizeOfShell} \n ") 

# Output information about all Zoo animals
# Note: Length and height in metres, weight in kilograms
# kanarek, lew, orzeł, sójka, ślimak, wąż boa, antylopa, żaba, chrząszcz, modliszka, sum, rekin
Kanarek = Bird("Kanarek", 0.23, 0.05, 0.05, "yellow", 0.15, "herbivore", "singing")   
Kanarek.ShowInfoAboutAnimals()

Lew = Mammals("Lew", 1.2, 2.8, 189, "brown", "predator", "growling", "four limbs")
Lew.ShowInfoAboutAnimals()

Orzeł = Bird("Orzeł", 0.75, 0.35, 5, "dark brown", 1.75, "predator", "makes loud noise")
Orzeł.ShowInfoAboutAnimals()

Sójka = Bird("Sójka",0.32, 0.20, 0.200, "light brown", 0.55, "predator", "makes noises" )
Sójka.ShowInfoAboutAnimals()

Ślimak = Molluscs("Ślimak", 0.05, 0.07, 0.015, "white", "herbivore", "It doesn't have shell", "doesn't make any noise")
Ślimak.ShowInfoAboutAnimals() 

Waz_Boa = Amphibian("Waz Boa", 0.07, 0.75, 0.300, "green", "predator", "Waz doesnt make any noise", "Skin is sleppery and tight")
Waz_Boa.ShowInfoAboutAnimals()

Antylopa = Mammals("Antylopa", 0.80, 1.50, 65, "brown", "herbivare", "makes some noise", "four limbs")
Antylopa.ShowInfoAboutAnimals()

Zaba = Amphibian("Zaba", 0.05, 0.15, 0.250, "brown or green", "predator", "make laud 'KWA'", "Skin is sleppery")
Zaba.ShowInfoAboutAnimals()

Chrzaszcz = Insect("Chrząszcz", 0.001, 0.0036, 0.001, "brown", "herbivore", "Makes noise when fly", "two wings")
Chrzaszcz.ShowInfoAboutAnimals()

Modliszka = Insect("Modliszka", 0.01, 0.058, 0.1, "green", "predator", "doesn't make any noise", "doesn't have any wings")
Modliszka.ShowInfoAboutAnimals()

Sum = Fish("Sum", 0.45, 5, 200, "Grey", "predator", 120, "Doesn't make any noise, because lives under water xD")
Sum.ShowInfoAboutAnimals()

Rekin = Fish("Rekin", 0.50, 18, 4000, "grey or white", "predator", "2 - 2000", "Doesn't make any noise, because lives under water xD")
Rekin.ShowInfoAboutAnimals()
