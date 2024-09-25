class carshowroom:
    def __init__(self, cgst, sgst, insurance):
        self.cgst = cgst
        self.sgst = sgst
        self.insurance = insurance

    def company(self, name):
        self.n = name
        print("Welcome to ", self.n, "family")

    def model(self):
        models = {
            "maruthi": ["X", "Y"],
            "MG": ["Z", "I"],
            "hyundai": ["O", "H"]
        }
        if self.n in models:
            print("Available models:")
            for model in models[self.n]:
                print(model)
        else:
            print(f"Sorry, {self.n} is not currently available.")

    def price(self, model_choice):
        prices = {
            "maruthi": {"X": 25, "Y": 30},
            "MG": {"Z": 40, "I": 50},
            "hyundai": {"O": 60, "H": 70}
        }
        if self.n in prices and model_choice in prices[self.n]:
            base_price = prices[self.n][model_choice]
            total_price = base_price + self.cgst + self.sgst + self.insurance
            print(f"The on-road price for {model_choice} is: ₹{total_price}")
        else:
            print(f"Invalid model choice for {self.n}.")

# Get user input for company name outside the class
company_name = input("Enter company name: ")

p = carshowroom(1, 2, 3)
p.company(company_name)
p.model()
p.price(input("Enter model choice: "))  # Prompt user for model choice