"""Модуль для визначення ієрархії користувацьких виключень."""

class NetworkAppError(Exception):
    """Базовий клас виключень для всього застосунку."""
    pass

class ConfigValidationError(NetworkAppError):
    """
    Виключення, що піднімається при помилках валідації конфігурації.
    
    Args:
        message (str): Опис помилки.
        error_code (int): Код помилки валідації.
    """
    def __init__(self, message: str, error_code: int) -> None:
        super().__init__(message)
        self.error_code = error_code

    def __str__(self) -> str:
        return f"[Код: {self.error_code}] Помилка валідації: {self.args[0]}"

class ResourceAccessError(NetworkAppError):
    """
    Виключення для помилок доступу до ресурсів (файлів, мережі).
    
    Args:
        message (str): Опис помилки.
        resource_path (str): Шлях або URI ресурсу.
    """
    def __init__(self, message: str, resource_path: str) -> None:
        super().__init__(message)
        self.resource_path = resource_path

    def __str__(self) -> str:
        return f"Відмовлено в доступі до '{self.resource_path}': {self.args[0]}"

class BusinessLogicError(NetworkAppError):
    """
    Виключення для порушень бізнес-правил програми.
    
    Args:
        message (str): Опис помилки.
        operation (str): Назва операції, що викликала помилку.
    """
    def __init__(self, message: str, operation: str) -> None:
        super().__init__(message)
        self.operation = operation

    def __str__(self) -> str:
        return f"Помилка логіки в операції '{self.operation}': {self.args[0]}"