class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_data(self):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


person1 = student("Kiril", 16)
person2 = student("Asen", 24)


print (person1.get_name(), person1.get_age())
print (person2.get_name(), person2.get_age())