import datetime

# Базалық класс
class Transaction:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def get_info(self):
        return f"{self.date} | {self.category}: {self.amount} тг"

# Мұрагер класс (Inheritance)
class Expense(Transaction):
    def __init__(self, amount, category, description=""):
        super().__init__(amount, category)
        self.description = description

    def get_info(self): # Polymorphism (әдісті өзгерту)
        info = super().get_info()
        return f"[Шығын] {info} ({self.description})"