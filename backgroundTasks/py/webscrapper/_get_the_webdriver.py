from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def _get_the_webdriver(url):

    options = webdriver.ChromeOptions()
    options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                chrome_options= options)
    driver.get(url)

    return driver