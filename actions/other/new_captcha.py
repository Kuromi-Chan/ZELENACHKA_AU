# -*- coding: utf8 -*
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from loguru import logger

from time import sleep

class NewCaptcha:

    def __init__(self, driver, debug):
        self.driver = driver
        self.debug = debug


    def find_captcha(self):
        while True:
            try:
                button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form/button")))
                if button:
                    button.click_safe()
                    if self.debug == 1:
                        logger.success(f'[DEBUG] New captcha passed')
                        
                    return True
                    
            except:
                if self.debug == 1:
                    logger.success('[DEBUG] New captcha not found')
                sleep(15)
                continue