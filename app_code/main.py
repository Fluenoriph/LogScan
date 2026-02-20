import argparse
import re
import sys
import json
import requests
from modules.log_parser import LogParser
#from modules.virus_total import VirusTotal


loger = LogParser('.\\logs\\sample_1.log')
loger.parse()

#print(loger.matched_data)

class VirusTotal:
    def __init__(self, hash, api_key):
        self.api_url = f"https://www.virustotal.com/api/v3/files/{hash}"
        self.headers = {"x-apikey": api_key}

        self.response = requests.get(self.api_url, headers=self.headers)

        if self.response.status_code == 200:
            result = self.response.json()
            #print(self.response.content)
            print(json.dumps(result, sort_keys=False, indent=4))
        else:
            print(self.response.status_code)
            print('IP not found in VirusTotal !')

key = input('Input api key:')
file_hash = input('Input hash:')

virus = VirusTotal(file_hash, key)








'''
# Создаём парсер аргументов
parser = argparse.ArgumentParser(description="Log analyzer CLI utility")
parser.add_argument('--file', required=True, help='Path to log file')
parser.add_argument('--verbose', action='store_true', help='Enable detailed output')

args = parser.parse_args()

# Чтение логов
try:
    with open(args.file, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"[!] File {args.file} not found.")
    sys.exit(1)

# Обработка
for line in lines:
    if re.search(r'ERROR|WARNING', line):
        print(f"[!] Important: {line.strip()}")
        if args.verbose:
            # Покажем IP, если есть
            ip_match = re.search(r'\\d+\\.\\d+\\.\\d+\\.\\d+', line)
            if ip_match:
                print(f"    → IP found: {ip_match.group()}")'''