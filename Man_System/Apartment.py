class Apartment:
    def __init__(self, number, sq, rent_amount):
        self.number = number
        self.sq = sq
        self.rent_amount = rent_amount

    def get_number(self, number):
        return self.number
    def get_sq(self, sq):
        return self.sq
    def get_rent_amount(self, rent_amount):
        return self.rent_amount