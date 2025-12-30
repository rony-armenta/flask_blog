class SimpleCalculator:
    # 1. CLASS VARIABLE: All calculators of this type are made by this brand
    brand = "Pythonics"

    def __init__(self, owner):
        # 2. INSTANCE VARIABLES: Unique to this specific calculator
        self.owner = owner
        # 3. ENCAPSULATION: Private variable (starts with __)
        self.__current_value = 0

    # 4. METHODS: The actions the calculator can perform
    def add(self, amount):
        self.__current_value += amount
        return self.__current_value

    def subtract(self, amount):
        self.__current_value -= amount
        return self.__current_value

    def clear(self):
        self.__current_value = 0

    def get_result(self):
        # 5. ABSTRACTION: We show the result, but hide how it's stored
        return f"{self.owner}'s total is: {self.__current_value}"


# --- Using the Calculator ---
my_calc = SimpleCalculator("Alex")
print(my_calc.add(10))        # 10
print(my_calc.subtract(3))     # 7
print(my_calc.get_result())    # Alex's total is: 7
