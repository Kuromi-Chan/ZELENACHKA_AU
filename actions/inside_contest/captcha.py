from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from loguru import logger
from time import sleep

class Captcha:
    def captcha(self):
        try:
            
            # Проверю вдруг уже мы участвовали в конкурсе
            try:
                already_participate = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[@class='LztContest--alreadyParticipating button marginBlock alreadyParticipate']")))
                if already_participate.is_displayed():
                    return True
            except:
                pass

           
            iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='challenges.cloudflare.com']")))
            self.driver.switch_to.frame(iframe)
            captcha_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cf-stage']")))
            if 'Успешно.' in captcha_button.text or 'Success!' in captcha_button.text:
                self.driver.switch_to.default_content()
                return True

            if 'Подтвердите, что вы человек' in captcha_button.text or 'Verify you are human':
                captcha_button.click_safe()
                sleep(1)
                if Captcha.Captcha_Checker(self,captcha_button) == True:   
                    if self.debug == 1:
                        logger.info('[DEBUG] captcha_button pressed')
                    return True
                
            if 'Проверка не пройдена' in captcha_button.text or 'Failure!' in captcha_button.text:
                return False
            if 'Идет проверка' in captcha_button.text or 'Verifying' in captcha_button.text:
                sleep(6)
                return False
            sleep(1)
        except Exception as ex:
            print(ex)
            return False

    
    def Captcha_Checker(self, captcha_button):
        try:
            iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='challenges.cloudflare.com']")))
            self.driver.switch_to.frame(iframe)
            captcha_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cf-stage']")))
            
            if 'Успешно.' in captcha_button.text or 'Success!' in captcha_button.text:
                    self.driver.switch_to.default_content()
                    return True
            else:
                return False
        except:
            return False
   

    
   