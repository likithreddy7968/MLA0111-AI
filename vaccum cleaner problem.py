class VacuumCleaner:
    def __init__(self, location="A", environment=None):
        self.location = location
        self.environment = environment or {"A": "Dirty", "B": "Dirty"}

    def perceive(self):
        return self.environment[self.location]

    def suck(self):
        print(f"Vacuum at {self.location}: Sucking dirt...")
        self.environment[self.location] = "Clean"

    def move(self):
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"
        print(f"Vacuum moved to {self.location}")

    def run(self, steps=4):
        for _ in range(steps):
            status = self.perceive()
            if status == "Dirty":
                self.suck()
            else:
                print(f"Vacuum at {self.location}: Already clean.")
            self.move()

# Example usage
vacuum = VacuumCleaner(location="A", environment={"A": "Dirty", "B": "Dirty"})
vacuum.run()
