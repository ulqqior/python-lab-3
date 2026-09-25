import json 
import os

from network_app.utils.logger import log_and_reraise

from network_app import *
from network_app.exceptions.custom_errors import BusinessLogicError

def create_dummy_config():
    """Створює тимчасові файли для демонстрації."""
    with open("valid_config.json", "w") as f:
        json.dump({"host": "127.0.0.1"}, f)
    with open("bad_config.json", "w") as f:
        f.write("{bad_json: }")

def cleanup():
    """Видаляє тимчасові файли."""
    for file in ["valid_config.json", "bad_config.json"]:
        if os.path.exists(file):
            os.remove(file)

if __name__ == "__main__":
    print("="*50)
    print("ЛБ №3: Обробка виключень та документація")
    print("="*50)
    
    create_dummy_config()

    print("\n СЦЕНАРІЙ 1: Успішний шлях (try/except/else/finally) ")
    try:
        conf = read_config("valid_config.json")
    except NetworkAppError as e:
        print(e)

    print("\n СЦЕНАРІЙ 2: Перехоплення кількох типів (FileNotFoundError) ")
    try:
        read_config("missing_file.json")
    except NetworkAppError as e:
        print(f"Спіймано помилку: {e}")
        print(f"Оригінальна причина (__cause__): {e.__cause__}")

    print("\n СЦЕНАРІЙ 3: Ланцюжок виключень (raise from) ")
    try:
        read_config("bad_config.json")
    except ConfigValidationError as e:
        print(f"Спіймано помилку: {e}")
        print(f"Оригінальна причина (__cause__): {e.__cause__}")

    print("\n СЦЕНАРІЙ 4: Повторне піднесення (re-raise) та бізнес-логіка")
    try:
        try:
            raise BusinessLogicError("Невірний пароль", "auth_user")
        except BusinessLogicError as e:
            log_and_reraise(e)
    except BusinessLogicError as final_e:
        print(f"Остаточне перехоплення у main: {final_e}")

    print("\n СЦЕНАРІЙ 5: Інтроспекція (Завдання 4) ")
    print(f"Docstring модуля file_handler:\n{read_config.__doc__}")
    print(f"Анотації функції read_config: {read_config.__annotations__}")
    print("\nВиклик help() для ConfigValidationError:")
    help(ConfigValidationError)

    cleanup()
