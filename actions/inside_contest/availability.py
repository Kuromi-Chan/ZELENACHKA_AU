# -*- coding: utf8 -*
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from loguru import logger
from re import findall

class Availability:

    def __init__(self, driver, domain, debug=False):
        self.driver = driver
        self.domain = domain
        self.debug = debug

    def check_participation_eligibility(self, available_contest):
        """Проверяет, может ли пользователь принять участие в конкурсе"""

        # thread_id = findall('\d+', available_contest)
        # url = f'https://{self.domain}/threads/{thread_id}/'

        # if self.driver.current_url != url:
        #     self.driver.get(url)


        if Availability.participation_eligibility(self):
            return True

    def participation_eligibility(self):
        """Проверяет, есть ли у пользователя право на участие в конкурсе"""

        retries = 1
        max_retries = 3

        while retries <= max_retries:
            try:
                if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='error mn-15-0-0']"))):
                
                    if self.debug:
                        logger.error(f'[DEBUG] Error button found. Retry: [{retries}/{max_retries}]')

                    retries += 1
                    
                    self.driver.refresh()

                    if retries > max_retries:
                        if Availability.refresh_cookies(self):
                            return False

            except (NoSuchElementException, TimeoutException):
                return True

    def refresh_cookies(self):
        """Перезагружает куки, чтобы обновить информацию об участии в конкурсе"""

        self.driver.add_cookie({
            "name": "xf_viewedContestsHidden", 
            "value": "1", 
            "domain": self.domain, 
            "path": "/", 
            "expiry": 2876403645
        })

        self.driver.get(f'https://{self.domain}/forums/contests')

        if self.debug:
            logger.info('[DEBUG] Flag reinjected')

        return True
