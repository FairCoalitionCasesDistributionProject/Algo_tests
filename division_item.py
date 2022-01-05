class Division_item:
    curr_id = 0

    def __init__(self, name: str):
        self.id = self.curr_id
        self.curr_id += 1
        self.name = name

    def getname(self):
        return self.name

    def getid(self):
        return self.id

    def setname(self, new_name: str):
        self.name = new_name

    def setid(self, new_id: int):
        self.id = new_id

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, Division_item):
            return self.name == other.name
        return False
