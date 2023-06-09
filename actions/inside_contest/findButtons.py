# -*- coding: utf8 -*
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from loguru import logger

class FindButtons:
    def participate(self):
        try:
            participate_button = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, "//a[@class='LztContest--Participate button mn-15-0-0 primary']")))
            if self.debug == 1:
                logger.info('[DEBUG] Participate button found')
            return participate_button

        except TimeoutException:
            logger.warning('Ошибка поиска кнопки принятия участия')

    def sympathy(self):

        try:
            if self.debug == 1:
                logger.info('[DEBUG] Sympathy button found')

            return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//a[starts-with(@href,'posts/')]")))

        except Exception:
            logger.warning("Ошибка при открытии розыгрыша")
            