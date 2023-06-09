# -*- coding: utf8 -*
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from actions.other.telegram_notifications import Telegram

from loguru import logger
from time import sleep
from datetime import datetime, timedelta

class Get:

    def time(self):
        return (datetime.now() + timedelta(minutes=int(self.no_contests_delay / 60))).strftime("%H:%M")
    
    def searching_for_contests(self, elements):
        contests_list = []
        ASAP_elements = elements.copy()
        try:
            for el in ASAP_elements:
                for el1 in el.text.split("\n"):
                    if "минут" in el1:
                        contests_list.append(el1.split()[0])

            for min_element in ASAP_elements:
                if f'{min(contests_list)} минут' in min_element.text:
                    if self.debug == 1:
                        logger.debug(f'[DEBUG] [ASAP] Contest found, {min(contests_list)} minutes left')
                    return min_element
        except:
            pass
                    
        for el in elements:
            if "Быстрый" in el.text:
                if self.debug == 1:
                    logger.debug('[DEBUG] [FAST] Available contests found')
                return el

        if self.debug == 1:
            logger.debug('[DEBUG] Available contests found')

        # assert elements, "No contests found"
        return elements[0]

    def contests(self):
        try:
            if self.driver.current_url != f'https://{self.domain}/forums/contests/':
                self.driver.get(f'https://{self.domain}/forums/contests/')

            elements = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//*[starts-with(@id, 'thread-')]")))
            available_contest = Get.searching_for_contests(self, elements)
            return available_contest

        except TimeoutException:
            logger.error(f'Нет доступных розыгрышей, ожидание до {Get.time(self)}')
            Telegram.send_notification(self, f"Нет доступных розыгрышей, ожидание до {Get.time(self)}")
            sleep(self.no_contests_delay)
            # Statistic.sendToDataBase(self)
            
            try:
                self.driver.refresh()
            except:
                sleep(5)
                self.driver.get(f'https://{self.domain}/forums/contests/')
        except Exception as ex:
            print(ex)
            return