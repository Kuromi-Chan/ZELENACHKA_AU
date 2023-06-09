# -*- coding: utf8 -*-
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException

from loguru import logger
from time import sleep
from actions.other.telegram_notifications import Telegram
from undetected_chromedriver import ChromeOptions, Chrome
from os import getcwd, makedirs, listdir
from os.path import exists, join
from shutil import rmtree

class Launch:
    def browser(self):
        try:
            options = ChromeOptions()
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument("--disable-backgrounding-occluded-windows")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--disable-background-timer-throttling")
            options.add_argument('--disable-hang-monitor') 
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-web-security')
            options.add_argument('--dns-prefetch-disable')
            options.add_argument('--disable-popup-blocking')
            options.add_argument('--disable-setuid-sandbox')
            options.add_argument('--enable-quic')
            options.add_argument('--disable-renderer-backgrounding')
            options.add_argument('--no-default-browser-check')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-features=VizDisplayCompositor')
            
            options.add_argument(f'--user-data-dir={getcwd()}\\data\\temp')

            if not exists('data\\extensions'):
                makedirs('data\\extensions')
                
            extensions = listdir('data\\extensions')
            if extensions:
                for extension in extensions:
                    extension_path = join('data\\extensions', extension)
                    options.add_argument(f'--load-extension={getcwd()}\\{extension_path}')


            with Chrome(options=options, driver_executable_path='data//chromedriver.exe') as self.driver:
                self.driver.set_window_size(1280, 960)

                if int(self.extensions) == 1:
                    input("[Extensions] Для продолжения нажмите любую клавишу")
                self.driver.get('https://' + self.domain + '/login')

            try:
                if exists('data\temp'):
                    rmtree('data\temp')
                    sleep(2)
                    makedirs('data\temp')    
            except:
                pass
            
            if self.debug == 1:
                logger.info('[DEBUG] Browser launched')

            return True

        except SessionNotCreatedException as ex:
            sleep(1)
            logger.error('Ошибка при открытии браузера')
        
        except WebDriverException as ex:
            
            sleep(1)
            logger.error(f'Не удалось открыть сайт, проверь домен в settings.ini или подключение к интернету')
            Telegram.send_notification(self, f'Не удалось открыть сайт, проверь домен в settings.ini или подключение к интернету')

        except Exception as ex:
            logger.info(ex)
            return False