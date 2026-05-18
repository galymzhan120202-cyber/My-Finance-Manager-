from telebot import types

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("💸 Шығын қосу")
    btn2 = types.KeyboardButton("📊 Тарихты көру")
    markup.add(btn1, btn2)
    return markup

def category_menu():
    markup = types.InlineKeyboardMarkup()
    categories = ["Тамақ", "Көлік", "Оқу", "Ойын-сауық"]
    for cat in categories:
        markup.add(types.InlineKeyboardButton(cat, callback_data=f"cat_{cat}"))
    return markup