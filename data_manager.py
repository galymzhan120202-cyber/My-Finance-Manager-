import json

def save_to_json(data, filename="data.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Қате орын алды: {e}") # Exception handling 

def load_from_json(filename="data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {} # Файл жоқ болса, бос сөздік қайтару