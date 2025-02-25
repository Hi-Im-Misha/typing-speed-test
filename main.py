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
    print("Печатайте следующий текст:")
    print(text)
    
    input("Нажмите Enter, когда будете готовы начать...")
    
    start_time = time.time()
    user_input = input("Начинайте печатать: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words = text.split()
    num_words = len(words)
    user_words = user_input.split()
    num_user_words = len(user_words)
    
    correct_words = sum(1 for expected, actual in zip(words, user_words) if expected == actual)
    
    accuracy = (correct_words / num_words) * 100
    wpm = (num_user_words / elapsed_time) * 60
    
    print(f"\nВаша скорость: {wpm:.2f} слов в минуту")
    print(f"Точность: {accuracy:.2f}%")

typing_test()
