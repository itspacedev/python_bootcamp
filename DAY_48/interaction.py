from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# # Find an elm that contains the number of english articles
# articles_count_elm = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# articles_count = int(articles_count_elm.text.replace(",", ""))
# # Click on the link
# articles_count_elm.click()
# print(f"The number of english articles on Wikipedia is {articles_count}")


# Find an element by link text
# all_portals_link = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals_link.click()

# Search something
search_bar = driver.find_element(By.ID, value="searchInput")
search_bar.send_keys("Python", Keys.ENTER)
# search_bar.send_keys(Keys.ENTER)

