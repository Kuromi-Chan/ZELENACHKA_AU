# -*- coding: utf8 -*-
from random import randint
from time import sleep
from loguru import logger
from threading import Thread
from queue import Queue
from selenium.webdriver.support.ui import WebDriverWait
from actions.launcher import Settings
from actions.launcher import Launch
from actions.launcher import Login

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from actions.select_contest import Get
from actions.select_contest import Join
from actions.inside_contest import FindButtons
from actions.inside_contest import Availability

from actions.inside_contest import Clicks

from actions.other.scroll import Scroll
from actions.other.telegram_notifications import Telegram
from actions.other.new_captcha import NewCaptcha

# from actions.launcher import License
from actions.inside_contest.captcha import Captcha
from os import _exit as script_exit

from loguru import logger

def participiating(self):
    while True:
        try:


            if Settings.check(self) != True:
                logger.error("Ошибка в settings.ini")
                Telegram.send_notification(self, f'Ошибка в settings.ini')
                input()
                script_exit(1)
            else:
                sleep(1)

            if Launch.browser(self) != True:
                logger.error("Ошибка с созданием браузера")
                Telegram.send_notification(self, f'Ошибка с созданием браузера')
                input()
                script_exit(1)
            else:
                pass

            new_captcha_instance = NewCaptcha(driver = self.driver, debug = self.debug)
            captcha_thread = Thread(target=new_captcha_instance.find_captcha)
            captcha_thread.start()

            sleep(5)

            if Login.authorization(self) != True:
                logger.error("Ошибка с авторизацией")
                Telegram.send_notification(self, f'Ошибка с авторизацией')
                # self.driver.quit()
                input('Для продолжения нажми любую клавишу')
                # script_exit(1)
            else:
                pass

            logger.success("Скрипт начал работу")
            Telegram.send_notification(self, "Скрипт начал работу")
            sleep(7)

            # username_retries = 5
            # for attempt in range(username_retries):
            #     try:
            #         if self.driver.current_url != f'https://{self.domain}/forums/contests/':
            #             self.driver.get(f'https://{self.domain}/forums/contests/')
            #             sleep(3)
            #             # username = License.get_username(self)
                        
            #     except Exception as e:
            #         logger.error(e)
            #         logger.info(f"Ошибка при авторизации, попытка {attempt+1} из {username_retries}")
            #         if attempt == username_retries - 1:
            #             logger.error("Не удалось авторизоваться после нескольких попыток, проверьте cookies")
            #             self.driver.quit()
            #             input()
            #             script_exit(1)

            #     sleep(10)

            # license_instance = License(driver = self.driver, telegram_token = self.telegram_token, user_id = self.user_id,debug = self.debug, isLicensed=self.isLicensed)
            # license_thread = Thread(target=license_instance.check_license, args=(username,))
            # license_thread.start()

            while True:
                
                # if not self.driver.current_url:
                #     raise Exception

                sleep(randint(self.start, self.end))
                found_contest = Get.contests(self)

                if found_contest is None:
                    continue
                
                if Scroll.scroll(self, found_contest) != True:
                    continue

                sleep(randint(self.start, self.end))
                Join.contest(self, found_contest)
                sleep(randint(self.start, self.end))
                sympathy_button = FindButtons.sympathy(self)

                if Scroll.scroll_contest(self, sympathy_button) != True:
                    self.driver.get(f'https://{self.domain}/forums/contests/')
                    continue

                if Availability.check_participation_eligibility(self, found_contest) != True:
                    self.driver.get(f'https://{self.domain}/forums/contests/')
                    continue
            
                retries = 1
                while Captcha.captcha(self) != True and retries < 3:
                    retries += 1
                    
                    if self.debug == 1:
                        logger.info(f"Повтор прохождения капчи ({retries}/3)")
                    
                    self.driver.switch_to.default_content()
                    self.driver.refresh()

                    sympathy_button = FindButtons.sympathy(self)
                    if Scroll.scroll_contest(self, sympathy_button) != True:
                        self.driver.get(f'https://{self.domain}/forums/contests/')
                        continue
                    
                if retries == 3:
                    self.driver.get(f'https://{self.domain}/forums/contests/')
                    continue
                
                if self.debug == 1:
                    logger.success('[DEBUG] Captcha passed')

                sleep(randint(self.start, self.end))
                participate_button = FindButtons.participate(self)
                if Clicks.participiate(self, participate_button) != True:
                    self.driver.get(f'https://{self.domain}/forums/contests/')
                    continue

                sleep(randint(self.start, self.end))
                if Clicks.sympathy(self, sympathy_button) != True:
                    self.driver.get(f'https://{self.domain}/forums/contests/')
                    continue

                # self.driver.back()
                # sleep(2)
                # self.driver.refresh()
                sleep(int(self.delay_between_contests))



        except:
            # if self.isLicensed == 0:
            continue
        