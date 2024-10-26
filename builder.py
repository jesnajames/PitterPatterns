class Beverage:
    def __init__(self):
        self.is_decaf = False
        self.is_iced = False
        self.name = None
        self.size = None
        self.shots = []
        self.syrup = []
        self.milk = None
        self.custom = []
        self.customer = None

    def describe(self):
        description = f"Beverage: "
        if self.is_decaf:
            description += "Decaf "
        if self.is_iced:
            description += "Iced "
        description += self.size + " "
        if self.shots:
            description += " ".join(self.shots)
        if self.syrup:
            description += " ".join(self.syrup)
        if self.milk:
            description += " " + self.milk + " "
        if self.custom:
            description += ' '.join(self.custom)
        description += f" {self.name} for {self.customer}"
        return description


class BeverageBuilder:
    def __init__(self):
        self.beverage = Beverage()

    def set_name(self, name):
        self.beverage.name = name
        return self

    def set_customer(self, name):
        self.beverage.customer = name
        return self

    def set_size(self, size):
        self.beverage.size = size
        return self

    def set_milk(self, milk):
        self.beverage.milk = milk
        return self

    def set_syrup(self, syrup):
        self.beverage.syrup = syrup
        return self

    def set_iced(self, is_iced):
        self.beverage.is_iced = is_iced
        return self

    def set_decaf(self, is_decaf):
        self.beverage.is_decaf = is_decaf
        return self

    def add_shot(self, shot):
        self.beverage.shots.append(shot)
        return self

    def add_custom(self, custom):
        self.beverage.custom.append(custom)
        return self

    def build(self):
        return self.beverage


class Barista:
    def __init__(self, builder):
        self.builder = builder

    def construct_beverage(self, name, size, customer, is_decaf=False, is_iced=False, milk=None, syrup=None,
                           shots=None, custom=None):
        self.builder.set_name(name).set_size(size).set_customer(customer)

        if is_decaf:
            self.builder.set_decaf(is_decaf)

        if is_iced:
            self.builder.set_iced(is_iced)

        if milk:
            self.builder.set_milk(milk)

        if syrup:
            self.builder.set_syrup(syrup)

        if shots:
            for shot in shots:
                self.builder.add_shot(shot)

        if custom:
            for cus in custom:
                self.builder.add_custom(cus)

        return self.builder.build()


caroline = Barista(BeverageBuilder()).construct_beverage(size="Venti", name="Triple Cappuccino",
                                                         custom=["No whip"], customer="Caroline")
max = Barista(BeverageBuilder()).construct_beverage(is_iced=True, size="Grande", name="Caramel Macchiato",
                                                    custom=["Light ice"], milk="Non-fat", customer="Max")

print(caroline.describe())
print(max.describe())
