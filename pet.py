class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5 
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        print(f"Creating pet {self.name}")

    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = min(0, self.hunger - 3)
        self.happiness = max(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = max(10, self.energy + 5)

    def play(self):
        if self.energy == 0:
            print(f"{self.name} is too tired")
            self.sleep
            self.play
        else:
            print(f"{self.name} is playing...")
            self.happiness = max(10, self.happiness + 2)
            self.energy = max(10, self.energy - 2)

    def train(self, trick):
        self.tricks = trick
        
    def show_tricks(self):
        for i in self.tricks:
            print(f"{self.name} can {i}")

    def get_status(self):
        print(f"{self.name}'s current status: "
              f"\nHunger: {self.hunger} "
              f"\nEnergy: {self.energy} "
              f"\nHappiness: {self.happiness}"
              f"\nTricks: {self.tricks}")