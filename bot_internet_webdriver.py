# # # BOT automatizado com interface com a internet

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

servico = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=servico)

nav.get("https://www.google.com/")

time.sleep(100)


# title = webdriver.title

# webdriver.implicitly_wait(2)

# webdriver.quit()
