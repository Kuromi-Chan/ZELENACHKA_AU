# -*- coding: utf8 -*-
from loguru import logger
from time import sleep
from actions.other.new_captcha import NewCaptcha

class Login:
    def authorization(self):
        try:
            self.driver.refresh()
            self.driver.delete_all_cookies()
            cookies = [ 
                {"name": "xf_logged_in", "value" :"1","domain": self.domain, "path": "/", "expiry": 3889363645},
                {"name": "xf_session","value":self.xf_session,"domain": self.domain, "path": "/", "expiry": 3889363645},
                {"name": "zelenka.guru_xf_tc_lmad", "value": self.xf_tc_lmad, "domain": self.domain, "path": "/", "expiry": 3889363645},
                {"name": "xf_tfa_trust", "value": self.xf_tfa_trust, "domain": self.domain, "path": "/", "expiry": 3889363645},
                {"name": "xf_user", "value": self.xf_user, "domain": self.domain, "path": "/", "expiry": 3876403645},
                {"name": "xf_viewedContestsHidden", "value": "1", "domain": self.domain, "path": "/", "expiry": 3876403645}]

            for cookie in cookies: 
                self.driver.add_cookie(cookie)
                
            sleep(1)
            self.driver.refresh()
            
            sleep(1)
            self.driver.get(f'https://{self.domain}/forums/contests/')
            NewCaptcha.find_captcha(self)
            
            if self.debug == 1:
                logger.info('[DEBUG] Cookies injected')
            
            return True

        except Exception as ex:
            print(ex)
            return False
