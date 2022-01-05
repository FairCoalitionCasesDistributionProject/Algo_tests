class Political_party:
    def __init__(self, name: str, mendates: int, preferences: list[float] = []):
        self.name = name
        self.mandates = mendates
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
