# -*- coding: utf8 -*-
from shutil import rmtree
from os import makedirs
from os.path import exists
from loguru import logger
from time import sleep

class Settings:
    def check(self):

        without_errors = True

        try:
            if exists('data/temp'):
                rmtree('data/temp')
                sleep(1)
                makedirs('data/temp')
        except:
            pass
        
        if self.xf_tfa_trust == '':
            logger.error('[Resources] xf_tfa_trust is None')
            without_errors = False

        if self.xf_user == '':
            logger.error('[Resources] xf_user is None')
            without_errors = False

        if self.domain == '':
            logger.error('[Settings] domain is None')
            without_errors = False

        if self.no_contests_delay == '':
            logger.error('[Settings] no_contests_delay is None')
            without_errors = False

        if self.delay == '':
            logger.error('[Settings] delay is None')
            without_errors = False

        if self.delay_between_contests == '':
            logger.error('[Settings] delay_between_contests is None')
            without_errors = False

        if self.telegram_token == '':
            logger.error('[Telegram] token is None')
            without_errors = False

        if self.user_id == '':
            logger.error('[Telegram] user_id is None')
            without_errors = False

        if self.sympathy_status == '':
            logger.error('[Likes] status is None')
            without_errors = False

        if self.debug == 1:
            logger.info('[DEBUG] settings.ini checked')

        return without_errors