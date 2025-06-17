from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

try:
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    wait=WebDriverWait(driver,20)
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    print("Все элементы найдены: username, password, login button")
except TimeoutException:
    print("Элементы не загрузились вовремя (TimeoutException)")

except NoSuchElementException:
    print("Один из элементов не найден (NoSuchElementException)")

finally:
    driver.quit()