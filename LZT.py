# -*- coding: utf8 -*-
from undetected_chromedriver import ChromeOptions
from configparser import ConfigParser
from actions.start import participiating
from os.path import abspath

class LZT:

    def __init__(self):
        self.options = ChromeOptions()
        self.config = ConfigParser(interpolation=None)
        config_file_path = abspath('settings.ini')
        self.config.read(config_file_path, encoding='utf-8')

        self.xf_tfa_trust = self.config.get('Resources', 'xf_tfa_trust')
        self.xf_user = self.config.get('Resources', 'xf_user')
        self.extensions = self.config.get('Settings', 'extensions')
        self.domain = self.config.get('Settings', 'domain')
        self.no_contests_delay = int(self.config.get('Settings', 'no_contests_delay')) * 60
        self.delay_between_contests = self.config.get('Settings', 'delay_between_contests')
        try:
            self.delay = self.config.get('Settings', 'delay')
        except:
            self.delay = None

        self.telegram_token = self.config.get('Telegram', 'token')
        self.user_id = self.config.get('Telegram', 'user_id')

        self.sympathy_status = self.config.get('Likes', 'status')
        self.sympathy_chance = self.config.get('Likes', 'chance')

        self.isLicensed = 0

        self.debug = int(self.config.get('Developing', 'debug'))

        if self.delay:
            self.start, self.end = map(int, self.delay.split(','))
        else:
            self.start, self.end = 3, 10

    def run(self):   
        print('''
              .-') _   .-') _                
             (  OO) ) (  OO) )               
 ,--.      ,(_)----.  /     '._     .-----.  
 |  |.-')  |       |  |'--...__)   '  .--./  
 |  | OO ) '--.   /   '--.  .--'   |  |('-.  
 |  |`-' | (_/   /       |  |     /_) |OO  ) 
(|  '---.'  /   /___     |  |     ||  |`-'|  
 |      |  |        |    |  |    (_'  '--'\  
 `------'  `--------'    `--'       `-----'                                         

 -------------------------------------------
 
        ''')
        participiating(self)