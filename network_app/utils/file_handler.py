"""Модуль для роботи з файлами та демонстрації обробки виключень."""

import json
from network_app.exceptions.custom_errors import ConfigValidationError, ResourceAccessError

def read_config(file_path: str) -> dict[str, str]:
    """
    Читає JSON-конфігурацію з файлу. Демонструє try/except/else/finally.
    
    Args:
        file_path (str): Шлях до файлу конфігурації.
        
    Returns:
        dict[str, str]: Словник із конфігурацією.
        
    Raises:
        ResourceAccessError: Якщо файл не знайдено або немає прав.
        ConfigValidationError: Якщо JSON пошкоджено (ланцюжок виключень).
    """
    config_data = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            config_data = json.loads(content)
            
    except (FileNotFoundError, PermissionError) as e:
        raise ResourceAccessError("Неможливо прочитати файл конфігурації", file_path) from e
        
    except json.JSONDecodeError as e:
        raise ConfigValidationError("Файл містить некоректний JSON", 1001) from e
        
    else:
        print(f"[УСПІХ] Конфігурацію успішно завантажено з {file_path}")
        
    finally:
        print(f"[ФІНАЛ] Спроба читання файлу '{file_path}' завершена.")
        
    return config_data