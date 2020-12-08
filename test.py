from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()
driver.find_element(By.XPATH, "//input[@class='_3704LK']").send_keys("Laptops")
driver.find_element(By.XPATH, "//button[@class='L0Z3Pu']").click()
driver.find_element(By.XPATH, "//div[contains(text(),'HP 14s Core i3 10th Gen - (8 GB/256 GB SSD/Windows')]").click()
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']")


