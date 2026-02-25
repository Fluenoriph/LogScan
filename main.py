"""
Название утилиты: Log Scaner
Версия: 0.9
Дата: Февраль 2026 г.
Лицензия: MIT License
Автор: Богданов Иван Иванович
Контакты: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

import os.path
import glob

from modules.argument_parser import ArgumentParser
from modules.program_process import ProgramProcess


if __name__ == '__main__':
    argument_parser = ArgumentParser()

    #key = input("Enter your key:")
    #result_format = input("Enter your format:")

    #source_log = os.path.abspath(r'logs')
    #out_path = os.path.abspath(r'output')



    if os.path.isfile(argument_parser.arguments.logfile):
        app = ProgramProcess(argument_parser.arguments.logfile,
                             argument_parser.arguments.apikey,
                             argument_parser.arguments.output,
                             argument_parser.arguments.format)

    elif os.path.isdir(argument_parser.arguments.logfile):
        files = glob.glob(rf'{argument_parser.arguments.logfile}\*.log') + glob.glob(rf'{argument_parser.arguments.logfile}\*.txt')

        for file in files:
            app = ProgramProcess(file, argument_parser.arguments.apikey,
                                 argument_parser.arguments.output, argument_parser.arguments.format)
