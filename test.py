# tests.py
import unittest
from logic import Expense

class TestFinanceBot(unittest.TestCase):
    def test_expense_creation(self):
        # Экземпляр құрылуын тексеру
        exp = Expense(5000, "Тамақ", "Тест")
        self.assertEqual(exp.amount, 5000)
        self.assertEqual(exp.category, "Тамақ")
    
    def test_get_info_format(self):
        # get_info әдісінің дұрыс қайтаруын тексеру
        exp = Expense(1000, "Көлік", "Такси")
        self.assertIn("1000", exp.get_info())
        self.assertIn("Көлік", exp.get_info())

if __name__ == "__main__":
    unittest.main()