from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
import time


def nw():
    browser = webdriver.Firefox()
    browser.get("https://ru.wikipedia.org")

    user_input = input("Введите запрос: ")
    search_box = browser.find_element(By.ID, 'searchInput')
    search_box.send_keys(user_input)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    while True:
        print("\nТекущая статья", browser.title)
        paragraphs = browser.find_elements(By.CLASS_NAME, 'mw-search-result-heading')
        links = browser.find_elements(By.TAG_NAME, 'a')
        print("Выберите действия: ")
        print("1 - Листать параграфы")
        print("2 - Перейти на одну из связанных страниц")
        print("3 - Выйти из программы")
        choice = input("Ваш выбор: ")
        if choice == "1":
            for index, paragraph in enumerate(paragraphs):
                print(f"Параграф {index + 1}:{paragraph.text}")
                if input("Нажмите Q для выхода") == "Q":
                    break
        elif choice == "2":
            for index, link in enumerate(links):
                print(f"{index + 1}:{link.get_attribute('href')}-{link.text}")
            link_choice = int(input(f"Выберите страницу для перехода")) - 1
            links[link_choice].click()
            time.sleep(3)
        elif choice == "3":
            break
        else:
            print(f"Неизвестная команда, попробуйте снова")
    browser.quit()



if __name__ == '__main__':
    nw()
