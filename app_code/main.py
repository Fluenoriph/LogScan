"""
Название утилиты: Log Scaner
Версия: 1.0
Дата: Февраль 2026 г.
Лицензия: MIT License
Автор: Богданов Иван Иванович
Контакты: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

import os.path
import glob

from app_code.modules.argument_parser import ArgumentParser
from app_code.modules.program_process import ProgramProcess


if __name__ == '__main__':
    #argument_parser = ArgumentParser()

    key = input("Enter your key:")
    result_format = input("Enter your format:")

    source_log = os.path.abspath(r'.\logs')
    out_path = os.path.abspath(r'.\output')

    if os.path.isfile(source_log):
        app = ProgramProcess(source_log, key, out_path, result_format)

    elif os.path.isdir(source_log):
        files = glob.glob(f'{source_log}\*.log') + glob.glob(f'{source_log}\*.txt')

        for file in files:
            app = ProgramProcess(file, key, out_path, result_format)
