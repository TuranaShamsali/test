from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

try:
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    WebDriverWait(driver, 10)
    if "Google" in driver.title:
        print("Успешно!")

except TimeoutException:
    print("Ошибка")
except NoSuchElementException:
    print("Ошибка: элемент не найден.")

finally:
    driver.quit()
