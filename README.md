# Personal Expense Tracker Bot 💸

Final project for the Introduction to Python Programming course. This Telegram bot allows users to efficiently track, categorize, and monitor their daily expenses using intuitive menus.

## ✨ Features
- **Add Expenses:** Register spending instantly with specific categories (Food, Transport, Education, Entertainment).
- **View History:** Display a complete logs of all added expenses with exact timestamps.
- **Data Persistence:** Automatically reads and writes all user records to a local JSON file, ensuring data safety even after server restarts.
- **Robust System:** Built-in exception handling to prevent application crashes from invalid user inputs.

## 🛠 Technologies Used
- **Programming Language:** Python 3 
- **Library:** pyTelegramBotAPI (telebot) 
- **Data Storage:** JSON (File-based storage) 

## 📁 Project Architecture & Modularity
The project is designed using a clean, modular structure split across 4 custom modules to separate business logic from UI elements:
- `bot.py` — The core application runner and message handlers.
- `logic.py` — OOP classes including the `Transaction` base class and `Expense` subclass.
- `data_manager.py` — Handles secure File I/O operations (JSON reading/writing).
- `keyboards.py` — Manages interactive menus, ReplyKeyboards, and InlineKeyboards.
- `tests.py` — Automated unit tests verifying logical component behavior.

## 👥 Team Members and Roles
As per the team requirements, tasks and responsibilities are clearly divided:
- **Team Member 1:** Core Logic, OOP System Architecture (`logic.py`), Main Loop Configurations (`bot.py`).
-**Team Member 2:** Data Management, JSON File Operations (`data_manager.py`), Automated Testing Framework (`tests.py`).
-**Team Member 3:** UI/UX Interface Design (`keyboards.py`), Technical Documentation, Project Report Preparation.