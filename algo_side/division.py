from fairpy.items.bounded_sharing import *
from fairpy.items.leximin import *
from .political_party import Political_party
# from .division_item import Division_item


class Division:

    def __init__(self, parties=None, number_of_items=0):
        if parties is None:
            parties = []
        self.parties = parties
        self.num_of_items = number_of_items
        self.num_of_parties = len(parties)
        self.number_of_mandates = sum([party.getmandates() for party in parties])
        self.__check_mandates_sum()

    def get_items(self):
        return self.items

    def get_parties(self):
        return self.parties

    def add_parties(self, parties: list[tuple[int,int]]):
        for id, mandates in parties:
            self.add_party(id, mandates)

    def add_party(self, id:int, mandates: int):
        self.parties.append(Political_party(id, mandates))
        self.num_of_parties += 1
        self.number_of_mandates += mandates
        self.__check_mandates_sum()

    def remove_parties(self, parties: list[int]):
        for party in parties:
            self.remove_party(party)

    def remove_party(self, party_name: int):
        if party_name in self.parties:
            party_index = self.parties.index(party_name)
            party = self.parties[party_index]
            self.num_of_parties -= 1
            self.number_of_mandates -= party.getmandates()
            self.parties.pop(party_index)

    def set_party_preferences(self, id_of_party: int, new_preferences: list[float]):
        if len(new_preferences) != self.num_of_items:
            raise Exception("Preference list is of length: ", len(new_preferences), " number of items is: ",self.num_of_items)
        if id_of_party in self.parties:
            self.parties[self.parties.index(id_of_party)].setpreferences(new_preferences)

    def divide(self):
        self.__check_preference_lists()
        self.__check_not_empty_item_list()
        parties_preferences_list = [
            [party.getpreferences()[j] / party.getmandates() for j in range(len(party.getpreferences()))] for party in
            self.parties]
        allocation = dominating_allocation_with_bounded_sharing(parties_preferences_list, leximin_optimal_allocation(
            parties_preferences_list).round(2).utility_profile())
        return allocation

    def __check_not_empty_item_list(self):
        if self.num_of_items == 0:
            raise Exception("No items to divide")

    def __check_preference_lists(self):
        for party in self.parties:
            if len(party.getpreferences()) != self.num_of_items:
                raise Exception("The party: " + party.getname() + " allocated only " + str(
                    len(party.getpreferences())) + " out of " + str(self.num_of_items))

    def __check_mandates_sum(self):
        if self.number_of_mandates > 120:
            raise Exception("Number of mandates can't exceed 120")
