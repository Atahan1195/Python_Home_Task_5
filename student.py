class Student:

    def __init__(self, name, date_of_birth, sex):
        self.name = name
        self.date_of_birth = date_of_birth
        self.sex = sex

    def __str__(self):
        return f'{self.name}'
