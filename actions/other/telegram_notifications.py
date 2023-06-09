from requests import post
from loguru import logger

class Telegram:

    def send_notification(self, message):

        try:
            url = f'https://api.telegram.org/bot{self.telegram_token}/sendMessage'
            
            data = {
                "chat_id": self.user_id,
                "text": f'{message}',
                "disable_web_page_preview": "True",
                'parse_mode': 'HTML'
            }

            post(url, data)

            if self.debug == 1:
                logger.info("[DEBUG] Notification sent")

        except Exception as ex:
            logger.info(f"Ошибка с отпракой уведомления в Telegram\n{ex}")