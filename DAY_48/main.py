import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a Chrome browser window
driver = webdriver.Chrome(options=chrome_options)
# Go to a website
driver.get("https://python.org/")

# Get the price of an item in an online store
# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_whole.text}.{price_fraction.text}")

# Get elements using different approaches
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)
# button = driver.find_element(By.ID, value="submit")
# print(button)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# submit_bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug_link.text)

events = {}
# Get upcoming events on Python.org
upcoming_events = driver.find_elements(By.CSS_SELECTOR, value="div.medium-widget.event-widget.last ul.menu li")
for elm_idx, upcoming_event in enumerate(upcoming_events):
    link_tag = upcoming_event.find_element(By.TAG_NAME, value="a")
    time_tag = upcoming_event.find_element(By.TAG_NAME, value="time")

    event_name = link_tag.text
    datetime_attr = time_tag.get_attribute('datetime')
    event_datetime = dt.datetime.fromisoformat(datetime_attr)

    events[elm_idx] = {
        "time": event_datetime.strftime("%Y-%m-%d"),
        "name": event_name
    }

print(events)

# Close a browser tab
# driver.close()
# Quit all tabs
driver.quit()

