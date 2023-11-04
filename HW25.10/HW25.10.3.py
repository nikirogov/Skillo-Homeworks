class bankacc:
    def __init__(self, name, __money):
        self.name = name
        self.__money = __money
    def withdrawal(self, __amount):
        self.__money -= __amount
        return self.__money
    def deposit(self, __amount):
        self.__money += __amount
        return self.__money
    def balance(self, __money):
        return self.__money

person1 = bankacc("Bob", 900)
print(person1.withdrawal(200))
print(person1.deposit(500))
print(person1.balance(200))