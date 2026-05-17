import telebot
from logic import Expense
from data_manager import save_to_json, load_from_json
from keyboards import main_menu, category_menu

TOKEN = "8834328613:AAG_V6BK9fuAInXyrj-j2E5hgbRwStjrvX4"
bot = telebot.TeleBot(TOKEN)

user_data = load_from_json()
# Пайдаланушы енгізген соманы уақытша сақтау үшін
temp_amounts = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Сәлем! Мен сенің шығындарыңды бақылайтын ботпын.", reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "💸 Шығын қосу")
def ask_amount(message):
    msg = bot.send_message(message.chat.id, "Қанша ақша жұмсадыңыз? (Тек сан жазыңыз):")
    bot.register_next_step_handler(msg, process_amount)

def process_amount(message):
    try:
        amount = float(message.text)
        temp_amounts[message.chat.id] = amount # Соманы сақтаймыз
        bot.send_message(message.chat.id, f"Сома: {amount} тг. Категория таңдаңыз:", reply_markup=category_menu())
    except ValueError:
        bot.send_message(message.chat.id, "⚠️ Қате! Тек сан енгізіңіз.")

# Категория таңдалғанда жұмыс істейтін бөлек handler
@bot.callback_query_handler(func=lambda call: call.data.startswith('cat_'))
def callback_inline(call):
    user_id = call.message.chat.id
    
    # Уақытша сақталған соманы аламыз
    if user_id in temp_amounts:
        amount = temp_amounts[user_id]
        category = call.data.split('_')[1]
        
        # OOP қолдану (Expense класы)
        new_expense = Expense(amount, category, "Бот арқылы қосылды")
        
        user_id_str = str(user_id)
        if user_id_str not in user_data:
            user_data[user_id_str] = []
        
        user_data[user_id_str].append(new_expense.get_info())
        save_to_json(user_data) # Файлға сақтау 
        
        bot.edit_message_text(chat_id=user_id, 
                             message_id=call.message.id, 
                             text=f"✅ Сақталды: {new_expense.get_info()}")
        
        # Тазарту
        del temp_amounts[user_id]
    else:
        bot.send_message(user_id, "Қате орын алды. Қайтадан соманы енгізіңіз.")

@bot.message_handler(func=lambda message: message.text == "📊 Тарихты көру")
def show_history(message):
    user_id = str(message.chat.id)
    if user_id in user_data and user_data[user_id]:
        history = "\n".join(user_data[user_id])
        bot.send_message(message.chat.id, f"Сенің шығындарың:\n\n{history}")
    else:
        bot.send_message(message.chat.id, "Тарих бос.")

bot.polling(none_stop=True)