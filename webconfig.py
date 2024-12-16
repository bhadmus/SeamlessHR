import dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

dotenv.load_dotenv()
headless = bool(int(os.getenv('headless')))


class Driver:
    """
    This class file creates the webdriver and assigns the
    headless and non-headless capabilities.
    This shall only cover chrome browser.
    """

    def __init__(self):
        """
        The main instance of the webdriver
        (headless & non-headless) is instantiated here
        """
        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--window-size=1920,1200")
            chrome_options.add_argument("--disable-dev-shm-usage")

            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                           options=chrome_options)
        else:
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
