
# try:
#
#     num1 = float(input("Введите числитель: "))
#     num2 = float(input("Введите знаменатель: "))
#
#     result = num1 / num2
#
# except ZeroDivisionError:
#     print("Ошибка: Деление на ноль невозможно.")
# except ValueError:
#     print("Ошибка: Введите корректные числовые значения.")

#
# my_list=["apple","samsung","honor","nokia"]
# try:
#     index = int(input("Введите индекс элемента списка: "))
#     print(f"Элемент с индексом {index}: {my_list[index]}")
# except ValueError:
#     print("Ошибка: нужно ввести целое число.")
# except IndexError:
#     print("Ошибка: индекс выходит за пределы списка.")

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
try:
    element = driver.find_element(By.ID,"Gerry")
    element.click()
    print(" Элемент успешно найден и кликнут.")
except NoSuchElementException:
    print(f" Элемент с ID  не найден.")
except ElementNotInteractableException:
    print(f" Элемент с ID  найден, но недоступен для клика.")

