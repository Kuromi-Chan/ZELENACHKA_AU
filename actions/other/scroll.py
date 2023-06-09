from time import sleep
from loguru import logger

class Scroll:
    def scroll(self, scroll_element):

        try:
            if self.debug == 1:
                logger.info('[DEBUG] Scroll')

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroll_element)
            return True
        except Exception as ex:
            logger.warning("Ошибка в скроле")
            

    def scroll_contest(self, scroll_element):
        try:
            if self.debug == 1:
                logger.info('[DEBUG] Scroll')
            
            sleep(2)

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroll_element)
            self.driver.execute_script("window.scrollBy(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2))", scroll_element)
            return True
        except Exception as ex:
            logger.warning("Ошибка в скроле")