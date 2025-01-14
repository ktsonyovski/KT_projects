class car_make_model:
    def __init__(self,make: str,model: str,year: int,color: str):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def what_am_i(self):
        print(f"This is a {self.make}. It is a {self.year} year {self.model} in {self.color} colour!")
    