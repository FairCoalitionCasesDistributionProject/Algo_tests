from fairpy.items.bounded_sharing import *
from political_party import Political_party
from division_item import Division_item


class Division:

    def __init__(self, parties=None, items=None):
        if items is None:
            items = []
        if parties is None:
            parties = []
        self.parties = parties
        self.items = items
        self.num_of_items = len(items)
        self.num_of_parties = len(parties)
        self.number_of_mandates = sum([party.getmandates() for party in parties])
        self.__check_mandates_sum()

    def get_items(self):
        return self.items

    def get_parties(self):
        return self.parties

    def add_parties(self, parties: list[tuple[str, int]]):
        for party, mandates in parties:
            self.add_party(party, mandates)

    def add_party(self, party_name: str, mandates: int):
        if party_name in self.parties:
            return
        self.parties.append(Political_party(party_name, mandates))
        self.num_of_parties += 1
        self.number_of_mandates += mandates
        self.__check_mandates_sum()

    def remove_parties(self, parties: list[str]):
        for party in parties:
            self.remove_party(party)

    def remove_party(self, party_name: str):
        if party_name in self.parties:
            party_index = self.parties.index(party_name)
            party = self.parties[party_index]
            self.num_of_parties -= 1
            self.number_of_mandates -= party.getmandates()
            self.parties.pop(party_index)

    def add_items(self, list_of_items: list[str]):
        for item in list_of_items:
            self.add_item(item)

    def add_item(self, name_of_item: str):
        if name_of_item in self.items:
            return
        self.items.append(Division_item(name_of_item))
        self.num_of_items += 1

    def remove_items(self, list_of_items: list[str]):
        for item in list_of_items:
            self.remove_item(item)

    def remove_item(self, name_of_item: str):
        if name_of_item in self.items:
            self.items.remove(name_of_item)
            self.num_of_items -= 1

    def set_party_preferences(self, name_of_party: str, new_preferences: list[float]):
        if len(new_preferences) != self.num_of_items:
            raise Exception("Preference list is of length: ", len(new_preferences), " number of items is: ",
                            len(self.num_of_items))

        if name_of_party in self.parties:
            self.parties[self.parties.index(name_of_party)].setpreferences(new_preferences)

    def divide(self):
        self.__check_preference_lists()
        self.__check_not_empty_item_list()
        parties_mandates_list = [party.getmandates() for party in self.parties]
        parties_preferences_list = [party.getpreferences() for party in self.parties]
        allocation = proportional_allocation_with_bounded_sharing(parties_preferences_list,
                                                                  parties_mandates_list).round(2)
        return allocation

    def __check_not_empty_item_list(self):
        if self.items == 0:
            raise Exception("No items to divide")

    def __check_preference_lists(self):
        for party in self.parties:
            if len(party.getpreferences()) != self.num_of_items:
                raise Exception("The party: " + party.getname() + " allocated only " + str(
                    len(party.getpreferences())) + " out of " + str(self.num_of_items))

    def __check_mandates_sum(self):
        if self.number_of_mandates > 120:
            raise Exception("Number of mandates can't exceed 120")
