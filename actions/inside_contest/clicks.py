# -*- coding: utf8 -*
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from actions.other.telegram_notifications import Telegram


from time import sleep
from loguru import logger
from random import randint

class Clicks:

    # def contest_info(self):
    #     title_amount = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div/div[2]/h1")))                                                                                                    
    #     end_info = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'post-')]/div[2]/div[3]/article/div/div[2]")))
    #     username = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'post-')]/div[2]/div[2]/span[1]/a")))

    #     title_amount = title_amount.text
    #     end_info = end_info.text
    #     username = username.text

    #     title_amount_parts = title_amount.split(' ')
    #     if 'Быстрый' in title_amount_parts:
    #         amount = title_amount_parts[1]
    #     else:
    #         amount = title_amount_parts[0]
            
    #     title = ' '.join(title_amount_parts[2:])

    #     return {'title': title, 'amount': amount, 'end_info': end_info, 'username': username}


    def participiate(self, participiate_button):
        try:
            # if participiate_button.is_displayed():                
            participiate_button.click_safe()
            # already_participate = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            #     (By.XPATH, "//span[@class='LztContest--alreadyParticipating button marginBlock alreadyParticipate']")))
        # if already_participate.is_displayed():
#             contest_info = Clicks.contest_info(self)
#             Telegram.send_notification(self, f"""<b>
# Сумма: <code>{contest_info.get('amount', 'Ошибка при получении данных')}</code> ₽
# Название: <code>{contest_info.get('title', 'Ошибка при получении данных')}</code>
# Автор: <code>{contest_info.get('username', 'Ошибка при получении данных')}</code>
        
# <code>{contest_info.get('end_info', 'Ошибка при получении данных')}</code>
# {self.driver.current_url}</b>""")
            Telegram.send_notification(self, f'🌸 {self.driver.current_url}')
            if self.debug == 1:
                logger.info('[DEBUG] Participiate button pressed')
            else:
                logger.success(f'✓ {self.driver.current_url}')
            
            # Statistic.IncrementStatistic()
            
            return True
        except Exception as ex:
            print(ex)
            return False

    def sympathy(self, sympathy_button):
        try:
            rand = randint(1, 100)

            if self.debug == 1:
                logger.info(f'[DEBUG] Sympathy got {rand}')

            if rand <= int(self.sympathy_chance):
                
                try:
                    sympathy_button.click_safe()

                    if self.debug == 1:
                        logger.info('[DEBUG] Sympathy button pressed')
        
                except ElementClickInterceptedException:
                        ActionChains(self.driver).click(sympathy_button).perform()         
    
        except Exception:
            # self.driver.refresh()
            logger.warning("Ошибка в клике по кнопке симпатии")
            return False