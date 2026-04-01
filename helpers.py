import random
import string

BASE_URL = "https://stellarburgers.education-services.ru"
LOGIN_URL = f"{BASE_URL}/login"
REGISTER_URL = f"{BASE_URL}/register"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
PROFILE_URL = f"{BASE_URL}/account/profile"


def generate_email():
    """Генерирует уникальный email в формате имя_фамилия_когорта_XXX@домен."""
    digits = "".join(random.choices(string.digits, k=3))
    return f"test_testov_999_{digits}@yandex.ru"


def generate_password(length=8):
    """Генерирует случайный пароль заданной длины (минимум 6 символов)."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))
