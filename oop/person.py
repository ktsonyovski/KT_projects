class Person:
    def __init__(self,name: str,sex: str,country: str,birth_year: int):
        self.name = name
        self.sex = sex.lower()
        self.country = country
        self.birth_year = birth_year
        pass

    def calc_age(self, current_year: int):
        age = current_year - self.birth_year
        if self.sex == "man" or self.sex == "boy":
            if age <= 18:
                print(f"Your person of choice is {self.name}.\nHe is a {age} years old boy from {self.country}!")
            else:
                print(f"Your person of choice is {self.name}.\nHe is a {age} years old gentleman from {self.country}!")
        elif self.sex == "woman" or self.sex == "girl":
            if age <= 18:
                print(f"Your person of choice is {self.name}.\nShe is a {age} years old girl from {self.country}!")
            else:
                print(f"Your person of choice is {self.name}.\nShe is a {age} years old lady from {self.country}!")
