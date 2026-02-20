import argparse
import re
import sys
import json
import requests
from modules.log_parser import LogParser
from modules.virus_total import VirusTotalChecker


loger = LogParser('.\\logs\\sample_2.log')
loger.parse()

key = input('Input api key:')

checker = VirusTotalChecker(key, loger.matched_data)

for item in checker.checks_result:
    print('------------------------------------------------')

    for key, value in item.items():
        print(f" {key}: {value}")









'''
# Создаём парсер аргументов
parser = argparse.ArgumentParser(description="Log analyzer CLI utility")
parser.add_argument('--file', required=True, help='Path to log file')
parser.add_argument('--verbose', action='store_true', help='Enable detailed output')

args = parser.parse_args()'''



