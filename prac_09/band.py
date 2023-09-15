class Band:

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name}({', '.join(str(i) for i in self.musicians)})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            if not vars(musician)['instruments']:
                print(f"{vars(musician)['name']} needs an instrument!")
            else:
                print(f"{vars(musician)['name']} is playing: {vars(musician)['instruments'][0]}")
        return ""