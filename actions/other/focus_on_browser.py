# import ctypes
# import win32com.client
# import time
# import pythoncom
# from loguru import logger

# class Focus:
#     def __init__(self):
#         pass
#     def focus(self):
#         pythoncom.CoInitialize()
#         while True:
#             """Тут фокусим 2 раза каждые 30 секунд"""
#             try:
#                 shell = win32com.client.Dispatch("WScript.Shell")
#                 time.sleep(2)
#                 chrome = shell.AppActivate("Google Chrome")
                
#                 hwnd = ctypes.windll.user32.FindWindowW(None, "Google Chrome")
#                 time.sleep(2)
#                 ctypes.windll.user32.SetForegroundWindow(hwnd)
#                 logger.success("Браузер в фокусе!")
#                 time.sleep(30)
                
#             except:
#                 logger.error("Браузер не в фокусе!")
#                 time.sleep(30)