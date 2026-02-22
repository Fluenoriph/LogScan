# Файл 'log_parser.py': класс для извлечения IP адреса, sha256 суммы загруженного файла и времени загрузки из файла лога с сервера.

import re


class LogParser:
    # Паттерны: ip адрес, sha256 хэш, дата и время.
    TARGET_DATA_PATTERNS = (re.compile(r'\d+\.\d+\.\d+\.\d+'), re.compile(r'[0-9A-Fa-f]{64}', re.IGNORECASE),
                            re.compile(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\..*]'))

    def __init__(self, log_file):
        self.log_file = log_file
        self._matched_data = []

    @property
    def matched_data(self):
        return self._matched_data

    def parse(self):
        with open(self.log_file, 'r') as file:
            logs = file.readlines()

            for line in logs:
                target_data = []

                for i in range(len(LogParser.TARGET_DATA_PATTERNS)):
                    match = re.search(LogParser.TARGET_DATA_PATTERNS[i], line)

                    if match:
                        target_data.append(match.group())
                    else:
                        target_data.append(None)

                self.matched_data.append(target_data)
