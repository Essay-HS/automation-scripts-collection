from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Use Selenium to open Firefox and navigate to Google.com
driver = webdriver.Firefox()
driver.get("https://duckduckgo.com")

time.sleep(2)

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='searchbox_input']")))
search_box.send_keys("teddy bear")
time.sleep(2)
search_box.send_keys(Keys.RETURN)
time.sleep(1.5)


first_result = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[2]/div[6]/div[4]/div/div/div/div[2]/section[1]/ol/li[2]/article/div[3]/h2/a")
))
first_result.click()

driver.maximize_window()
driver.save_full_page_screenshot("teddy_bear_search.png")

exit()

