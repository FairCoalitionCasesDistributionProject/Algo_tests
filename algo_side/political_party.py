class Political_party:
    def __init__(self, name: str, mandates: int, preferences: list[float] = []):
        if mandates == 0:
            raise Exception("A party cannot have 0 mandates")
        self.name = name
        self.mandates = mandates
        self.preferences = preferences

    def getname(self):
        return self.name

    def getmandates(self):
        return self.mandates

    def getpreferences(self):
        return self.preferences

    def setpreferences(self, new_preferences: list[float]):
        self.preferences = new_preferences

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, Political_party):
            return self.name == other.getname()
        return False
