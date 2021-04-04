class Student:

    def __init__(self, name, university):
        self.name = name
        self.university = university
        self.year = 1

    def get_name(self):
        return self.name

    def get_university(self):
        return self.university

    def get_year(self):
        return self.year

    def study(self):
        if self.year < 6:
            self.year += 1
        return self.year


class Employee:

    def __init__(self, name, company):
        self.name = name
        self.company = company
        self.year = 1
        self.position = 'junior'

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def get_position(self):
        return self.work

    def work(self):
        if self.position == 'junior':
            self.position = 'middle'
        elif self.position == 'middle':
            self.position = 'senior'
        elif self.position == 'senior':
            self.position= 'lead'
        elif self.position== 'senior':
            self.position = 'lead'


class Human:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name



empl = Employee("Ivan", "Yandex")
print(empl.get_position())
empl.work()
empl.work()
print(empl.get_position())
empl.work()
empl.work()
empl.work()
print(empl.get_position())