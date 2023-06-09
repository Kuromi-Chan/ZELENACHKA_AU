# -*- coding: utf8 -*
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from loguru import logger

class Join:
    def contest(self, found_contest):

        try:
            found_contest.click_safe()

            if self.debug == 1:
                logger.info('[DEBUG] Contest opened')

        except ElementClickInterceptedException:
            try:
                ActionChains(self.driver).click(found_contest)

            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click_safe();", found_contest)
                
        except:
            logger.error("Ошибка при попытке клика на розыгрыш")