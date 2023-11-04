class Rent:
    def __init__(self, amount, due_date):
        self.amount = amount
        self.due_date = due_date


    def rent_payments(self, amount, payment_status):
        self.payment_status = False
        if payments<self.amount:
            self.amount -= payments
        else:
            self.payment_status = True
        return self.amount
