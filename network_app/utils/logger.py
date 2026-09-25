"""Модуль для логування та обробки побічних дій."""

import sys
from typing import Any

def log_and_reraise(exception_obj: Exception) -> None:
    """
    Логує виключення і передає його далі по стеку.
    
    Args:
        exception_obj (Exception): Об'єкт виключення для логування.
        
    Raises:
        Exception: Повторно піднімає передане виключення.
    """
    print(f"[СИСТЕМНИЙ ЛОГ]: Зафіксовано критичну помилку -> {exception_obj}", file=sys.stderr)
    raise