# Файл 'argument_parser.py': класс для системы аргументов командной строки.

import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Log Scaner 1.0 Utility")
        self.parser.add_argument('--logfile', type=str, required=True, help='Path to source log file or logs directory')
        self.parser.add_argument('--apikey', type=str, required=True, help='VirusTotal API key')
        self.parser.add_argument('--output', type=str, required=True, help='Path to result log directory')
        self.parser.add_argument('--format', type=str, choices=['csv', 'json'], required=True, help='Result log format')

        self._arguments = self.parser.parse_args()

    @property
    def arguments(self):
        return self._arguments
