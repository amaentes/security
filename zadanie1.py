# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.

import hashlib

def check_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = input("Введите пароль: ")

if check_password(password):
    hashed_password = hash_password(password)
    print("Пароль сложный. Хэш-значение пароля:", hashed_password)
else:
    print("Пароль не соответствует требованиям по сложности.")
