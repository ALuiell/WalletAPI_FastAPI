from fastapi import FastAPI
from sqlalchemy.orm import Session
from models import *
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()

# Зависимость для получения сессии базы данных
def check_db_connection():
    """
    Проверяет подключение к базе данных, пытаясь выполнить простой запрос.

    Returns:
        None

    Raises:
        Exception: Если не удалось подключиться к базе данных.
    """

    try:
        with SessionLocal() as db:
            # Простой запрос для проверки подключения (например, SELECT 1)
            db.execute(text("SELECT 1"))
        print("OK")
    except Exception as e:
        raise Exception(f"Ошибка подключения к базе данных: {e}")


# Вызов функции для проверки подключения
if __name__ == "__main__":
    check_db_connection()
