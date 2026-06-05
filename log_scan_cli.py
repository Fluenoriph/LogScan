"""
Program name: Log Scanner
Version: 0.9
Date: February 2026 г.
Author: Ivan Bogdanov
Contacts: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

import os
import glob
from modules.argument_parser import ArgumentParser
from modules.program_process import ProgramProcess


argument_parser = ArgumentParser()

if os.path.isfile(argument_parser.arguments.logfile):
    app = ProgramProcess(argument_parser.arguments.logfile,
                         argument_parser.arguments.apikey,
                         argument_parser.arguments.output,
                         argument_parser.arguments.format)

elif os.path.isdir(argument_parser.arguments.logfile):
    files = (glob.glob(rf'{argument_parser.arguments.logfile}/*.log') +
             glob.glob(rf'{argument_parser.arguments.logfile}/*.txt'))

    for file in files:
        app = ProgramProcess(os.path.normcase(file), argument_parser.arguments.apikey,
                             argument_parser.arguments.output, argument_parser.arguments.format)
