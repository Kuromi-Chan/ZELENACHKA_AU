# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

# from actions.other.telegram_notifications import Telegram

# import mysql.connector
# from mysql.connector import Error

# from datetime import datetime
# from loguru import logger

# from time import sleep
# from os import _exit as script_exit



# class License:
#     _instance = None

#     def __init__(self, driver, telegram_token, user_id, debug,isLicensed):
#         self.driver =  driver
#         self.telegram_token = telegram_token
#         self.user_id = user_id
#         self.debug = debug
#         self.isLicensed=isLicensed
       
   
#     def __del__(self):
#         self.__conn.close()


#     def get_username(self):
#         try:
#             if f'https://{self.domain}/forums/contests/' not in self.driver.current_url:
#                 self.driver.get(f'https://{self.domain}/forums/contests/')
                
#             return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='NavigationAccountUsername']/span"))).text
#         except:
#             self.get_username(self)
            
#     def get_subscription(self, username):
#         for i in range(5):
#             try:
#                 try:
#                     self.__conn = mysql.connector.connect(
#                         host="",
#                         user="",
#                         port=3306,
#                         passwd="",
#                         database="",
#                         # connect_timeout=60
#                     )
#                 except Error as ex:
#                     # logger.error(ex)
#                     # logger.error(f"Ошибка при проверке лицензии, повтор {i}/10")
#                     sleep(3)
#                     continue

#                 with self.__conn.cursor() as cursor:
#                     # try:
#                     cursor.execute("SELECT subscription_data FROM lztc WHERE lzt_username=%s", (username,))
#                     results = cursor.fetchall()
#                     # except Exception as ex:
#                     #     logger.error("Никнейм лолза не установлен. @lztc_bot - Профиль - Указать никнейм")
#                     #     Telegram.send_notification(self, "Никнейм лолза не установлен. @lztc_bot - Профиль - Указать никнейм")
#                     #     input()
#                     #     script_exit(1)

#                     user_subscription_data = results[0][0]
#                     if user_subscription_data != '0' or user_subscription_data != 'TEST_OVER':
#                         user_subscription_data_converted = datetime.strptime(user_subscription_data, "%H:%M:%S %d.%m.%Y")
#                         current_time = datetime.now()

#                         if user_subscription_data_converted >= current_time:
#                             return True

#             except Exception as ex:
                
#                 current_date = datetime.now()
#                 for username in active_usernames:
#                     if username in active_usernames:
#                         subscription_date = active_usernames[username]
#                         subscription_datetime = datetime.strptime(subscription_date, '%H:%M:%S %d.%m.%Y')
#                         if subscription_datetime > current_date:
#                             return True
#                         else:
#                             return False
#                     else:
#                         return False
                


#                 # logger.exception(ex)
#                 # logger.error("Никнейм лолза не установлен. @lztc_bot - Профиль - Указать никнейм" )
#                 # Telegram.send_notification(self, "Никнейм лолза не установлен. @lztc_bot - Профиль - Указать никнейм")
#                 # self.driver.quit()
#                 # input()
#                 # script_exit(1)

#         # logger.error("Ошибка при проверке лицензии")
#         # self.driver.quit()
#         # input()
#         # script_exit(1)

#         current_date = datetime.now()
#         for username in active_usernames:
#             if username in active_usernames:
#                 subscription_date = active_usernames[username]
#                 subscription_datetime = datetime.strptime(subscription_date, '%H:%M:%S %d.%m.%Y')
#                 if subscription_datetime > current_date:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False

        
#     def check_license(self, username):
        
#         while True:
#             db_info = License.get_subscription(self, username)

#             if db_info == True:
#                 if self.debug == 1:
#                     logger.debug('[DEBUG] Лицензия активна')
#                     self.isLicensed = 1

#                 try:
#                     self.__conn.close()
#                 except:
#                     pass
                
#                 sleep(60*60)
#             else:
#                 self.__conn.close()
#                 Telegram.send_notification(self, "Отсутствует активная лицензия. Для покупки - @lztc_bot")
#                 self.driver.quit()
#                 input("Отсутствует активная лицензия. Для покупки - @lztc_bot")
#                 script_exit(1)