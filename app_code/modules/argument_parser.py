import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Log Scaner 1.0 Utility")
        self.parser.add_argument('--logfile', required=True, help='Path to source log file or logs directory')
        self.parser.add_argument('--apikey', required=True, help='VirusTotal API key')
        self.parser.add_argument('--output', required=True, help='Path to result log directory')
        self.parser.add_argument('--format', choices=['csv', 'json'], required=True, help='Result log format')

        self._arguments = self.parser.parse_args()

    @property
    def arguments(self):
        return self._arguments
