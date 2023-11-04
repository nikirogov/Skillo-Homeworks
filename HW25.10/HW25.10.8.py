class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def department(self):
        pass

class manager(employee):
    def __init__(self, depart):
        self.depart = depart
    def department(self):
        return self.depart
    def department_get(self, value):
        return self.depart
    def department_set(self, value):
        self.depart = value


employee1 = employee("Alice" , 924)
employee2 = employee("Bob" , 1200)
manager1 = manager("Pr")
print(employee1.department())
print(employee2.department())

