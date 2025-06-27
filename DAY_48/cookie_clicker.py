from selenium import webdriver
from selenium.webdriver.common.by import By
import time

GAME_URL = "https://orteil.dashnet.org/cookieclicker/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a Chrome browser window and navigate to the game page
driver = webdriver.Chrome(options=chrome_options)
driver.get(GAME_URL)

# Wait for 3 seconds until consent and cookie blocks appear
time.sleep(3)

accept_cookie_btn = driver.find_element(By.CSS_SELECTOR, value="div.cc_banner a.cc_btn.cc_btn_accept_all")
if accept_cookie_btn is not None:
    accept_cookie_btn.click()
else:
    print("Accept Cookie Btn not found")

consent_btn = driver.find_element(By.CSS_SELECTOR, value="div.fc-consent-root div.fc-dialog-container button.fc-button.fc-cta-consent.fc-primary-button")
if consent_btn is not None:
    consent_btn.click()
else:
    print("Consent Btn not found")

language_select_btn = driver.find_element(By.CSS_SELECTOR, value="div.langSelectButton")
if language_select_btn is not None:
    language_select_btn.click()
else:
    print("Select Language Btn not found")

# Play Game

