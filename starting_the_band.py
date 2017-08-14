class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Boom", "Pow"])

    def count(self):
        print("one, two, three, four")

    def combost(self):
        print("Oww, Wee")

class Band:
    def __init__(self):
        self.Jeremy = Bassist()
        self.Daniel = Guitarist()
        self.Christene = Drummer()

    def hire(self):
        print("You are hired!")

    def fire(self ):
        print("Youre fired! 'Donald Trump's voice'")

    def play(self):
        self.Christene.count()
        self.Jeremy.solo(2)
        self.Daniel.solo(4)
        self.Christene.solo(8)

if __name__ == "__main__":
    gig = Band()
    gig.play()





