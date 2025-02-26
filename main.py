import time
import random
import os

def get_random_text():
    script_dir = os.path.dirname(__file__)
    texts_dir = os.path.join(script_dir, "texts")
    text_files = os.listdir(texts_dir)
    random_text_file = random.choice(text_files)
    
    file_path = os.path.join(texts_dir, random_text_file)
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def typing_test():
    text = get_random_text()
    words = text.split()
    
    print("Печатайте следующий текст по одному слову:")
    input("Нажмите Enter, когда будете готовы начать...")
    
    start_time = time.time()
    correct_words = 0
    
    for word in words:
        print(word)  # Выводим слово на экран
        user_input = input("Введите слово: ")
        
        while user_input.strip() != word:  # Проверяем правильность ввода
            print("Ошибка! Попробуйте снова.")
            user_input = input("Введите слово: ")
        
        correct_words += 1
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    wpm = (correct_words / elapsed_time) * 60
    
    print(f"\nВаша скорость: {wpm:.2f} слов в минуту")
    print("Поздравляем! Тест завершён.")

typing_test()
