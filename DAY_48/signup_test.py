from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Go to the test sign up webpage
driver = webdriver.Chrome(chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Get form elements
first_name_input = driver.find_element(By.NAME, value="fName")
last_name_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, value="form.form-signin button")

# Fill in the sign up form
first_name_input.send_keys("Alice")
last_name_input.send_keys("Bredford")
email_input.send_keys("alice@example.com")

# Click Sign up
button.click()

