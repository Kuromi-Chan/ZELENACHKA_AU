from LZT import LZT
from os import remove, rename, getcwd, _exit
from os.path import exists, getsize
from sys import argv
from loguru import logger
from json import load, dump
from requests import get
from tqdm import tqdm
from shutil import move
from requests.exceptions import RequestException, HTTPError
from threading import Timer

# def download(url: str, file_path: str, version_path: str, current_version: str):

#     try:
#         data = {"version": current_version[0]}

#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
#         }

#         try:
#             response = get(url, stream=True, headers=headers, allow_redirects=True)
#             response.raise_for_status()
#         except HTTPError as e:
#             logger.error(f"Ошибка сервера: {e}")
#             input()
#             return
#         except RequestException as e:
#             logger.error(f"Ошибка при выполнение запроса: {e}")
#             input()
#             return

#         file_size = int(response.headers.get("content-length", 0))
#         file_size_mb = file_size/(1000*1000)
#         logger.info(f"Загрузка обновления, размер файла: {file_size_mb:.2f} Мбайт")

#         chunk_size = 1024 * 1024
#         progress = tqdm(total=file_size, unit="B", unit_scale=True, desc=file_path)

#         with open(file_path, "wb") as f:
#             for chunk in response.iter_content(chunk_size):
#                 f.write(chunk)
#                 progress.update(len(chunk))

#         progress.close()
#         try:
#             rename(argv[0], 'LZTC.exe')
#         except:
#             pass

#         with open(version_path, "w") as file:
#             dump(data, file)

#         logger.success(f"{file_path} обновлён, необходимо перезапустить скрипт\n")
#         print(f"\033[37m" + ''.join(map(str, current_version[1])) + "\033[0m")

#         input()
#         _exit(1)
            
#     except Exception as ex:
#         print(ex)
#         logger.warning(f"{ex}\n\nНе удалось обновить скрипт. Попробуйте ещё раз, либо обновите скрипт вручную - @lztc_bot")
#         input()
#         _exit(1)

# def remove_old_file():
#     if exists(old_file):
#         try:
#             remove(old_file)
#         except:
#             pass

if __name__ == '__main__':

    # exec = None
    # eval = None

    # URL_FOR_DOWNLOAD = get('https://pastebin.com/raw/GAQ1Fj4K').text
    # FILE_NAME = f"LZTC.exe"
    # VERSION_PATH = 'data\\version.json'
    # lines = get('https://pastebin.com/raw/KEnQSSx7').text.split('\n')
    # CURRENT_VERSION = [lines[0], '\n'.join(lines[1:])]

    # file_path = 'data\\version.json'
    # old_file = 'data\\LZTC.exe'

    # try:

    #     if not exists(file_path) or getsize(file_path) == 0:
    #         if exists(old_file):
    #             try:
    #                 remove(old_file)
    #             except:
    #                 pass

    #         move(argv[0], f'{getcwd()}\\data')
    #         download(URL_FOR_DOWNLOAD, FILE_NAME, VERSION_PATH, CURRENT_VERSION)

    #     else:
    #         if exists(old_file):
    #             try:
    #                 remove(old_file)
    #             except:
    #                 pass

    #         with open(file_path, 'r') as file:
    #             loaded_data = load(file)
                
    #             if str(loaded_data.get('version')) != str(CURRENT_VERSION[0]):
    #                 try:
    #                     move(argv[0], f'{getcwd()}\\data')
    #                 except:
    #                     pass
                    
    #                 download(URL_FOR_DOWNLOAD, FILE_NAME, VERSION_PATH, CURRENT_VERSION)

    # except Exception as ex:
    #     logger.error(f'{ex}\n\nНеизвестная ошибка. Если перезапуск не помогает - @lztc_sup')
    #     input()
    #     _exit(1)

    # timer = Timer(30, remove_old_file)
    # timer.start()

    script = LZT()
    script.run()
